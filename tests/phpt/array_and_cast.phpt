--TEST--
PHP arrays and Python object casts across Zend versions
--SKIPIF--
<?php if (!extension_loaded('phpy')) die('skip phpy extension required'); ?>
--FILE--
<?php
$module = PyCore::eval(<<<'PY'
def shape(value):
    return type(value).__name__

class Item:
    def __init__(self, truth):
        self.truth = truth

    def __str__(self):
        return "item"

    def __bool__(self):
        return self.truth
PY
);

foreach ([[], [10, 20], [0 => 10, 2 => 20], [1 => 20, 0 => 10], ['key' => 10]] as $value) {
    echo $module->shape($value), "\n";
}

$truthy = $module->Item(true);
$falsy = $module->Item(false);
var_dump((string) $truthy, (bool) $truthy, (bool) $falsy);
?>
--EXPECT--
list
list
dict
dict
dict
string(4) "item"
bool(true)
bool(false)
