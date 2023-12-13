import phpy

IMPL = "libiconv"
VERSION = "1.16"
MIME_DECODE_STRICT = 1
MIME_DECODE_CONTINUE_ON_ERROR = 2


def strlen(_string, _encoding=None):
    return phpy.call('iconv_strlen', _string, _encoding)


def substr(_string, _offset, _length=None, _encoding=None):
    return phpy.call('iconv_substr', _string, _offset, _length, _encoding)


def strpos(_haystack, _needle, _offset=0, _encoding=None):
    return phpy.call('iconv_strpos', _haystack, _needle, _offset, _encoding)


def strrpos(_haystack, _needle, _encoding=None):
    return phpy.call('iconv_strrpos', _haystack, _needle, _encoding)


def mime_encode(_field_name, _field_value, _options=[]):
    return phpy.call('iconv_mime_encode', _field_name, _field_value, _options)


def mime_decode(_string, _mode=0, _encoding=None):
    return phpy.call('iconv_mime_decode', _string, _mode, _encoding)


def mime_decode_headers(_headers, _mode=0, _encoding=None):
    return phpy.call('iconv_mime_decode_headers', _headers, _mode, _encoding)


def iconv(_from_encoding, _to_encoding, _string):
    return phpy.call('iconv', _from_encoding, _to_encoding, _string)


def set_encoding(_type, _encoding):
    return phpy.call('iconv_set_encoding', _type, _encoding)


def get_encoding(_type="all"):
    return phpy.call('iconv_get_encoding', _type)




