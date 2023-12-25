import pytest
import phpy
import random
import base64


def test_string():
    s = phpy.String("hello world")
    assert len(s) == 11


def test_random_bytes():
    rdata = phpy.call('random_bytes', 128)
    assert len(rdata) == 128


def test_base64_random_data():
    data = bytearray(128)
    for i in range(128):
        data[i] = random.randint(0, 255)
    assert bytes(phpy.call("base64_encode", data)) == base64.b64encode(data)


def test_string_to_str():
    rdata = phpy.call('uniqid')
    assert len(rdata) == 13


def test_string_concat():
    s = phpy.String()
    s += "hello"
    s += b" world"
    s += phpy.String(", swoole is best")
    assert s.__contains__('hello')
    assert s.__contains__('world')
    assert s.__contains__('swoole')
    assert s.__contains__('best')
    assert s[0] == ord('h')
