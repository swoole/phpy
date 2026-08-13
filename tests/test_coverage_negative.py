"""
Negative-path / error-branch coverage tests for the Python-embed mode of phpy.

These exercise the TypeError / ValueError / RuntimeError branches and the
remaining happy paths in src/python/*.cc (and a few shared bridge paths) that
are not hit by the basic positive tests: bad constructor args, unknown
classes/methods/functions, wrong-typed operands, missing include files,
class static property access, and a callable that throws.
"""

import pytest
import phpy

_INIT = r"""
class PhpyKw {
    public $prop = 'init';
    public function add($a, $b) { return $a * 10 + $b; }
}
class PhpyCover {
    public static $sp = 'orig';
    public $inst = 'made';
    public function __construct() {}
    public function noargs() { return 'ok'; }
}
function phpy_throwing_closure() {
    return function () { throw new Exception('boom'); };
}
"""
phpy.eval(_INIT)


# --------------------------------------------------------------------------
# zend_string: wrong-typed operands / comparisons / membership
# --------------------------------------------------------------------------

def test_string_ctor_bad_type():
    # String_init only accepts str / bytes; other types raise.
    with pytest.raises(TypeError):
        phpy.String(123)
    with pytest.raises(TypeError):
        phpy.String(object())
    with pytest.raises(TypeError):
        phpy.String(bytearray(b"x"))


def test_string_concat_wrong_type():
    s = phpy.String("a")
    with pytest.raises(TypeError):
        _ = s + 5
    with pytest.raises(TypeError):
        s += 5


def test_string_compare_non_string():
    s = phpy.String("a")
    # String_compare returns NotImplemented for non-string operand -> Python
    # falls back to identity, so it is never equal and always not-equal.
    assert (s == 5) is False
    assert (s != 5) is True


def test_string_contains_wrong_type():
    s = phpy.String("a")
    with pytest.raises(TypeError):
        _ = 5 in s


# --------------------------------------------------------------------------
# zend_object: bad ctor / method / property access
# --------------------------------------------------------------------------

def test_object_ctor_errors():
    with pytest.raises(TypeError):
        phpy.Object()
    with pytest.raises(TypeError):
        phpy.Object(123)
    with pytest.raises(TypeError):
        phpy.Object("NoSuchClassXYZ999")


def test_object_method_errors():
    o = phpy.Object("PhpyKw")
    with pytest.raises(TypeError):
        o.call()
    with pytest.raises(TypeError):
        o.call(123)
    # Object_invoke on a non-invokable object -> not-callable error
    with pytest.raises(TypeError):
        o("a", "b")
    with pytest.raises(TypeError):
        o.get(123)
    with pytest.raises(TypeError):
        o.set(123, "x")


# --------------------------------------------------------------------------
# zend_class: bad ctor / static property access
# --------------------------------------------------------------------------

def test_class_ctor_errors():
    with pytest.raises(TypeError):
        phpy.Class()
    with pytest.raises(TypeError):
        phpy.Class("NoSuchClassXYZ999")


def test_class_static_prop_access():
    c = phpy.Class("PhpyCover")
    with pytest.raises(TypeError):
        c.get(123)
    with pytest.raises(TypeError):
        c.set(123, "x")
    # happy paths: instantiate, read + write a static property
    inst = c.new()
    assert type(inst) is phpy.Object
    assert str(c.get("sp")) == "orig"
    assert c.set("sp", "changed") is True
    assert str(c.get("sp")) == "changed"


# --------------------------------------------------------------------------
# module helpers: bad args / missing function / include
# --------------------------------------------------------------------------

def test_call_no_args_and_unknown():
    with pytest.raises(TypeError):
        phpy.call()
    with pytest.raises(NameError):
        phpy.call("no_such_function_xyz_999")


def test_include_errors():
    # missing file -> returns False (open-failure path)
    assert phpy.include("./tests/nonexistent_xyz.php") is False
    with pytest.raises(TypeError):
        phpy.include(123)


def test_set_options_bad_arg():
    with pytest.raises(TypeError):
        phpy.setOptions("not-a-dict")


# --------------------------------------------------------------------------
# iterable: non-traversable object
# --------------------------------------------------------------------------

def test_iter_non_traversable():
    with pytest.raises(TypeError):
        iter(phpy.Object("PhpyKw"))


# --------------------------------------------------------------------------
# callable: a closure that throws propagates as RuntimeError
# --------------------------------------------------------------------------

def test_callable_throws():
    cb = phpy.call("phpy_throwing_closure")
    with pytest.raises(RuntimeError):
        cb()


# --------------------------------------------------------------------------
# zend_array: delitem + missing-key access
# --------------------------------------------------------------------------

def test_array_delitem_and_missing_key():
    arr = phpy.Array([1, 2, 3])
    # mp_ass_subscript with NULL value -> Array_delitem; removing index 0
    # leaves keys 1,2 (non-list) so collect() yields a dict.
    del arr[0]
    assert arr.collect() == {1: 2, 2: 3}
    # out-of-range / missing key -> None (Array_getitem miss path)
    assert arr[99] is None
    assert arr["missing"] is None
