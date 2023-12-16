import phpy

CONNECTION_ABORTED = 1
CONNECTION_NORMAL = 0
CONNECTION_TIMEOUT = 2
INI_USER = 1
INI_PERDIR = 2
INI_SYSTEM = 4
INI_ALL = 7
INI_SCANNER_NORMAL = 0
INI_SCANNER_RAW = 1
INI_SCANNER_TYPED = 2
PHP_URL_SCHEME = 0
PHP_URL_HOST = 1
PHP_URL_PORT = 2
PHP_URL_USER = 3
PHP_URL_PASS = 4
PHP_URL_PATH = 5
PHP_URL_QUERY = 6
PHP_URL_FRAGMENT = 7
PHP_QUERY_RFC1738 = 1
PHP_QUERY_RFC3986 = 2
M_E = 2.718281828459
M_LOG2E = 1.442695040889
M_LOG10E = 0.43429448190325
M_LN2 = 0.69314718055995
M_LN10 = 2.302585092994
M_PI = 3.1415926535898
M_PI_2 = 1.5707963267949
M_PI_4 = 0.78539816339745
M_1_PI = 0.31830988618379
M_2_PI = 0.63661977236758
M_SQRTPI = 1.7724538509055
M_2_SQRTPI = 1.1283791670955
M_LNPI = 1.1447298858494
M_EULER = 0.57721566490153
M_SQRT2 = 1.4142135623731
M_SQRT1_2 = 0.70710678118655
M_SQRT3 = 1.7320508075689
INF = float('inf')
NAN = float('nan')
PHP_ROUND_HALF_UP = 1
PHP_ROUND_HALF_DOWN = 2
PHP_ROUND_HALF_EVEN = 3
PHP_ROUND_HALF_ODD = 4
INFO_GENERAL = 1
INFO_CREDITS = 2
INFO_CONFIGURATION = 4
INFO_MODULES = 8
INFO_ENVIRONMENT = 16
INFO_VARIABLES = 32
INFO_LICENSE = 64
INFO_ALL = 4294967295
CREDITS_GROUP = 1
CREDITS_GENERAL = 2
CREDITS_SAPI = 4
CREDITS_MODULES = 8
CREDITS_DOCS = 16
CREDITS_FULLPAGE = 32
CREDITS_QA = 64
CREDITS_ALL = 4294967295
HTML_SPECIALCHARS = 0
HTML_ENTITIES = 1
ENT_COMPAT = 2
ENT_QUOTES = 3
ENT_NOQUOTES = 0
ENT_IGNORE = 4
ENT_SUBSTITUTE = 8
ENT_DISALLOWED = 128
ENT_HTML401 = 0
ENT_XML1 = 16
ENT_XHTML = 32
ENT_HTML5 = 48
STR_PAD_LEFT = 0
STR_PAD_RIGHT = 1
STR_PAD_BOTH = 2
PATHINFO_DIRNAME = 1
PATHINFO_BASENAME = 2
PATHINFO_EXTENSION = 4
PATHINFO_FILENAME = 8
PATHINFO_ALL = 15
CHAR_MAX = 127
LC_CTYPE = 0
LC_NUMERIC = 1
LC_TIME = 2
LC_COLLATE = 3
LC_MONETARY = 4
LC_ALL = 6
LC_MESSAGES = 5
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2
LOCK_SH = 1
LOCK_EX = 2
LOCK_UN = 3
LOCK_NB = 4
STREAM_NOTIFY_CONNECT = 2
STREAM_NOTIFY_AUTH_REQUIRED = 3
STREAM_NOTIFY_AUTH_RESULT = 10
STREAM_NOTIFY_MIME_TYPE_IS = 4
STREAM_NOTIFY_FILE_SIZE_IS = 5
STREAM_NOTIFY_REDIRECTED = 6
STREAM_NOTIFY_PROGRESS = 7
STREAM_NOTIFY_FAILURE = 9
STREAM_NOTIFY_COMPLETED = 8
STREAM_NOTIFY_RESOLVE = 1
STREAM_NOTIFY_SEVERITY_INFO = 0
STREAM_NOTIFY_SEVERITY_WARN = 1
STREAM_NOTIFY_SEVERITY_ERR = 2
STREAM_FILTER_READ = 1
STREAM_FILTER_WRITE = 2
STREAM_FILTER_ALL = 3
STREAM_CLIENT_PERSISTENT = 1
STREAM_CLIENT_ASYNC_CONNECT = 2
STREAM_CLIENT_CONNECT = 4
STREAM_CRYPTO_METHOD_ANY_CLIENT = 127
STREAM_CRYPTO_METHOD_SSLv2_CLIENT = 3
STREAM_CRYPTO_METHOD_SSLv3_CLIENT = 5
STREAM_CRYPTO_METHOD_SSLv23_CLIENT = 57
STREAM_CRYPTO_METHOD_TLS_CLIENT = 121
STREAM_CRYPTO_METHOD_TLSv1_0_CLIENT = 9
STREAM_CRYPTO_METHOD_TLSv1_1_CLIENT = 17
STREAM_CRYPTO_METHOD_TLSv1_2_CLIENT = 33
STREAM_CRYPTO_METHOD_TLSv1_3_CLIENT = 65
STREAM_CRYPTO_METHOD_ANY_SERVER = 126
STREAM_CRYPTO_METHOD_SSLv2_SERVER = 2
STREAM_CRYPTO_METHOD_SSLv3_SERVER = 4
STREAM_CRYPTO_METHOD_SSLv23_SERVER = 120
STREAM_CRYPTO_METHOD_TLS_SERVER = 120
STREAM_CRYPTO_METHOD_TLSv1_0_SERVER = 8
STREAM_CRYPTO_METHOD_TLSv1_1_SERVER = 16
STREAM_CRYPTO_METHOD_TLSv1_2_SERVER = 32
STREAM_CRYPTO_METHOD_TLSv1_3_SERVER = 64
STREAM_CRYPTO_PROTO_SSLv3 = 4
STREAM_CRYPTO_PROTO_TLSv1_0 = 8
STREAM_CRYPTO_PROTO_TLSv1_1 = 16
STREAM_CRYPTO_PROTO_TLSv1_2 = 32
STREAM_CRYPTO_PROTO_TLSv1_3 = 64
STREAM_SHUT_RD = 0
STREAM_SHUT_WR = 1
STREAM_SHUT_RDWR = 2
STREAM_PF_INET = 2
STREAM_PF_INET6 = 10
STREAM_PF_UNIX = 1
STREAM_IPPROTO_IP = 0
STREAM_IPPROTO_TCP = 6
STREAM_IPPROTO_UDP = 17
STREAM_IPPROTO_ICMP = 1
STREAM_IPPROTO_RAW = 255
STREAM_SOCK_STREAM = 1
STREAM_SOCK_DGRAM = 2
STREAM_SOCK_RAW = 3
STREAM_SOCK_SEQPACKET = 5
STREAM_SOCK_RDM = 4
STREAM_PEEK = 2
STREAM_OOB = 1
STREAM_SERVER_BIND = 4
STREAM_SERVER_LISTEN = 8
FILE_USE_INCLUDE_PATH = 1
FILE_IGNORE_NEW_LINES = 2
FILE_SKIP_EMPTY_LINES = 4
FILE_APPEND = 8
FILE_NO_DEFAULT_CONTEXT = 16
FILE_TEXT = 0
FILE_BINARY = 0
FNM_NOESCAPE = 2
FNM_PATHNAME = 1
FNM_PERIOD = 4
FNM_CASEFOLD = 16
PSFS_PASS_ON = 2
PSFS_FEED_ME = 1
PSFS_ERR_FATAL = 0
PSFS_FLAG_NORMAL = 0
PSFS_FLAG_FLUSH_INC = 1
PSFS_FLAG_FLUSH_CLOSE = 2
PASSWORD_DEFAULT = "2y"
PASSWORD_BCRYPT = "2y"
PASSWORD_BCRYPT_DEFAULT_COST = 10
MT_RAND_MT19937 = 0
MT_RAND_PHP = 1
ABDAY_1 = 131072
ABDAY_2 = 131073
ABDAY_3 = 131074
ABDAY_4 = 131075
ABDAY_5 = 131076
ABDAY_6 = 131077
ABDAY_7 = 131078
DAY_1 = 131079
DAY_2 = 131080
DAY_3 = 131081
DAY_4 = 131082
DAY_5 = 131083
DAY_6 = 131084
DAY_7 = 131085
ABMON_1 = 131086
ABMON_2 = 131087
ABMON_3 = 131088
ABMON_4 = 131089
ABMON_5 = 131090
ABMON_6 = 131091
ABMON_7 = 131092
ABMON_8 = 131093
ABMON_9 = 131094
ABMON_10 = 131095
ABMON_11 = 131096
ABMON_12 = 131097
MON_1 = 131098
MON_2 = 131099
MON_3 = 131100
MON_4 = 131101
MON_5 = 131102
MON_6 = 131103
MON_7 = 131104
MON_8 = 131105
MON_9 = 131106
MON_10 = 131107
MON_11 = 131108
MON_12 = 131109
AM_STR = 131110
PM_STR = 131111
D_T_FMT = 131112
D_FMT = 131113
T_FMT = 131114
T_FMT_AMPM = 131115
ERA = 131116
ERA_D_T_FMT = 131120
ERA_D_FMT = 131118
ERA_T_FMT = 131121
ALT_DIGITS = 131119
CRNCYSTR = 262159
RADIXCHAR = 65536
THOUSEP = 65537
YESEXPR = 327680
NOEXPR = 327681
YESSTR = 327682
NOSTR = 327683
CODESET = 14
CRYPT_SALT_LENGTH = 123
CRYPT_STD_DES = 1
CRYPT_EXT_DES = 1
CRYPT_MD5 = 1
CRYPT_BLOWFISH = 1
CRYPT_SHA256 = 1
CRYPT_SHA512 = 1
DIRECTORY_SEPARATOR = "/"
PATH_SEPARATOR = ":"
SCANDIR_SORT_ASCENDING = 0
SCANDIR_SORT_DESCENDING = 1
SCANDIR_SORT_NONE = 2
GLOB_MARK = 2
GLOB_NOSORT = 4
GLOB_NOCHECK = 16
GLOB_NOESCAPE = 64
GLOB_ERR = 1
GLOB_ONLYDIR = 1073741824
GLOB_AVAILABLE_FLAGS = 1073741911
LOG_EMERG = 0
LOG_ALERT = 1
LOG_CRIT = 2
LOG_ERR = 3
LOG_WARNING = 4
LOG_NOTICE = 5
LOG_INFO = 6
LOG_DEBUG = 7
LOG_KERN = 0
LOG_USER = 8
LOG_MAIL = 16
LOG_DAEMON = 24
LOG_AUTH = 32
LOG_SYSLOG = 40
LOG_LPR = 48
LOG_NEWS = 56
LOG_UUCP = 64
LOG_CRON = 72
LOG_AUTHPRIV = 80
LOG_LOCAL0 = 128
LOG_LOCAL1 = 136
LOG_LOCAL2 = 144
LOG_LOCAL3 = 152
LOG_LOCAL4 = 160
LOG_LOCAL5 = 168
LOG_LOCAL6 = 176
LOG_LOCAL7 = 184
LOG_PID = 1
LOG_CONS = 2
LOG_ODELAY = 4
LOG_NDELAY = 8
LOG_NOWAIT = 16
LOG_PERROR = 32
EXTR_OVERWRITE = 0
EXTR_SKIP = 1
EXTR_PREFIX_SAME = 2
EXTR_PREFIX_ALL = 3
EXTR_PREFIX_INVALID = 4
EXTR_PREFIX_IF_EXISTS = 5
EXTR_IF_EXISTS = 6
EXTR_REFS = 256
SORT_ASC = 4
SORT_DESC = 3
SORT_REGULAR = 0
SORT_NUMERIC = 1
SORT_STRING = 2
SORT_LOCALE_STRING = 5
SORT_NATURAL = 6
SORT_FLAG_CASE = 8
CASE_LOWER = 0
CASE_UPPER = 1
COUNT_NORMAL = 0
COUNT_RECURSIVE = 1
ARRAY_FILTER_USE_BOTH = 1
ARRAY_FILTER_USE_KEY = 2
ASSERT_ACTIVE = 1
ASSERT_CALLBACK = 2
ASSERT_BAIL = 3
ASSERT_WARNING = 4
ASSERT_EXCEPTION = 5
STREAM_USE_PATH = 1
STREAM_IGNORE_URL = 2
STREAM_REPORT_ERRORS = 8
STREAM_MUST_SEEK = 16
STREAM_URL_STAT_LINK = 1
STREAM_URL_STAT_QUIET = 2
STREAM_MKDIR_RECURSIVE = 1
STREAM_IS_URL = 1
STREAM_OPTION_BLOCKING = 1
STREAM_OPTION_READ_TIMEOUT = 4
STREAM_OPTION_READ_BUFFER = 2
STREAM_OPTION_WRITE_BUFFER = 3
STREAM_BUFFER_NONE = 0
STREAM_BUFFER_LINE = 1
STREAM_BUFFER_FULL = 2
STREAM_CAST_AS_STREAM = 0
STREAM_CAST_FOR_SELECT = 3
STREAM_META_TOUCH = 1
STREAM_META_OWNER = 3
STREAM_META_OWNER_NAME = 2
STREAM_META_GROUP = 5
STREAM_META_GROUP_NAME = 4
STREAM_META_ACCESS = 6
IMAGETYPE_GIF = 1
IMAGETYPE_JPEG = 2
IMAGETYPE_PNG = 3
IMAGETYPE_SWF = 4
IMAGETYPE_PSD = 5
IMAGETYPE_BMP = 6
IMAGETYPE_TIFF_II = 7
IMAGETYPE_TIFF_MM = 8
IMAGETYPE_JPC = 9
IMAGETYPE_JP2 = 10
IMAGETYPE_JPX = 11
IMAGETYPE_JB2 = 12
IMAGETYPE_SWC = 13
IMAGETYPE_IFF = 14
IMAGETYPE_WBMP = 15
IMAGETYPE_JPEG2000 = 9
IMAGETYPE_XBM = 16
IMAGETYPE_ICO = 17
IMAGETYPE_WEBP = 18
IMAGETYPE_AVIF = 19
IMAGETYPE_UNKNOWN = 0
IMAGETYPE_COUNT = 20
DNS_A = 1
DNS_NS = 2
DNS_CNAME = 16
DNS_SOA = 32
DNS_PTR = 2048
DNS_HINFO = 4096
DNS_CAA = 8192
DNS_MX = 16384
DNS_TXT = 32768
DNS_SRV = 33554432
DNS_NAPTR = 67108864
DNS_AAAA = 134217728
DNS_A6 = 16777216
DNS_ANY = 268435456
DNS_ALL = 251721779


def set_time_limit(_seconds):
    return phpy.call('set_time_limit', _seconds)


def header_register_callback(_callback):
    return phpy.call('header_register_callback', _callback)


def ob_start(_callback=None, _chunk_size=0, _flags=112):
    return phpy.call('ob_start', _callback, _chunk_size, _flags)


def ob_flush():
    return phpy.call('ob_flush', )


def ob_clean():
    return phpy.call('ob_clean', )


def ob_end_flush():
    return phpy.call('ob_end_flush', )


def ob_end_clean():
    return phpy.call('ob_end_clean', )


def ob_get_flush():
    return phpy.call('ob_get_flush', )


def ob_get_clean():
    return phpy.call('ob_get_clean', )


def ob_get_contents():
    return phpy.call('ob_get_contents', )


def ob_get_level():
    return phpy.call('ob_get_level', )


def ob_get_length():
    return phpy.call('ob_get_length', )


def ob_list_handlers():
    return phpy.call('ob_list_handlers', )


def ob_get_status(_full_status=False):
    return phpy.call('ob_get_status', _full_status)


def ob_implicit_flush(_enable=True):
    return phpy.call('ob_implicit_flush', _enable)


def output_reset_rewrite_vars():
    return phpy.call('output_reset_rewrite_vars', )


def output_add_rewrite_var(_name, _value):
    return phpy.call('output_add_rewrite_var', _name, _value)


def stream_wrapper_register(_protocol, _class, _flags=0):
    return phpy.call('stream_wrapper_register', _protocol, _class, _flags)


def stream_register_wrapper(_protocol, _class, _flags=0):
    return phpy.call('stream_register_wrapper', _protocol, _class, _flags)


def stream_wrapper_unregister(_protocol):
    return phpy.call('stream_wrapper_unregister', _protocol)


def stream_wrapper_restore(_protocol):
    return phpy.call('stream_wrapper_restore', _protocol)


def array_push(_array, _values=None):
    return phpy.call('array_push', _array, _values)


def krsort(_array, _flags=0):
    return phpy.call('krsort', _array, _flags)


def ksort(_array, _flags=0):
    return phpy.call('ksort', _array, _flags)


def count(_value, _mode=0):
    return phpy.call('count', _value, _mode)


def sizeof(_value, _mode=0):
    return phpy.call('sizeof', _value, _mode)


def natsort(_array):
    return phpy.call('natsort', _array)


def natcasesort(_array):
    return phpy.call('natcasesort', _array)


def asort(_array, _flags=0):
    return phpy.call('asort', _array, _flags)


def arsort(_array, _flags=0):
    return phpy.call('arsort', _array, _flags)


def sort(_array, _flags=0):
    return phpy.call('sort', _array, _flags)


def rsort(_array, _flags=0):
    return phpy.call('rsort', _array, _flags)


def usort(_array, _callback):
    return phpy.call('usort', _array, _callback)


def uasort(_array, _callback):
    return phpy.call('uasort', _array, _callback)


def uksort(_array, _callback):
    return phpy.call('uksort', _array, _callback)


def end(_array):
    return phpy.call('end', _array)


def prev(_array):
    return phpy.call('prev', _array)


def next(_array):
    return phpy.call('next', _array)


def reset(_array):
    return phpy.call('reset', _array)


def current(_array):
    return phpy.call('current', _array)


def pos(_array):
    return phpy.call('pos', _array)


def key(_array):
    return phpy.call('key', _array)


def min(_value, _values=None):
    return phpy.call('min', _value, _values)


def max(_value, _values=None):
    return phpy.call('max', _value, _values)


def array_walk(_array, _callback, _arg=None):
    return phpy.call('array_walk', _array, _callback, _arg)


def array_walk_recursive(_array, _callback, _arg=None):
    return phpy.call('array_walk_recursive', _array, _callback, _arg)


def in_array(_needle, _haystack, _strict=False):
    return phpy.call('in_array', _needle, _haystack, _strict)


def array_search(_needle, _haystack, _strict=False):
    return phpy.call('array_search', _needle, _haystack, _strict)


def extract(_array, _flags=0, _prefix=""):
    return phpy.call('extract', _array, _flags, _prefix)


def compact(_var_name, _var_names=None):
    return phpy.call('compact', _var_name, _var_names)


def array_fill(_start_index, _count, _value):
    return phpy.call('array_fill', _start_index, _count, _value)


def array_fill_keys(_keys, _value):
    return phpy.call('array_fill_keys', _keys, _value)


def range(_start, _end, _step=1):
    return phpy.call('range', _start, _end, _step)


def shuffle(_array):
    return phpy.call('shuffle', _array)


def array_pop(_array):
    return phpy.call('array_pop', _array)


def array_shift(_array):
    return phpy.call('array_shift', _array)


def array_unshift(_array, _values=None):
    return phpy.call('array_unshift', _array, _values)


def array_splice(_array, _offset, _length=None, _replacement=[]):
    return phpy.call('array_splice', _array, _offset, _length, _replacement)


def array_slice(_array, _offset, _length=None, _preserve_keys=False):
    return phpy.call('array_slice', _array, _offset, _length, _preserve_keys)


def array_merge(_arrays=None):
    return phpy.call('array_merge', _arrays)


def array_merge_recursive(_arrays=None):
    return phpy.call('array_merge_recursive', _arrays)


def array_replace(_array, _replacements=None):
    return phpy.call('array_replace', _array, _replacements)


def array_replace_recursive(_array, _replacements=None):
    return phpy.call('array_replace_recursive', _array, _replacements)


def array_keys(_array, _filter_value=None, _strict=False):
    return phpy.call('array_keys', _array, _filter_value, _strict)


def array_key_first(_array):
    return phpy.call('array_key_first', _array)


def array_key_last(_array):
    return phpy.call('array_key_last', _array)


def array_values(_array):
    return phpy.call('array_values', _array)


def array_count_values(_array):
    return phpy.call('array_count_values', _array)


def array_column(_array, _column_key, _index_key=None):
    return phpy.call('array_column', _array, _column_key, _index_key)


def array_reverse(_array, _preserve_keys=False):
    return phpy.call('array_reverse', _array, _preserve_keys)


def array_pad(_array, _length, _value):
    return phpy.call('array_pad', _array, _length, _value)


def array_flip(_array):
    return phpy.call('array_flip', _array)


def array_change_key_case(_array, _case=0):
    return phpy.call('array_change_key_case', _array, _case)


def array_unique(_array, _flags=2):
    return phpy.call('array_unique', _array, _flags)


def array_intersect_key(_array, _arrays=None):
    return phpy.call('array_intersect_key', _array, _arrays)


def array_intersect_ukey(_array, _rest=None):
    return phpy.call('array_intersect_ukey', _array, _rest)


def array_intersect(_array, _arrays=None):
    return phpy.call('array_intersect', _array, _arrays)


def array_uintersect(_array, _rest=None):
    return phpy.call('array_uintersect', _array, _rest)


def array_intersect_assoc(_array, _arrays=None):
    return phpy.call('array_intersect_assoc', _array, _arrays)


def array_uintersect_assoc(_array, _rest=None):
    return phpy.call('array_uintersect_assoc', _array, _rest)


def array_intersect_uassoc(_array, _rest=None):
    return phpy.call('array_intersect_uassoc', _array, _rest)


def array_uintersect_uassoc(_array, _rest=None):
    return phpy.call('array_uintersect_uassoc', _array, _rest)


def array_diff_key(_array, _arrays=None):
    return phpy.call('array_diff_key', _array, _arrays)


def array_diff_ukey(_array, _rest=None):
    return phpy.call('array_diff_ukey', _array, _rest)


def array_diff(_array, _arrays=None):
    return phpy.call('array_diff', _array, _arrays)


def array_udiff(_array, _rest=None):
    return phpy.call('array_udiff', _array, _rest)


def array_diff_assoc(_array, _arrays=None):
    return phpy.call('array_diff_assoc', _array, _arrays)


def array_diff_uassoc(_array, _rest=None):
    return phpy.call('array_diff_uassoc', _array, _rest)


def array_udiff_assoc(_array, _rest=None):
    return phpy.call('array_udiff_assoc', _array, _rest)


def array_udiff_uassoc(_array, _rest=None):
    return phpy.call('array_udiff_uassoc', _array, _rest)


def array_multisort(_array, _rest=None):
    return phpy.call('array_multisort', _array, _rest)


def array_rand(_array, _num=1):
    return phpy.call('array_rand', _array, _num)


def array_sum(_array):
    return phpy.call('array_sum', _array)


def array_product(_array):
    return phpy.call('array_product', _array)


def array_reduce(_array, _callback, _initial=None):
    return phpy.call('array_reduce', _array, _callback, _initial)


def array_filter(_array, _callback=None, _mode=0):
    return phpy.call('array_filter', _array, _callback, _mode)


def array_map(_callback, _array, _arrays=None):
    return phpy.call('array_map', _callback, _array, _arrays)


def array_key_exists(_key, _array):
    return phpy.call('array_key_exists', _key, _array)


def key_exists(_key, _array):
    return phpy.call('key_exists', _key, _array)


def array_chunk(_array, _length, _preserve_keys=False):
    return phpy.call('array_chunk', _array, _length, _preserve_keys)


def array_combine(_keys, _values):
    return phpy.call('array_combine', _keys, _values)


def array_is_list(_array):
    return phpy.call('array_is_list', _array)


def base64_encode(_string):
    return phpy.call('base64_encode', _string)


def base64_decode(_string, _strict=False):
    return phpy.call('base64_decode', _string, _strict)


def constant(_name):
    return phpy.call('constant', _name)


def ip2long(_ip):
    return phpy.call('ip2long', _ip)


def long2ip(_ip):
    return phpy.call('long2ip', _ip)


def getenv(_name=None, _local_only=False):
    return phpy.call('getenv', _name, _local_only)


def putenv(_assignment):
    return phpy.call('putenv', _assignment)


def getopt(_short_options, _long_options=[], _rest_index=None):
    return phpy.call('getopt', _short_options, _long_options, _rest_index)


def flush():
    return phpy.call('flush', )


def sleep(_seconds):
    return phpy.call('sleep', _seconds)


def usleep(_microseconds):
    return phpy.call('usleep', _microseconds)


def time_nanosleep(_seconds, _nanoseconds):
    return phpy.call('time_nanosleep', _seconds, _nanoseconds)


def time_sleep_until(_timestamp):
    return phpy.call('time_sleep_until', _timestamp)


def get_current_user():
    return phpy.call('get_current_user', )


def get_cfg_var(_option):
    return phpy.call('get_cfg_var', _option)


def error_log(_message, _message_type=0, _destination=None, _additional_headers=None):
    return phpy.call('error_log', _message, _message_type, _destination, _additional_headers)


def error_get_last():
    return phpy.call('error_get_last', )


def error_clear_last():
    return phpy.call('error_clear_last', )


def call_user_func(_callback, _args=None):
    return phpy.call('call_user_func', _callback, _args)


def call_user_func_array(_callback, _args):
    return phpy.call('call_user_func_array', _callback, _args)


def forward_static_call(_callback, _args=None):
    return phpy.call('forward_static_call', _callback, _args)


def forward_static_call_array(_callback, _args):
    return phpy.call('forward_static_call_array', _callback, _args)


def register_shutdown_function(_callback, _args=None):
    return phpy.call('register_shutdown_function', _callback, _args)


def highlight_file(_filename, _return=False):
    return phpy.call('highlight_file', _filename, _return)


def show_source(_filename, _return=False):
    return phpy.call('show_source', _filename, _return)


def php_strip_whitespace(_filename):
    return phpy.call('php_strip_whitespace', _filename)


def highlight_string(_string, _return=False):
    return phpy.call('highlight_string', _string, _return)


def ini_get(_option):
    return phpy.call('ini_get', _option)


def ini_get_all(_extension=None, _details=True):
    return phpy.call('ini_get_all', _extension, _details)


def ini_set(_option, _value):
    return phpy.call('ini_set', _option, _value)


def ini_alter(_option, _value):
    return phpy.call('ini_alter', _option, _value)


def ini_restore(_option):
    return phpy.call('ini_restore', _option)


def set_include_path(_include_path):
    return phpy.call('set_include_path', _include_path)


def get_include_path():
    return phpy.call('get_include_path', )


def print_r(_value, _return=False):
    return phpy.call('print_r', _value, _return)


def connection_aborted():
    return phpy.call('connection_aborted', )


def connection_status():
    return phpy.call('connection_status', )


def ignore_user_abort(_enable=None):
    return phpy.call('ignore_user_abort', _enable)


def getservbyname(_service, _protocol):
    return phpy.call('getservbyname', _service, _protocol)


def getservbyport(_port, _protocol):
    return phpy.call('getservbyport', _port, _protocol)


def getprotobyname(_protocol):
    return phpy.call('getprotobyname', _protocol)


def getprotobynumber(_protocol):
    return phpy.call('getprotobynumber', _protocol)


def register_tick_function(_callback, _args=None):
    return phpy.call('register_tick_function', _callback, _args)


def unregister_tick_function(_callback):
    return phpy.call('unregister_tick_function', _callback)


def is_uploaded_file(_filename):
    return phpy.call('is_uploaded_file', _filename)


def move_uploaded_file(_from, _to):
    return phpy.call('move_uploaded_file', _from, _to)


def parse_ini_file(_filename, _process_sections=False, _scanner_mode=0):
    return phpy.call('parse_ini_file', _filename, _process_sections, _scanner_mode)


def parse_ini_string(_ini_string, _process_sections=False, _scanner_mode=0):
    return phpy.call('parse_ini_string', _ini_string, _process_sections, _scanner_mode)


def sys_getloadavg():
    return phpy.call('sys_getloadavg', )


def get_browser(_user_agent=None, _return_array=False):
    return phpy.call('get_browser', _user_agent, _return_array)


def crc32(_string):
    return phpy.call('crc32', _string)


def crypt(_string, _salt):
    return phpy.call('crypt', _string, _salt)


def strptime(_timestamp, _format):
    return phpy.call('strptime', _timestamp, _format)


def gethostname():
    return phpy.call('gethostname', )


def gethostbyaddr(_ip):
    return phpy.call('gethostbyaddr', _ip)


def gethostbyname(_hostname):
    return phpy.call('gethostbyname', _hostname)


def gethostbynamel(_hostname):
    return phpy.call('gethostbynamel', _hostname)


def dns_check_record(_hostname, _type="MX"):
    return phpy.call('dns_check_record', _hostname, _type)


def checkdnsrr(_hostname, _type="MX"):
    return phpy.call('checkdnsrr', _hostname, _type)


def dns_get_record(_hostname, _type=268435456, _authoritative_name_servers=None, _additional_records=None, _raw=False):
    return phpy.call('dns_get_record', _hostname, _type, _authoritative_name_servers, _additional_records, _raw)


def dns_get_mx(_hostname, _hosts, _weights=None):
    return phpy.call('dns_get_mx', _hostname, _hosts, _weights)


def getmxrr(_hostname, _hosts, _weights=None):
    return phpy.call('getmxrr', _hostname, _hosts, _weights)


def net_get_interfaces():
    return phpy.call('net_get_interfaces', )


def ftok(_filename, _project_id):
    return phpy.call('ftok', _filename, _project_id)


def hrtime(_as_number=False):
    return phpy.call('hrtime', _as_number)


def lcg_value():
    return phpy.call('lcg_value', )


def md5(_string, _binary=False):
    return phpy.call('md5', _string, _binary)


def md5_file(_filename, _binary=False):
    return phpy.call('md5_file', _filename, _binary)


def getmyuid():
    return phpy.call('getmyuid', )


def getmygid():
    return phpy.call('getmygid', )


def getmypid():
    return phpy.call('getmypid', )


def getmyinode():
    return phpy.call('getmyinode', )


def getlastmod():
    return phpy.call('getlastmod', )


def sha1(_string, _binary=False):
    return phpy.call('sha1', _string, _binary)


def sha1_file(_filename, _binary=False):
    return phpy.call('sha1_file', _filename, _binary)


def openlog(_prefix, _flags, _facility):
    return phpy.call('openlog', _prefix, _flags, _facility)


def closelog():
    return phpy.call('closelog', )


def syslog(_priority, _message):
    return phpy.call('syslog', _priority, _message)


def inet_ntop(_ip):
    return phpy.call('inet_ntop', _ip)


def inet_pton(_ip):
    return phpy.call('inet_pton', _ip)


def metaphone(_string, _max_phonemes=0):
    return phpy.call('metaphone', _string, _max_phonemes)


def header(_header, _replace=True, _response_code=0):
    return phpy.call('header', _header, _replace, _response_code)


def header_remove(_name=None):
    return phpy.call('header_remove', _name)


def setrawcookie(_name, _value="", _expires_or_options=0, _path="", _domain="", _secure=False, _httponly=False):
    return phpy.call('setrawcookie', _name, _value, _expires_or_options, _path, _domain, _secure, _httponly)


def setcookie(_name, _value="", _expires_or_options=0, _path="", _domain="", _secure=False, _httponly=False):
    return phpy.call('setcookie', _name, _value, _expires_or_options, _path, _domain, _secure, _httponly)


def http_response_code(_response_code=0):
    return phpy.call('http_response_code', _response_code)


def headers_sent(_filename=None, _line=None):
    return phpy.call('headers_sent', _filename, _line)


def headers_list():
    return phpy.call('headers_list', )


def htmlspecialchars(_string, _flags=11, _encoding=None, _double_encode=True):
    return phpy.call('htmlspecialchars', _string, _flags, _encoding, _double_encode)


def htmlspecialchars_decode(_string, _flags=11):
    return phpy.call('htmlspecialchars_decode', _string, _flags)


def html_entity_decode(_string, _flags=11, _encoding=None):
    return phpy.call('html_entity_decode', _string, _flags, _encoding)


def htmlentities(_string, _flags=11, _encoding=None, _double_encode=True):
    return phpy.call('htmlentities', _string, _flags, _encoding, _double_encode)


def get_html_translation_table(_table=0, _flags=11, _encoding="UTF-8"):
    return phpy.call('get_html_translation_table', _table, _flags, _encoding)


def _assert(_assertion, _description=None):
    return phpy.call('assert', _assertion, _description)


def assert_options(_option, _value=None):
    return phpy.call('assert_options', _option, _value)


def bin2hex(_string):
    return phpy.call('bin2hex', _string)


def hex2bin(_string):
    return phpy.call('hex2bin', _string)


def strspn(_string, _characters, _offset=0, _length=None):
    return phpy.call('strspn', _string, _characters, _offset, _length)


def strcspn(_string, _characters, _offset=0, _length=None):
    return phpy.call('strcspn', _string, _characters, _offset, _length)


def nl_langinfo(_item):
    return phpy.call('nl_langinfo', _item)


def strcoll(_string1, _string2):
    return phpy.call('strcoll', _string1, _string2)


def trim(_string, _characters=" \n\r\t\v\x00"):
    return phpy.call('trim', _string, _characters)


def rtrim(_string, _characters=" \n\r\t\v\x00"):
    return phpy.call('rtrim', _string, _characters)


def chop(_string, _characters=" \n\r\t\v\x00"):
    return phpy.call('chop', _string, _characters)


def ltrim(_string, _characters=" \n\r\t\v\x00"):
    return phpy.call('ltrim', _string, _characters)


def wordwrap(_string, _width=75, _break="\n", _cut_long_words=False):
    return phpy.call('wordwrap', _string, _width, _break, _cut_long_words)


def explode(_separator, _string, _limit=9223372036854775807):
    return phpy.call('explode', _separator, _string, _limit)


def implode(_separator, _array=None):
    return phpy.call('implode', _separator, _array)


def join(_separator, _array=None):
    return phpy.call('join', _separator, _array)


def strtok(_string, _token=None):
    return phpy.call('strtok', _string, _token)


def strtoupper(_string):
    return phpy.call('strtoupper', _string)


def strtolower(_string):
    return phpy.call('strtolower', _string)


def basename(_path, _suffix=""):
    return phpy.call('basename', _path, _suffix)


def dirname(_path, _levels=1):
    return phpy.call('dirname', _path, _levels)


def pathinfo(_path, _flags=15):
    return phpy.call('pathinfo', _path, _flags)


def stristr(_haystack, _needle, _before_needle=False):
    return phpy.call('stristr', _haystack, _needle, _before_needle)


def strstr(_haystack, _needle, _before_needle=False):
    return phpy.call('strstr', _haystack, _needle, _before_needle)


def strchr(_haystack, _needle, _before_needle=False):
    return phpy.call('strchr', _haystack, _needle, _before_needle)


def strpos(_haystack, _needle, _offset=0):
    return phpy.call('strpos', _haystack, _needle, _offset)


def stripos(_haystack, _needle, _offset=0):
    return phpy.call('stripos', _haystack, _needle, _offset)


def strrpos(_haystack, _needle, _offset=0):
    return phpy.call('strrpos', _haystack, _needle, _offset)


def strripos(_haystack, _needle, _offset=0):
    return phpy.call('strripos', _haystack, _needle, _offset)


def strrchr(_haystack, _needle):
    return phpy.call('strrchr', _haystack, _needle)


def str_contains(_haystack, _needle):
    return phpy.call('str_contains', _haystack, _needle)


def str_starts_with(_haystack, _needle):
    return phpy.call('str_starts_with', _haystack, _needle)


def str_ends_with(_haystack, _needle):
    return phpy.call('str_ends_with', _haystack, _needle)


def chunk_split(_string, _length=76, _separator="\r\n"):
    return phpy.call('chunk_split', _string, _length, _separator)


def substr(_string, _offset, _length=None):
    return phpy.call('substr', _string, _offset, _length)


def substr_replace(_string, _replace, _offset, _length=None):
    return phpy.call('substr_replace', _string, _replace, _offset, _length)


def quotemeta(_string):
    return phpy.call('quotemeta', _string)


def ord(_character):
    return phpy.call('ord', _character)


def chr(_codepoint):
    return phpy.call('chr', _codepoint)


def ucfirst(_string):
    return phpy.call('ucfirst', _string)


def lcfirst(_string):
    return phpy.call('lcfirst', _string)


def ucwords(_string, _separators=" \t\r\n\v"):
    return phpy.call('ucwords', _string, _separators)


def strtr(_string, _from, _to=None):
    return phpy.call('strtr', _string, _from, _to)


def strrev(_string):
    return phpy.call('strrev', _string)


def similar_text(_string1, _string2, _percent=None):
    return phpy.call('similar_text', _string1, _string2, _percent)


def addcslashes(_string, _characters):
    return phpy.call('addcslashes', _string, _characters)


def addslashes(_string):
    return phpy.call('addslashes', _string)


def stripcslashes(_string):
    return phpy.call('stripcslashes', _string)


def stripslashes(_string):
    return phpy.call('stripslashes', _string)


def str_replace(_search, _replace, _subject, _count=None):
    return phpy.call('str_replace', _search, _replace, _subject, _count)


def str_ireplace(_search, _replace, _subject, _count=None):
    return phpy.call('str_ireplace', _search, _replace, _subject, _count)


def hebrev(_string, _max_chars_per_line=0):
    return phpy.call('hebrev', _string, _max_chars_per_line)


def nl2br(_string, _use_xhtml=True):
    return phpy.call('nl2br', _string, _use_xhtml)


def strip_tags(_string, _allowed_tags=None):
    return phpy.call('strip_tags', _string, _allowed_tags)


def setlocale(_category, _locales, _rest=None):
    return phpy.call('setlocale', _category, _locales, _rest)


def parse_str(_string, _result):
    return phpy.call('parse_str', _string, _result)


def str_getcsv(_string, _separator=",", _enclosure="\"", _escape="\\"):
    return phpy.call('str_getcsv', _string, _separator, _enclosure, _escape)


def str_repeat(_string, _times):
    return phpy.call('str_repeat', _string, _times)


def count_chars(_string, _mode=0):
    return phpy.call('count_chars', _string, _mode)


def strnatcmp(_string1, _string2):
    return phpy.call('strnatcmp', _string1, _string2)


def localeconv():
    return phpy.call('localeconv', )


def strnatcasecmp(_string1, _string2):
    return phpy.call('strnatcasecmp', _string1, _string2)


def substr_count(_haystack, _needle, _offset=0, _length=None):
    return phpy.call('substr_count', _haystack, _needle, _offset, _length)


def str_pad(_string, _length, _pad_string=" ", _pad_type=1):
    return phpy.call('str_pad', _string, _length, _pad_string, _pad_type)


def sscanf(_string, _format, _vars=None):
    return phpy.call('sscanf', _string, _format, _vars)


def str_rot13(_string):
    return phpy.call('str_rot13', _string)


def str_shuffle(_string):
    return phpy.call('str_shuffle', _string)


def str_word_count(_string, _format=0, _characters=None):
    return phpy.call('str_word_count', _string, _format, _characters)


def str_split(_string, _length=1):
    return phpy.call('str_split', _string, _length)


def strpbrk(_string, _characters):
    return phpy.call('strpbrk', _string, _characters)


def substr_compare(_haystack, _needle, _offset, _length=None, _case_insensitive=False):
    return phpy.call('substr_compare', _haystack, _needle, _offset, _length, _case_insensitive)


def utf8_encode(_string):
    return phpy.call('utf8_encode', _string)


def utf8_decode(_string):
    return phpy.call('utf8_decode', _string)


def opendir(_directory, _context=None):
    return phpy.call('opendir', _directory, _context)


def dir(_directory, _context=None):
    return phpy.call('dir', _directory, _context)


def closedir(_dir_handle=None):
    return phpy.call('closedir', _dir_handle)


def chdir(_directory):
    return phpy.call('chdir', _directory)


def chroot(_directory):
    return phpy.call('chroot', _directory)


def getcwd():
    return phpy.call('getcwd', )


def rewinddir(_dir_handle=None):
    return phpy.call('rewinddir', _dir_handle)


def readdir(_dir_handle=None):
    return phpy.call('readdir', _dir_handle)


def scandir(_directory, _sorting_order=0, _context=None):
    return phpy.call('scandir', _directory, _sorting_order, _context)


def glob(_pattern, _flags=0):
    return phpy.call('glob', _pattern, _flags)


def exec(_command, _output=None, _result_code=None):
    return phpy.call('exec', _command, _output, _result_code)


def system(_command, _result_code=None):
    return phpy.call('system', _command, _result_code)


def passthru(_command, _result_code=None):
    return phpy.call('passthru', _command, _result_code)


def escapeshellcmd(_command):
    return phpy.call('escapeshellcmd', _command)


def escapeshellarg(_arg):
    return phpy.call('escapeshellarg', _arg)


def shell_exec(_command):
    return phpy.call('shell_exec', _command)


def proc_nice(_priority):
    return phpy.call('proc_nice', _priority)


def flock(_stream, _operation, _would_block=None):
    return phpy.call('flock', _stream, _operation, _would_block)


def get_meta_tags(_filename, _use_include_path=False):
    return phpy.call('get_meta_tags', _filename, _use_include_path)


def pclose(_handle):
    return phpy.call('pclose', _handle)


def popen(_command, _mode):
    return phpy.call('popen', _command, _mode)


def readfile(_filename, _use_include_path=False, _context=None):
    return phpy.call('readfile', _filename, _use_include_path, _context)


def rewind(_stream):
    return phpy.call('rewind', _stream)


def rmdir(_directory, _context=None):
    return phpy.call('rmdir', _directory, _context)


def umask(_mask=None):
    return phpy.call('umask', _mask)


def fclose(_stream):
    return phpy.call('fclose', _stream)


def feof(_stream):
    return phpy.call('feof', _stream)


def fgetc(_stream):
    return phpy.call('fgetc', _stream)


def fgets(_stream, _length=None):
    return phpy.call('fgets', _stream, _length)


def fread(_stream, _length):
    return phpy.call('fread', _stream, _length)


def fopen(_filename, _mode, _use_include_path=False, _context=None):
    return phpy.call('fopen', _filename, _mode, _use_include_path, _context)


def fscanf(_stream, _format, _vars=None):
    return phpy.call('fscanf', _stream, _format, _vars)


def fpassthru(_stream):
    return phpy.call('fpassthru', _stream)


def ftruncate(_stream, _size):
    return phpy.call('ftruncate', _stream, _size)


def fstat(_stream):
    return phpy.call('fstat', _stream)


def fseek(_stream, _offset, _whence=0):
    return phpy.call('fseek', _stream, _offset, _whence)


def ftell(_stream):
    return phpy.call('ftell', _stream)


def fflush(_stream):
    return phpy.call('fflush', _stream)


def fsync(_stream):
    return phpy.call('fsync', _stream)


def fdatasync(_stream):
    return phpy.call('fdatasync', _stream)


def fwrite(_stream, _data, _length=None):
    return phpy.call('fwrite', _stream, _data, _length)


def fputs(_stream, _data, _length=None):
    return phpy.call('fputs', _stream, _data, _length)


def mkdir(_directory, _permissions=511, _recursive=False, _context=None):
    return phpy.call('mkdir', _directory, _permissions, _recursive, _context)


def rename(_from, _to, _context=None):
    return phpy.call('rename', _from, _to, _context)


def copy(_from, _to, _context=None):
    return phpy.call('copy', _from, _to, _context)


def tempnam(_directory, _prefix):
    return phpy.call('tempnam', _directory, _prefix)


def tmpfile():
    return phpy.call('tmpfile', )


def file(_filename, _flags=0, _context=None):
    return phpy.call('file', _filename, _flags, _context)


def file_get_contents(_filename, _use_include_path=False, _context=None, _offset=0, _length=None):
    return phpy.call('file_get_contents', _filename, _use_include_path, _context, _offset, _length)


def unlink(_filename, _context=None):
    return phpy.call('unlink', _filename, _context)


def file_put_contents(_filename, _data, _flags=0, _context=None):
    return phpy.call('file_put_contents', _filename, _data, _flags, _context)


def fputcsv(_stream, _fields, _separator=",", _enclosure="\"", _escape="\\", _eol="\n"):
    return phpy.call('fputcsv', _stream, _fields, _separator, _enclosure, _escape, _eol)


def fgetcsv(_stream, _length=None, _separator=",", _enclosure="\"", _escape="\\"):
    return phpy.call('fgetcsv', _stream, _length, _separator, _enclosure, _escape)


def realpath(_path):
    return phpy.call('realpath', _path)


def fnmatch(_pattern, _filename, _flags=0):
    return phpy.call('fnmatch', _pattern, _filename, _flags)


def sys_get_temp_dir():
    return phpy.call('sys_get_temp_dir', )


def fileatime(_filename):
    return phpy.call('fileatime', _filename)


def filectime(_filename):
    return phpy.call('filectime', _filename)


def filegroup(_filename):
    return phpy.call('filegroup', _filename)


def fileinode(_filename):
    return phpy.call('fileinode', _filename)


def filemtime(_filename):
    return phpy.call('filemtime', _filename)


def fileowner(_filename):
    return phpy.call('fileowner', _filename)


def fileperms(_filename):
    return phpy.call('fileperms', _filename)


def filesize(_filename):
    return phpy.call('filesize', _filename)


def filetype(_filename):
    return phpy.call('filetype', _filename)


def file_exists(_filename):
    return phpy.call('file_exists', _filename)


def is_writable(_filename):
    return phpy.call('is_writable', _filename)


def is_writeable(_filename):
    return phpy.call('is_writeable', _filename)


def is_readable(_filename):
    return phpy.call('is_readable', _filename)


def is_executable(_filename):
    return phpy.call('is_executable', _filename)


def is_file(_filename):
    return phpy.call('is_file', _filename)


def is_dir(_filename):
    return phpy.call('is_dir', _filename)


def is_link(_filename):
    return phpy.call('is_link', _filename)


def stat(_filename):
    return phpy.call('stat', _filename)


def lstat(_filename):
    return phpy.call('lstat', _filename)


def chown(_filename, _user):
    return phpy.call('chown', _filename, _user)


def chgrp(_filename, _group):
    return phpy.call('chgrp', _filename, _group)


def lchown(_filename, _user):
    return phpy.call('lchown', _filename, _user)


def lchgrp(_filename, _group):
    return phpy.call('lchgrp', _filename, _group)


def chmod(_filename, _permissions):
    return phpy.call('chmod', _filename, _permissions)


def touch(_filename, _mtime=None, _atime=None):
    return phpy.call('touch', _filename, _mtime, _atime)


def clearstatcache(_clear_realpath_cache=False, _filename=""):
    return phpy.call('clearstatcache', _clear_realpath_cache, _filename)


def disk_total_space(_directory):
    return phpy.call('disk_total_space', _directory)


def disk_free_space(_directory):
    return phpy.call('disk_free_space', _directory)


def diskfreespace(_directory):
    return phpy.call('diskfreespace', _directory)


def realpath_cache_get():
    return phpy.call('realpath_cache_get', )


def realpath_cache_size():
    return phpy.call('realpath_cache_size', )


def sprintf(_format, _values=None):
    return phpy.call('sprintf', _format, _values)


def printf(_format, _values=None):
    return phpy.call('printf', _format, _values)


def vprintf(_format, _values):
    return phpy.call('vprintf', _format, _values)


def vsprintf(_format, _values):
    return phpy.call('vsprintf', _format, _values)


def fprintf(_stream, _format, _values=None):
    return phpy.call('fprintf', _stream, _format, _values)


def vfprintf(_stream, _format, _values):
    return phpy.call('vfprintf', _stream, _format, _values)


def fsockopen(_hostname, _port=-1, _error_code=None, _error_message=None, _timeout=None):
    return phpy.call('fsockopen', _hostname, _port, _error_code, _error_message, _timeout)


def pfsockopen(_hostname, _port=-1, _error_code=None, _error_message=None, _timeout=None):
    return phpy.call('pfsockopen', _hostname, _port, _error_code, _error_message, _timeout)


def http_build_query(_data, _numeric_prefix="", _arg_separator=None, _encoding_type=1):
    return phpy.call('http_build_query', _data, _numeric_prefix, _arg_separator, _encoding_type)


def image_type_to_mime_type(_image_type):
    return phpy.call('image_type_to_mime_type', _image_type)


def image_type_to_extension(_image_type, _include_dot=True):
    return phpy.call('image_type_to_extension', _image_type, _include_dot)


def getimagesize(_filename, _image_info=None):
    return phpy.call('getimagesize', _filename, _image_info)


def getimagesizefromstring(_string, _image_info=None):
    return phpy.call('getimagesizefromstring', _string, _image_info)


def phpinfo(_flags=4294967295):
    return phpy.call('phpinfo', _flags)


def phpversion(_extension=None):
    return phpy.call('phpversion', _extension)


def phpcredits(_flags=4294967295):
    return phpy.call('phpcredits', _flags)


def php_sapi_name():
    return phpy.call('php_sapi_name', )


def php_uname(_mode="a"):
    return phpy.call('php_uname', _mode)


def php_ini_scanned_files():
    return phpy.call('php_ini_scanned_files', )


def php_ini_loaded_file():
    return phpy.call('php_ini_loaded_file', )


def iptcembed(_iptc_data, _filename, _spool=0):
    return phpy.call('iptcembed', _iptc_data, _filename, _spool)


def iptcparse(_iptc_block):
    return phpy.call('iptcparse', _iptc_block)


def levenshtein(_string1, _string2, _insertion_cost=1, _replacement_cost=1, _deletion_cost=1):
    return phpy.call('levenshtein', _string1, _string2, _insertion_cost, _replacement_cost, _deletion_cost)


def readlink(_path):
    return phpy.call('readlink', _path)


def linkinfo(_path):
    return phpy.call('linkinfo', _path)


def symlink(_target, _link):
    return phpy.call('symlink', _target, _link)


def link(_target, _link):
    return phpy.call('link', _target, _link)


def mail(_to, _subject, _message, _additional_headers=[], _additional_params=""):
    return phpy.call('mail', _to, _subject, _message, _additional_headers, _additional_params)


def abs(_num):
    return phpy.call('abs', _num)


def ceil(_num):
    return phpy.call('ceil', _num)


def floor(_num):
    return phpy.call('floor', _num)


def round(_num, _precision=0, _mode=1):
    return phpy.call('round', _num, _precision, _mode)


def sin(_num):
    return phpy.call('sin', _num)


def cos(_num):
    return phpy.call('cos', _num)


def tan(_num):
    return phpy.call('tan', _num)


def asin(_num):
    return phpy.call('asin', _num)


def acos(_num):
    return phpy.call('acos', _num)


def atan(_num):
    return phpy.call('atan', _num)


def atanh(_num):
    return phpy.call('atanh', _num)


def atan2(_y, _x):
    return phpy.call('atan2', _y, _x)


def sinh(_num):
    return phpy.call('sinh', _num)


def cosh(_num):
    return phpy.call('cosh', _num)


def tanh(_num):
    return phpy.call('tanh', _num)


def asinh(_num):
    return phpy.call('asinh', _num)


def acosh(_num):
    return phpy.call('acosh', _num)


def expm1(_num):
    return phpy.call('expm1', _num)


def log1p(_num):
    return phpy.call('log1p', _num)


def pi():
    return phpy.call('pi', )


def is_finite(_num):
    return phpy.call('is_finite', _num)


def is_nan(_num):
    return phpy.call('is_nan', _num)


def intdiv(_num1, _num2):
    return phpy.call('intdiv', _num1, _num2)


def is_infinite(_num):
    return phpy.call('is_infinite', _num)


def pow(_num, _exponent):
    return phpy.call('pow', _num, _exponent)


def exp(_num):
    return phpy.call('exp', _num)


def log(_num, _base=2.718281828459):
    return phpy.call('log', _num, _base)


def log10(_num):
    return phpy.call('log10', _num)


def sqrt(_num):
    return phpy.call('sqrt', _num)


def hypot(_x, _y):
    return phpy.call('hypot', _x, _y)


def deg2rad(_num):
    return phpy.call('deg2rad', _num)


def rad2deg(_num):
    return phpy.call('rad2deg', _num)


def bindec(_binary_string):
    return phpy.call('bindec', _binary_string)


def hexdec(_hex_string):
    return phpy.call('hexdec', _hex_string)


def octdec(_octal_string):
    return phpy.call('octdec', _octal_string)


def decbin(_num):
    return phpy.call('decbin', _num)


def decoct(_num):
    return phpy.call('decoct', _num)


def dechex(_num):
    return phpy.call('dechex', _num)


def base_convert(_num, _from_base, _to_base):
    return phpy.call('base_convert', _num, _from_base, _to_base)


def number_format(_num, _decimals=0, _decimal_separator=".", _thousands_separator=","):
    return phpy.call('number_format', _num, _decimals, _decimal_separator, _thousands_separator)


def fmod(_num1, _num2):
    return phpy.call('fmod', _num1, _num2)


def fdiv(_num1, _num2):
    return phpy.call('fdiv', _num1, _num2)


def microtime(_as_float=False):
    return phpy.call('microtime', _as_float)


def gettimeofday(_as_float=False):
    return phpy.call('gettimeofday', _as_float)


def getrusage(_mode=0):
    return phpy.call('getrusage', _mode)


def pack(_format, _values=None):
    return phpy.call('pack', _format, _values)


def unpack(_format, _string, _offset=0):
    return phpy.call('unpack', _format, _string, _offset)


def password_get_info(_hash):
    return phpy.call('password_get_info', _hash)


def password_hash(_password, _algo, _options=[]):
    return phpy.call('password_hash', _password, _algo, _options)


def password_needs_rehash(_hash, _algo, _options=[]):
    return phpy.call('password_needs_rehash', _hash, _algo, _options)


def password_verify(_password, _hash):
    return phpy.call('password_verify', _password, _hash)


def password_algos():
    return phpy.call('password_algos', )


def proc_open(_command, _descriptor_spec, _pipes, _cwd=None, _env_vars=None, _options=None):
    return phpy.call('proc_open', _command, _descriptor_spec, _pipes, _cwd, _env_vars, _options)


def proc_close(_process):
    return phpy.call('proc_close', _process)


def proc_terminate(_process, _signal=15):
    return phpy.call('proc_terminate', _process, _signal)


def proc_get_status(_process):
    return phpy.call('proc_get_status', _process)


def quoted_printable_decode(_string):
    return phpy.call('quoted_printable_decode', _string)


def quoted_printable_encode(_string):
    return phpy.call('quoted_printable_encode', _string)


def mt_srand(_seed=0, _mode=0):
    return phpy.call('mt_srand', _seed, _mode)


def srand(_seed=0, _mode=0):
    return phpy.call('srand', _seed, _mode)


def rand(_min=None, _max=None):
    return phpy.call('rand', _min, _max)


def mt_rand(_min=None, _max=None):
    return phpy.call('mt_rand', _min, _max)


def mt_getrandmax():
    return phpy.call('mt_getrandmax', )


def getrandmax():
    return phpy.call('getrandmax', )


def random_bytes(_length):
    return phpy.call('random_bytes', _length)


def random_int(_min, _max):
    return phpy.call('random_int', _min, _max)


def soundex(_string):
    return phpy.call('soundex', _string)


def stream_select(_read, _write, _except, _seconds, _microseconds=None):
    return phpy.call('stream_select', _read, _write, _except, _seconds, _microseconds)


def stream_context_create(_options=None, _params=None):
    return phpy.call('stream_context_create', _options, _params)


def stream_context_set_params(_context, _params):
    return phpy.call('stream_context_set_params', _context, _params)


def stream_context_get_params(_context):
    return phpy.call('stream_context_get_params', _context)


def stream_context_set_option(_context, _wrapper_or_options, _option_name=None, _value=None):
    return phpy.call('stream_context_set_option', _context, _wrapper_or_options, _option_name, _value)


def stream_context_get_options(_stream_or_context):
    return phpy.call('stream_context_get_options', _stream_or_context)


def stream_context_get_default(_options=None):
    return phpy.call('stream_context_get_default', _options)


def stream_context_set_default(_options):
    return phpy.call('stream_context_set_default', _options)


def stream_filter_prepend(_stream, _filter_name, _mode=0, _params=None):
    return phpy.call('stream_filter_prepend', _stream, _filter_name, _mode, _params)


def stream_filter_append(_stream, _filter_name, _mode=0, _params=None):
    return phpy.call('stream_filter_append', _stream, _filter_name, _mode, _params)


def stream_filter_remove(_stream_filter):
    return phpy.call('stream_filter_remove', _stream_filter)


def stream_socket_client(_address, _error_code=None, _error_message=None, _timeout=None, _flags=4, _context=None):
    return phpy.call('stream_socket_client', _address, _error_code, _error_message, _timeout, _flags, _context)


def stream_socket_server(_address, _error_code=None, _error_message=None, _flags=12, _context=None):
    return phpy.call('stream_socket_server', _address, _error_code, _error_message, _flags, _context)


def stream_socket_accept(_socket, _timeout=None, _peer_name=None):
    return phpy.call('stream_socket_accept', _socket, _timeout, _peer_name)


def stream_socket_get_name(_socket, _remote):
    return phpy.call('stream_socket_get_name', _socket, _remote)


def stream_socket_recvfrom(_socket, _length, _flags=0, _address=None):
    return phpy.call('stream_socket_recvfrom', _socket, _length, _flags, _address)


def stream_socket_sendto(_socket, _data, _flags=0, _address=""):
    return phpy.call('stream_socket_sendto', _socket, _data, _flags, _address)


def stream_socket_enable_crypto(_stream, _enable, _crypto_method=None, _session_stream=None):
    return phpy.call('stream_socket_enable_crypto', _stream, _enable, _crypto_method, _session_stream)


def stream_socket_shutdown(_stream, _mode):
    return phpy.call('stream_socket_shutdown', _stream, _mode)


def stream_socket_pair(_domain, _type, _protocol):
    return phpy.call('stream_socket_pair', _domain, _type, _protocol)


def stream_copy_to_stream(_from, _to, _length=None, _offset=0):
    return phpy.call('stream_copy_to_stream', _from, _to, _length, _offset)


def stream_get_contents(_stream, _length=None, _offset=-1):
    return phpy.call('stream_get_contents', _stream, _length, _offset)


def stream_supports_lock(_stream):
    return phpy.call('stream_supports_lock', _stream)


def stream_set_write_buffer(_stream, _size):
    return phpy.call('stream_set_write_buffer', _stream, _size)


def set_file_buffer(_stream, _size):
    return phpy.call('set_file_buffer', _stream, _size)


def stream_set_read_buffer(_stream, _size):
    return phpy.call('stream_set_read_buffer', _stream, _size)


def stream_set_blocking(_stream, _enable):
    return phpy.call('stream_set_blocking', _stream, _enable)


def socket_set_blocking(_stream, _enable):
    return phpy.call('socket_set_blocking', _stream, _enable)


def stream_get_meta_data(_stream):
    return phpy.call('stream_get_meta_data', _stream)


def socket_get_status(_stream):
    return phpy.call('socket_get_status', _stream)


def stream_get_line(_stream, _length, _ending=""):
    return phpy.call('stream_get_line', _stream, _length, _ending)


def stream_resolve_include_path(_filename):
    return phpy.call('stream_resolve_include_path', _filename)


def stream_get_wrappers():
    return phpy.call('stream_get_wrappers', )


def stream_get_transports():
    return phpy.call('stream_get_transports', )


def stream_is_local(_stream):
    return phpy.call('stream_is_local', _stream)


def stream_isatty(_stream):
    return phpy.call('stream_isatty', _stream)


def stream_set_chunk_size(_stream, _size):
    return phpy.call('stream_set_chunk_size', _stream, _size)


def stream_set_timeout(_stream, _seconds, _microseconds=0):
    return phpy.call('stream_set_timeout', _stream, _seconds, _microseconds)


def socket_set_timeout(_stream, _seconds, _microseconds=0):
    return phpy.call('socket_set_timeout', _stream, _seconds, _microseconds)


def gettype(_value):
    return phpy.call('gettype', _value)


def get_debug_type(_value):
    return phpy.call('get_debug_type', _value)


def settype(_var, _type):
    return phpy.call('settype', _var, _type)


def intval(_value, _base=10):
    return phpy.call('intval', _value, _base)


def floatval(_value):
    return phpy.call('floatval', _value)


def doubleval(_value):
    return phpy.call('doubleval', _value)


def boolval(_value):
    return phpy.call('boolval', _value)


def strval(_value):
    return phpy.call('strval', _value)


def is_null(_value):
    return phpy.call('is_null', _value)


def is_resource(_value):
    return phpy.call('is_resource', _value)


def is_bool(_value):
    return phpy.call('is_bool', _value)


def is_int(_value):
    return phpy.call('is_int', _value)


def is_integer(_value):
    return phpy.call('is_integer', _value)


def is_long(_value):
    return phpy.call('is_long', _value)


def is_float(_value):
    return phpy.call('is_float', _value)


def is_double(_value):
    return phpy.call('is_double', _value)


def is_numeric(_value):
    return phpy.call('is_numeric', _value)


def is_string(_value):
    return phpy.call('is_string', _value)


def is_array(_value):
    return phpy.call('is_array', _value)


def is_object(_value):
    return phpy.call('is_object', _value)


def is_scalar(_value):
    return phpy.call('is_scalar', _value)


def is_callable(_value, _syntax_only=False, _callable_name=None):
    return phpy.call('is_callable', _value, _syntax_only, _callable_name)


def is_iterable(_value):
    return phpy.call('is_iterable', _value)


def is_countable(_value):
    return phpy.call('is_countable', _value)


def uniqid(_prefix="", _more_entropy=False):
    return phpy.call('uniqid', _prefix, _more_entropy)


def parse_url(_url, _component=-1):
    return phpy.call('parse_url', _url, _component)


def urlencode(_string):
    return phpy.call('urlencode', _string)


def urldecode(_string):
    return phpy.call('urldecode', _string)


def rawurlencode(_string):
    return phpy.call('rawurlencode', _string)


def rawurldecode(_string):
    return phpy.call('rawurldecode', _string)


def get_headers(_url, _associative=False, _context=None):
    return phpy.call('get_headers', _url, _associative, _context)


def stream_bucket_make_writeable(_brigade):
    return phpy.call('stream_bucket_make_writeable', _brigade)


def stream_bucket_prepend(_brigade, _bucket):
    return phpy.call('stream_bucket_prepend', _brigade, _bucket)


def stream_bucket_append(_brigade, _bucket):
    return phpy.call('stream_bucket_append', _brigade, _bucket)


def stream_bucket_new(_stream, _buffer):
    return phpy.call('stream_bucket_new', _stream, _buffer)


def stream_get_filters():
    return phpy.call('stream_get_filters', )


def stream_filter_register(_filter_name, _class):
    return phpy.call('stream_filter_register', _filter_name, _class)


def convert_uuencode(_string):
    return phpy.call('convert_uuencode', _string)


def convert_uudecode(_string):
    return phpy.call('convert_uudecode', _string)


def var_dump(_value, _values=None):
    return phpy.call('var_dump', _value, _values)


def var_export(_value, _return=False):
    return phpy.call('var_export', _value, _return)


def debug_zval_dump(_value, _values=None):
    return phpy.call('debug_zval_dump', _value, _values)


def serialize(_value):
    return phpy.call('serialize', _value)


def unserialize(_data, _options=[]):
    return phpy.call('unserialize', _data, _options)


def memory_get_usage(_real_usage=False):
    return phpy.call('memory_get_usage', _real_usage)


def memory_get_peak_usage(_real_usage=False):
    return phpy.call('memory_get_peak_usage', _real_usage)


def version_compare(_version1, _version2, _operator=None):
    return phpy.call('version_compare', _version1, _version2, _operator)


def cli_set_process_title(_title):
    return phpy.call('cli_set_process_title', _title)


def cli_get_process_title():
    return phpy.call('cli_get_process_title', )




class __PHP_Incomplete_Class():

    def __init__(self):
        self.__this = phpy.Object(f'__PHP_Incomplete_Class')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class AssertionError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'AssertionError', _message, _code, _previous)

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

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class php_user_filter():

    def filter(self, _in, _out, _consumed, _closing):
        return self.__this.call(f"filter", _in, _out, _consumed, _closing)

    def onCreate(self):
        return self.__this.call(f"onCreate", )

    def onClose(self):
        return self.__this.call(f"onClose", )

    def __init__(self):
        self.__this = phpy.Object(f'php_user_filter')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class Directory():

    def close(self):
        return self.__this.call(f"close", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def read(self):
        return self.__this.call(f"read", )

    def __init__(self):
        self.__this = phpy.Object(f'Directory')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

