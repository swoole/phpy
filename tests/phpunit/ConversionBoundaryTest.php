<?php

final class ConversionBoundaryTest extends PHPUnit\Framework\TestCase
{
    public function testNestedPhpValuesRoundTripThroughPython(): void
    {
        $builtins = PyCore::import('builtins');
        $value = ['nested' => [null, true, 42, 1.5, '你好', ['name' => 'phpy']]];

        $this->assertSame($value, PyCore::scalar($builtins->dict($value)));
        $this->assertSame([], PyCore::scalar($builtins->list([])));
    }

    public function testInvalidUtf8IsReportedAsPythonError(): void
    {
        $this->expectException(PyError::class);
        PyCore::import('builtins')->repr("\xff");
    }

    public function testRecursivePhpArrayIsRejected(): void
    {
        $recursive = [];
        $recursive['self'] = &$recursive;

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('recursive PHP array');
        PyCore::import('builtins')->repr($recursive);
    }

    public function testRecursivePythonContainerIsRejectedByScalarConversion(): void
    {
        $recursive = new PyList();
        $recursive[] = $recursive;

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('recursive Python container');
        PyCore::scalar($recursive);
    }

    public function testUnencodablePythonDictionaryKeyFailsCleanly(): void
    {
        $module = PyCore::import('app.user');

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('surrogates not allowed');
        PyCore::scalar($module->unencodable_key_dict());
    }

    public function testNestedCallbackCannotChangeOuterConversionPolicy(): void
    {
        $module = PyCore::import('app.user');
        $value = $module->reentrant_list(static function (): PyList {
            // This performs an object-preserving conversion while the outer
            // scalar conversion is suspended in Python's iterator protocol.
            return PyCore::import('builtins')->list(['nested']);
        });

        $this->assertSame(['first', 'second'], PyCore::scalar($value));
    }

    public function testFailedContainerConversionsReleaseCompletedElements(): void
    {
        PyCore::setOptions(['return_as_object' => false]);
        $sys = PyCore::import('sys');
        $sentinel = PyCore::object();
        $before = $sys->getrefcount($sentinel);

        for ($i = 0; $i < 20; $i++) {
            foreach ([PyList::class, PyTuple::class, PySet::class] as $class) {
                try {
                    new $class([$sentinel, "\xff"]);
                    $this->fail("$class conversion must fail");
                } catch (PyError) {
                }
            }

            try {
                new PyDict(['sentinel' => $sentinel, 'invalid' => "\xff"]);
                $this->fail('PyDict conversion must fail');
            } catch (PyError) {
            }
        }

        $this->assertSame($before, $sys->getrefcount($sentinel));
    }
}
