<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$os = PyCore::import('os');
foreach ($_ENV as $k => $v) {
    $os->environ[$k] = $v;
}
$gr = PyCore::import('gradio');
$demo = $gr->Interface(fn: function ($name, $intensity) {
    return str_repeat("Hello ", $intensity) . $name . "!";
}, inputs: new PyList(["text", "slider"]), outputs: new PyList(["text"]));
$demo->launch();
