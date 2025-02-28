<?php

use PHPUnit\Framework\TestCase;

class ZendTest extends TestCase
{
    public function testZendObject()
    {
        $dict = PyCore::dict();
        $zojb = new stdClass();
        $dict['zend_object'] = $zojb;

        $m = PyCore::import('app.user');

        $type = strval($m->get_type($dict, 'zend_object'));
        $this->assertStringStartsWith('<zend_object object at', $type);
    }

    public function testCallMethodInPython()
    {
        $m = PyCore::import('app.user');

        $redis = new redis();
        $redis->connect('127.0.0.1');
        $rs = $m->test_redis($redis);
        $this->assertEquals($rs, 'hello phpy');
    }

    public function testCallFuncInPython()
    {
        $m = PyCore::import('app.phpy');
        $this->assertContains('phpy', $m->test_import());
    }
}
