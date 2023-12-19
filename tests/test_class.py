import pytest
import phpy
import math


def test_static_property():
    c = phpy.Class('PhpyObject')
    assert c.get("name") == 'empty'
    uuid = phpy.call('uniqid')
    c.set("name", uuid)
    assert c.get("name") == uuid


def test_static_property_not_exists():
    c = phpy.Class('PhpyObject')
    assert c.get("name_not_exists") is None


def test_class_ctor():
    c = phpy.Class('TestClass')
    uuid = phpy.call('uniqid')
    num = phpy.call('random_int', 10000000, 99999999)
    o = c.new(uuid, num, math.pi, {'swoole': 2023}, ['swoole', 2023])

    items = o.get('array')
    assert items.get(0) == uuid
    assert items.get(1) == num
    assert items.get(2) == math.pi

    d = items.get(3)
    assert type(d) is phpy.Array
    assert d.get('swoole') == 2023

    l = items.get(4)
    assert type(l) is phpy.Array
    assert phpy.call('array_search', 'swoole', l) == 0
    assert phpy.call('array_search', 2023, l) == 1
