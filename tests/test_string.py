import pytest
import phpy
import random
import base64


def test_string():
    s = phpy.String("hello world")
    assert s.len() == 11


def test_random_bytes():
    rdata = phpy.call('random_bytes', 128)
    assert rdata.len() == 128


def test_base64_random_data():
    data = bytearray(128)
    for i in range(128):
        data[i] = random.randint(0, 255)
    assert bytes(phpy.call("base64_encode", data)) == base64.b64encode(data)


def test_string_to_str():
    rdata = phpy.call('uniqid')
    assert rdata.len() == 13
