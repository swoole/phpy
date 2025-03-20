<?php

define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');

require ROOT_PATH . '/vendor/autoload.php';
$pui = PyCore::import('PUI.PySide6');

#[PyAnnotation('PUIApp')]
#[PyImport('PUIApp', 'PUI.PySide6')]
function Example(): void
{
    global $pui;
    PyWith(function ($target) use ($pui) {
        $pui->Label("Hello world");
    }, $pui->Window(title: "test", size: [320, 240]));
}

PyClass::setProxyPath(ROOT_PATH, true);
$root = PyNamedFn('Example')();
$root->run();
