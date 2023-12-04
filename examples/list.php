<?php
function main()
{
    $list = new PyList;

    $n = 10;
    while ($n--) {
        $list[] = uniqid();
    }

    echo "foreach [1]\n";
    foreach ($list as $k => $v) {
        var_dump($k, strval($v));
    }

    echo "foreach [2]\n";
    foreach ($list as $k => $v) {
        var_dump($k, strval($v));
    }
}

main();
