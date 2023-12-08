<?php

use PHPUnit\Framework\TestCase;

class ZendTest extends TestCase
{
    function testZendObject()
    {
        $dict = PyCore::dict();
        $zojb = new stdClass();
        $dict['zend_object'] = $zojb;

        $m = PyCore::import('app.user');

        $type = strval($m->get_type($dict, 'zend_object'));
        $this->assertStringStartsWith('<zend_object object at', $type);
    }
}
