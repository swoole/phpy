<?php

class PhpyObject
{
    static public string $name = 'empty';
    public $b;

    function __construct(string $b)
    {
        $this->b = $b;
    }

    function test()
    {
        return $this->b;
    }
}
