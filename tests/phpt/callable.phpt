--TEST--
Positional PHP callbacks and Python keyword calls across Zend versions
--SKIPIF--
<?php if (!extension_loaded('phpy')) die('skip phpy extension required'); ?>
--FILE--
<?php
$module = PyCore::eval(<<<'PY'
def apply_twice(fn):
    return fn(20, 22) + fn(19, 23)

def add(a, *, b):
    return a + b

def keywords(fn):
    return fn(b=22, a=20)
PY
);

$add = static function ($a, $b) {
    return $a + $b;
};

var_dump($module->apply_twice($add));
var_dump($module->__call('add', [20, 'b' => 22]));
$pow = PyCore::import('builtins')->pow;
var_dump($pow(2, 5));

if (PHP_VERSION_ID < 80000) {
    $called = false;
    try {
        $module->keywords(static function ($a, $b) use (&$called) {
            $called = true;
        });
        throw new RuntimeException('Expected PHP 7.4 to reject named callback arguments');
    } catch (Throwable $error) {
        var_dump(strpos((string) $error, 'Calling PHP functions with named arguments requires PHP 8') !== false && !$called);
    }
} else {
    var_dump($module->keywords($add) === 42);
}
?>
--EXPECT--
int(84)
int(42)
int(32)
bool(true)
