<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$gi = PyCore::import('gi');
$gi->require_version("Gtk", "3.0");
$Gtk = PyCore::import('gi.repository.Gtk');
$win = $Gtk->Window(title: "Hello World");
$win->connect("destroy", $Gtk->main_quit);
$win->show_all();
$Gtk->main();
