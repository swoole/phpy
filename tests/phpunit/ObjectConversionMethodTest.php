<?php

use PHPUnit\Framework\TestCase;

final class ObjectConversionMethodTest extends TestCase
{
    protected function setUp(): void
    {
        PyCore::setOptions(['return_as_object' => true]);
    }

    protected function tearDown(): void
    {
        PyCore::setOptions(['return_as_object' => false]);
    }

    public function testToValueMatchesScalarConversion(): void
    {
        $value = new PyDict([
            'items' => [1, 2, 3],
            'enabled' => true,
        ]);

        $this->assertSame(PyCore::scalar($value), $value->toValue());
    }

    public function testToArrayConvertsSupportedContainers(): void
    {
        $this->assertSame([1, 2, 3], (new PyList([1, 2, 3]))->toArray());
        $this->assertSame([1, 2, 3], (new PyTuple([1, 2, 3]))->toArray());
        $this->assertSame(['name' => 'phpy'], (new PyDict(['name' => 'phpy']))->toArray());

        $set = (new PySet([1, 2, 3]))->toArray();
        sort($set);
        $this->assertSame([1, 2, 3], $set);
    }

    public function testToArrayConsumesPythonIterator(): void
    {
        $iterator = PyCore::iter(new PyList([1, 2, 3]));

        $this->assertSame([1, 2, 3], $iterator->toArray());
        $this->assertSame([], $iterator->toArray());
    }

    public function testToArrayReturnsEmptyArrayForUnsupportedValues(): void
    {
        $this->assertSame([], PyCore::int(42)->toArray());
        $this->assertSame([], PyCore::str('phpy')->toArray());
        $this->assertSame([], PyCore::import('sys')->toArray());
    }
}
