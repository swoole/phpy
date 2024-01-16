<?php

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$t = PyCore::import('turtle');
$t->pensize(2);
$d = 0;
$__iter = PyCore::iter(PyCore::range(1, 13));
while ($current = PyCore::next($__iter)) {
    $i = $current;
    $t->forward(40);
    $d += 30;
    $t->seth($d);
}
$t->done();
