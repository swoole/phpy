import pytest
import phpy


def test_array():
    rs = phpy.globals('_SERVER')
    assert type(rs) is dict
    assert rs['argc'] == 1


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


def test_object():
    o = phpy.Object('redis')
    assert o.call('connect', '127.0.0.1', 6379)
    rdata = phpy.call('uniqid')
    assert o.call('set', 'key', rdata)
    assert o.call('get', 'key') == rdata


def test_property():
    o = phpy.Object('stdClass')
    rdata = phpy.call('uniqid')
    o.set("value", rdata)
    assert o.get("value") == rdata


def test_return_object():
    o = phpy.call('curl_init')
    _type = phpy.call('get_class', o)
    assert _type == 'CurlHandle'


def test_return_string():
    m1 = phpy.call('memory_get_usage')
    total = 0
    for i in range(1, 20):
        s = phpy.call('str_repeat', 'A', 1024 * i)
        total += 1024 * i
        assert s == 'A' * (1024 * i)
    m2 = phpy.call('memory_get_usage')
    assert m2 - m1 < total


def test_new_object():
    c = phpy.Class('PhpyObject')
    uuid = phpy.call('uniqid')
    o = c.new(uuid)
    uuid2 = o.call('test')
    assert uuid2 == uuid


def test_new_object_not_exists():
    try:
        c = phpy.Class('NotFound')
    except TypeError as e:
        var = str(e).find('Class "NotFound" not found')
        assert var != -1


def test_static_property():
    c = phpy.Class('PhpyObject')
    assert c.get("name") == 'empty'
    uuid = phpy.call('uniqid')
    c.set("name", uuid)
    assert c.get("name") == uuid


def test_static_property_not_exists():
    c = phpy.Class('PhpyObject')
    assert c.get("name_not_exists") is None
