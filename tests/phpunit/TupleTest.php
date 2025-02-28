<?php


use PHPUnit\Framework\TestCase;

class TupleTest extends TestCase
{
    private function test($list, $v1, $v2)
    {
        $tuple = new PyTuple($list);

        $this->assertEquals($tuple->count(), 4);
        $array = PyCore::scalar($tuple);
        $this->assertTrue($tuple->contains($v1));
        $this->assertTrue($tuple->contains($v2));
        $this->assertContains($v1, $array);
        $this->assertContains($v2, $array);
        $this->assertEquals($tuple[3], 12345);

        $this->assertEquals($tuple->index($v1), 1);
        $this->assertEquals($tuple->index($v2), 2);

        $slice = $tuple->slice(1, 3);
        $this->assertEquals(PyCore::scalar($slice), [$v1, $v2]);

        $this->assertTrue(isset($tuple[1]));
        $this->assertFalse(isset($tuple[5]));
        $this->assertFalse(isset($tuple[-1]));
    }

    public function testList()
    {
        $list = new PyList();
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);

        $list[] = 2;
        $list[] = $v1;
        $list[] = $v2;
        $list[] = 12345;

        $this->test($list, $v1, $v2);
    }

    public function testArray()
    {
        $list = [];
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);

        $list[] = 2;
        $list[] = $v1;
        $list[] = $v2;
        $list[] = 12345;

        $this->test($list, $v1, $v2);
    }
}
