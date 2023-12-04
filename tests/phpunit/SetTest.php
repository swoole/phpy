<?php


use PHPUnit\Framework\TestCase;

class SetTest extends TestCase
{
    public function testSet()
    {
        $set = new PySet();
        $v1 = random_int(1000, 99999);
        $v2 = random_int(1000, 99999);
        $set->add(2);
        $set->add($v1);
        $set->add($v2);
        $set->add(2);

        $this->assertEquals($set->count(), 3);
        $array = PyCore::scalar($set);
        $this->assertTrue($set->contains($v1));
        $this->assertTrue($set->contains($v2));
        $this->assertContains($v1, $array);
        $this->assertContains($v2, $array);
    }
}
