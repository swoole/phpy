<?php
require dirname(__DIR__, 2) . '/vendor/autoload.php';
require __DIR__ . '/Dog.php';

PyCore::import('sys')->path->append('.');

$dog = new Dog('dog', 1);
$dog->speak('hello');
