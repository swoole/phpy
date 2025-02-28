<?php


use PHPUnit\Framework\TestCase;

class ListTest extends TestCase
{
    public function testList()
    {
        $list = new PyList();
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);

        $list[] = 2;
        $list[] = $v1;
        $list[] = $v2;
        $list[] = 12345;

        $this->assertEquals($list->count(), 4);
        $array = PyCore::scalar($list);
        $this->assertTrue($list->contains($v1));
        $this->assertTrue($list->contains($v2));
        $this->assertContains($v1, $array);
        $this->assertContains($v2, $array);
        $this->assertEquals($list[3], 12345);

        $list[3] = 9999;
        $this->assertEquals($list[3], 9999);

        $this->assertEquals($list->index($v1), 1);
        $this->assertEquals($list->index($v2), 2);

        $slice = $list->slice(1, 3);
        $this->assertEquals(PyCore::scalar($slice), [$v1, $v2]);
    }

    public function testIterator()
    {
        $c = 10;
        $n = $c;
        $list = new PyList();
        $values = [];
        while ($n--) {
            $s = uniqid();
            $list[] = $s;
            $values[] = $s;
        }

        $iter_keys = [];
        $iter_values = [];
        foreach ($list as $k => $v) {
            $iter_keys[] = $k;
            $iter_values[] = strval($v);
        }
        $this->assertSame($iter_values, $values);
        $this->assertSame($iter_keys, array_keys($values));
    }

    public function testCtor()
    {
        $list = new PyList([1, 3, 5, 7, 9]);

        $this->assertEquals($list->count(), 5);
        $this->assertEquals($list->index(9), 4);
    }

    public function testUb1()
    {
        $list = new PyList([1, 2, 3, 4]);
        $this->assertEmpty($list->current());
    }

    public function testUb2()
    {
        $list = new PyList([1, 2, 3, 4]);
        $this->assertEmpty($list->next());

        foreach ($list as $l) {
            $this->assertEquals($l, $list->current());
            $list->next();
            $this->assertNotEquals($l, $list->current());
        }
    }
}
