<?php


use PHPUnit\Framework\TestCase;

class DictTest extends TestCase
{
    public function testDict()
    {
        $dict = new PyDict();
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

    public function testKeyNotString()
    {
        $pycode = <<<CODE
key1 = ("sum", "数量")
key2 = ("mean", "数量")
dict_data = {key1: 1, key2: 2}
CODE;
        $json = json_encode(PyCore::scalar(PyCore::eval($pycode)->dict_data));
        $result = "{\"('sum', '\u6570\u91cf')\":1,\"('mean', '\u6570\u91cf')\":2}";
        $this->assertEquals($json, $result);
    }

    public function testUb1()
    {
        $this->assertEmpty((new PyDict())->current());
    }

    public function testUb2()
    {
        $this->assertEmpty((new PyDict())->key());
    }
}
