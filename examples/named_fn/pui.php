<?php

define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');

require ROOT_PATH . '/vendor/autoload.php';
$pui = PyCore::import('PUI.PySide6');

#[Annotation('PUIApp')]
#[Import('PUI.PySide6', '*')]
function Example()
{
    global $pui;
    $____object = $pui->Window(title: "test", size: [320, 240]);
    $__ = $____object->__enter__();
    try {
        $pui->Label("Hello world");
    } finally {
        $____object->__exit__(null, null, null);
    }
}

PyClass::setProxyPath(__DIR__, true);
$fn = PyNamedFn('Example');
$root = $fn();
$root->run();
