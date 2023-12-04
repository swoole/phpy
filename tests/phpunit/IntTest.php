<?php

use PHPUnit\Framework\TestCase;

class IntTest extends TestCase
{
    function testIntOverflow()
    {
        $i = PyCore::int(12345435);

        $this->assertEquals(strval($i->__pow__(3)), '1881564851360655187875');
    }
}
