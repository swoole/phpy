<?php

use phpy\PyClass;


#[parent('Animal', 'animal')]
class Dog extends PyClass
{
    function __construct(string $name, int $age)
    {
        parent::__construct();
        $this->color = 'black';
        $this->super()->__init__($name, $age);
    }

    protected function test()
    {
        debug_print_backtrace();
    }

    function speak(string $name): void
    {
        echo "Dog $name, color: {$this->self()->color}, speak: wang wang wang\n";
        $this->super()->speak('dog');
    }
}
