<?php

function PyNamedFn(string $fnName): PyObject
{
    return (new PyNamedFn($fnName))->get();
}

function PyWith(callable $fn, ...$objects): void
{
    $targets = [];
    foreach ($objects as $object) {
        $targets[] = $object->__enter__();
    }
    try {
        $fn(...$targets);
    } finally {
        foreach ($objects as $object) {
            $object->__exit__(null, null, null);
        }
    }
}
