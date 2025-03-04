<?php

/**
 * @param string $fnName
 * @return PyObject
 * @throws Exception
 */
function PyNamedFn(string $fnName): PyObject
{
    return (new PyNamedFn($fnName))->getPyFn();
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
