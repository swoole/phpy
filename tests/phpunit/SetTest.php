<?php


use PHPUnit\Framework\TestCase;

class SetTest extends TestCase
{
    private function test($set, $v1, $v2)
    {
        $this->assertEquals($set->count(), 3);
        $array = PyCore::scalar($set);
        $this->assertTrue($set->contains($v1));
        $this->assertTrue($set->contains($v2));
        $this->assertContains($v1, $array);
        $this->assertContains($v2, $array);
    }

    public function testSet()
    {
        $set = new PySet();
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);
        $set->add(2);
        $set->add($v1);
        $set->add($v2);
        $set->add(2);

        $this->test($set, $v1, $v2);
    }

    public function testSetCtor()
    {
        $list = [];
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);
        $list[] = 2;
        $list[] = $v1;
        $list[] = $v2;
        $list[] = 2;

        $set = new PySet($list);
        $this->test($set, $v1, $v2);
    }

    public function testUb1()
    {
        $this->assertEmpty((new PySet())->current());
    }

    public function testUb2()
    {
        $this->assertEmpty((new PySet())->key());
    }
}
