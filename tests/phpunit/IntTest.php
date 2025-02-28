<?php

use PHPUnit\Framework\TestCase;

class IntTest extends TestCase
{
    public function testIntOverflow()
    {
        $i = PyCore::int(12345435);

        $this->assertEquals(strval($i->__pow__(3)), '1881564851360655187875');
    }

    public function testEnum()
    {
        $m = PyCore::import('app.user');
        $v = $m->Color->GREEN;
        $this->assertIsNotInt($v);
        $this->assertEquals($v->value, 3);
    }
}
