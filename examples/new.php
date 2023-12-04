<?php
$sys = PyCore::import('sys');
PyCore::import('sys')->path->append(dirname(__DIR__) . '/tests/lib');

$m = PyCore::import('app.user');
$name = uniqid();
$o = $m->User($name);
var_dump($o->echo());
