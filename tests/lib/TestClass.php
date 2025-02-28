<?php

class TestClass
{
    public array $array = [];

    public function __construct(string $a, int $b, float $c, array $d, array $e)
    {
        $this->array[] = $a;
        $this->array[] = $b;
        $this->array[] = $c;
        $this->array[] = $d;
        $this->array[] = $e;
    }
}
