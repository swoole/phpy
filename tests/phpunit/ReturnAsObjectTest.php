<?php

final class ReturnAsObjectTest extends PHPUnit\Framework\TestCase
{
    protected function tearDown(): void
    {
        PyCore::setOptions(['return_as_object' => false]);
    }

    public function testPythonScalarResultsCanRemainWrappedObjects(): void
    {
        PyCore::setOptions(['return_as_object' => true]);
        $builtins = PyCore::import('builtins');

        $this->assertInstanceOf(PyObject::class, $builtins->len([1, 2, 3]));
        $this->assertInstanceOf(PyObject::class, $builtins->bool(1));
        $this->assertInstanceOf(PyObject::class, $builtins->print());
    }

    public function testReturnAsObjectIsDisabledByDefault(): void
    {
        $builtins = PyCore::import('builtins');

        $this->assertSame(3, $builtins->len([1, 2, 3]));
        $this->assertTrue($builtins->bool(1));
        $this->assertNull($builtins->print());
    }

    public function testNumericConstructorsUsePythonConversionSemantics(): void
    {
        $this->assertSame(42, PyCore::scalar(PyCore::int('42')));
        $this->assertSame(0, PyCore::scalar(PyCore::int()));
        $this->assertSame(2.5, PyCore::scalar(PyCore::float(new PyStr('2.5'))));
        $this->assertSame(0.0, PyCore::scalar(PyCore::float()));
    }
}
