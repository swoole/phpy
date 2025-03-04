<?php
PyCore::print(PyCore::type(3.14));
PyCore::print(PyCore::type(true));
PyCore::print(PyCore::type(null));

$type_int = PyCore::type(1);


$type_list = PyCore::type([1, 2, 3]);
$type_dict = PyCore::type(['a' => 1, 'b' => 2]);
$type_tuple = PyCore::type([1, 2, 3]);

PyCore::print($type_int);
PyCore::print($type_list);
PyCore::print($type_dict);
PyCore::print($type_tuple);

var_dump(PyCore::type(0));

PyCore::print($type_int(9990000));

