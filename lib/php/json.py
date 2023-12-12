import phpy

HEX_TAG = 1
HEX_AMP = 2
HEX_APOS = 4
HEX_QUOT = 8
FORCE_OBJECT = 16
NUMERIC_CHECK = 32
UNESCAPED_SLASHES = 64
PRETTY_PRINT = 128
UNESCAPED_UNICODE = 256
PARTIAL_OUTPUT_ON_ERROR = 512
PRESERVE_ZERO_FRACTION = 1024
UNESCAPED_LINE_TERMINATORS = 2048
OBJECT_AS_ARRAY = 1
BIGINT_AS_STRING = 2
INVALID_UTF8_IGNORE = 1048576
INVALID_UTF8_SUBSTITUTE = 2097152
THROW_ON_ERROR = 4194304
ERROR_NONE = 0
ERROR_DEPTH = 1
ERROR_STATE_MISMATCH = 2
ERROR_CTRL_CHAR = 3
ERROR_SYNTAX = 4
ERROR_UTF8 = 5
ERROR_RECURSION = 6
ERROR_INF_OR_NAN = 7
ERROR_UNSUPPORTED_TYPE = 8
ERROR_INVALID_PROPERTY_NAME = 9
ERROR_UTF16 = 10
ERROR_NON_BACKED_ENUM = 11


def encode(_value, _flags=0, _depth=512):
    return phpy.call('json_encode', _value, _flags, _depth)


def decode(_json, _associative=None, _depth=512, _flags=0):
    return phpy.call('json_decode', _json, _associative, _depth, _flags)


def last_error():
    return phpy.call('json_last_error', )


def last_error_msg():
    return phpy.call('json_last_error_msg', )




class JsonSerializable():

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def __init__(self):
        self.__this = phpy.Object(f'JsonSerializable')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class JsonException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'JsonException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

