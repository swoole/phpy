import pytest
import phpy


def test_stream_client():
    errno = phpy.Reference()
    errstr = phpy.Reference()
    rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
    assert rs is False
    assert errno.get() == phpy.constant('SOCKET_ECONNREFUSED')
    assert errstr.get() == 'Connection refused'


def test_stream_client_baidu():
    errno = phpy.Reference()
    errstr = phpy.Reference()
    rs = phpy.call("stream_socket_client", 'tcp://www.baidu.com:80', errno, errstr, 30)
    assert rs
    assert errno.get() == 0
    assert errstr.get() == ''

    phpy.call('fwrite', rs, "GET / HTTP/1.0\r\nHost: www.baidu.com\r\nAccept: */*\r\n\r\n")

    content = ''
    while not phpy.call('feof', rs):
        content += str(phpy.call('fread', rs, 8192))

    assert content.find('百度搜索') != -1
