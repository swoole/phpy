<?php
define('ROOT_PATH', dirname(__DIR__, 2));
require ROOT_PATH . '/vendor/autoload.php';

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$np = PyCore::import('numpy');

$arr = $np->arange(100)->reshape(10, 10);
$key = PyTuple([PySlice(1, 5), PySlice(1, 5)]);
PyPrint($arr[$key]);
