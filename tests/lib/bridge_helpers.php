<?php

/**
 * Helpers for the Python-mode (embed) test suite.
 *
 * These exercise C++ paths in src/python/*.cc that are otherwise only reached
 * through the PHP-facing API: wrapping a PHP Closure as a Python callable,
 * iterating a PHP Traversable/Generator from Python, and objects implementing
 * __invoke.
 */

function phpy_kw_closure()
{
    return function ($a, $b) {
        return $a * 10 + $b;
    };
}

function phpy_test_iter()
{
    return new ArrayIterator(['a' => 1, 'b' => 2, 'c' => 3]);
}

function phpy_gen()
{
    yield 'x';
    yield 'y';
    yield 'z';
}

class PhpyInvokable
{
    public function __invoke($a, $b)
    {
        return $a . '-' . $b;
    }
}
