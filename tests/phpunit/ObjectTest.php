<?php


use PHPUnit\Framework\TestCase;

class ObjectTest extends TestCase
{
    protected function assertForKwargs($inst)
    {
        $today = date('Y-m-d');
        $this->assertEquals(strval($inst->args['a']), 'a');
        $this->assertEquals(strval($inst->args['name']), 'default_name');
        $this->assertEquals(strval($inst->args['date']), $today);
    }

    public function testKwargs()
    {
        $user = PyCore::import('app.user');
        $class = $user->KwargsCtor;
        // __invoke
        $inst = $class('a', 'b', date: date('Y-m-d'));
        $this->assertForKwargs($inst);
        // __call
        $inst = $user->KwargsCtor('a', 'b', date: date('Y-m-d'));
        $this->assertForKwargs($inst);
    }

    public function testGetItem()
    {
        $user = PyCore::import('app.user');
        $kv = $user->KvReadonly('ikey', 'skey');
        $this->assertEquals($kv['ikey'], 123456);
        $this->assertEquals($kv['skey'], 'hello');
        try {
            $kv['skey'] = 'world';
        } catch (\PyError $error) {
            $this->assertStringContainsString('object does not support item assignment', $error->getMessage());
        }
        $this->assertTrue(isset($kv['ikey']));
        $this->assertTrue(isset($kv['skey']));
        $this->assertFalse(isset($kv[uniqid()]));

        var_dump(get_class($kv));
    }

    public function testSetItem()
    {
        $user = PyCore::import('app.user');
        $kv = $user->Kv('ikey', 'skey');
        $this->assertEquals($kv['ikey'], 123456);
        $this->assertEquals($kv['skey'], 'hello');
        $val = uniqid();
        $kv['val'] = $val;
        $this->assertEquals($kv['val'], $val);
        $this->assertArrayHasKey('ikey', $kv);
        $this->assertArrayNotHasKey('ikey2', $kv);
    }

    public function testCount()
    {
        $user = PyCore::import('app.user');
        $kv = $user->KvReadonly('ikey', 'skey');
        $this->assertEquals(-1, count($kv));

        $kvc = $user->KvCount('ikey', 'skey');
        $this->assertEquals(2, count($kvc));
    }

    public function testIter()
    {
        $arr = [1, 2, 3, 7, 8];
        $fset = PyCore::frozenset($arr);
        $data = iterator_to_array($fset);
        $this->assertEquals($data, $arr);
    }

    public function testBytes2Str()
    {
        $bytes = random_bytes(128);
        $data = PyCore::bytes($bytes);
        $this->assertEquals($bytes, strval($data));
    }

    public function testInvalidArgs()
    {
        $user = PyCore::import('app.user');
        try {
            $user->test_str_concat('hello', random_bytes(128));
        } catch (\PyError $error) {
            $this->assertStringContainsString("'utf-8' codec can't decode byte", $error->getMessage());
        }
    }
}
