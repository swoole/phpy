--TEST--
PHP callbacks and Python keyword calls across Zend versions
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

var_dump($module->keywords($add));
?>
--EXPECT--
int(84)
int(42)
int(32)
int(42)
