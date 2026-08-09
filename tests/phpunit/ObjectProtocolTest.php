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
}
