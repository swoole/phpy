<?php

/**
 * @generate-function-entries
 */

/**
 * @method static print(PyObject $o)
 * @method static exec(string $code, $global = null, $locals = null)
 * @method static type(mixed $value): PyType
 * @method static slice(?int $start = null, ?int $stop = null, ?int $step = null): PyObject
 * @method static list(array $values): PyObject
 * @method static str(string $str): PyStr
 * @method static open(string $filename, string $mode = 'r'): PyObject
 * @method static len(PyObject $o): int
 * @method static iter($uname)
 * @method static range(int $start, int $stop, int $step = 1)
 * @method static dict()
 * @method static isinstance($object, $type): bool
 * @method static tuple(array $array)
 * @method static set(array $array)
 */
class PyCore
{
    public static function import(string $name): mixed
    {

    }

    public static function eval(string $code, ?array $globals = null): mixed
    {

    }

    public static function int(mixed $value): PyObject
    {

    }

    public static function float(mixed $value): PyObject
    {

    }

    public static function bytes(mixed $value = null): PyObject
    {

    }

    public static function object(mixed $value = null): PyObject
    {

    }

    public static function fn(callable $cb): PyObject
    {

    }

    public static function scalar(mixed $value): mixed
    {

    }

    public static function next(PyObject $iter): mixed
    {

    }

    /**
     * @param resource $fp
     */
    public static function fileno($fp): int|false
    {

    }

    public static function setOptions(array $options): void
    {

    }

    public static function raise(PyObject $type, mixed $value = null): void
    {

    }

    public static function __callStatic(string $name, array $arguments): mixed
    {

    }
}
