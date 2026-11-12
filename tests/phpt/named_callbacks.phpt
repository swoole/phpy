--TEST--
Named PHP callbacks bind declared parameters and fill skipped user defaults
--SKIPIF--
<?php if (!extension_loaded('phpy')) die('skip phpy extension required'); ?>
--FILE--
<?php
$module = PyCore::eval(<<<'PY'
def skipped(fn):
    return fn(c=22, a=20)

def mixed(fn):
    return fn(20, c=22)

def internal(fn):
    return fn(needle="c", haystack="abc")
PY
);

class Callback {
    private const DEFAULT_B = 10;

    public function add($a, &$b = self::DEFAULT_B, $c = 0) {
        return [$a, ++$b, $c];
    }

    public function __invoke($a, $b = 10, $c = 0, ...$rest) {
        return $a + $b + $c;
    }
}

$callback = new Callback();
$method = PyCore::fn([$callback, 'add']);
echo implode(',', $module->skipped($method)), "\n";
echo implode(',', $module->mixed($method)), "\n";
var_dump($module->skipped($callback));
var_dump($module->internal(PyCore::fn('strpos')));
?>
--EXPECT--
20,11,22
20,11,22
int(52)
int(2)
