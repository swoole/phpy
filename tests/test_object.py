import os

import pytest
import phpy


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


def test_property():
    o = phpy.Object('stdClass')
    rdata = phpy.call('uniqid')
    o.set("value", rdata)
    assert o.get("value") == rdata


def test_object():
    if os.environ.get('IN_CI'):
        return
    o = phpy.Object('redis')
    assert o.call('connect', '127.0.0.1', 6379)
    rdata = phpy.call('uniqid')
    assert o.call('set', 'key', rdata)
    assert o.call('get', 'key') == rdata


def test_return_object():
    if os.environ.get('IN_CI'):
        return
    o = phpy.call('curl_init')
    _type = phpy.call('get_class', o)
    assert _type == 'CurlHandle'


def test_argument_as_object():
    phpy.setOptions({'argument_as_object': True})
    d = {'name': 'swoole'}
    assert str(phpy.call('gettype', d)) == 'object'
    assert str(phpy.call('get_class', d)) == 'PyDict'
    phpy.setOptions({'argument_as_object': False})
