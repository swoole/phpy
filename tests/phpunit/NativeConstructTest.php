<?php

use PHPUnit\Framework\TestCase;

/**
 * Covers every branch of the native bridge constructor phpy_construct()
 * (src/bridge/api.cc) through the phpy_test extension.
 *
 * The regular Py* PHP classes (PyList, PyDict, ...) build their Python values
 * inline, so they never reach the native bridge. Only phpy_test_native_construct()
 * dispatches through the api->construct() ABI, which is why the
 * PHPY_NATIVE_CONSTRUCT_DICT/TUPLE/SET/STR/OBJECT/INT/FLOAT/BYTES cases (and the
 * error branches) are exercised here.
 */
final class NativeConstructTest extends TestCase
{
    protected function setUp(): void
    {
        if (!function_exists('phpy_test_native_construct')) {
            $this->markTestSkipped('The native bridge test extension is not loaded');
        }
    }

    public function testConstructList(): void
    {
        $list = phpy_test_native_construct(0, [1, 2, 3]);
        $this->assertInstanceOf(PyList::class, $list);
        $this->assertSame([1, 2, 3], $list->toArray());
    }

    public function testConstructDict(): void
    {
        $dict = phpy_test_native_construct(1, ['a' => 1, 'b' => 2]);
        $this->assertInstanceOf(PyDict::class, $dict);
        $this->assertSame(1, $dict['a']);
        $this->assertSame(2, $dict->count());

        // omitted and empty arguments both produce an empty dict (PyDict_New)
        $this->assertSame(0, phpy_test_native_construct(1)->count());
        $this->assertSame(0, phpy_test_native_construct(1, [])->count());
    }

    public function testConstructDictRejectsUnsupportedType(): void
    {
        $this->expectException(Error::class);
        $this->expectExceptionMessage('PyDict: unsupported type');
        phpy_test_native_construct(1, 42);
    }

    public function testConstructTuple(): void
    {
        $tuple = phpy_test_native_construct(2, [1, 2]);
        $this->assertInstanceOf(PyTuple::class, $tuple);
        $this->assertSame([1, 2], $tuple->toArray());

        $this->assertSame(0, phpy_test_native_construct(2, [])->count());

        // A PyObject sequence argument goes through PySequence_Tuple.
        $fromList = phpy_test_native_construct(2, PyCore::list([7, 8]));
        $this->assertInstanceOf(PyTuple::class, $fromList);
        $this->assertSame([7, 8], $fromList->toArray());
    }

    public function testConstructTupleRequiresArgument(): void
    {
        $this->expectException(ArgumentCountError::class);
        phpy_test_native_construct(2);
    }

    public function testConstructTupleRejectsUnsupportedType(): void
    {
        $this->expectException(Error::class);
        $this->expectExceptionMessage('PyTuple: unsupported type');
        phpy_test_native_construct(2, 42);
    }

    public function testConstructSet(): void
    {
        $set = phpy_test_native_construct(3, [1, 2, 2, 3]);
        $this->assertInstanceOf(PySet::class, $set);
        $this->assertTrue($set->contains(2));
        $this->assertFalse($set->contains(9));
        $this->assertSame(3, $set->count());

        $this->assertSame(0, phpy_test_native_construct(3)->count());
    }

    public function testConstructSetRejectsUnsupportedType(): void
    {
        $this->expectException(Error::class);
        $this->expectExceptionMessage('PySet: unsupported type');
        phpy_test_native_construct(3, 42);
    }

    public function testConstructStr(): void
    {
        $str = phpy_test_native_construct(4, 'hello');
        $this->assertInstanceOf(PyStr::class, $str);
        $this->assertSame('hello', (string) $str);

        // A PyObject string argument goes through PyUnicode_FromObject.
        $fromStr = phpy_test_native_construct(4, PyCore::str('hi'));
        $this->assertInstanceOf(PyStr::class, $fromStr);
        $this->assertSame('hi', (string) $fromStr);
    }

    public function testConstructStrRequiresArgument(): void
    {
        $this->expectException(ArgumentCountError::class);
        phpy_test_native_construct(4);
    }

    public function testConstructStrFromNonStringPyObjectFails(): void
    {
        $this->expectException(PyError::class);
        phpy_test_native_construct(4, PyCore::int(123));
    }

    public function testConstructObject(): void
    {
        $none = phpy_test_native_construct(5);
        $this->assertInstanceOf(PyObject::class, $none);
        $this->assertNull($none->toValue());

        $int = phpy_test_native_construct(5, 42);
        $this->assertInstanceOf(PyObject::class, $int);
        $this->assertSame(42, $int->toValue());

        $str = phpy_test_native_construct(5, PyCore::str('x'));
        $this->assertSame('x', (string) $str);
    }

    public function testConstructInt(): void
    {
        $int = phpy_test_native_construct(6, 42);
        $this->assertInstanceOf(PyObject::class, $int);
        $this->assertSame(42, $int->toValue());

        // php2py('42') + PyNumber_Long
        $fromStr = phpy_test_native_construct(6, '42');
        $this->assertSame(42, $fromStr->toValue());

        // omitted argument -> PyLong_FromLong(0)
        $default = phpy_test_native_construct(6);
        $this->assertSame(0, $default->toValue());
    }

    public function testConstructFloat(): void
    {
        $float = phpy_test_native_construct(7, 3.5);
        $this->assertInstanceOf(PyObject::class, $float);
        $this->assertSame(3.5, $float->toValue());

        // omitted argument -> PyFloat_FromDouble(0.0)
        $this->assertSame(0.0, phpy_test_native_construct(7)->toValue());
    }

    public function testConstructBytes(): void
    {
        $bytes = phpy_test_native_construct(8, 'abc');
        $this->assertInstanceOf(PyObject::class, $bytes);
        $this->assertSame('abc', (string) $bytes);

        $this->assertSame('', (string) phpy_test_native_construct(8));

        // A non-string scalar goes through zval_get_string().
        $fromInt = phpy_test_native_construct(8, 42);
        $this->assertSame('42', (string) $fromInt);
    }

    public function testConstructBytesFromStrPyObjectFails(): void
    {
        $this->expectException(PyError::class);
        phpy_test_native_construct(8, PyCore::str('xyz'));
    }

    public function testConstructUnknownType(): void
    {
        $this->expectException(ValueError::class);
        $this->expectExceptionMessage('Unknown phpy native constructor');
        phpy_test_native_construct(99);
    }
}
