<?php

PyCore::import('sys')->path->append('.');

$types = PyCore::import('types');

$Animal = PyCore::import('animal')->Animal;
$Dog = $types->new_class(
    'Dog',
    (PyCore::tuple([$Animal])),
    []
);

$dog = $Dog('狗', 1);
$dog->speak = $types->MethodType(function ($self, $name) use ($Animal, $Dog) {
    PyCore::print("My name is {$self->name}, age is {$self->age}");
    $super = PyCore::super($Dog, $self);
    $super->speak('dog');
}, $dog);
$dog->speak('哈士奇');
