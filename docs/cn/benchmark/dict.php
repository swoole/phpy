<?php

$dict = new PyDict();
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'dict set: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'dict get: ' . round(microtime(true) - $s, 6) . ' seconds' . PHP_EOL;
