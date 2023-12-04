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
}
