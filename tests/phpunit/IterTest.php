<?php

use PHPUnit\Framework\TestCase;

class IterTest extends TestCase
{
    function testIter()
    {
        $os = PyCore::import('os');
        $uname = $os->uname();

        $iter = PyCore::iter($uname);
        $this->assertTrue($iter instanceof PyIter);

        $list = [];
        while ($next = PyCore::next($iter)) {
            $list[] = PyCore::scalar($next);
        }
        $this->assertIsArray($list);
        $this->assertEquals(count($list), 5);
    }
}
