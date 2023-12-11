<?php
require dirname(__DIR__) . '/vendor/autoload.php';
function main()
{
    $m = python\os::import();
    var_dump($m instanceof PyObject);
    $rs = $m->uname();
    echo $rs;
    echo $rs->version;
    echo PHP_EOL;
}

main();
