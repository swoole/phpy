import pytest
import phpy


def test_array():
    rs = phpy.globals('_SERVER')
    assert type(rs) is phpy.Array
    assert rs.get('argc') == 1


def test_constant():
    rs = phpy.constant('PHP_VERSION')
    assert rs.startswith('8.')
    assert phpy.constant('Pdo::PARAM_LOB') == 3


def test_include():
    rs = phpy.include("./tests/lib/init.php")
    assert type(rs) is dict
    assert type(rs['data']) is list
    assert rs['hello'] == 'swoole'
    assert phpy.call('class_exists', 'PhpyObject')

    assert not phpy.include("./tests/lib/not_exists.php")


def test_return_string():
    m1 = phpy.call('memory_get_usage')
    total = 0
    for i in range(1, 20):
        s = phpy.call('str_repeat', 'A', 1024 * i)
        total += 1024 * i
        assert s == 'A' * (1024 * i)
    m2 = phpy.call('memory_get_usage')
    assert m2 - m1 < total
