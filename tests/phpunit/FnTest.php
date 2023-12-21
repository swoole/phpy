<?php

use PHPUnit\Framework\TestCase;

class FnTest extends TestCase
{
    function testFn()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
            $this->assertEquals($namespace, 'app.user');
            return $uuid;
        }));
        $this->assertEquals($rs, $uuid);
    }

    function testClosure()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $rs = $m->test_callback(function ($namespace) use ($uuid) {
            $this->assertEquals($namespace, 'app.user');
            return $uuid;
        });
        $this->assertEquals($rs, $uuid);
    }

    function testObjectInvoke()
    {
        $m = PyCore::import('app.user');
        $uuid = uniqid();
        $obj = new class($this, $uuid) {
            private $phpunit;
            private $uuid;

            function __construct($phpunit, $uuid)
            {
                $this->phpunit = $phpunit;
                $this->uuid = $uuid;
            }

            function __invoke($namespace)
            {
                $this->phpunit->assertEquals($namespace, 'app.user');
                return $this->uuid;
            }
        };
        $rs = $m->test_callback($obj);
        $this->assertEquals($rs, $uuid);
    }

    function testObjectNotInvoke()
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

}
