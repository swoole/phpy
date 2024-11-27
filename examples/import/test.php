<?php
$sys = PyCore::import('sys');
// Add the directory containing the `fun.py` file to the Python `sys.path`.
$sys->path->append(__DIR__);

$fun = PyCore::import('fun');
$fun->test();

