import subprocess
import sys

import pytest

import phpy

phpy.include("./tests/lib/bridge_helpers.php")


def test_recursive_argument_conversion_does_not_bailout_python_process():
    code = r'''
import phpy

recursive = []
recursive.append(recursive)

try:
    phpy.call("strlen", recursive)
except ValueError as error:
    assert "recursive Python container" in str(error)
else:
    raise AssertionError("recursive conversion must fail")

assert phpy.call("strlen", "alive") == 5
'''
    result = subprocess.run(
        [sys.executable, "-c", code],
        cwd=".",
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_php_closure_called_from_python():
    cb = phpy.call('Closure::fromCallable', 'strlen')
    assert type(cb).__name__ == 'zend_callable'
    assert cb("hello world") == 11


def test_php_closure_called_with_keyword_args():
    cb = phpy.call('phpy_kw_closure')
    assert cb(a=3, b=7) == 37


def test_php_closure_can_be_called_repeatedly():
    cb = phpy.call('phpy_kw_closure')
    for i in range(10_000):
        assert cb(i, 1) == i * 10 + 1


def test_php_traversable_iterated_from_python():
    it = phpy.call('phpy_test_iter')
    assert type(it).__name__ == 'zend_iterator'
    assert [k for k in it] == [1, 2, 3]
    # PHP iterators are one-shot: a second pass is exhausted.
    assert [k for k in it] == []


def test_php_generator_iterated_from_python():
    g = phpy.call('phpy_gen')
    assert type(g).__name__ == 'zend_iterator'
    assert [k for k in g] == ['x', 'y', 'z']


def test_string_binop_concat():
    s = phpy.String("hello")
    s2 = s + " world"
    assert type(s2).__name__ == 'zend_string'
    assert str(s2) == "hello world"


def test_string_inplace_concat():
    s = phpy.String("hello")
    s += " world"
    assert type(s).__name__ == 'zend_string'
    assert str(s) == "hello world"


def test_string_equality():
    s = phpy.String("hello")
    assert s == phpy.String("hello")
    assert not (s != phpy.String("hello"))
    assert s != phpy.String("world")


def test_string_index_out_of_range():
    s = phpy.String("hello")
    with pytest.raises(IndexError):
        s[100]


def test_string_bytes():
    assert bytes(phpy.String("hello")) == b'hello'


def test_object_call_non_string_method():
    o = phpy.Object('stdClass')
    with pytest.raises(TypeError):
        o.call(123)


def test_object_call_missing_method():
    o = phpy.Object('stdClass')
    with pytest.raises(NameError):
        o.call('noSuchMethod')


def test_object_invoke_positional():
    o = phpy.Object('PhpyInvokable')
    assert o(1, 2) == '1-2'


def test_object_invoke_keyword_args():
    o = phpy.Object('PhpyInvokable')
    assert o(a='x', b='y') == 'x-y'


def test_object_get_set():
    o = phpy.Object('stdClass')
    o.set("value", "v1")
    assert o.get("value") == "v1"


def test_top_level_call_no_args():
    with pytest.raises(TypeError):
        phpy.call()


def test_top_level_call_non_string_name():
    with pytest.raises(TypeError):
        phpy.call(123)


def test_undefined_constant_returns_none():
    assert phpy.constant('THIS_DOES_NOT_EXIST_XYZ') is None


def test_eval_returns_exit_status():
    assert phpy.eval("echo 'hello';") == 0
