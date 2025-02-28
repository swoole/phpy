<?php

function test_fn_1(int $a, float $b, bool $c, string $d, PyObject $e, PyList $f, PyStr $g): PyList
{
    return PyCore::list([$a, $b, $c, $d, $e, $f, $g]);
}
