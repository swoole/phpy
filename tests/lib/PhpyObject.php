<?php

class PhpyObject
{
    public static string $name = 'empty';
    public $b;

    public function __construct(string $b)
    {
        $this->b = $b;
    }

    public function test()
    {
        return $this->b;
    }
}
