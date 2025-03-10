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

function PyEnum(string $class): PyObject
{
    return (new PyEnum($class))->getPyEnum();
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

function PyImport($module, $from = '')
{
    if ($from === '') {
        return PyCore::import($module);
    } else {
        return PyCore::import($from)->$module;
    }
}

function PyStr($str): PyStr
{
    return new PyStr($str);
}

function PyDict(array $data = []): PyDict
{
    return new PyDict($data);
}

function PyList(array $data = []): PyList
{
    return new PyList($data);
}

function PyTuple(array $data = []): PyTuple
{
    return new PyTuple($data);
}

function PySet(array $data = []): PySet
{
    return new PySet($data);
}

function PySlice(int $start, int $stop, ?int $step = null): PyObject
{
    return PyCore::slice($start, $stop, $step);
}

function PyRange(int $start, int $stop, int $step = 1): PyObject
{
    return PyCore::range($start, $stop, $step);
}

function PyInt($value): PyObject
{
    return PyCore::int($value);
}

function PyFloat($value): PyObject
{
    return PyCore::float($value);
}

function PyLen(PyObject $object): int|PyObject
{
    return PyCore::len($object);
}

function PyNext($iterator)
{
    return PyCore::next($iterator);
}

function PyOpen(string|PyStr $filename, string $mode = 'r'): PyObject
{
    return PyCore::open($filename, $mode);
}

function PyPrint(): void
{
    PyCore::print(...func_get_args());
}

function PyFn(callable $cb): PyFn
{
    return new PyFn($cb);
}