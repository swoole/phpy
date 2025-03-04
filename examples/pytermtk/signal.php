<?php
define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');

require ROOT_PATH . '/vendor/autoload.php';

PyClass::setProxyPath(ROOT_PATH, true);

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$ttk = PyCore::import('TermTk');

$ttk->TTkLog->use_default_stdout_logging();
$signal = $ttk->pyTTkSignal();
$otherSignal = $ttk->pyTTkSignal(PyCore::type(0));



#[PyAnnotation("@ttk.pyTTkSlot()")]
#[PyImport('ttk', 'TermTk')]
function slot()
{
    global $ttk;
    $ttk->TTkLog->debug("Received a simple signal");
}

#[PyAnnotation("ttk.pyTTkSlot()")]
#[PyImport('ttk', 'TermTk')]
function otherSlot($val)
{
    global $ttk;
    $ttk->TTkLog->debug("[otherSlot] Received a valued signal, val:" . $val);
}

#[PyAnnotation("ttk.pyTTkSlot()")]
#[PyImport('ttk', 'TermTk')]
function anotherSlot($val)
{
    global $ttk;
    $ttk->TTkLog->debug("[anootherSlot] Received a valued signal, val:" . $val);
}


try {
    $signal->connect(PyNamedFn('slot'));
    $otherSignal->connect(PyNamedFn('otherSlot'));
    $otherSignal->connect(PyNamedFn('anotherSlot'));
    $ttk->TTkLog->debug("Emit a simple signal");
    $signal->emit();
    $ttk->TTkLog->debug("Emit a valued signal");
    $otherSignal->emit(123);
} catch (PyError $e) {
    echo $e->getMessage();
    PyCore::print($e->error);
}



