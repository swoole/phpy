<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$dpg = PyCore::import('dearpygui.dearpygui');

$demo = PyCore::import('dearpygui.demo');

$dpg->create_context();
$dpg->create_viewport(title: "Custom Title", width: 600, height: 600);
$demo->show_demo();
$dpg->setup_dearpygui();
$dpg->show_viewport();
$dpg->start_dearpygui();
$dpg->destroy_context();
