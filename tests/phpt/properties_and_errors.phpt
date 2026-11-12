--TEST--
PHP property access, Python exception properties and serialization restrictions
--SKIPIF--
<?php if (!extension_loaded('phpy')) die('skip phpy extension required'); ?>
--FILE--
<?php
$module = PyCore::eval(<<<'PY'
def update(obj):
    obj.set("value", obj.get("value") + 2)
    return obj.get("value")

def fail():
    raise ValueError("bridge failure")

item = object()
PY
);

$obj = (object) ['value' => 40];
var_dump($module->update($obj), $obj->value);

try {
    $module->fail();
} catch (PyError $error) {
    var_dump($error->getMessage(), $error->type instanceof PyObject, $error->value instanceof PyObject);
}

try {
    serialize($module->item);
} catch (Exception $error) {
    var_dump(strpos($error->getMessage(), 'not allowed') !== false);
}
?>
--EXPECT--
int(42)
int(42)
string(14) "bridge failure"
bool(true)
bool(true)
bool(true)
