<?php


use PHPUnit\Framework\TestCase;

/**
 * Focused tests for PHP-mode code paths that the existing suite did not exercise,
 * to raise C/C++ line and branch coverage (gcov).
 */
final class CoverageGapSequence extends PySequence
{
}

class CoverageGapTest extends TestCase
{
    public function testPyStrConstructFromPyObject(): void
    {
        // PyStr::__construct from another PyObject exercises the instanceof branch.
        $fromStr = new PyStr(PyCore::str('hello'));
        $this->assertInstanceOf(PyStr::class, $fromStr);
        $this->assertSame('hello', (string) $fromStr);

        // A non-string PyObject cannot be converted implicitly; this exercises the
        // PyUnicode_FromObject() == NULL error branch of PyStr::__construct.
        $this->expectException(PyError::class);
        new PyStr(PyCore::int(123));
    }

    public function testSequenceContains(): void
    {
        $list = new PyList([1, 2, 3]);
        $this->assertTrue($list->contains(2));
        $this->assertFalse($list->contains(99));
    }

    public function testSetContainsAndCount(): void
    {
        $set = new PySet([1, 2, 2, 3]);
        $this->assertTrue($set->contains(2));
        $this->assertFalse($set->contains(9));
        // A Python set deduplicates, so the size is 3.
        $this->assertSame(3, $set->count());
    }

    public function testDictOffsetUnsetAndExists(): void
    {
        $dict = new PyDict(['a' => 1, 'b' => 2]);

        $this->assertTrue(isset($dict['a']));
        $this->assertTrue($dict->offsetExists('b'));
        $this->assertFalse(isset($dict['x']));
        $this->assertFalse($dict->offsetExists('x'));

        unset($dict['a']);
        $this->assertFalse(isset($dict['a']));
        $this->assertSame(1, $dict->count());

        // Unsetting a missing key must not throw (KeyError is swallowed).
        unset($dict['missing']);
        $this->assertSame(1, $dict->count());
    }

    public function testDictReadPropagatesUnhashableKeyError(): void
    {
        $dict = new PyDict(['present' => 1]);

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('unhashable type');
        $dict[new PyList()];
    }

    public function testDictExistsAndUnsetPropagateUnhashableKeyErrors(): void
    {
        $dict = new PyDict(['present' => 1]);

        foreach ([
            static fn() => isset($dict[new PyList()]),
            static function () use ($dict): void {
                unset($dict[new PyList()]);
            },
        ] as $operation) {
            try {
                $operation();
                $this->fail('An unhashable dictionary key must raise PyError');
            } catch (PyError $error) {
                $this->assertStringContainsString('unhashable type', $error->getMessage());
            }
        }

        $this->assertSame(1, $dict['present']);
    }

    public function testSequenceCountPropagatesPythonLengthError(): void
    {
        $object = PyCore::import('app.user')->broken_length_list();
        $sequence = new CoverageGapSequence($object);

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('length failed');
        $sequence->count();
    }

    public function testListOffsetUnset(): void
    {
        $list = new PyList([10, 20, 30]);
        unset($list[1]);
        $this->assertSame([10, 30], $list->toArray());
    }

    public function testListAndTupleBoundaryErrors(): void
    {
        $list = new PyList([10]);
        foreach ([-2, 1] as $index) {
            try {
                $list[$index];
                $this->fail("Reading list index $index must fail");
            } catch (Error $error) {
                $this->assertStringContainsString('out of range', $error->getMessage());
            }

            try {
                $list[$index] = 20;
                $this->fail("Writing list index $index must fail");
            } catch (Error $error) {
                $this->assertStringContainsString('out of range', $error->getMessage());
            }
        }

        $tuple = new PyTuple([10]);
        try {
            $tuple[0] = 20;
            $this->fail('A tuple must reject item writes');
        } catch (Error $error) {
            $this->assertStringContainsString('does not support offsetSet', $error->getMessage());
        }

        try {
            unset($tuple[0]);
            $this->fail('A tuple must reject item deletion');
        } catch (Error $error) {
            $this->assertStringContainsString('does not support offsetUnset', $error->getMessage());
        }
    }

    public function testContainerConstructorsRejectUnsupportedTypes(): void
    {
        foreach ([PyList::class, PyTuple::class, PyDict::class, PySet::class] as $class) {
            try {
                new $class(42);
                $this->fail("$class must reject unsupported constructor input");
            } catch (Error $error) {
                $this->assertStringContainsString('unsupported type', $error->getMessage());
            }
        }
    }

    public function testIterationUsesIteratorProtocol(): void
    {
        $list = new PyList([1, 2, 3]);
        $collected = [];
        foreach ($list as $key => $value) {
            $collected[$key] = $value;
        }
        $this->assertSame([1, 2, 3], $collected);
    }

    public function testPyObjectMethodsCoverTheGenericObjectProtocol(): void
    {
        $module = PyCore::import('app.user');
        $object = $module->protocol_object();

        $this->assertSame('initial', (string) $object->__get('name'));
        $object->__set('name', 'changed');
        $this->assertSame('hello changed!', (string) $object->__call('greet', ['hello']));
        $this->assertSame(7, $object->__invoke(3, right: 4));
        $object->__unset('name');

        $values = $object->__get('values');
        $this->assertSame(10, $values->offsetGet(0));
        $values->offsetSet(1, 25);
        $this->assertTrue($values->offsetExists(1));
        $values->offsetUnset(2);
        $this->assertSame([10, 25], $values->toArray());
        $this->assertSame([10, 25], $values->toValue());
        $this->assertSame(2, $values->count());
        $this->assertSame('[10, 25]', (string) $values);
        $this->assertTrue((bool) $values);
    }

    public function testGenericPyObjectOffsetUnset(): void
    {
        $object = PyCore::import('app.user')->Kv('first', 'second');

        $this->assertTrue($object->offsetExists('first'));
        $object->offsetUnset('first');
        $this->assertFalse($object->offsetExists('first'));

        // Python KeyError follows PHP unset semantics and is ignored.
        $object->offsetUnset('missing');
        $this->addToAssertionCount(1);
    }

    public function testPyObjectIteratorMethodsCanBeCalledDirectly(): void
    {
        $iterator = PyCore::iter(['first', 'second']);

        $iterator->rewind();
        $this->assertTrue($iterator->valid());
        $this->assertSame(0, $iterator->key());
        $this->assertSame('first', (string) $iterator->current());

        $iterator->next();
        $this->assertTrue($iterator->valid());
        $this->assertSame(1, $iterator->key());
        $this->assertSame('second', (string) $iterator->current());

        $iterator->next();
        $this->assertFalse($iterator->valid());
        $this->assertNull($iterator->current());
    }

    public function testPyObjectConstructorAndBooleanCast(): void
    {
        $zero = new PyObject(0);
        $value = new PyObject(42);

        $this->assertFalse((bool) $zero);
        $this->assertTrue((bool) $value);
        $this->assertSame(42, $value->toValue());
    }

    public function testObjectCountIsCountable(): void
    {
        $list = new PyList([1, 2, 3, 4]);
        $this->assertSame(4, count($list));

        $dict = new PyDict(['x' => 1, 'y' => 2, 'z' => 3]);
        $this->assertSame(3, count($dict));
    }

    public function testPyCoreFloat(): void
    {
        $this->assertSame('3.5', (string) PyCore::float(3.5));
        $this->assertSame('2.0', (string) PyCore::float('2.0'));
        $this->assertSame('0.0', (string) PyCore::float());
    }

    public function testPyCoreObject(): void
    {
        $obj = PyCore::object(123);
        $this->assertInstanceOf(\PyObject::class, $obj);

        $empty = PyCore::object();
        $this->assertInstanceOf(\PyObject::class, $empty);
    }

    public function testPyCoreNext(): void
    {
        $builtins = PyCore::import('builtins');
        $iter = $builtins->iter([10, 20, 30]);
        $this->assertSame(10, PyCore::next($iter));
        $this->assertSame(20, PyCore::next($iter));
    }

    public function testPyCoreBytes(): void
    {
        $bytes = PyCore::bytes('hello');
        $this->assertSame('hello', PyCore::scalar($bytes));

        $empty = PyCore::bytes();
        $this->assertSame('', PyCore::scalar($empty));
    }

    public function testPyCoreFileno(): void
    {
        $tmp = tempnam(sys_get_temp_dir(), 'phpy');
        $fp = fopen($tmp, 'r');
        $fd = PyCore::fileno($fp);
        $this->assertIsInt($fd);
        $this->assertGreaterThan(0, $fd);
        fclose($fp);
        unlink($tmp);
    }

    public function testInvokeNonCallableThrows(): void
    {
        // PyObject::__invoke on a non-callable exercises the TypeError branch.
        $this->expectException(PyError::class);
        $s = PyCore::str('hello');
        $s();
    }

    public function testIntFromUnconvertibleThrows(): void
    {
        // PyCore::int on a non-numeric PyObject exercises the PyNumber_Long error branch.
        $this->expectException(PyError::class);
        PyCore::int(new PyList([1, 2]));
    }

    public function testFloatFromUnconvertibleThrows(): void
    {
        $this->expectException(PyError::class);
        PyCore::float(new PyList([1, 2]));
    }
}
