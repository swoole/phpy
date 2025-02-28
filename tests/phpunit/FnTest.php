<?php

use PHPUnit\Framework\TestCase;

class FnTest extends TestCase
{
    public function testFn()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
            $this->assertEquals($namespace, 'app.user');
            return $uuid;
        }));
        $this->assertEquals($rs, $uuid);
    }

    public function testClosure()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $rs = $m->test_callback(function ($namespace) use ($uuid) {
            $this->assertEquals($namespace, 'app.user');
            return $uuid;
        });
        $this->assertEquals($rs, $uuid);
    }

    public function testObjectInvoke()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $obj = new FnCallableClass($this, $uuid);
        $rs = $m->test_callback($obj);
        $this->assertEquals($rs, $uuid);
    }

    public function testObjectNotInvoke()
    {
        $m = PyCore::import('app.user');
        $obj = new stdClass();
        $success = true;
        try {
            @$m->test_callback($obj);
            $this->assertTrue(false);
        } catch (PyError $error) {
            $this->assertStringContainsString('zend_object is not callable', $error->getMessage());
            if (PHP_VERSION_ID >= 80200) {
                $this->assertStringContainsString('Invalid callback', $error->getPrevious()->getMessage());
            }
            $success = false;
        }
        $this->assertFalse($success);
    }

    public function testObjectErrorArgs()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $success = true;
        $obj = new FnCallableClass($this, $uuid);
        try {
            $rs = $m->test_callback(fn () => [$obj, 'test']());
        } catch (PyError $error) {
            $this->assertStringContainsString('Function call failed', $error->getMessage());
            $this->assertStringContainsString('Too few arguments', $error->getPrevious()->getMessage());
            $success = false;
        }
        $this->assertFalse($success);
    }

    public function testCtor()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $fn = new PyFn(function ($namespace) use ($uuid) {
            $this->assertEquals($namespace, 'app.user');
            return $uuid;
        });
        $rs = $m->test_callback($fn);
        $this->assertEquals($rs, $uuid);
    }
}
