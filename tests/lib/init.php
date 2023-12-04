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

var_dump(__DIR__);

$list = ["hello", "world", 2024];
$map = ['hello' => 'swoole', 'day' => date('Y-m-d'), 'data' => $list];

return $map;
