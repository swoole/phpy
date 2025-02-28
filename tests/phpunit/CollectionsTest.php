<?php

use PHPUnit\Framework\TestCase;

class CollectionsTest extends TestCase
{
    public function testNamedTuple()
    {
        $namedtuple = PyCore::import('collections')->namedtuple;
        $Person = $namedtuple('Person', ['name', 'age', 'gender']);
        $p1 = $Person(name: '阮奇桢', age: 40, gender: '男');
        $this->assertEquals('阮奇桢', $p1->name);
        $this->assertEquals(40, $p1->age);
        $this->assertEquals('男', $p1->gender);

        [$name, $age, $gender] = $p1;
        $this->assertEquals(['阮奇桢', 40, '男'], [(string)$name, (int)$age, (string)$gender]);
    }

    public function testCounter()
    {
        $Counter = PyCore::import('collections')->Counter;

        $words = ['red', 'blue', 'red', 'green', 'blue', 'blue'];
        $word_counts = $Counter($words);
        $this->assertEquals(['blue' => 3, 'red' => 2, 'green' => 1], [...PyCore::dict($word_counts)]);
    }
}
