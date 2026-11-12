--TEST--
PHP 7.4 rejects ambiguous or unsupported named callback arguments
--SKIPIF--
<?php
if (!extension_loaded('phpy')) die('skip phpy extension required');
if (PHP_VERSION_ID >= 80000) die('skip PHP 7.4 compatibility branch only');
?>
--FILE--
<?php
$module = PyCore::eval(<<<'PY'
def check(fn, mode):
    try:
        if mode == "unknown":
            fn(a=1, extra=2)
        elif mode == "duplicate":
            fn(1, a=2)
        elif mode == "missing":
            fn(b=2)
        elif mode == "internal":
            fn([1, 2], 0, preserve_keys=True)
        else:
            fn(a=1)
    except TypeError as error:
        return str(error)
    return "call completed"
PY
);

$calls = 0;
$fn = static function ($a, $b = 0, ...$rest) use (&$calls) {
    ++$calls;
    return $a + $b;
};
foreach (['unknown', 'duplicate', 'missing'] as $mode) {
    echo $module->check($fn, $mode), "\n";
}
echo $module->check(PyCore::fn('array_slice'), 'internal'), "\n";
echo $module->check($fn, 'valid'), "\n";
var_dump($calls);
?>
--EXPECT--
Unknown PHP callback parameter $extra
PHP callback parameter $a was supplied more than once
Missing required PHP callback parameter 1
Cannot fill default for PHP callback parameter 3 on PHP 7.4
call completed
int(1)
