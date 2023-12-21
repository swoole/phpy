<?php
$cef = PyCore::import('cefpython3')->cefpython;
$sys = PyCore::import('sys');

function check_version($cef)
{
    $platform = PyCore::import('platform');
    $ver = $cef->GetVersion();
    var_dump(PyCore::scalar($ver));
    echo "[hello_world.py] CEF Python {ver}" . $ver["version"];
    echo "[hello_world.py] Chromium {ver}" . $ver["chrome_version"];
    echo "[hello_world.py] CEF {ver}" . $ver["cef_version"];
    echo "[hello_world.py] Python {ver} {arch}" . $platform->python_version() . ', arch: ' . $platform->architecture()[0];
}

check_version($cef);

$sys->excepthook = $cef->ExceptHook;
$cef->Initialize();

$cef->CreateBrowserSync(
    url: "https://chat.swoole.com/",
    window_title: "Hello World!");

$cef->MessageLoop();
$cef->Shutdown();
