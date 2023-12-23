<?php
/**
 * 简化对PyCore::iter和PyCore::next的使用
 */
function iter($res)
{
    $iter = PyCore::iter($res);
    while (!is_null($value = PyCore::next($iter))) {
        yield $value;
    }
}

foreach (iter(PyCore::range(3)) as $v) {
    echo $v . PHP_EOL;
}
