<?php
define('ROOT_PATH', dirname(__DIR__, 2));
require ROOT_PATH . '/vendor/autoload.php';
require ROOT_PATH . '/tests/lib/Dog.php';

PyCore::import('sys')->path->append(ROOT_PATH . '/tests/lib');

PyClass::setProxyPath(ROOT_PATH, true);

$dog = new Dog('dog', 1);
$dog->speak('hello');
var_dump($dog->age);
$dog->age = 3;
var_dump($dog->get_age());
