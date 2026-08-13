<?php

class PhpyObject
{
    public static string $name = 'empty';
    public static array $items = ['stable' => 42];
    public static ?object $sharedObject = null;
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
