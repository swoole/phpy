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
    assert d.unset("php") is False
    assert d.get("php") is None


def test_mp_protocol():
    uuid = phpy.call("uniqid")
    d = phpy.Array({"hello": "world", "php": "swoole", "uuid": uuid})

    uuid2 = phpy.call("uniqid")

    assert d['test'] is None

    assert len(d) == 3
    assert d['uuid'] == uuid
    d['test'] = uuid2
    assert d['test'] == uuid2

    del d['test']
    assert d['test'] is None
