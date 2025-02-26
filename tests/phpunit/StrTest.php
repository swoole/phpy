<?php


use PHPUnit\Framework\TestCase;

class StrTest extends TestCase
{
    public function testStr()
    {
        $str = new PyStr("hello world, hello swoole");
        $this->assertTrue($str->endswith('swoole'));
        $this->assertTrue($str->startswith('hello'));
        $this->assertFalse($str->endswith('golang'));

        $s2 = $str->replace('swoole', 'java');
        $this->assertTrue($s2->endswith('java'));
    }

    public function testBytes()
    {
        $os = PyCore::import('os');
        $bytes = PyCore::scalar($os->urandom(128));
        $this->assertEquals(128, strlen($bytes));
    }

    public function testOffsetGet()
    {
        $str = new PyStr("我是中国人");
        $this->assertEquals($str[0], '我');
        $this->assertEquals($str[2], '中');
        $this->assertEquals($str[PyCore::slice(2, 4)], '中国');
    }

    public function testSlice()
    {
        $s = new PyStr("Python Programming");
        $this->assertEquals($s[PyCore::slice(0, 3)], "Pyt");
        $this->assertEquals($s[PyCore::slice(7, 12)], "Progr");
        $this->assertEquals($s[PyCore::slice(null, null, null)], "Python Programming");
        $this->assertEquals($s[PyCore::slice(null, null, 2)], "Pto rgamn");
        $this->assertEquals($s[PyCore::slice(null, null, -1)], "gnimmargorP nohtyP");
        $this->assertEquals($s[PyCore::slice(-1, null)], "g");
        $this->assertEquals($s[PyCore::slice(-3, -1)], "in");
    }
}
