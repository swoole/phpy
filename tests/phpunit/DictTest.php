<?php


use PHPUnit\Framework\TestCase;

class DictTest extends TestCase
{
    public function testDict()
    {
        $dict = new PyDict;
        $dict['hello'] = uniqid();

        $this->assertTrue(isset($dict['hello']));
        $this->assertFalse(isset($dict['golang']));

        unset($dict['hello']);
        $this->assertFalse(isset($dict['hello']));

        $n = 10;
        while ($n--) {
            $dict['key-' . $n] = uniqid();
        }

        $this->assertEquals(10, $dict->count());
    }

    public function testIter()
    {
        $map = [];
        $dict = new PyDict();
        $n = 10;
        while ($n--) {
            $key = 'key-' . $n;
            $value = uniqid();
            $map[$key] = $value;
            $dict[$key] = $value;
        }
        $keys = [];
        foreach ($dict as $k => $v) {
            $keys[] = $k;
            $this->assertEquals($v, $map[$k]);
        }
        $this->assertEquals($keys, array_keys($map));
    }

    public function testIterInt()
    {
        $map = [];
        $dict = new PyDict();
        $n = 10;
        while ($n--) {
            $key = random_int(1, 1 << 31);
            $value = uniqid();
            $map[$key] = $value;
            $dict[$key] = $value;
        }
        $keys = [];
        foreach ($dict as $k => $v) {
            $keys[] = $k;
            $this->assertEquals($v, $map[$k]);
        }
        $this->assertEquals($keys, array_keys($map));
    }
}
