<?php
if (PHP_ZTS) {
    die("not support ZTS.");
}

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$sys = PyCore::import('sys');
$dpg = PyCore::import('dearpygui.dearpygui');

$dpg->create_context();
$dpg->create_viewport();
$dpg->setup_dearpygui();

$sys->path->append(__DIR__);


$app = PyCore::import('app');

$____object = $dpg->window(label: "Example Window");
$__ = $____object->__enter__();
try {
    $dpg->add_text("Hello world");
    $dpg->add_button(label: "Save", callback: $app->wrap(function () {
        PyCore::print("Save Clicked");
    }));
    $dpg->add_input_text(label: "string");
    $dpg->add_slider_float(label: "float");
} finally {
    $____object->__exit__(null, null, null);
}

$dpg->show_viewport();
$dpg->start_dearpygui();
$dpg->destroy_context();

