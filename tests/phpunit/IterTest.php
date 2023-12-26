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

    function testNewIter()
    {
        try {
            new PyIter;
        } catch (Error $error) {
            $this->assertStringContainsString('private PyIter::__construct()', $error->getMessage());
            $success = false;
        }
        $this->assertFalse($success);
    }
}
