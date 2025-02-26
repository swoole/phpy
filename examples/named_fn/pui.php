<?php

define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');

require ROOT_PATH . '/vendor/autoload.php';
$pui = PyCore::import('PUI.PySide6');

#[Annotation('PUIApp')]
#[Import('PUI.PySide6', 'PUIApp')]
function Example(): void
{
    global $pui;
    $window = $pui->Window(title: "test", size: [320, 240]);
    $window->__enter__();
    try {
        $pui->Label("Hello world");
    } finally {
        $window->__exit__(null, null, null);
    }
}

PyClass::setProxyPath(__DIR__, true);
$root = PyNamedFn('Example')();
$root->run();
