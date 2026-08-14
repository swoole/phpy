import pytest
import phpy


def test_array_constructor_rejects_non_iterable_without_bailout():
    with pytest.raises(TypeError, match="not iterable"):
        phpy.Array(123)

    # A conversion failure must not corrupt the embedded PHP runtime.
    assert phpy.call("strlen", "alive") == 5


def test_array_constructor_preserves_recursive_nested_container():
    recursive = []
    recursive.append(recursive)

    array = phpy.Array(recursive)
    assert array.count() == 1
    assert array[0] is recursive
    assert array[0][0] is recursive


def test_empty_array_remains_writable():
    array = phpy.Array()
    assert array.count() == 0
    assert array.append("first")
    array["name"] = "phpy"
    assert array[0] == "first"
    assert array["name"] == "phpy"


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

    assert 'uuid' in d

    l = phpy.Array([1, 3, 5, 2023, 7, 9])
    assert l.is_list()
    assert l[3] == 2023


def test_iter():
    uuid = phpy.call("uniqid")
    d = phpy.Array({"hello": "world", "php": "swoole", "uuid": uuid})
    keys = phpy.call('array_keys', d).collect()
    keys2 = []

    for k in d:
        keys2.append(k)

    assert keys == keys2
