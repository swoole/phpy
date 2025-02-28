<?php

use PHPUnit\Framework\TestCase;

class IterTest extends TestCase
{
    public function testIter()
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

    public function testNewIter()
    {
        try {
            new PyIter();
        } catch (Error $error) {
            $this->assertStringContainsString('private PyIter::__construct()', $error->getMessage());
            $success = false;
        }
        $this->assertFalse($success);
    }

    public function testNextInt()
    {
        $array = [];
        $__iter = PyCore::iter(PyCore::range(1, 13));
        while ($current = PyCore::next($__iter)) {
            $this->assertIsInt($current);
            $array[] = $current;
        }
        $this->assertEquals($array, range(1, 12));
    }

    public function testNotIterable()
    {
        $slice = PyCore::slice(1, 10);
        try {
            $iter = PyCore::iter($slice);
        } catch (PyError $error) {
            $this->assertStringContainsString("'slice' object is not iterable", $error->getMessage());
        }
    }
}
