<?php

$dict = new PyDict();
const COUNT = 10000000;

$n = COUNT;
$s = microtime(true);
while ($n--) {
    $dict['key-' . $n] = $n * 3;
}
echo 'set from dict: ' . (microtime(true) - $s) . ' seconds' . PHP_EOL;

$c = 0;
$n = COUNT;
$s = microtime(true);
while ($n--) {
    $c += $dict['key-' . $n];
}
echo 'get from dict: ' . (microtime(true) - $s) . ' seconds' . PHP_EOL;
