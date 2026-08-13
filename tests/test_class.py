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


def test_static_property_get_keeps_borrowed_value_alive():
    c = phpy.Class('PhpyObject')

    first = c.get("items")
    second = c.get("items")
    assert first.collect() == {"stable": 42}
    assert second.collect() == {"stable": 42}
    assert phpy.call("count", c.get("items")) == 1


def test_static_property_set_transfers_a_safe_value():
    c = phpy.Class('PhpyObject')
    value = phpy.Array({"updated": [1, 2, 3]})

    assert c.set("items", value) is True
    del value
    assert c.get("items").collect()["updated"] == [1, 2, 3]


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
