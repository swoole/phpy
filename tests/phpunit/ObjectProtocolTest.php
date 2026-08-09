<?php

use PHPUnit\Framework\TestCase;

final class ObjectProtocolTest extends TestCase
{
    protected function setUp(): void
    {
        PyCore::setOptions(['return_as_object' => true]);
    }

    protected function tearDown(): void
    {
        PyCore::setOptions(['return_as_object' => false]);
    }

    public function testAttributesMethodsCallableAndNamedArguments(): void
    {
        $object = PyCore::import('app.user')->protocol_object();

        $this->assertSame('initial', PyCore::scalar($object->name));
        $object->name = 'changed';
        $this->assertSame('hello changed?', PyCore::scalar($object->greet('hello', suffix: '?')));
        $this->assertSame(7, PyCore::scalar($object(3, right: 4)));

        unset($object->name);
        try {
            $object->name;
            $this->fail('Reading a deleted Python attribute must fail');
        } catch (PyError $error) {
            $this->assertStringContainsString("has no attribute 'name'", $error->getMessage());
        }
    }

    public function testCallingNonCallablePythonValuesRaisesPyError(): void
    {
        $object = PyCore::import('app.user')->protocol_object();

        try {
            $object->name();
            $this->fail('Calling a non-callable Python attribute must fail');
        } catch (PyError $error) {
            $this->assertStringContainsString('not callable', $error->getMessage());
        }

        try {
            $object->name();
            $this->fail('Repeated failures must not leave stale Python error state');
        } catch (PyError $error) {
            $this->assertStringContainsString('not callable', $error->getMessage());
        }
    }

    public function testInvokingNonCallablePyObjectRaisesPyError(): void
    {
        $integer = PyCore::import('builtins')->int(42);

        try {
            $integer();
            $this->fail('Invoking a non-callable PyObject must fail');
        } catch (PyError $error) {
            $this->assertStringContainsString('not callable', $error->getMessage());
        }
    }

    public function testGeneralObjectItemProtocolUsesIssetSemantics(): void
    {
        $object = PyCore::import('app.user')->protocol_object();

        $this->assertTrue(isset($object->values[0]));
        $this->assertFalse(isset($object->values[99]));
        $object->values[-1] = 40;
        $this->assertSame(40, PyCore::scalar($object->values[-1]));
        unset($object->values[-1]);
        $this->assertSame([10, 20], PyCore::scalar($object->values));
    }

    public function testListSupportsNegativeIndexesAndDeletion(): void
    {
        $list = new PyList([10, 20, 30]);

        $this->assertTrue(isset($list[-1]));
        $this->assertFalse(isset($list[-4]));
        $this->assertSame(30, PyCore::scalar($list[-1]));
        $list[-1] = 40;
        unset($list[-2]);

        $this->assertSame([10, 40], PyCore::scalar($list));
    }

    public function testIssetTreatsPythonNoneAsNullAndTupleUsesPythonIndexes(): void
    {
        $list = new PyList([null, 20]);
        $tuple = new PyTuple([null, 20]);

        $this->assertFalse(isset($list[0]));
        $this->assertTrue(isset($list[-1]));
        $this->assertFalse(isset($tuple[0]));
        $this->assertTrue(isset($tuple[-1]));
        $this->assertSame(20, PyCore::scalar($tuple[-1]));
    }

    public function testDictionaryMissingKeyIsNotAnExceptionForIsset(): void
    {
        $dict = new PyDict(['present' => 1]);

        $this->assertTrue(isset($dict['present']));
        $this->assertFalse(isset($dict['missing']));
        unset($dict['present']);
        $this->assertFalse(isset($dict['present']));

        $dict['none'] = null;
        $this->assertFalse(isset($dict['none']));
    }

    public function testIteratorFailurePropagatesAsPyError(): void
    {
        $iterator = PyCore::import('app.user')->broken_iterator();

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('iterator failed');
        foreach ($iterator as $value) {
        }
    }

    public function testPyCoreNextPropagatesIteratorFailure(): void
    {
        $iterator = PyCore::import('app.user')->broken_iterator();

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('iterator failed');
        PyCore::next($iterator);
    }

    public function testPyCoreNextReleasesYieldedReferences(): void
    {
        $module = PyCore::import('app.user');
        $sys = PyCore::import('sys');
        $sentinel = $module->next_sentinel;
        $iterator = $module->repeated_sentinel(20);
        $before = PyCore::scalar($sys->getrefcount($sentinel));
        $iteratorBefore = PyCore::scalar($sys->getrefcount($iterator));

        for ($i = 0; $i < 20; $i++) {
            $value = PyCore::next($iterator);
            unset($value);
        }

        $this->assertSame($before, PyCore::scalar($sys->getrefcount($sentinel)));
        $this->assertSame($iteratorBefore, PyCore::scalar($sys->getrefcount($iterator)));
        $this->assertNull(PyCore::next($iterator));
    }

    public function testRepeatedPythonExceptionsReleaseFetchedReferences(): void
    {
        $module = PyCore::import('app.user');
        $builtins = PyCore::import('builtins');
        $sys = PyCore::import('sys');
        $runtimeError = $builtins->RuntimeError;

        // Warm up Python and Zend exception metadata before measuring it.
        try {
            $module->raise_runtime_error();
        } catch (PyError $error) {
            unset($error);
        }
        gc_collect_cycles();
        $before = PyCore::scalar($sys->getrefcount($runtimeError));

        for ($i = 0; $i < 20; $i++) {
            try {
                $module->raise_runtime_error();
            } catch (PyError $error) {
                unset($error);
            }
        }
        gc_collect_cycles();

        $this->assertSame($before, PyCore::scalar($sys->getrefcount($runtimeError)));
    }

    public function testRepeatedImportsReleaseTheOwnedModuleReference(): void
    {
        $sys = PyCore::import('sys');
        $before = PyCore::scalar($sys->getrefcount($sys));

        for ($i = 0; $i < 20; $i++) {
            $module = PyCore::import('sys');
            unset($module);
        }

        $this->assertSame($before, PyCore::scalar($sys->getrefcount($sys)));
    }

    public function testFailedItemConversionDoesNotCorruptContainers(): void
    {
        $invalidUtf8 = "\xff";
        $list = new PyList([1]);
        $dict = new PyDict(['key' => 1]);
        $object = PyCore::import('app.user')->Kv('first', 'second');

        $this->assertConversionFails(static fn() => $list[0] = $invalidUtf8);
        $this->assertConversionFails(static fn() => $dict[$invalidUtf8] = 2);
        $this->assertConversionFails(static fn() => $object[$invalidUtf8] = 2);

        $this->assertSame([1], PyCore::scalar($list));
        $this->assertSame(['key' => 1], PyCore::scalar($dict));
        $object['valid'] = 3;
        $this->assertSame(3, PyCore::scalar($object['valid']));
    }

    public function testFailedConstructorConversionRaisesPyError(): void
    {
        $invalidUtf8 = "\xff";

        $this->assertConversionFails(static fn() => new PyList([$invalidUtf8]));
        $this->assertConversionFails(static fn() => new PyDict(['value' => $invalidUtf8]));
        $this->assertConversionFails(static fn() => new PyTuple([$invalidUtf8]));
        $this->assertConversionFails(static fn() => new PySet([$invalidUtf8]));
    }

    public function testContainsConversionAndPythonErrorsPropagate(): void
    {
        $invalidUtf8 = "\xff";
        $list = new PyList([1]);
        $set = new PySet([1]);

        $this->assertConversionFails(static fn() => $list->contains($invalidUtf8));
        $this->assertConversionFails(static fn() => $set->contains($invalidUtf8));

        try {
            $set->contains([]);
            $this->fail('An unhashable set member must raise PyError');
        } catch (PyError $error) {
            $this->assertStringContainsString('unhashable type', $error->getMessage());
        }
    }

    private function assertConversionFails(callable $operation): void
    {
        try {
            $operation();
            $this->fail('Invalid UTF-8 must fail conversion');
        } catch (PyError $error) {
            $this->assertStringContainsString('decode', $error->getMessage());
        }
    }
}
