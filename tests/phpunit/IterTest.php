<?php

use PHPUnit\Framework\TestCase;

class IterTest extends TestCase
{
    function testIter()
    {
        $platform = PyCore::import('platform');
        $uname = $platform->uname();

        $iter = PyCore::iter($uname);
        $this->assertTrue($iter instanceof PyIter);

        $list = [];
        while ($next = PyCore::next($iter)) {
            $list[] = PyCore::scalar($next);
        }
        $this->assertIsArray($list);
        $this->assertGreaterThanOrEqual(5, count($list));
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
