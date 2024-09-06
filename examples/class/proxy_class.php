<?php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
require __DIR__ . '/Dog.php';

PyCore::import('sys')->path->append('.');

\phpy\PyClass::setProxyPath(__DIR__, true);

$dog = new Dog('dog', 1);
$dog->speak('hello');
var_dump($dog->age);
$dog->age = 3;
var_dump($dog->get_age());
