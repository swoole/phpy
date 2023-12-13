import phpy

INPUT_POST = 0
INPUT_GET = 1
INPUT_COOKIE = 2
INPUT_ENV = 4
INPUT_SERVER = 5
FLAG_NONE = 0
REQUIRE_SCALAR = 33554432
REQUIRE_ARRAY = 16777216
FORCE_ARRAY = 67108864
NULL_ON_FAILURE = 134217728
VALIDATE_INT = 257
VALIDATE_BOOLEAN = 258
VALIDATE_BOOL = 258
VALIDATE_FLOAT = 259
VALIDATE_REGEXP = 272
VALIDATE_DOMAIN = 277
VALIDATE_URL = 273
VALIDATE_EMAIL = 274
VALIDATE_IP = 275
VALIDATE_MAC = 276
DEFAULT = 516
UNSAFE_RAW = 516
SANITIZE_STRING = 513
SANITIZE_STRIPPED = 513
SANITIZE_ENCODED = 514
SANITIZE_SPECIAL_CHARS = 515
SANITIZE_FULL_SPECIAL_CHARS = 522
SANITIZE_EMAIL = 517
SANITIZE_URL = 518
SANITIZE_NUMBER_INT = 519
SANITIZE_NUMBER_FLOAT = 520
SANITIZE_ADD_SLASHES = 523
CALLBACK = 1024
FLAG_ALLOW_OCTAL = 1
FLAG_ALLOW_HEX = 2
FLAG_STRIP_LOW = 4
FLAG_STRIP_HIGH = 8
FLAG_STRIP_BACKTICK = 512
FLAG_ENCODE_LOW = 16
FLAG_ENCODE_HIGH = 32
FLAG_ENCODE_AMP = 64
FLAG_NO_ENCODE_QUOTES = 128
FLAG_EMPTY_STRING_NULL = 256
FLAG_ALLOW_FRACTION = 4096
FLAG_ALLOW_THOUSAND = 8192
FLAG_ALLOW_SCIENTIFIC = 16384
FLAG_PATH_REQUIRED = 262144
FLAG_QUERY_REQUIRED = 524288
FLAG_IPV4 = 1048576
FLAG_IPV6 = 2097152
FLAG_NO_RES_RANGE = 4194304
FLAG_NO_PRIV_RANGE = 8388608
FLAG_HOSTNAME = 1048576
FLAG_EMAIL_UNICODE = 1048576


def has_var(_input_type, _var_name):
    return phpy.call('filter_has_var', _input_type, _var_name)


def input(_type, _var_name, _filter=516, _options=0):
    return phpy.call('filter_input', _type, _var_name, _filter, _options)


def var(_value, _filter=516, _options=0):
    return phpy.call('filter_var', _value, _filter, _options)


def input_array(_type, _options=516, _add_empty=True):
    return phpy.call('filter_input_array', _type, _options, _add_empty)


def var_array(_array, _options=516, _add_empty=True):
    return phpy.call('filter_var_array', _array, _options, _add_empty)


def list():
    return phpy.call('filter_list', )


def id(_name):
    return phpy.call('filter_id', _name)




