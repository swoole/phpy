import pytest
import phpy


def test_index_array():
    s = phpy.Array([1, 3, 5, 2023, 7, 9])
    assert phpy.call('array_search', 2023, s) == 3

    assert s.count() == 6
    assert s.get(3) == 2023
    assert s.get(13) is None
    assert s.unset(3)
    assert s.count() == 5
    assert s.get(3) is None


def test_assoc_array():
    uuid = phpy.call("uniqid")
    d = phpy.Array({"hello": "world", "php": "swoole", "uuid": uuid})
    assert d.count() == 3
    assert d.get("uuid") == str(uuid)
    assert d.get("php") == "swoole"
    assert d.unset("php")
    assert d.unset("php") == False
    assert d.get("php") is None
