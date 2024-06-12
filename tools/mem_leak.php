<?php

ini_set('memory_limit', '1G');

$gc = PyCore::import('gc');

class a
{
    public function __construct(
        public array $a
    )
    {
    }
}

// 内存不会持续增长
function test()
{
    $arr = [];

    for ($i = 0; $i < 100000; $i++) {
        $arr[] = $i;
    }

    $a = new a($arr);
}

// 内存会持续增长
function test1()
{
    $arr = [];
    for ($i = 0; $i < 100000; $i++) {
        $arr[] = $i;
    }
    $a = new PyTuple($arr);
    $a[1] = uniqid();
    echo $a[1];

    $a[] = uniqid();

    $a = null;
    unset($a);
}

function test2()
{
    $arr = [];
    for ($i = 0; $i < 10000; $i++) {
        $arr['key-' . $i] = $i;
    }
    $a = new PyDict($arr);
    $a = null;
    unset($a);
}

function test_tuple()
{
    $arr = [];
    for ($i = 0; $i < 100000; $i++) {
        $arr[] = $i;
    }
    $a = new PyTuple($arr);
    $a = null;
    unset($a);
}

$n = 1000;


while ($n--) {
    test_tuple();
    sleep(1);
    var_dump(memory_get_usage());
}
