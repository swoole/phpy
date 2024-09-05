<?php

use phpy\PyClass;


#[parent('Animal', 'animal')]
class Dog extends PyClass
{
    function __construct(string $name, int $age)
    {
        parent::__construct();
        $this->self()->color = 'black';
        $this->super()->__init__($name, $age);
    }

    function speak(string $name): void
    {
        echo "Dog $name, color: {$this->self()->color}, speak: wang wang wang\n";
        $this->super()->speak('dog');
    }
}
