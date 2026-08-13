<?php

use PHPUnit\Framework\TestCase;

final class PhpyTest extends TestCase
{
    protected function setUp(): void
    {
        if (!function_exists('phpy_test_native_call_member')) {
            $this->markTestSkipped('The native bridge test extension is not loaded');
        }
    }

    public function testCallMemberSupportsPositionalAndNamedArguments(): void
    {
        $object = PyCore::import('app.user')->protocol_object();

        $this->assertSame(
            'hello initial?',
            (string) phpy_test_native_call_member($object, 'greet', 'hello', suffix: '?'),
        );
    }

    public function testCallInvokesPythonCallable(): void
    {
        $callable = PyCore::import('app.user')->protocol_object();

        $this->assertSame(7, phpy_test_native_call($callable, 3, right: 4));
    }

    public function testNativeRuntimeConfigurationCanBeChangedAndRestored(): void
    {
        try {
            $this->assertTrue(phpy_test_native_configure_runtime(true));
            $this->assertInstanceOf(PyObject::class, PyCore::import('builtins')->len([1, 2]));
        } finally {
            phpy_test_native_configure_runtime(false);
        }

        $this->assertSame(2, PyCore::import('builtins')->len([1, 2]));
    }

    public function testNativeConstructorCreatesPhpPyObjects(): void
    {
        $list = phpy_test_native_construct(0, [1, 2, 3]);

        $this->assertInstanceOf(PyList::class, $list);
        $this->assertSame([1, 2, 3], $list->toArray());
    }

    public function testBridgeCoreHelpers(): void
    {
        $this->assertGreaterThan(0, phpy_test_bridge_mode());
        $this->assertSame(42, phpy_test_bridge_number_to_long(42));
        $this->assertSame(3, phpy_test_bridge_number_to_long(3.9));

        putenv('PHPY_BRIDGE_TEST=enabled');
        try {
            $this->assertTrue(phpy_test_bridge_env_equals('PHPY_BRIDGE_TEST', 'ENABLED'));
            $this->assertFalse(phpy_test_bridge_env_equals('PHPY_BRIDGE_TEST', 'disabled'));
            $this->assertFalse(phpy_test_bridge_env_equals('PHPY_BRIDGE_TEST_MISSING', 'enabled'));
        } finally {
            putenv('PHPY_BRIDGE_TEST');
        }
    }

    public function testDumpHelpersCanBeCalled(): void
    {
        phpy_test_bridge_dump_helpers(['value' => 42]);
        $this->addToAssertionCount(1);
    }
}
