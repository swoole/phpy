<?php

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$gi = PyCore::import('gi');
$gi->require_version("Gtk", "3.0");
$Gtk = PyCore::import('gi.repository.Gtk');
$builder = $Gtk->Builder();
$builder->add_from_file(__DIR__ . '/test.glade');
$window = $builder->get_object('window1');
$window->set_title("hello world");
$window->show_all();
$handlers = new PyDict([
    "onDestroy" => $Gtk->main_quit,
    "onButtonPressed" => function () {
        echo "hello\n";
    }
]);
$builder->connect_signals($handlers);
$Gtk->main();
