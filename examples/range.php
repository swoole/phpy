<?php
$py = PyCore::import('builtins');
$array = PyCore::scalar($py->range(3));
var_dump($array);

var_dump(PyCore::scalar(PyCore::range(5)));

var_dump(PyCore::scalar(PyCore::range(7)));

var_dump(PyCore::scalar(PyCore::range(4, 2)));
