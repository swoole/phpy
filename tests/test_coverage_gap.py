"""
Coverage-gap tests for the Python-embed mode of phpy.

Targets C++ paths in src/python/*.cc and src/bridge/core.cc that are not
exercised by the basic tests: zend_array OO API + iteration, zend_reference,
zend_resource, zend_string rich ops, phpy module helpers (constant/eval/
globals/scalar/setOptions), phpy.Class static props edge cases, phpy.Object
method call with keyword args, and iterator over Traversable/Generator.
"""

import gc
import pytest
import phpy


# Helper PHP definitions reachable from Python.
_INIT = r"""
class PhpyKw {
    public $prop = 'init';
    public function add($a, $b) {
        return $a * 10 + $b;
    }
}
function &phpy_ref() {
    static $x = 42;
    return $x;
}
function phpy_ref_set($value) {
    $x =& phpy_ref();
    $x = $value;
}
function phpy_ref_same(&$value) {
    $x =& phpy_ref();
    return \ReflectionReference::fromArrayElement([&$x, &$value], 0)->getId()
        === \ReflectionReference::fromArrayElement([&$x, &$value], 1)->getId();
}
function phpy_obj() {
    return new PhpyKw();
}
function phpy_call_typed_closure(Closure $fn, $a, $b) {
    return $fn($a, $b);
}
function phpy_get_sys_module() {
    return PyCore::import('sys');
}
function phpy_module_name($m) {
    return (string) $m->__name__;
}
function phpy_is_float($v) {
    return is_float($v) ? 1 : 0;
}
function phpy_type_name($v) {
    return is_object($v) ? get_class($v) : gettype($v);
}
class PhpyBadCtor {
    public function __construct() {
        throw new Exception("ctor boom");
    }
}
"""
phpy.eval(_INIT)
phpy.include("./tests/lib/bridge_helpers.php")


# --------------------------------------------------------------------------
# zend_array
# --------------------------------------------------------------------------

def test_array_from_php_return_new_array():
    # phpy.call returning an array wraps it via new_array(zval*)
    arr = phpy.call("array_keys", {"x": 1, "y": 2})
    assert type(arr) is phpy.Array
    # array_keys returns a list-shaped array -> array2list path in Array_collect
    assert arr.collect() == ["x", "y"]


def test_array_collect_dict():
    # assoc array -> array2dict path in Array_collect
    arr = phpy.Array({"k": "v", "n": 7})
    assert arr.collect() == {"k": "v", "n": 7}


def test_array_iterate_string_keys():
    # Iterating a zend_array yields its KEYS (Array_next).
    arr = phpy.Array({"a": 1, "b": 2, "c": 3})
    assert list(arr) == ["a", "b", "c"]
    # A list-shaped array yields its numeric indices.
    lst = phpy.Array(["x", "y", "z"])
    assert list(lst) == [0, 1, 2]


def test_array_oo_set_append_unset():
    arr = phpy.Array([1, 2, 3])
    # Array_set (OO method) with a numeric key -> Array_setitem long-index path
    assert arr.set(1, 99) is True
    assert arr.get(1) == 99
    # append + unset
    assert arr.append(4) is True
    assert arr.is_list() is True
    assert arr.unset(0) is True
    assert arr.count() == 3
    # After removing index 0 the keys are 1,2,3 -> no longer a list.
    assert arr.is_list() is False
    # non-list array -> array2dict path, keys preserved
    assert arr.collect() == {1: 99, 2: 3, 3: 4}


def test_array_collect_list():
    arr = phpy.Array([10, 20, 30])
    assert arr.collect() == [10, 20, 30]


def test_array_dtor_on_gc():
    arr = phpy.Array([1, 2, 3])
    arr.append(4)
    del arr
    gc.collect()
    # Just ensure no crash / leak report during teardown.
    assert True


# --------------------------------------------------------------------------
# zend_reference
# --------------------------------------------------------------------------

def test_reference_from_php():
    # The Python carrier shares the original zend_reference rather than a
    # snapshot of its current value.
    r = phpy.call("phpy_ref")
    assert type(r) is phpy.Reference
    assert r.get() == 42
    phpy.call("phpy_ref_set", 99)
    assert r.get() == 99
    assert phpy.call("phpy_ref_same", r) is True

    del r
    gc.collect()
    assert phpy.call("phpy_ref").get() == 99


def test_reference_local():
    r = phpy.Reference()
    assert r.get() is None


def test_reference_dtor_releases_zval():
    # Reference_dtor runs when a ZendReference wrapper is garbage-collected,
    # freeing the copied zend_reference zval. Creating and dropping many
    # wrappers must not crash, and the PHP-side static reference must stay
    # usable afterwards (its container is shared, not stolen).
    phpy.call("phpy_ref_set", 42)
    for _ in range(5):
        r = phpy.call("phpy_ref")
        assert r.get() == 42
        del r
        gc.collect()
    assert phpy.call("phpy_ref").get() == 42

    local = phpy.Reference()
    assert local.get() is None
    del local
    gc.collect()
    assert phpy.call("phpy_ref").get() == 42


# --------------------------------------------------------------------------
# zend_resource
# --------------------------------------------------------------------------

def test_resource_from_php():
    f = phpy.call("fopen", "/tmp/phpy_cov.txt", "w")
    assert type(f) is phpy.Resource
    assert phpy.call("fclose", f) is True
    del f
    gc.collect()


# --------------------------------------------------------------------------
# zend_string
# --------------------------------------------------------------------------

def test_string_at_out_of_range():
    s = phpy.String("hello")
    assert s[0] == ord("h")
    with pytest.raises(IndexError):
        _ = s[100]


def test_string_compare_ops():
    s = phpy.String("hello")
    assert s == phpy.String("hello")
    # op != Py_EQ -> String_compare returns NotImplemented, Python falls back
    assert (s != phpy.String("zzz")) is True
    # Py_LT (unsupported) returns NotImplemented -> Python raises TypeError
    with pytest.raises(TypeError):
        _ = s < phpy.String("z")


def test_string_bytes_and_inplace_concat():
    s = phpy.String("hi")
    assert bytes(s) == b"hi"
    s2 = phpy.String("a")
    s2 += "b"
    s2 += b"c"
    assert str(s2) == "abc"


def test_string_bytearray_operands():
    # bytearray operands exercise the PyByteArray_Check branch of
    # string2char_ptr (concat, in-place concat, and membership).
    assert str(phpy.String("hi") + bytearray(b" there")) == "hi there"
    s = phpy.String("a")
    s += bytearray(b"b")
    assert str(s) == "ab"
    assert (b"b" in s) is True
    assert (b"z" in s) is False


def test_string_contains():
    s = phpy.String("hello world")
    assert ("world" in s) is True
    assert ("xyz" in s) is False


def test_string_from_bytes():
    s = phpy.String(b"raw")
    assert str(s) == "raw"


# --------------------------------------------------------------------------
# phpy module helpers
# --------------------------------------------------------------------------

def test_constant_missing():
    assert phpy.constant("NONEXISTENT_CONST_XYZ_123") is None


def test_eval_ok_and_error():
    assert phpy.eval('echo "hi";') == 0
    with pytest.raises(RuntimeError, match="Unclosed"):
        phpy.eval("$x = [")
    with pytest.raises(RuntimeError, match="x"):
        phpy.eval('throw new Exception("x");')
    # Transferring the PHP exception must leave the executor usable.
    assert phpy.call("strlen", "abc") == 3


def test_globals_missing():
    assert phpy.globals("DEFINITELY_NOT_A_GLOBAL_XYZ") is None


def test_scalar_roundtrip():
    assert phpy.scalar(123) == 123
    assert phpy.scalar("abc") == "abc"


def test_set_options():
    assert phpy.setOptions({"numeric_as_object": True}) is None
    assert phpy.setOptions({"return_as_object": False}) is None
    # argument_as_object / display_exception branches in phpy_setOptions
    assert phpy.setOptions({"argument_as_object": True}) is None
    assert phpy.setOptions({"display_exception": True}) is None
    assert phpy.setOptions({"argument_as_object": False, "display_exception": False}) is None


def test_globals_and_eval_bad_args():
    # PyArg_ParseTuple failure branches in phpy_globals / phpy_eval
    with pytest.raises(TypeError):
        phpy.globals(123)
    with pytest.raises(TypeError):
        phpy.eval(123)


def test_scalar_container_arrays():
    # py2py_scalar routes dict/set/list/tuple through new_array(PyObject*),
    # exercising the Python-object overload in array.cc.
    for value in ([1, 2, 3], {"a": 1}, (1, 2), {1, 2}):
        assert type(phpy.scalar(value)) is phpy.Array


def test_scalar_bytes_and_bytearray():
    # py2py_scalar routes bytes/bytearray through new_string(PyObject*),
    # covering the PyBytes_Check / PyByteArray_Check branches in string.cc.
    assert str(phpy.scalar(b"abc")) == "abc"
    assert str(phpy.scalar(bytearray(b"xy"))) == "xy"


def test_object_passed_back_to_php():
    # Passing a phpy.Object back into PHP exercises zend_object_cast in
    # try_convert_python_base_value (object.cc / core.cc).
    o = phpy.Object("PhpyKw")
    assert str(phpy.call("get_class", o)) == "PhpyKw"
    # A PHP function returning a plain object hits the generic branch of
    # new_object(zval*) (neither closure, phpy-object, nor traversable).
    wrapped = phpy.call("phpy_obj")
    assert type(wrapped) is phpy.Object
    assert wrapped.call("add", 3, 7) == 37


def test_object_bad_constructor():
    # object_create() reports a failing PHP constructor as a TypeError.
    with pytest.raises(TypeError):
        phpy.Object("PhpyBadCtor")


def test_call_internal():
    assert phpy.call("abs", -5) == 5
    assert phpy.call("strlen", "hello") == 5


# --------------------------------------------------------------------------
# phpy.Class
# --------------------------------------------------------------------------

def test_class_static_prop_missing():
    c = phpy.Class("PhpyObject")
    assert c.get("no_such_static_prop") is None


# --------------------------------------------------------------------------
# phpy.Object
# --------------------------------------------------------------------------

def test_object_method_call_and_invoke_kwargs():
    o = phpy.Object("PhpyKw")
    # Object_call (positional method args)
    assert o.call("add", 3, 7) == 37
    # property get/set via Object_get / Object_set
    o.set("prop", "changed")
    assert o.get("prop") == "changed"


def test_object_invokable():
    o = phpy.Object("PhpyInvokable")
    # Object_invoke (tp_call) dispatches to __invoke; all tuple args are passed
    # positionally to __invoke. Return value is a PHP string wrapped as a
    # zend_string, so compare via str().
    assert str(o("a", "b")) == "a-b"
    # Object_invoke with keyword args exercises the named_params path in call_fn.
    assert str(o(a="x", b="y")) == "x-y"


def test_module_preserved_as_object():
    # PyModule_CheckExact branch of PythonToPhpConverter::convertPreservingObjects:
    # with argument_as_object enabled, a Python module argument is wrapped as a
    # phpy PyModule (new_module) when it crosses back into PHP.
    module = phpy.call("phpy_get_sys_module")
    assert type(module).__name__ == "module"
    phpy.setOptions({"argument_as_object": True})
    try:
        assert str(phpy.call("phpy_module_name", module)) == "sys"
    finally:
        phpy.setOptions({"argument_as_object": False})


def test_set_preserved_as_object():
    # PySet_CheckExact branch of PythonToPhpConverter::convertPreservingObjects:
    # with argument_as_object enabled, a Python set argument is wrapped as a
    # phpy PySet (new_set) when it crosses back into PHP.
    phpy.setOptions({"argument_as_object": True})
    try:
        assert phpy.call("phpy_type_name", {1, 2, 3}) == "PySet"
    finally:
        phpy.setOptions({"argument_as_object": False})


def test_scalar_float_with_numeric_as_object():
    # convertRecursively's PyFloat_Check branch: with numeric_as_object
    # enabled, try_convert_python_base_value skips the float, so it is
    # converted to a PHP double here instead.
    phpy.setOptions({"numeric_as_object": True})
    try:
        assert phpy.call("phpy_is_float", 3.5) == 1
    finally:
        phpy.setOptions({"numeric_as_object": False})


def test_arbitrary_object_arg_wrapped_as_pyobject():
    # convertRecursively's else branch: an arbitrary Python object (a module)
    # passed with the default argument_as_object=false is wrapped as a
    # PyObject via new_object.
    module = phpy.call("phpy_get_sys_module")
    assert phpy.call("phpy_type_name", module) == "PyObject"


# --------------------------------------------------------------------------
# iterable (Traversable / Generator)
# --------------------------------------------------------------------------

def test_traversable_values():
    it = phpy.call("phpy_test_iter")
    assert list(it) == [1, 2, 3]


def test_generator_values():
    gen = phpy.call("phpy_gen")
    assert list(gen) == ["x", "y", "z"]


# --------------------------------------------------------------------------
# callable (closure, positional + keyword args)
# --------------------------------------------------------------------------

def test_closure_positional_and_keyword():
    cb = phpy.call("phpy_kw_closure")
    assert cb(3, 7) == 37
    assert cb(a=3, b=7) == 37


def test_closure_passed_back_to_php_closure_hint():
    # A ZendCallable (PHP closure wrapped in Python) passed back into PHP is
    # restored to the original PHP closure via zend_callable_cast, so a
    # function with a Closure type hint accepts it.
    cb = phpy.call("phpy_kw_closure")
    assert phpy.call("phpy_call_typed_closure", cb, 3, 7) == 37


def test_array_rejects_iterable_raising_during_iteration():
    # An iterator whose __next__ raises mid-iteration sets a Python error, so
    # convertIterable's PyErr_Occurred branch calls discard_result().
    class BadIter:
        def __init__(self):
            self.n = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.n == 1:
                raise ValueError("iter boom")
            self.n += 1
            return self.n

    with pytest.raises(ValueError, match="iter boom"):
        phpy.Array(BadIter())


def test_array_rejects_dict_raising_during_iteration():
    # A dict subclass whose iterator raises after the first key sets a Python
    # error, hitting convertDictionary's PyErr_Occurred branch.
    class D(dict):
        def __iter__(self):
            yield "a"
            raise ValueError("dict iter boom")

    with pytest.raises(ValueError, match="dict iter boom"):
        phpy.Array(D({"a": 1}))


def test_array_rejects_key_with_failing_string_conversion():
    # A dict key whose __str__ raises makes StrObject fail, hitting the
    # zval_ptr_dtor(&item) + discard_result() branch of convertDictionary.
    class BadKey:
        def __hash__(self):
            return 1

        def __str__(self):
            raise ValueError("bad str")

    with pytest.raises(ValueError, match="bad str"):
        phpy.Array({BadKey(): "v"})
