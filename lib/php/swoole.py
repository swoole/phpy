import phpy

VERSION = "5.1.0"
VERSION_ID = 50100
MAJOR_VERSION = 5
MINOR_VERSION = 1
RELEASE_VERSION = 0
EXTRA_VERSION = ""
DEBUG = False
HAVE_COMPRESSION = True
HAVE_ZLIB = True
HAVE_BROTLI = True
USE_HTTP2 = True
USE_SHORTNAME = True
SOCK_TCP = 1
SOCK_TCP6 = 3
SOCK_UDP = 2
SOCK_UDP6 = 4
SOCK_UNIX_DGRAM = 6
SOCK_UNIX_STREAM = 5
TCP = 1
TCP6 = 3
UDP = 2
UDP6 = 4
UNIX_DGRAM = 6
UNIX_STREAM = 5
SOCK_SYNC = False
SOCK_ASYNC = True
SYNC = 2048
ASYNC = 1024
KEEP = 4096
SSL = 512
SSLv3_METHOD = 1
SSLv3_SERVER_METHOD = 2
SSLv3_CLIENT_METHOD = 3
TLSv1_METHOD = 6
TLSv1_SERVER_METHOD = 7
TLSv1_CLIENT_METHOD = 8
TLSv1_1_METHOD = 9
TLSv1_1_SERVER_METHOD = 10
TLSv1_1_CLIENT_METHOD = 11
TLSv1_2_METHOD = 12
TLSv1_2_SERVER_METHOD = 13
TLSv1_2_CLIENT_METHOD = 14
DTLS_SERVER_METHOD = 16
DTLS_CLIENT_METHOD = 15
SSLv23_METHOD = 0
SSLv23_SERVER_METHOD = 4
SSLv23_CLIENT_METHOD = 5
TLS_METHOD = 0
TLS_SERVER_METHOD = 4
TLS_CLIENT_METHOD = 5
SSL_TLSv1 = 8
SSL_TLSv1_1 = 16
SSL_TLSv1_2 = 32
SSL_TLSv1_3 = 64
SSL_DTLS = 128
SSL_SSLv2 = 2
EVENT_READ = 512
EVENT_WRITE = 1024
STRERROR_SYSTEM = 0
STRERROR_GAI = 1
STRERROR_DNS = 2
STRERROR_SWOOLE = 9
ERROR_MALLOC_FAIL = 501
ERROR_SYSTEM_CALL_FAIL = 502
ERROR_PHP_FATAL_ERROR = 503
ERROR_NAME_TOO_LONG = 504
ERROR_INVALID_PARAMS = 505
ERROR_QUEUE_FULL = 506
ERROR_OPERATION_NOT_SUPPORT = 507
ERROR_PROTOCOL_ERROR = 508
ERROR_WRONG_OPERATION = 509
ERROR_PHP_RUNTIME_NOTICE = 510
ERROR_FILE_NOT_EXIST = 700
ERROR_FILE_TOO_LARGE = 701
ERROR_FILE_EMPTY = 702
ERROR_DNSLOOKUP_DUPLICATE_REQUEST = 710
ERROR_DNSLOOKUP_RESOLVE_FAILED = 711
ERROR_DNSLOOKUP_RESOLVE_TIMEOUT = 712
ERROR_DNSLOOKUP_UNSUPPORTED = 713
ERROR_DNSLOOKUP_NO_SERVER = 714
ERROR_BAD_IPV6_ADDRESS = 720
ERROR_UNREGISTERED_SIGNAL = 721
ERROR_EVENT_SOCKET_REMOVED = 800
ERROR_SESSION_CLOSED_BY_SERVER = 1001
ERROR_SESSION_CLOSED_BY_CLIENT = 1002
ERROR_SESSION_CLOSING = 1003
ERROR_SESSION_CLOSED = 1004
ERROR_SESSION_NOT_EXIST = 1005
ERROR_SESSION_INVALID_ID = 1006
ERROR_SESSION_DISCARD_TIMEOUT_DATA = 1007
ERROR_SESSION_DISCARD_DATA = 1008
ERROR_OUTPUT_BUFFER_OVERFLOW = 1009
ERROR_OUTPUT_SEND_YIELD = 1010
ERROR_SSL_NOT_READY = 1011
ERROR_SSL_CANNOT_USE_SENFILE = 1012
ERROR_SSL_EMPTY_PEER_CERTIFICATE = 1013
ERROR_SSL_VERIFY_FAILED = 1014
ERROR_SSL_BAD_CLIENT = 1015
ERROR_SSL_BAD_PROTOCOL = 1016
ERROR_SSL_RESET = 1017
ERROR_SSL_HANDSHAKE_FAILED = 1018
ERROR_PACKAGE_LENGTH_TOO_LARGE = 1201
ERROR_PACKAGE_LENGTH_NOT_FOUND = 1202
ERROR_DATA_LENGTH_TOO_LARGE = 1203
ERROR_PACKAGE_MALFORMED_DATA = 1204
ERROR_TASK_PACKAGE_TOO_BIG = 2001
ERROR_TASK_DISPATCH_FAIL = 2002
ERROR_TASK_TIMEOUT = 2003
ERROR_HTTP2_STREAM_ID_TOO_BIG = 3001
ERROR_HTTP2_STREAM_NO_HEADER = 3002
ERROR_HTTP2_STREAM_NOT_FOUND = 3003
ERROR_HTTP2_STREAM_IGNORE = 3004
ERROR_HTTP2_SEND_CONTROL_FRAME_FAILED = 3005
ERROR_AIO_BAD_REQUEST = 4001
ERROR_AIO_CANCELED = 4002
ERROR_AIO_TIMEOUT = 4003
ERROR_CLIENT_NO_CONNECTION = 5001
ERROR_SOCKET_CLOSED = 6001
ERROR_SOCKET_POLL_TIMEOUT = 6002
ERROR_SOCKS5_UNSUPPORT_VERSION = 7001
ERROR_SOCKS5_UNSUPPORT_METHOD = 7002
ERROR_SOCKS5_AUTH_FAILED = 7003
ERROR_SOCKS5_SERVER_ERROR = 7004
ERROR_SOCKS5_HANDSHAKE_FAILED = 7005
ERROR_HTTP_PROXY_HANDSHAKE_ERROR = 7101
ERROR_HTTP_INVALID_PROTOCOL = 7102
ERROR_HTTP_PROXY_HANDSHAKE_FAILED = 7103
ERROR_HTTP_PROXY_BAD_RESPONSE = 7104
ERROR_HTTP_CONFLICT_HEADER = 7105
ERROR_WEBSOCKET_BAD_CLIENT = 8501
ERROR_WEBSOCKET_BAD_OPCODE = 8502
ERROR_WEBSOCKET_UNCONNECTED = 8503
ERROR_WEBSOCKET_HANDSHAKE_FAILED = 8504
ERROR_WEBSOCKET_PACK_FAILED = 8505
ERROR_WEBSOCKET_UNPACK_FAILED = 8506
ERROR_WEBSOCKET_INCOMPLETE_PACKET = 8507
ERROR_SERVER_MUST_CREATED_BEFORE_CLIENT = 9001
ERROR_SERVER_TOO_MANY_SOCKET = 9002
ERROR_SERVER_WORKER_TERMINATED = 9003
ERROR_SERVER_INVALID_LISTEN_PORT = 9004
ERROR_SERVER_TOO_MANY_LISTEN_PORT = 9005
ERROR_SERVER_PIPE_BUFFER_FULL = 9006
ERROR_SERVER_NO_IDLE_WORKER = 9007
ERROR_SERVER_ONLY_START_ONE = 9008
ERROR_SERVER_SEND_IN_MASTER = 9009
ERROR_SERVER_INVALID_REQUEST = 9010
ERROR_SERVER_CONNECT_FAIL = 9011
ERROR_SERVER_INVALID_COMMAND = 9012
ERROR_SERVER_IS_NOT_REGULAR_FILE = 9013
ERROR_SERVER_SEND_TO_WOKER_TIMEOUT = 9014
ERROR_SERVER_WORKER_EXIT_TIMEOUT = 9101
ERROR_SERVER_WORKER_ABNORMAL_PIPE_DATA = 9102
ERROR_SERVER_WORKER_UNPROCESSED_DATA = 9103
ERROR_CO_OUT_OF_COROUTINE = 10001
ERROR_CO_HAS_BEEN_BOUND = 10002
ERROR_CO_HAS_BEEN_DISCARDED = 10003
ERROR_CO_MUTEX_DOUBLE_UNLOCK = 10004
ERROR_CO_BLOCK_OBJECT_LOCKED = 10005
ERROR_CO_BLOCK_OBJECT_WAITING = 10006
ERROR_CO_YIELD_FAILED = 10007
ERROR_CO_GETCONTEXT_FAILED = 10008
ERROR_CO_SWAPCONTEXT_FAILED = 10009
ERROR_CO_MAKECONTEXT_FAILED = 10010
ERROR_CO_IOCPINIT_FAILED = 10011
ERROR_CO_PROTECT_STACK_FAILED = 10012
ERROR_CO_STD_THREAD_LINK_ERROR = 10013
ERROR_CO_DISABLED_MULTI_THREAD = 10014
ERROR_CO_CANNOT_CANCEL = 10015
ERROR_CO_NOT_EXISTS = 10016
ERROR_CO_CANCELED = 10017
ERROR_CO_TIMEDOUT = 10018
ERROR_CO_SOCKET_CLOSE_WAIT = 10019
TRACE_SERVER = 2
TRACE_CLIENT = 4
TRACE_BUFFER = 8
TRACE_CONN = 16
TRACE_EVENT = 32
TRACE_WORKER = 64
TRACE_MEMORY = 128
TRACE_REACTOR = 256
TRACE_PHP = 512
TRACE_HTTP = 1024
TRACE_HTTP2 = 2048
TRACE_EOF_PROTOCOL = 4096
TRACE_LENGTH_PROTOCOL = 8192
TRACE_CLOSE = 16384
TRACE_WEBSOCKET = 32768
TRACE_REDIS_CLIENT = 65536
TRACE_MYSQL_CLIENT = 131072
TRACE_HTTP_CLIENT = 262144
TRACE_AIO = 524288
TRACE_SSL = 1048576
TRACE_NORMAL = 2097152
TRACE_CHANNEL = 4194304
TRACE_TIMER = 8388608
TRACE_SOCKET = 16777216
TRACE_COROUTINE = 33554432
TRACE_CONTEXT = 67108864
TRACE_CO_HTTP_SERVER = 134217728
TRACE_TABLE = 268435456
TRACE_CO_CURL = 536870912
TRACE_CARES = 1073741824
TRACE_ZLIB = 2147483648
TRACE_CO_PGSQL = 4294967296
TRACE_CO_ODBC = 8589934592
TRACE_CO_ORACLE = 17179869184
TRACE_ALL = 9223372036854775807
LOG_DEBUG = 0
LOG_TRACE = 1
LOG_INFO = 2
LOG_NOTICE = 3
LOG_WARNING = 4
LOG_ERROR = 5
LOG_NONE = 6
LOG_ROTATION_SINGLE = 0
LOG_ROTATION_MONTHLY = 1
LOG_ROTATION_DAILY = 2
LOG_ROTATION_HOURLY = 3
LOG_ROTATION_EVERY_MINUTE = 4
IPC_NONE = 0
IPC_UNIXSOCK = 1
IPC_SOCKET = 3
IOV_MAX = 1024
FILELOCK = 2
MUTEX = 3
SEM = 4
RWLOCK = 1
SPINLOCK = 5
MSGQUEUE_ORIENT = 1
MSGQUEUE_BALANCE = 2
TIMER_MIN_MS = 1
TIMER_MIN_SEC = 0.001
TIMER_MAX_MS = 9223372036854775807
TIMER_MAX_SEC = 9.2233720368548E+15
DEFAULT_MAX_CORO_NUM = 100000
CORO_MAX_NUM_LIMIT = 9223372036854775807
CORO_INIT = 0
CORO_WAITING = 1
CORO_RUNNING = 2
CORO_END = 3
EXIT_IN_COROUTINE = 2
EXIT_IN_SERVER = 4
CHANNEL_OK = 0
CHANNEL_TIMEOUT = -1
CHANNEL_CLOSED = -2
CHANNEL_CANCELED = -3
HOOK_TCP = 2
HOOK_UDP = 4
HOOK_UNIX = 8
HOOK_UDG = 16
HOOK_SSL = 32
HOOK_TLS = 64
HOOK_STREAM_FUNCTION = 128
HOOK_STREAM_SELECT = 128
HOOK_FILE = 256
HOOK_STDIO = 32768
HOOK_SLEEP = 512
HOOK_PROC = 1024
HOOK_CURL = 2048
HOOK_NATIVE_CURL = 4096
HOOK_BLOCKING_FUNCTION = 8192
HOOK_SOCKETS = 16384
HOOK_PDO_PGSQL = 65536
HOOK_ALL = 2147481599
SOCKET_ECANCELED = 125
HTTP_CLIENT_ESTATUS_CONNECT_FAILED = -1
HTTP_CLIENT_ESTATUS_REQUEST_TIMEOUT = -2
HTTP_CLIENT_ESTATUS_SERVER_RESET = -3
HTTP_CLIENT_ESTATUS_SEND_FAILED = -4
HTTP2_TYPE_DATA = 0
HTTP2_TYPE_HEADERS = 1
HTTP2_TYPE_PRIORITY = 2
HTTP2_TYPE_RST_STREAM = 3
HTTP2_TYPE_SETTINGS = 4
HTTP2_TYPE_PUSH_PROMISE = 5
HTTP2_TYPE_PING = 6
HTTP2_TYPE_GOAWAY = 7
HTTP2_TYPE_WINDOW_UPDATE = 8
HTTP2_TYPE_CONTINUATION = 9
HTTP2_ERROR_NO_ERROR = 0
HTTP2_ERROR_PROTOCOL_ERROR = 1
HTTP2_ERROR_INTERNAL_ERROR = 2
HTTP2_ERROR_FLOW_CONTROL_ERROR = 3
HTTP2_ERROR_SETTINGS_TIMEOUT = 4
HTTP2_ERROR_STREAM_CLOSED = 5
HTTP2_ERROR_FRAME_SIZE_ERROR = 6
HTTP2_ERROR_REFUSED_STREAM = 7
HTTP2_ERROR_CANCEL = 8
HTTP2_ERROR_COMPRESSION_ERROR = 9
HTTP2_ERROR_CONNECT_ERROR = 10
HTTP2_ERROR_ENHANCE_YOUR_CALM = 11
HTTP2_ERROR_INADEQUATE_SECURITY = 12
HTTP2_ERROR_HTTP_1_1_REQUIRED = 13
MYSQLND_CR_UNKNOWN_ERROR = 2000
MYSQLND_CR_CONNECTION_ERROR = 2002
MYSQLND_CR_SERVER_GONE_ERROR = 2006
MYSQLND_CR_OUT_OF_MEMORY = 2008
MYSQLND_CR_SERVER_LOST = 2013
MYSQLND_CR_COMMANDS_OUT_OF_SYNC = 2014
MYSQLND_CR_CANT_FIND_CHARSET = 2019
MYSQLND_CR_MALFORMED_PACKET = 2027
MYSQLND_CR_NOT_IMPLEMENTED = 2054
MYSQLND_CR_NO_PREPARE_STMT = 2030
MYSQLND_CR_PARAMS_NOT_BOUND = 2031
MYSQLND_CR_INVALID_PARAMETER_NO = 2034
MYSQLND_CR_INVALID_BUFFER_USE = 2035
REDIS_MODE_MULTI = 0
REDIS_MODE_PIPELINE = 1
REDIS_TYPE_NOT_FOUND = 0
REDIS_TYPE_STRING = 1
REDIS_TYPE_SET = 2
REDIS_TYPE_LIST = 3
REDIS_TYPE_ZSET = 4
REDIS_TYPE_HASH = 5
REDIS_ERR_IO = 1
REDIS_ERR_OTHER = 2
REDIS_ERR_EOF = 3
REDIS_ERR_PROTOCOL = 4
REDIS_ERR_OOM = 5
REDIS_ERR_CLOSED = 6
REDIS_ERR_NOAUTH = 7
REDIS_ERR_ALLOC = 8
BASE = 1
PROCESS = 2
IPC_UNSOCK = 1
IPC_MSGQUEUE = 2
IPC_PREEMPTIVE = 3
SERVER_COMMAND_MASTER = 2
SERVER_COMMAND_MANAGER = 32
SERVER_COMMAND_REACTOR_THREAD = 4
SERVER_COMMAND_EVENT_WORKER = 8
SERVER_COMMAND_WORKER = 8
SERVER_COMMAND_TASK_WORKER = 16
DISPATCH_ROUND = 1
DISPATCH_FDMOD = 2
DISPATCH_IDLE_WORKER = 3
DISPATCH_IPMOD = 4
DISPATCH_UIDMOD = 5
DISPATCH_USERFUNC = 6
DISPATCH_STREAM = 7
DISPATCH_CO_CONN_LB = 8
DISPATCH_CO_REQ_LB = 9
DISPATCH_CONCURRENT_LB = 10
DISPATCH_RESULT_DISCARD_PACKET = -1
DISPATCH_RESULT_CLOSE_CONNECTION = -2
DISPATCH_RESULT_USERFUNC_FALLBACK = -3
TASK_TMPFILE = 1
TASK_SERIALIZE = 2
TASK_NONBLOCK = 4
TASK_CALLBACK = 8
TASK_WAITALL = 16
TASK_COROUTINE = 32
TASK_PEEK = 64
TASK_NOREPLY = 128
WORKER_BUSY = 1
WORKER_IDLE = 2
WORKER_EXIT = 3
WEBSOCKET_STATUS_CONNECTION = 1
WEBSOCKET_STATUS_HANDSHAKE = 2
WEBSOCKET_STATUS_ACTIVE = 3
WEBSOCKET_STATUS_CLOSING = 4
WEBSOCKET_OPCODE_CONTINUATION = 0
WEBSOCKET_OPCODE_TEXT = 1
WEBSOCKET_OPCODE_BINARY = 2
WEBSOCKET_OPCODE_CLOSE = 8
WEBSOCKET_OPCODE_PING = 9
WEBSOCKET_OPCODE_PONG = 10
WEBSOCKET_FLAG_FIN = 1
WEBSOCKET_FLAG_RSV1 = 4
WEBSOCKET_FLAG_RSV2 = 8
WEBSOCKET_FLAG_RSV3 = 16
WEBSOCKET_FLAG_MASK = 32
WEBSOCKET_FLAG_COMPRESS = 2
WEBSOCKET_CLOSE_NORMAL = 1000
WEBSOCKET_CLOSE_GOING_AWAY = 1001
WEBSOCKET_CLOSE_PROTOCOL_ERROR = 1002
WEBSOCKET_CLOSE_DATA_ERROR = 1003
WEBSOCKET_CLOSE_STATUS_ERROR = 1005
WEBSOCKET_CLOSE_ABNORMAL = 1006
WEBSOCKET_CLOSE_MESSAGE_ERROR = 1007
WEBSOCKET_CLOSE_POLICY_ERROR = 1008
WEBSOCKET_CLOSE_MESSAGE_TOO_BIG = 1009
WEBSOCKET_CLOSE_EXTENSION_MISSING = 1010
WEBSOCKET_CLOSE_SERVER_ERROR = 1011
WEBSOCKET_CLOSE_TLS = 1015
WEBSOCKET_STATUS_FRAME = 3
SW_PGSQL_ASSOC = 1
SW_PGSQL_NUM = 2
SW_PGSQL_BOTH = 3


def version():
    return phpy.call('swoole_version', )


def cpu_num():
    return phpy.call('swoole_cpu_num', )


def last_error():
    return phpy.call('swoole_last_error', )


def async_dns_lookup_coro(_domain_name, _timeout=60, _type=2):
    return phpy.call('swoole_async_dns_lookup_coro', _domain_name, _timeout, _type)


def async_set(_settings):
    return phpy.call('swoole_async_set', _settings)


def coroutine_create(_func, _params=None):
    return phpy.call('swoole_coroutine_create', _func, _params)


def coroutine_defer(_callback):
    return phpy.call('swoole_coroutine_defer', _callback)


def coroutine_socketpair(_domain, _type, _protocol):
    return phpy.call('swoole_coroutine_socketpair', _domain, _type, _protocol)


def test_kernel_coroutine(_count=100, _sleep_time=1):
    return phpy.call('swoole_test_kernel_coroutine', _count, _sleep_time)


def client_select(_read_array, _write_array, _error_array, _timeout=0.5):
    return phpy.call('swoole_client_select', _read_array, _write_array, _error_array, _timeout)


def select(_read_array, _write_array, _error_array, _timeout=0.5):
    return phpy.call('swoole_select', _read_array, _write_array, _error_array, _timeout)


def set_process_name(_process_name):
    return phpy.call('swoole_set_process_name', _process_name)


def get_local_ip():
    return phpy.call('swoole_get_local_ip', )


def get_local_mac():
    return phpy.call('swoole_get_local_mac', )


def strerror(_errno, _error_type=0):
    return phpy.call('swoole_strerror', _errno, _error_type)


def errno():
    return phpy.call('swoole_errno', )


def clear_error():
    return phpy.call('swoole_clear_error', )


def error_log(_level, _msg):
    return phpy.call('swoole_error_log', _level, _msg)


def error_log_ex(_level, _error, _msg):
    return phpy.call('swoole_error_log_ex', _level, _error, _msg)


def ignore_error(_error):
    return phpy.call('swoole_ignore_error', _error)


def hashcode(_data, _type=0):
    return phpy.call('swoole_hashcode', _data, _type)


def mime_type_add(_suffix, _mime_type):
    return phpy.call('swoole_mime_type_add', _suffix, _mime_type)


def mime_type_set(_suffix, _mime_type):
    return phpy.call('swoole_mime_type_set', _suffix, _mime_type)


def mime_type_delete(_suffix):
    return phpy.call('swoole_mime_type_delete', _suffix)


def mime_type_get(_filename):
    return phpy.call('swoole_mime_type_get', _filename)


def get_mime_type(_filename):
    return phpy.call('swoole_get_mime_type', _filename)


def mime_type_exists(_filename):
    return phpy.call('swoole_mime_type_exists', _filename)


def mime_type_list():
    return phpy.call('swoole_mime_type_list', )


def clear_dns_cache():
    return phpy.call('swoole_clear_dns_cache', )


def substr_unserialize(_str, _offset, _length=0, _options=[]):
    return phpy.call('swoole_substr_unserialize', _str, _offset, _length, _options)


def substr_json_decode(_str, _offset, _length=0, _associative=False, _depth=512, _flags=0):
    return phpy.call('swoole_substr_json_decode', _str, _offset, _length, _associative, _depth, _flags)


def internal_call_user_shutdown_begin():
    return phpy.call('swoole_internal_call_user_shutdown_begin', )


def get_objects():
    return phpy.call('swoole_get_objects', )


def get_vm_status():
    return phpy.call('swoole_get_vm_status', )


def get_object_by_handle(_handle):
    return phpy.call('swoole_get_object_by_handle', _handle)


def name_resolver_lookup(_name, _ctx):
    return phpy.call('swoole_name_resolver_lookup', _name, _ctx)


def name_resolver_add(_ns):
    return phpy.call('swoole_name_resolver_add', _ns)


def name_resolver_remove(_ns):
    return phpy.call('swoole_name_resolver_remove', _ns)


def go(_func):
    return phpy.call('go', _func)


def defer(_callback):
    return phpy.call('defer', _callback)


def event_add(_fd, _read_callback=None, _write_callback=None, _events=512):
    return phpy.call('swoole_event_add', _fd, _read_callback, _write_callback, _events)


def event_del(_fd):
    return phpy.call('swoole_event_del', _fd)


def event_set(_fd, _read_callback=None, _write_callback=None, _events=0):
    return phpy.call('swoole_event_set', _fd, _read_callback, _write_callback, _events)


def event_wait():
    return phpy.call('swoole_event_wait', )


def event_isset(_fd, _events=1536):
    return phpy.call('swoole_event_isset', _fd, _events)


def event_dispatch():
    return phpy.call('swoole_event_dispatch', )


def event_defer(_callback):
    return phpy.call('swoole_event_defer', _callback)


def event_cycle(_callback, _before=False):
    return phpy.call('swoole_event_cycle', _callback, _before)


def event_write(_fd, _data):
    return phpy.call('swoole_event_write', _fd, _data)


def event_exit():
    return phpy.call('swoole_event_exit', )


def timer_set(_settings):
    return phpy.call('swoole_timer_set', _settings)


def timer_after(_ms, _callback):
    return phpy.call('swoole_timer_after', _ms, _callback)


def timer_tick(_ms, _callback):
    return phpy.call('swoole_timer_tick', _ms, _callback)


def timer_info(_timer_id):
    return phpy.call('swoole_timer_info', _timer_id)


def timer_list():
    return phpy.call('swoole_timer_list', )


def timer_exists(_timer_id):
    return phpy.call('swoole_timer_exists', _timer_id)


def timer_stats():
    return phpy.call('swoole_timer_stats', )


def timer_clear(_timer_id):
    return phpy.call('swoole_timer_clear', _timer_id)


def timer_clear_all():
    return phpy.call('swoole_timer_clear_all', )


def native_curl_close(_handle):
    return phpy.call('swoole_native_curl_close', _handle)


def native_curl_copy_handle(_handle):
    return phpy.call('swoole_native_curl_copy_handle', _handle)


def native_curl_errno(_handle):
    return phpy.call('swoole_native_curl_errno', _handle)


def native_curl_error(_handle):
    return phpy.call('swoole_native_curl_error', _handle)


def native_curl_exec(_handle):
    return phpy.call('swoole_native_curl_exec', _handle)


def native_curl_getinfo(_handle, _option=None):
    return phpy.call('swoole_native_curl_getinfo', _handle, _option)


def native_curl_init(_url=None):
    return phpy.call('swoole_native_curl_init', _url)


def native_curl_setopt(_handle, _option, _value):
    return phpy.call('swoole_native_curl_setopt', _handle, _option, _value)


def native_curl_setopt_array(_handle, _options):
    return phpy.call('swoole_native_curl_setopt_array', _handle, _options)


def native_curl_reset(_handle):
    return phpy.call('swoole_native_curl_reset', _handle)


def native_curl_escape(_handle, _string):
    return phpy.call('swoole_native_curl_escape', _handle, _string)


def native_curl_unescape(_handle, _string):
    return phpy.call('swoole_native_curl_unescape', _handle, _string)


def native_curl_pause(_handle, _flags):
    return phpy.call('swoole_native_curl_pause', _handle, _flags)


def native_curl_multi_add_handle(_multi_handle, _handle):
    return phpy.call('swoole_native_curl_multi_add_handle', _multi_handle, _handle)


def native_curl_multi_close(_multi_handle):
    return phpy.call('swoole_native_curl_multi_close', _multi_handle)


def native_curl_multi_errno(_multi_handle):
    return phpy.call('swoole_native_curl_multi_errno', _multi_handle)


def native_curl_multi_exec(_multi_handle, _still_running):
    return phpy.call('swoole_native_curl_multi_exec', _multi_handle, _still_running)


def native_curl_multi_select(_multi_handle, _timeout=1):
    return phpy.call('swoole_native_curl_multi_select', _multi_handle, _timeout)


def native_curl_multi_setopt(_multi_handle, _option, _value):
    return phpy.call('swoole_native_curl_multi_setopt', _multi_handle, _option, _value)


def native_curl_multi_getcontent(_handle):
    return phpy.call('swoole_native_curl_multi_getcontent', _handle)


def native_curl_multi_info_read(_multi_handle, _queued_messages=None):
    return phpy.call('swoole_native_curl_multi_info_read', _multi_handle, _queued_messages)


def native_curl_multi_init():
    return phpy.call('swoole_native_curl_multi_init', )


def native_curl_multi_remove_handle(_multi_handle, _handle):
    return phpy.call('swoole_native_curl_multi_remove_handle', _multi_handle, _handle)




class Exception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Exception', _message, _code, _previous)

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

class Error():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Error', _message, _code, _previous)

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

class Event():

    def add(_fd, _read_callback=None, _write_callback=None, _events=512):
        return phpy.call(f"Swoole\\Event::add", _fd, _read_callback, _write_callback, _events)

    def _del(_fd):
        return phpy.call(f"Swoole\\Event::del", _fd)

    def set(_fd, _read_callback=None, _write_callback=None, _events=0):
        return phpy.call(f"Swoole\\Event::set", _fd, _read_callback, _write_callback, _events)

    def isset(_fd, _events=1536):
        return phpy.call(f"Swoole\\Event::isset", _fd, _events)

    def dispatch():
        return phpy.call(f"Swoole\\Event::dispatch", )

    def defer(_callback):
        return phpy.call(f"Swoole\\Event::defer", _callback)

    def cycle(_callback, _before=False):
        return phpy.call(f"Swoole\\Event::cycle", _callback, _before)

    def write(_fd, _data):
        return phpy.call(f"Swoole\\Event::write", _fd, _data)

    def wait():
        return phpy.call(f"Swoole\\Event::wait", )

    def rshutdown():
        return phpy.call(f"Swoole\\Event::rshutdown", )

    def exit():
        return phpy.call(f"Swoole\\Event::exit", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Event')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Atomic():

    def __init__(self, _value=0):
        self.__this = phpy.Object(f'Swoole\\Atomic', _value)

    def add(self, _add_value=1):
        return self.__this.call(f"add", _add_value)

    def sub(self, _sub_value=1):
        return self.__this.call(f"sub", _sub_value)

    def get(self):
        return self.__this.call(f"get", )

    def set(self, _value):
        return self.__this.call(f"set", _value)

    def wait(self, _timeout=1):
        return self.__this.call(f"wait", _timeout)

    def wakeup(self, _count=1):
        return self.__this.call(f"wakeup", _count)

    def cmpset(self, _cmp_value, _new_value):
        return self.__this.call(f"cmpset", _cmp_value, _new_value)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class AtomicLong():

    def __init__(self, _value=0):
        self.__this = phpy.Object(f'Swoole\\Atomic\\Long', _value)

    def add(self, _add_value=1):
        return self.__this.call(f"add", _add_value)

    def sub(self, _sub_value=1):
        return self.__this.call(f"sub", _sub_value)

    def get(self):
        return self.__this.call(f"get", )

    def set(self, _value):
        return self.__this.call(f"set", _value)

    def cmpset(self, _cmp_value, _new_value):
        return self.__this.call(f"cmpset", _cmp_value, _new_value)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Lock():
    FILELOCK = 2
    MUTEX = 3
    SEM = 4
    RWLOCK = 1
    SPINLOCK = 5

    def __init__(self, _type=3, _filename=""):
        self.__this = phpy.Object(f'Swoole\\Lock', _type, _filename)

    def lock(self):
        return self.__this.call(f"lock", )

    def lockwait(self, _timeout=1):
        return self.__this.call(f"lockwait", _timeout)

    def trylock(self):
        return self.__this.call(f"trylock", )

    def lock_read(self):
        return self.__this.call(f"lock_read", )

    def trylock_read(self):
        return self.__this.call(f"trylock_read", )

    def unlock(self):
        return self.__this.call(f"unlock", )

    def destroy(self):
        return self.__this.call(f"destroy", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Process():
    IPC_NOWAIT = 256
    PIPE_MASTER = 1
    PIPE_WORKER = 2
    PIPE_READ = 3
    PIPE_WRITE = 4

    def __init__(self, _callback, _redirect_stdin_and_stdout=False, _pipe_type=2, _enable_coroutine=False):
        self.__this = phpy.Object(f'Swoole\\Process', _callback, _redirect_stdin_and_stdout, _pipe_type, _enable_coroutine)

    def wait(_blocking=True):
        return phpy.call(f"Swoole\\Process::wait", _blocking)

    def signal(_signal_no, _callback=None):
        return phpy.call(f"Swoole\\Process::signal", _signal_no, _callback)

    def alarm(_usec, _type=0):
        return phpy.call(f"Swoole\\Process::alarm", _usec, _type)

    def kill(_pid, _signal_no=15):
        return phpy.call(f"Swoole\\Process::kill", _pid, _signal_no)

    def daemon(_nochdir=True, _noclose=True, _pipes=[]):
        return phpy.call(f"Swoole\\Process::daemon", _nochdir, _noclose, _pipes)

    def setAffinity(_cpu_settings):
        return phpy.call(f"Swoole\\Process::setAffinity", _cpu_settings)

    def setPriority(self, _which, _priority, _who=None):
        return self.__this.call(f"setPriority", _which, _priority, _who)

    def getPriority(self, _which, _who=None):
        return self.__this.call(f"getPriority", _which, _who)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def setTimeout(self, _seconds):
        return self.__this.call(f"setTimeout", _seconds)

    def setBlocking(self, _blocking):
        return self.__this.call(f"setBlocking", _blocking)

    def useQueue(self, _key=0, _mode=2, _capacity=-1):
        return self.__this.call(f"useQueue", _key, _mode, _capacity)

    def statQueue(self):
        return self.__this.call(f"statQueue", )

    def freeQueue(self):
        return self.__this.call(f"freeQueue", )

    def start(self):
        return self.__this.call(f"start", )

    def write(self, _data):
        return self.__this.call(f"write", _data)

    def close(self, _which=0):
        return self.__this.call(f"close", _which)

    def read(self, _size=8192):
        return self.__this.call(f"read", _size)

    def push(self, _data):
        return self.__this.call(f"push", _data)

    def pop(self, _size=65536):
        return self.__this.call(f"pop", _size)

    def exit(self, _exit_code=0):
        return self.__this.call(f"exit", _exit_code)

    def exec(self, _exec_file, _args):
        return self.__this.call(f"exec", _exec_file, _args)

    def exportSocket(self):
        return self.__this.call(f"exportSocket", )

    def name(self, _process_name):
        return self.__this.call(f"name", _process_name)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ProcessPool():

    def __init__(self, _worker_num, _ipc_type=0, _msgqueue_key=0, _enable_coroutine=False):
        self.__this = phpy.Object(f'Swoole\\Process\\Pool', _worker_num, _ipc_type, _msgqueue_key, _enable_coroutine)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def on(self, _name, _callback):
        return self.__this.call(f"on", _name, _callback)

    def getProcess(self, _work_id=-1):
        return self.__this.call(f"getProcess", _work_id)

    def listen(self, _host, _port=0, _backlog=2048):
        return self.__this.call(f"listen", _host, _port, _backlog)

    def write(self, _data):
        return self.__this.call(f"write", _data)

    def sendMessage(self, _data, _dst_worker_id):
        return self.__this.call(f"sendMessage", _data, _dst_worker_id)

    def detach(self):
        return self.__this.call(f"detach", )

    def start(self):
        return self.__this.call(f"start", )

    def stop(self):
        return self.__this.call(f"stop", )

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Table():
    TYPE_INT = 1
    TYPE_STRING = 3
    TYPE_FLOAT = 2

    def __init__(self, _table_size, _conflict_proportion=0.2):
        self.__this = phpy.Object(f'Swoole\\Table', _table_size, _conflict_proportion)

    def column(self, _name, _type, _size=0):
        return self.__this.call(f"column", _name, _type, _size)

    def create(self):
        return self.__this.call(f"create", )

    def destroy(self):
        return self.__this.call(f"destroy", )

    def set(self, _key, _value):
        return self.__this.call(f"set", _key, _value)

    def get(self, _key, _field=None):
        return self.__this.call(f"get", _key, _field)

    def count(self):
        return self.__this.call(f"count", )

    def _del(self, _key):
        return self.__this.call(f"del", _key)

    def delete(self, _key):
        return self.__this.call(f"delete", _key)

    def exists(self, _key):
        return self.__this.call(f"exists", _key)

    def exist(self, _key):
        return self.__this.call(f"exist", _key)

    def incr(self, _key, _column, _incrby=1):
        return self.__this.call(f"incr", _key, _column, _incrby)

    def decr(self, _key, _column, _incrby=1):
        return self.__this.call(f"decr", _key, _column, _incrby)

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getMemorySize(self):
        return self.__this.call(f"getMemorySize", )

    def stats(self):
        return self.__this.call(f"stats", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Timer():

    def set(_settings):
        return phpy.call(f"Swoole\\Timer::set", _settings)

    def tick(_ms, _callback, _params=None):
        return phpy.call(f"Swoole\\Timer::tick", _ms, _callback, _params)

    def after(_ms, _callback, _params=None):
        return phpy.call(f"Swoole\\Timer::after", _ms, _callback, _params)

    def exists(_timer_id):
        return phpy.call(f"Swoole\\Timer::exists", _timer_id)

    def info(_timer_id):
        return phpy.call(f"Swoole\\Timer::info", _timer_id)

    def stats():
        return phpy.call(f"Swoole\\Timer::stats", )

    def list():
        return phpy.call(f"Swoole\\Timer::list", )

    def clear(_timer_id):
        return phpy.call(f"Swoole\\Timer::clear", _timer_id)

    def clearAll():
        return phpy.call(f"Swoole\\Timer::clearAll", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Timer')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class TimerIterator():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0):
        self.__this = phpy.Object(f'Swoole\\Timer\\Iterator', _array, _flags)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def append(self, _value):
        return self.__this.call(f"append", _value)

    def getArrayCopy(self):
        return self.__this.call(f"getArrayCopy", )

    def count(self):
        return self.__this.call(f"count", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def asort(self, _flags=0):
        return self.__this.call(f"asort", _flags)

    def ksort(self, _flags=0):
        return self.__this.call(f"ksort", _flags)

    def uasort(self, _callback):
        return self.__this.call(f"uasort", _callback)

    def uksort(self, _callback):
        return self.__this.call(f"uksort", _callback)

    def natsort(self):
        return self.__this.call(f"natsort", )

    def natcasesort(self):
        return self.__this.call(f"natcasesort", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Coroutine():

    def create(_func, _param=None):
        return phpy.call(f"Swoole\\Coroutine::create", _func, _param)

    def defer(_callback):
        return phpy.call(f"Swoole\\Coroutine::defer", _callback)

    def set(_options):
        return phpy.call(f"Swoole\\Coroutine::set", _options)

    def getOptions():
        return phpy.call(f"Swoole\\Coroutine::getOptions", )

    def exists(_cid):
        return phpy.call(f"Swoole\\Coroutine::exists", _cid)

    def _yield():
        return phpy.call(f"Swoole\\Coroutine::yield", )

    def cancel(_cid):
        return phpy.call(f"Swoole\\Coroutine::cancel", _cid)

    def join(_cid_array, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::join", _cid_array, _timeout)

    def isCanceled():
        return phpy.call(f"Swoole\\Coroutine::isCanceled", )

    def suspend():
        return phpy.call(f"Swoole\\Coroutine::suspend", )

    def resume(_cid):
        return phpy.call(f"Swoole\\Coroutine::resume", _cid)

    def stats():
        return phpy.call(f"Swoole\\Coroutine::stats", )

    def getCid():
        return phpy.call(f"Swoole\\Coroutine::getCid", )

    def getuid():
        return phpy.call(f"Swoole\\Coroutine::getuid", )

    def getPcid(_cid=0):
        return phpy.call(f"Swoole\\Coroutine::getPcid", _cid)

    def getContext(_cid=0):
        return phpy.call(f"Swoole\\Coroutine::getContext", _cid)

    def getBackTrace(_cid=0, _options=1, _limit=0):
        return phpy.call(f"Swoole\\Coroutine::getBackTrace", _cid, _options, _limit)

    def printBackTrace(_cid=0, _options=0, _limit=0):
        return phpy.call(f"Swoole\\Coroutine::printBackTrace", _cid, _options, _limit)

    def getElapsed(_cid=0):
        return phpy.call(f"Swoole\\Coroutine::getElapsed", _cid)

    def getStackUsage(_cid=0):
        return phpy.call(f"Swoole\\Coroutine::getStackUsage", _cid)

    def list():
        return phpy.call(f"Swoole\\Coroutine::list", )

    def listCoroutines():
        return phpy.call(f"Swoole\\Coroutine::listCoroutines", )

    def enableScheduler():
        return phpy.call(f"Swoole\\Coroutine::enableScheduler", )

    def disableScheduler():
        return phpy.call(f"Swoole\\Coroutine::disableScheduler", )

    def gethostbyname(_domain_name, _type=2, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::gethostbyname", _domain_name, _type, _timeout)

    def dnsLookup(_domain_name, _timeout=60, _type=2):
        return phpy.call(f"Swoole\\Coroutine::dnsLookup", _domain_name, _timeout, _type)

    def exec(_command, _get_error_stream=False):
        return phpy.call(f"Swoole\\Coroutine::exec", _command, _get_error_stream)

    def sleep(_seconds):
        return phpy.call(f"Swoole\\Coroutine::sleep", _seconds)

    def getaddrinfo(_domain, _family=2, _socktype=1, _protocol=6, _service=None, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::getaddrinfo", _domain, _family, _socktype, _protocol, _service, _timeout)

    def statvfs(_path):
        return phpy.call(f"Swoole\\Coroutine::statvfs", _path)

    def readFile(_filename, _flag=0):
        return phpy.call(f"Swoole\\Coroutine::readFile", _filename, _flag)

    def writeFile(_filename, _file_content, _flags=0):
        return phpy.call(f"Swoole\\Coroutine::writeFile", _filename, _file_content, _flags)

    def wait(_timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::wait", _timeout)

    def waitPid(_pid, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::waitPid", _pid, _timeout)

    def waitSignal(_signo, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::waitSignal", _signo, _timeout)

    def waitEvent(_socket, _events=512, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine::waitEvent", _socket, _events, _timeout)

    def fread(_handle, _length=0):
        return phpy.call(f"Swoole\\Coroutine::fread", _handle, _length)

    def fgets(_handle):
        return phpy.call(f"Swoole\\Coroutine::fgets", _handle)

    def fwrite(_handle, _data, _length=0):
        return phpy.call(f"Swoole\\Coroutine::fwrite", _handle, _data, _length)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class co():

    def create(_func, _param=None):
        return phpy.call(f"co::create", _func, _param)

    def defer(_callback):
        return phpy.call(f"co::defer", _callback)

    def set(_options):
        return phpy.call(f"co::set", _options)

    def getOptions():
        return phpy.call(f"co::getOptions", )

    def exists(_cid):
        return phpy.call(f"co::exists", _cid)

    def _yield():
        return phpy.call(f"co::yield", )

    def cancel(_cid):
        return phpy.call(f"co::cancel", _cid)

    def join(_cid_array, _timeout=-1):
        return phpy.call(f"co::join", _cid_array, _timeout)

    def isCanceled():
        return phpy.call(f"co::isCanceled", )

    def suspend():
        return phpy.call(f"co::suspend", )

    def resume(_cid):
        return phpy.call(f"co::resume", _cid)

    def stats():
        return phpy.call(f"co::stats", )

    def getCid():
        return phpy.call(f"co::getCid", )

    def getuid():
        return phpy.call(f"co::getuid", )

    def getPcid(_cid=0):
        return phpy.call(f"co::getPcid", _cid)

    def getContext(_cid=0):
        return phpy.call(f"co::getContext", _cid)

    def getBackTrace(_cid=0, _options=1, _limit=0):
        return phpy.call(f"co::getBackTrace", _cid, _options, _limit)

    def printBackTrace(_cid=0, _options=0, _limit=0):
        return phpy.call(f"co::printBackTrace", _cid, _options, _limit)

    def getElapsed(_cid=0):
        return phpy.call(f"co::getElapsed", _cid)

    def getStackUsage(_cid=0):
        return phpy.call(f"co::getStackUsage", _cid)

    def list():
        return phpy.call(f"co::list", )

    def listCoroutines():
        return phpy.call(f"co::listCoroutines", )

    def enableScheduler():
        return phpy.call(f"co::enableScheduler", )

    def disableScheduler():
        return phpy.call(f"co::disableScheduler", )

    def gethostbyname(_domain_name, _type=2, _timeout=-1):
        return phpy.call(f"co::gethostbyname", _domain_name, _type, _timeout)

    def dnsLookup(_domain_name, _timeout=60, _type=2):
        return phpy.call(f"co::dnsLookup", _domain_name, _timeout, _type)

    def exec(_command, _get_error_stream=False):
        return phpy.call(f"co::exec", _command, _get_error_stream)

    def sleep(_seconds):
        return phpy.call(f"co::sleep", _seconds)

    def getaddrinfo(_domain, _family=2, _socktype=1, _protocol=6, _service=None, _timeout=-1):
        return phpy.call(f"co::getaddrinfo", _domain, _family, _socktype, _protocol, _service, _timeout)

    def statvfs(_path):
        return phpy.call(f"co::statvfs", _path)

    def readFile(_filename, _flag=0):
        return phpy.call(f"co::readFile", _filename, _flag)

    def writeFile(_filename, _file_content, _flags=0):
        return phpy.call(f"co::writeFile", _filename, _file_content, _flags)

    def wait(_timeout=-1):
        return phpy.call(f"co::wait", _timeout)

    def waitPid(_pid, _timeout=-1):
        return phpy.call(f"co::waitPid", _pid, _timeout)

    def waitSignal(_signo, _timeout=-1):
        return phpy.call(f"co::waitSignal", _signo, _timeout)

    def waitEvent(_socket, _events=512, _timeout=-1):
        return phpy.call(f"co::waitEvent", _socket, _events, _timeout)

    def fread(_handle, _length=0):
        return phpy.call(f"co::fread", _handle, _length)

    def fgets(_handle):
        return phpy.call(f"co::fgets", _handle)

    def fwrite(_handle, _data, _length=0):
        return phpy.call(f"co::fwrite", _handle, _data, _length)

    def __init__(self):
        self.__this = phpy.Object(f'co')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineIterator():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Iterator', _array, _flags)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def append(self, _value):
        return self.__this.call(f"append", _value)

    def getArrayCopy(self):
        return self.__this.call(f"getArrayCopy", )

    def count(self):
        return self.__this.call(f"count", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def asort(self, _flags=0):
        return self.__this.call(f"asort", _flags)

    def ksort(self, _flags=0):
        return self.__this.call(f"ksort", _flags)

    def uasort(self, _callback):
        return self.__this.call(f"uasort", _callback)

    def uksort(self, _callback):
        return self.__this.call(f"uksort", _callback)

    def natsort(self):
        return self.__this.call(f"natsort", )

    def natcasesort(self):
        return self.__this.call(f"natcasesort", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class iterator():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0):
        self.__this = phpy.Object(f'co\\iterator', _array, _flags)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def append(self, _value):
        return self.__this.call(f"append", _value)

    def getArrayCopy(self):
        return self.__this.call(f"getArrayCopy", )

    def count(self):
        return self.__this.call(f"count", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def asort(self, _flags=0):
        return self.__this.call(f"asort", _flags)

    def ksort(self, _flags=0):
        return self.__this.call(f"ksort", _flags)

    def uasort(self, _callback):
        return self.__this.call(f"uasort", _callback)

    def uksort(self, _callback):
        return self.__this.call(f"uksort", _callback)

    def natsort(self):
        return self.__this.call(f"natsort", )

    def natcasesort(self):
        return self.__this.call(f"natcasesort", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineContext():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0, _iterator_class="ArrayIterator"):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Context', _array, _flags, _iterator_class)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def append(self, _value):
        return self.__this.call(f"append", _value)

    def getArrayCopy(self):
        return self.__this.call(f"getArrayCopy", )

    def count(self):
        return self.__this.call(f"count", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def asort(self, _flags=0):
        return self.__this.call(f"asort", _flags)

    def ksort(self, _flags=0):
        return self.__this.call(f"ksort", _flags)

    def uasort(self, _callback):
        return self.__this.call(f"uasort", _callback)

    def uksort(self, _callback):
        return self.__this.call(f"uksort", _callback)

    def natsort(self):
        return self.__this.call(f"natsort", )

    def natcasesort(self):
        return self.__this.call(f"natcasesort", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def exchangeArray(self, _array):
        return self.__this.call(f"exchangeArray", _array)

    def setIteratorClass(self, _iterator_class):
        return self.__this.call(f"setIteratorClass", _iterator_class)

    def getIteratorClass(self):
        return self.__this.call(f"getIteratorClass", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class context():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0, _iterator_class="ArrayIterator"):
        self.__this = phpy.Object(f'co\\context', _array, _flags, _iterator_class)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def append(self, _value):
        return self.__this.call(f"append", _value)

    def getArrayCopy(self):
        return self.__this.call(f"getArrayCopy", )

    def count(self):
        return self.__this.call(f"count", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def asort(self, _flags=0):
        return self.__this.call(f"asort", _flags)

    def ksort(self, _flags=0):
        return self.__this.call(f"ksort", _flags)

    def uasort(self, _callback):
        return self.__this.call(f"uasort", _callback)

    def uksort(self, _callback):
        return self.__this.call(f"uksort", _callback)

    def natsort(self):
        return self.__this.call(f"natsort", )

    def natcasesort(self):
        return self.__this.call(f"natcasesort", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def exchangeArray(self, _array):
        return self.__this.call(f"exchangeArray", _array)

    def setIteratorClass(self, _iterator_class):
        return self.__this.call(f"setIteratorClass", _iterator_class)

    def getIteratorClass(self):
        return self.__this.call(f"getIteratorClass", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ExitException():

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def getStatus(self):
        return self.__this.call(f"getStatus", )

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\ExitException', _message, _code, _previous)

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

class CoroutineSystem():

    def gethostbyname(_domain_name, _type=2, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::gethostbyname", _domain_name, _type, _timeout)

    def dnsLookup(_domain_name, _timeout=60, _type=2):
        return phpy.call(f"Swoole\\Coroutine\\System::dnsLookup", _domain_name, _timeout, _type)

    def exec(_command, _get_error_stream=False):
        return phpy.call(f"Swoole\\Coroutine\\System::exec", _command, _get_error_stream)

    def sleep(_seconds):
        return phpy.call(f"Swoole\\Coroutine\\System::sleep", _seconds)

    def getaddrinfo(_domain, _family=2, _socktype=1, _protocol=6, _service=None, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::getaddrinfo", _domain, _family, _socktype, _protocol, _service, _timeout)

    def statvfs(_path):
        return phpy.call(f"Swoole\\Coroutine\\System::statvfs", _path)

    def readFile(_filename, _flag=0):
        return phpy.call(f"Swoole\\Coroutine\\System::readFile", _filename, _flag)

    def writeFile(_filename, _file_content, _flags=0):
        return phpy.call(f"Swoole\\Coroutine\\System::writeFile", _filename, _file_content, _flags)

    def wait(_timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::wait", _timeout)

    def waitPid(_pid, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::waitPid", _pid, _timeout)

    def waitSignal(_signo, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::waitSignal", _signo, _timeout)

    def waitEvent(_socket, _events=512, _timeout=-1):
        return phpy.call(f"Swoole\\Coroutine\\System::waitEvent", _socket, _events, _timeout)

    def fread(_handle, _length=0):
        return phpy.call(f"Swoole\\Coroutine\\System::fread", _handle, _length)

    def fwrite(_handle, _data, _length=0):
        return phpy.call(f"Swoole\\Coroutine\\System::fwrite", _handle, _data, _length)

    def fgets(_handle):
        return phpy.call(f"Swoole\\Coroutine\\System::fgets", _handle)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\System')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class system():

    def gethostbyname(_domain_name, _type=2, _timeout=-1):
        return phpy.call(f"co\\system::gethostbyname", _domain_name, _type, _timeout)

    def dnsLookup(_domain_name, _timeout=60, _type=2):
        return phpy.call(f"co\\system::dnsLookup", _domain_name, _timeout, _type)

    def exec(_command, _get_error_stream=False):
        return phpy.call(f"co\\system::exec", _command, _get_error_stream)

    def sleep(_seconds):
        return phpy.call(f"co\\system::sleep", _seconds)

    def getaddrinfo(_domain, _family=2, _socktype=1, _protocol=6, _service=None, _timeout=-1):
        return phpy.call(f"co\\system::getaddrinfo", _domain, _family, _socktype, _protocol, _service, _timeout)

    def statvfs(_path):
        return phpy.call(f"co\\system::statvfs", _path)

    def readFile(_filename, _flag=0):
        return phpy.call(f"co\\system::readFile", _filename, _flag)

    def writeFile(_filename, _file_content, _flags=0):
        return phpy.call(f"co\\system::writeFile", _filename, _file_content, _flags)

    def wait(_timeout=-1):
        return phpy.call(f"co\\system::wait", _timeout)

    def waitPid(_pid, _timeout=-1):
        return phpy.call(f"co\\system::waitPid", _pid, _timeout)

    def waitSignal(_signo, _timeout=-1):
        return phpy.call(f"co\\system::waitSignal", _signo, _timeout)

    def waitEvent(_socket, _events=512, _timeout=-1):
        return phpy.call(f"co\\system::waitEvent", _socket, _events, _timeout)

    def fread(_handle, _length=0):
        return phpy.call(f"co\\system::fread", _handle, _length)

    def fwrite(_handle, _data, _length=0):
        return phpy.call(f"co\\system::fwrite", _handle, _data, _length)

    def fgets(_handle):
        return phpy.call(f"co\\system::fgets", _handle)

    def __init__(self):
        self.__this = phpy.Object(f'co\\system')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineScheduler():

    def add(self, _func, _param=None):
        return self.__this.call(f"add", _func, _param)

    def parallel(self, _n, _func, _param=None):
        return self.__this.call(f"parallel", _n, _func, _param)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def getOptions(self):
        return self.__this.call(f"getOptions", )

    def start(self):
        return self.__this.call(f"start", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Scheduler')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class scheduler():

    def add(self, _func, _param=None):
        return self.__this.call(f"add", _func, _param)

    def parallel(self, _n, _func, _param=None):
        return self.__this.call(f"parallel", _n, _func, _param)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def getOptions(self):
        return self.__this.call(f"getOptions", )

    def start(self):
        return self.__this.call(f"start", )

    def __init__(self):
        self.__this = phpy.Object(f'co\\scheduler')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineChannel():

    def __init__(self, _size=1):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Channel', _size)

    def push(self, _data, _timeout=-1):
        return self.__this.call(f"push", _data, _timeout)

    def pop(self, _timeout=-1):
        return self.__this.call(f"pop", _timeout)

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def isFull(self):
        return self.__this.call(f"isFull", )

    def close(self):
        return self.__this.call(f"close", )

    def stats(self):
        return self.__this.call(f"stats", )

    def length(self):
        return self.__this.call(f"length", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class channel():

    def __init__(self, _size=1):
        self.__this = phpy.Object(f'co\\channel', _size)

    def push(self, _data, _timeout=-1):
        return self.__this.call(f"push", _data, _timeout)

    def pop(self, _timeout=-1):
        return self.__this.call(f"pop", _timeout)

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def isFull(self):
        return self.__this.call(f"isFull", )

    def close(self):
        return self.__this.call(f"close", )

    def stats(self):
        return self.__this.call(f"stats", )

    def length(self):
        return self.__this.call(f"length", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class chan():

    def __init__(self, _size=1):
        self.__this = phpy.Object(f'chan', _size)

    def push(self, _data, _timeout=-1):
        return self.__this.call(f"push", _data, _timeout)

    def pop(self, _timeout=-1):
        return self.__this.call(f"pop", _timeout)

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def isFull(self):
        return self.__this.call(f"isFull", )

    def close(self):
        return self.__this.call(f"close", )

    def stats(self):
        return self.__this.call(f"stats", )

    def length(self):
        return self.__this.call(f"length", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Runtime():

    def enableCoroutine(_enable=2147481599, _flags=2147481599):
        return phpy.call(f"Swoole\\Runtime::enableCoroutine", _enable, _flags)

    def getHookFlags():
        return phpy.call(f"Swoole\\Runtime::getHookFlags", )

    def setHookFlags(_flags):
        return phpy.call(f"Swoole\\Runtime::setHookFlags", _flags)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Runtime')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineCurlException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Curl\\Exception', _message, _code, _previous)

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

class coroutinecurlexception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'co\\coroutine\\curl\\exception', _message, _code, _previous)

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

class CoroutineSocket():

    def __init__(self, _domain, _type, _protocol=0):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Socket', _domain, _type, _protocol)

    def bind(self, _address, _port=0):
        return self.__this.call(f"bind", _address, _port)

    def listen(self, _backlog=512):
        return self.__this.call(f"listen", _backlog)

    def accept(self, _timeout=0):
        return self.__this.call(f"accept", _timeout)

    def connect(self, _host, _port=0, _timeout=0):
        return self.__this.call(f"connect", _host, _port, _timeout)

    def checkLiveness(self):
        return self.__this.call(f"checkLiveness", )

    def getBoundCid(self, _event):
        return self.__this.call(f"getBoundCid", _event)

    def peek(self, _length=65536):
        return self.__this.call(f"peek", _length)

    def recv(self, _length=65536, _timeout=0):
        return self.__this.call(f"recv", _length, _timeout)

    def recvAll(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvAll", _length, _timeout)

    def recvLine(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvLine", _length, _timeout)

    def recvWithBuffer(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvWithBuffer", _length, _timeout)

    def recvPacket(self, _timeout=0):
        return self.__this.call(f"recvPacket", _timeout)

    def send(self, _data, _timeout=0):
        return self.__this.call(f"send", _data, _timeout)

    def readVector(self, _io_vector, _timeout=0):
        return self.__this.call(f"readVector", _io_vector, _timeout)

    def readVectorAll(self, _io_vector, _timeout=0):
        return self.__this.call(f"readVectorAll", _io_vector, _timeout)

    def writeVector(self, _io_vector, _timeout=0):
        return self.__this.call(f"writeVector", _io_vector, _timeout)

    def writeVectorAll(self, _io_vector, _timeout=0):
        return self.__this.call(f"writeVectorAll", _io_vector, _timeout)

    def sendFile(self, _file, _offset=0, _length=0):
        return self.__this.call(f"sendFile", _file, _offset, _length)

    def sendAll(self, _data, _timeout=0):
        return self.__this.call(f"sendAll", _data, _timeout)

    def recvfrom(self, _peername, _timeout=0):
        return self.__this.call(f"recvfrom", _peername, _timeout)

    def sendto(self, _addr, _port, _data):
        return self.__this.call(f"sendto", _addr, _port, _data)

    def getOption(self, _level, _opt_name):
        return self.__this.call(f"getOption", _level, _opt_name)

    def setProtocol(self, _settings):
        return self.__this.call(f"setProtocol", _settings)

    def setOption(self, _level, _opt_name, _opt_value):
        return self.__this.call(f"setOption", _level, _opt_name, _opt_value)

    def sslHandshake(self):
        return self.__this.call(f"sslHandshake", )

    def shutdown(self, _how=2):
        return self.__this.call(f"shutdown", _how)

    def cancel(self, _event=512):
        return self.__this.call(f"cancel", _event)

    def close(self):
        return self.__this.call(f"close", )

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def isClosed(self):
        return self.__this.call(f"isClosed", )

    def _import(_stream):
        return phpy.call(f"Swoole\\Coroutine\\Socket::import", _stream)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class socket():

    def __init__(self, _domain, _type, _protocol=0):
        self.__this = phpy.Object(f'co\\socket', _domain, _type, _protocol)

    def bind(self, _address, _port=0):
        return self.__this.call(f"bind", _address, _port)

    def listen(self, _backlog=512):
        return self.__this.call(f"listen", _backlog)

    def accept(self, _timeout=0):
        return self.__this.call(f"accept", _timeout)

    def connect(self, _host, _port=0, _timeout=0):
        return self.__this.call(f"connect", _host, _port, _timeout)

    def checkLiveness(self):
        return self.__this.call(f"checkLiveness", )

    def getBoundCid(self, _event):
        return self.__this.call(f"getBoundCid", _event)

    def peek(self, _length=65536):
        return self.__this.call(f"peek", _length)

    def recv(self, _length=65536, _timeout=0):
        return self.__this.call(f"recv", _length, _timeout)

    def recvAll(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvAll", _length, _timeout)

    def recvLine(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvLine", _length, _timeout)

    def recvWithBuffer(self, _length=65536, _timeout=0):
        return self.__this.call(f"recvWithBuffer", _length, _timeout)

    def recvPacket(self, _timeout=0):
        return self.__this.call(f"recvPacket", _timeout)

    def send(self, _data, _timeout=0):
        return self.__this.call(f"send", _data, _timeout)

    def readVector(self, _io_vector, _timeout=0):
        return self.__this.call(f"readVector", _io_vector, _timeout)

    def readVectorAll(self, _io_vector, _timeout=0):
        return self.__this.call(f"readVectorAll", _io_vector, _timeout)

    def writeVector(self, _io_vector, _timeout=0):
        return self.__this.call(f"writeVector", _io_vector, _timeout)

    def writeVectorAll(self, _io_vector, _timeout=0):
        return self.__this.call(f"writeVectorAll", _io_vector, _timeout)

    def sendFile(self, _file, _offset=0, _length=0):
        return self.__this.call(f"sendFile", _file, _offset, _length)

    def sendAll(self, _data, _timeout=0):
        return self.__this.call(f"sendAll", _data, _timeout)

    def recvfrom(self, _peername, _timeout=0):
        return self.__this.call(f"recvfrom", _peername, _timeout)

    def sendto(self, _addr, _port, _data):
        return self.__this.call(f"sendto", _addr, _port, _data)

    def getOption(self, _level, _opt_name):
        return self.__this.call(f"getOption", _level, _opt_name)

    def setProtocol(self, _settings):
        return self.__this.call(f"setProtocol", _settings)

    def setOption(self, _level, _opt_name, _opt_value):
        return self.__this.call(f"setOption", _level, _opt_name, _opt_value)

    def sslHandshake(self):
        return self.__this.call(f"sslHandshake", )

    def shutdown(self, _how=2):
        return self.__this.call(f"shutdown", _how)

    def cancel(self, _event=512):
        return self.__this.call(f"cancel", _event)

    def close(self):
        return self.__this.call(f"close", )

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def isClosed(self):
        return self.__this.call(f"isClosed", )

    def _import(_stream):
        return phpy.call(f"co\\socket::import", _stream)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineSocketException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Socket\\Exception', _message, _code, _previous)

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

class socketexception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'co\\socket\\exception', _message, _code, _previous)

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

class Client():
    MSG_OOB = 1
    MSG_PEEK = 2
    MSG_DONTWAIT = 64
    MSG_WAITALL = 256
    SHUT_RDWR = 2
    SHUT_RD = 0
    SHUT_WR = 1

    def __init__(self, _type, _async=False, _id=""):
        self.__this = phpy.Object(f'Swoole\\Client', _type, _async, _id)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def connect(self, _host, _port=0, _timeout=0.5, _sock_flag=0):
        return self.__this.call(f"connect", _host, _port, _timeout, _sock_flag)

    def recv(self, _size=65536, _flag=0):
        return self.__this.call(f"recv", _size, _flag)

    def send(self, _data, _flag=0):
        return self.__this.call(f"send", _data, _flag)

    def sendfile(self, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _filename, _offset, _length)

    def sendto(self, _ip, _port, _data):
        return self.__this.call(f"sendto", _ip, _port, _data)

    def shutdown(self, _how):
        return self.__this.call(f"shutdown", _how)

    def enableSSL(self):
        return self.__this.call(f"enableSSL", )

    def getPeerCert(self):
        return self.__this.call(f"getPeerCert", )

    def verifyPeerCert(self):
        return self.__this.call(f"verifyPeerCert", )

    def isConnected(self):
        return self.__this.call(f"isConnected", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def close(self, _force=False):
        return self.__this.call(f"close", _force)

    def getSocket(self):
        return self.__this.call(f"getSocket", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ClientException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Client\\Exception', _message, _code, _previous)

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

class CoroutineClient():
    MSG_OOB = 1
    MSG_PEEK = 2
    MSG_DONTWAIT = 64
    MSG_WAITALL = 256

    def __init__(self, _type):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Client', _type)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def connect(self, _host, _port=0, _timeout=0, _sock_flag=0):
        return self.__this.call(f"connect", _host, _port, _timeout, _sock_flag)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def peek(self, _length=65535):
        return self.__this.call(f"peek", _length)

    def send(self, _data, _timeout=0):
        return self.__this.call(f"send", _data, _timeout)

    def sendfile(self, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _filename, _offset, _length)

    def sendto(self, _address, _port, _data):
        return self.__this.call(f"sendto", _address, _port, _data)

    def recvfrom(self, _length, _address, _port=0):
        return self.__this.call(f"recvfrom", _length, _address, _port)

    def enableSSL(self):
        return self.__this.call(f"enableSSL", )

    def getPeerCert(self):
        return self.__this.call(f"getPeerCert", )

    def verifyPeerCert(self, _allow_self_signed=False):
        return self.__this.call(f"verifyPeerCert", _allow_self_signed)

    def isConnected(self):
        return self.__this.call(f"isConnected", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def close(self):
        return self.__this.call(f"close", )

    def exportSocket(self):
        return self.__this.call(f"exportSocket", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class client():
    MSG_OOB = 1
    MSG_PEEK = 2
    MSG_DONTWAIT = 64
    MSG_WAITALL = 256

    def __init__(self, _type):
        self.__this = phpy.Object(f'co\\client', _type)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def connect(self, _host, _port=0, _timeout=0, _sock_flag=0):
        return self.__this.call(f"connect", _host, _port, _timeout, _sock_flag)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def peek(self, _length=65535):
        return self.__this.call(f"peek", _length)

    def send(self, _data, _timeout=0):
        return self.__this.call(f"send", _data, _timeout)

    def sendfile(self, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _filename, _offset, _length)

    def sendto(self, _address, _port, _data):
        return self.__this.call(f"sendto", _address, _port, _data)

    def recvfrom(self, _length, _address, _port=0):
        return self.__this.call(f"recvfrom", _length, _address, _port)

    def enableSSL(self):
        return self.__this.call(f"enableSSL", )

    def getPeerCert(self):
        return self.__this.call(f"getPeerCert", )

    def verifyPeerCert(self, _allow_self_signed=False):
        return self.__this.call(f"verifyPeerCert", _allow_self_signed)

    def isConnected(self):
        return self.__this.call(f"isConnected", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def close(self):
        return self.__this.call(f"close", )

    def exportSocket(self):
        return self.__this.call(f"exportSocket", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineHttpClient():

    def __init__(self, _host, _port=0, _ssl=False):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Http\\Client', _host, _port, _ssl)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer=True):
        return self.__this.call(f"setDefer", _defer)

    def setMethod(self, _method):
        return self.__this.call(f"setMethod", _method)

    def setHeaders(self, _headers):
        return self.__this.call(f"setHeaders", _headers)

    def setBasicAuth(self, _username, _password):
        return self.__this.call(f"setBasicAuth", _username, _password)

    def setCookies(self, _cookies):
        return self.__this.call(f"setCookies", _cookies)

    def setData(self, _data):
        return self.__this.call(f"setData", _data)

    def addFile(self, _path, _name, _type=None, _filename=None, _offset=0, _length=0):
        return self.__this.call(f"addFile", _path, _name, _type, _filename, _offset, _length)

    def addData(self, _path, _name, _type=None, _filename=None):
        return self.__this.call(f"addData", _path, _name, _type, _filename)

    def execute(self, _path):
        return self.__this.call(f"execute", _path)

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def get(self, _path):
        return self.__this.call(f"get", _path)

    def post(self, _path, _data):
        return self.__this.call(f"post", _path, _data)

    def download(self, _path, _file, _offset=0):
        return self.__this.call(f"download", _path, _file, _offset)

    def getBody(self):
        return self.__this.call(f"getBody", )

    def getHeaders(self):
        return self.__this.call(f"getHeaders", )

    def getCookies(self):
        return self.__this.call(f"getCookies", )

    def getStatusCode(self):
        return self.__this.call(f"getStatusCode", )

    def getHeaderOut(self):
        return self.__this.call(f"getHeaderOut", )

    def getPeerCert(self):
        return self.__this.call(f"getPeerCert", )

    def upgrade(self, _path):
        return self.__this.call(f"upgrade", _path)

    def push(self, _data, _opcode=1, _flags=1):
        return self.__this.call(f"push", _data, _opcode, _flags)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class httpclient():

    def __init__(self, _host, _port=0, _ssl=False):
        self.__this = phpy.Object(f'co\\http\\client', _host, _port, _ssl)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer=True):
        return self.__this.call(f"setDefer", _defer)

    def setMethod(self, _method):
        return self.__this.call(f"setMethod", _method)

    def setHeaders(self, _headers):
        return self.__this.call(f"setHeaders", _headers)

    def setBasicAuth(self, _username, _password):
        return self.__this.call(f"setBasicAuth", _username, _password)

    def setCookies(self, _cookies):
        return self.__this.call(f"setCookies", _cookies)

    def setData(self, _data):
        return self.__this.call(f"setData", _data)

    def addFile(self, _path, _name, _type=None, _filename=None, _offset=0, _length=0):
        return self.__this.call(f"addFile", _path, _name, _type, _filename, _offset, _length)

    def addData(self, _path, _name, _type=None, _filename=None):
        return self.__this.call(f"addData", _path, _name, _type, _filename)

    def execute(self, _path):
        return self.__this.call(f"execute", _path)

    def getpeername(self):
        return self.__this.call(f"getpeername", )

    def getsockname(self):
        return self.__this.call(f"getsockname", )

    def get(self, _path):
        return self.__this.call(f"get", _path)

    def post(self, _path, _data):
        return self.__this.call(f"post", _path, _data)

    def download(self, _path, _file, _offset=0):
        return self.__this.call(f"download", _path, _file, _offset)

    def getBody(self):
        return self.__this.call(f"getBody", )

    def getHeaders(self):
        return self.__this.call(f"getHeaders", )

    def getCookies(self):
        return self.__this.call(f"getCookies", )

    def getStatusCode(self):
        return self.__this.call(f"getStatusCode", )

    def getHeaderOut(self):
        return self.__this.call(f"getHeaderOut", )

    def getPeerCert(self):
        return self.__this.call(f"getPeerCert", )

    def upgrade(self, _path):
        return self.__this.call(f"upgrade", _path)

    def push(self, _data, _opcode=1, _flags=1):
        return self.__this.call(f"push", _data, _opcode, _flags)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineHttpClientException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Http\\Client\\Exception', _message, _code, _previous)

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

class httpclientexception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'co\\http\\client\\exception', _message, _code, _previous)

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

class CoroutineHttp2Client():

    def __init__(self, _host, _port=80, _open_ssl=False):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Http2\\Client', _host, _port, _open_ssl)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def connect(self):
        return self.__this.call(f"connect", )

    def stats(self, _key=""):
        return self.__this.call(f"stats", _key)

    def isStreamExist(self, _stream_id):
        return self.__this.call(f"isStreamExist", _stream_id)

    def send(self, _request):
        return self.__this.call(f"send", _request)

    def write(self, _stream_id, _data, _end_stream=False):
        return self.__this.call(f"write", _stream_id, _data, _end_stream)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def read(self, _timeout=0):
        return self.__this.call(f"read", _timeout)

    def goaway(self, _error_code=0, _debug_data=""):
        return self.__this.call(f"goaway", _error_code, _debug_data)

    def ping(self):
        return self.__this.call(f"ping", )

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class http2client():

    def __init__(self, _host, _port=80, _open_ssl=False):
        self.__this = phpy.Object(f'co\\http2\\client', _host, _port, _open_ssl)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def connect(self):
        return self.__this.call(f"connect", )

    def stats(self, _key=""):
        return self.__this.call(f"stats", _key)

    def isStreamExist(self, _stream_id):
        return self.__this.call(f"isStreamExist", _stream_id)

    def send(self, _request):
        return self.__this.call(f"send", _request)

    def write(self, _stream_id, _data, _end_stream=False):
        return self.__this.call(f"write", _stream_id, _data, _end_stream)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def read(self, _timeout=0):
        return self.__this.call(f"read", _timeout)

    def goaway(self, _error_code=0, _debug_data=""):
        return self.__this.call(f"goaway", _error_code, _debug_data)

    def ping(self):
        return self.__this.call(f"ping", )

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineHttp2ClientException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Http2\\Client\\Exception', _message, _code, _previous)

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

class http2clientexception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'co\\http2\\client\\exception', _message, _code, _previous)

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

class Http2Request():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Http2\\Request')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Http2Response():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Http2\\Response')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineMySQL():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\MySQL', )

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer=None):
        return self.__this.call(f"setDefer", _defer)

    def connect(self, _server_config=None):
        return self.__this.call(f"connect", _server_config)

    def query(self, _sql, _timeout=None):
        return self.__this.call(f"query", _sql, _timeout)

    def fetch(self):
        return self.__this.call(f"fetch", )

    def fetchAll(self):
        return self.__this.call(f"fetchAll", )

    def nextResult(self):
        return self.__this.call(f"nextResult", )

    def prepare(self, _query, _timeout=None):
        return self.__this.call(f"prepare", _query, _timeout)

    def recv(self):
        return self.__this.call(f"recv", )

    def begin(self, _timeout=None):
        return self.__this.call(f"begin", _timeout)

    def commit(self, _timeout=None):
        return self.__this.call(f"commit", _timeout)

    def rollback(self, _timeout=None):
        return self.__this.call(f"rollback", _timeout)

    def escape(self, _string, _flags=None):
        return self.__this.call(f"escape", _string, _flags)

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class mysql():

    def __init__(self):
        self.__this = phpy.Object(f'co\\mysql', )

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer=None):
        return self.__this.call(f"setDefer", _defer)

    def connect(self, _server_config=None):
        return self.__this.call(f"connect", _server_config)

    def query(self, _sql, _timeout=None):
        return self.__this.call(f"query", _sql, _timeout)

    def fetch(self):
        return self.__this.call(f"fetch", )

    def fetchAll(self):
        return self.__this.call(f"fetchAll", )

    def nextResult(self):
        return self.__this.call(f"nextResult", )

    def prepare(self, _query, _timeout=None):
        return self.__this.call(f"prepare", _query, _timeout)

    def recv(self):
        return self.__this.call(f"recv", )

    def begin(self, _timeout=None):
        return self.__this.call(f"begin", _timeout)

    def commit(self, _timeout=None):
        return self.__this.call(f"commit", _timeout)

    def rollback(self, _timeout=None):
        return self.__this.call(f"rollback", _timeout)

    def escape(self, _string, _flags=None):
        return self.__this.call(f"escape", _string, _flags)

    def close(self):
        return self.__this.call(f"close", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineMySQLStatement():

    def execute(self, _params=None, _timeout=None):
        return self.__this.call(f"execute", _params, _timeout)

    def fetch(self, _timeout=None):
        return self.__this.call(f"fetch", _timeout)

    def fetchAll(self, _timeout=None):
        return self.__this.call(f"fetchAll", _timeout)

    def nextResult(self, _timeout=None):
        return self.__this.call(f"nextResult", _timeout)

    def recv(self, _timeout=None):
        return self.__this.call(f"recv", _timeout)

    def close(self):
        return self.__this.call(f"close", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\MySQL\\Statement')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class mysqlstatement():

    def execute(self, _params=None, _timeout=None):
        return self.__this.call(f"execute", _params, _timeout)

    def fetch(self, _timeout=None):
        return self.__this.call(f"fetch", _timeout)

    def fetchAll(self, _timeout=None):
        return self.__this.call(f"fetchAll", _timeout)

    def nextResult(self, _timeout=None):
        return self.__this.call(f"nextResult", _timeout)

    def recv(self, _timeout=None):
        return self.__this.call(f"recv", _timeout)

    def close(self):
        return self.__this.call(f"close", )

    def __init__(self):
        self.__this = phpy.Object(f'co\\mysql\\statement')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineMySQLException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\MySQL\\Exception', _message, _code, _previous)

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

class mysqlexception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'co\\mysql\\exception', _message, _code, _previous)

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

class CoroutineRedis():

    def __init__(self, _config=None):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Redis', _config)

    def connect(self, _host, _port=None, _serialize=None):
        return self.__this.call(f"connect", _host, _port, _serialize)

    def getAuth(self):
        return self.__this.call(f"getAuth", )

    def getDBNum(self):
        return self.__this.call(f"getDBNum", )

    def getOptions(self):
        return self.__this.call(f"getOptions", )

    def setOptions(self, _options):
        return self.__this.call(f"setOptions", _options)

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer):
        return self.__this.call(f"setDefer", _defer)

    def recv(self):
        return self.__this.call(f"recv", )

    def request(self, _params):
        return self.__this.call(f"request", _params)

    def close(self):
        return self.__this.call(f"close", )

    def set(self, _key, _value, _timeout=None, _opt=None):
        return self.__this.call(f"set", _key, _value, _timeout, _opt)

    def setBit(self, _key, _offset, _value):
        return self.__this.call(f"setBit", _key, _offset, _value)

    def setEx(self, _key, _expire, _value):
        return self.__this.call(f"setEx", _key, _expire, _value)

    def psetEx(self, _key, _expire, _value):
        return self.__this.call(f"psetEx", _key, _expire, _value)

    def lSet(self, _key, _index, _value):
        return self.__this.call(f"lSet", _key, _index, _value)

    def get(self, _key):
        return self.__this.call(f"get", _key)

    def mGet(self, _keys):
        return self.__this.call(f"mGet", _keys)

    def _del(self, _key, _other_keys=None):
        return self.__this.call(f"del", _key, _other_keys)

    def hDel(self, _key, _member, _other_members=None):
        return self.__this.call(f"hDel", _key, _member, _other_members)

    def hSet(self, _key, _member, _value):
        return self.__this.call(f"hSet", _key, _member, _value)

    def hMSet(self, _key, _pairs):
        return self.__this.call(f"hMSet", _key, _pairs)

    def hSetNx(self, _key, _member, _value):
        return self.__this.call(f"hSetNx", _key, _member, _value)

    def delete(self, _key, _other_keys=None):
        return self.__this.call(f"delete", _key, _other_keys)

    def mSet(self, _pairs):
        return self.__this.call(f"mSet", _pairs)

    def mSetNx(self, _pairs):
        return self.__this.call(f"mSetNx", _pairs)

    def getKeys(self, _pattern):
        return self.__this.call(f"getKeys", _pattern)

    def keys(self, _pattern):
        return self.__this.call(f"keys", _pattern)

    def exists(self, _key, _other_keys=None):
        return self.__this.call(f"exists", _key, _other_keys)

    def type(self, _key):
        return self.__this.call(f"type", _key)

    def strLen(self, _key):
        return self.__this.call(f"strLen", _key)

    def lPop(self, _key):
        return self.__this.call(f"lPop", _key)

    def blPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"blPop", _key, _timeout_or_key, _extra_args)

    def rPop(self, _key):
        return self.__this.call(f"rPop", _key)

    def brPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"brPop", _key, _timeout_or_key, _extra_args)

    def bRPopLPush(self, _src, _dst, _timeout):
        return self.__this.call(f"bRPopLPush", _src, _dst, _timeout)

    def lSize(self, _key):
        return self.__this.call(f"lSize", _key)

    def lLen(self, _key):
        return self.__this.call(f"lLen", _key)

    def sSize(self, _key):
        return self.__this.call(f"sSize", _key)

    def scard(self, _key):
        return self.__this.call(f"scard", _key)

    def sPop(self, _key):
        return self.__this.call(f"sPop", _key)

    def sMembers(self, _key):
        return self.__this.call(f"sMembers", _key)

    def sGetMembers(self, _key):
        return self.__this.call(f"sGetMembers", _key)

    def sRandMember(self, _key, _count=None):
        return self.__this.call(f"sRandMember", _key, _count)

    def persist(self, _key):
        return self.__this.call(f"persist", _key)

    def ttl(self, _key):
        return self.__this.call(f"ttl", _key)

    def pttl(self, _key):
        return self.__this.call(f"pttl", _key)

    def zCard(self, _key):
        return self.__this.call(f"zCard", _key)

    def zSize(self, _key):
        return self.__this.call(f"zSize", _key)

    def hLen(self, _key):
        return self.__this.call(f"hLen", _key)

    def hKeys(self, _key):
        return self.__this.call(f"hKeys", _key)

    def hVals(self, _key):
        return self.__this.call(f"hVals", _key)

    def hGetAll(self, _key):
        return self.__this.call(f"hGetAll", _key)

    def debug(self, _key):
        return self.__this.call(f"debug", _key)

    def restore(self, _ttl, _key, _value):
        return self.__this.call(f"restore", _ttl, _key, _value)

    def dump(self, _key):
        return self.__this.call(f"dump", _key)

    def renameKey(self, _key, _newkey):
        return self.__this.call(f"renameKey", _key, _newkey)

    def rename(self, _key, _newkey):
        return self.__this.call(f"rename", _key, _newkey)

    def renameNx(self, _key, _newkey):
        return self.__this.call(f"renameNx", _key, _newkey)

    def rpoplpush(self, _src, _dst):
        return self.__this.call(f"rpoplpush", _src, _dst)

    def randomKey(self):
        return self.__this.call(f"randomKey", )

    def pfadd(self, _key, _elements):
        return self.__this.call(f"pfadd", _key, _elements)

    def pfcount(self, _key):
        return self.__this.call(f"pfcount", _key)

    def pfmerge(self, _dstkey, _keys):
        return self.__this.call(f"pfmerge", _dstkey, _keys)

    def ping(self):
        return self.__this.call(f"ping", )

    def auth(self, _password):
        return self.__this.call(f"auth", _password)

    def unwatch(self):
        return self.__this.call(f"unwatch", )

    def watch(self, _key, _other_keys=None):
        return self.__this.call(f"watch", _key, _other_keys)

    def save(self):
        return self.__this.call(f"save", )

    def bgSave(self):
        return self.__this.call(f"bgSave", )

    def lastSave(self):
        return self.__this.call(f"lastSave", )

    def flushDB(self):
        return self.__this.call(f"flushDB", )

    def flushAll(self):
        return self.__this.call(f"flushAll", )

    def dbSize(self):
        return self.__this.call(f"dbSize", )

    def bgrewriteaof(self):
        return self.__this.call(f"bgrewriteaof", )

    def time(self):
        return self.__this.call(f"time", )

    def role(self):
        return self.__this.call(f"role", )

    def setRange(self, _key, _offset, _value):
        return self.__this.call(f"setRange", _key, _offset, _value)

    def setNx(self, _key, _value):
        return self.__this.call(f"setNx", _key, _value)

    def getSet(self, _key, _value):
        return self.__this.call(f"getSet", _key, _value)

    def append(self, _key, _value):
        return self.__this.call(f"append", _key, _value)

    def lPushx(self, _key, _value):
        return self.__this.call(f"lPushx", _key, _value)

    def lPush(self, _key, _value):
        return self.__this.call(f"lPush", _key, _value)

    def rPush(self, _key, _value):
        return self.__this.call(f"rPush", _key, _value)

    def rPushx(self, _key, _value):
        return self.__this.call(f"rPushx", _key, _value)

    def sContains(self, _key, _value):
        return self.__this.call(f"sContains", _key, _value)

    def sismember(self, _key, _value):
        return self.__this.call(f"sismember", _key, _value)

    def zScore(self, _key, _member):
        return self.__this.call(f"zScore", _key, _member)

    def zRank(self, _key, _member):
        return self.__this.call(f"zRank", _key, _member)

    def zRevRank(self, _key, _member):
        return self.__this.call(f"zRevRank", _key, _member)

    def hGet(self, _key, _member):
        return self.__this.call(f"hGet", _key, _member)

    def hMGet(self, _key, _keys):
        return self.__this.call(f"hMGet", _key, _keys)

    def hExists(self, _key, _member):
        return self.__this.call(f"hExists", _key, _member)

    def publish(self, _channel, _message):
        return self.__this.call(f"publish", _channel, _message)

    def zIncrBy(self, _key, _value, _member):
        return self.__this.call(f"zIncrBy", _key, _value, _member)

    def zAdd(self, _key, _score, _value):
        return self.__this.call(f"zAdd", _key, _score, _value)

    def zPopMin(self, _key, _count):
        return self.__this.call(f"zPopMin", _key, _count)

    def zPopMax(self, _key, _count):
        return self.__this.call(f"zPopMax", _key, _count)

    def bzPopMin(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMin", _key, _timeout_or_key, _extra_args)

    def bzPopMax(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMax", _key, _timeout_or_key, _extra_args)

    def zDeleteRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zDeleteRangeByScore", _key, _min, _max)

    def zRemRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByScore", _key, _min, _max)

    def zCount(self, _key, _min, _max):
        return self.__this.call(f"zCount", _key, _min, _max)

    def zRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRange", _key, _start, _end, _scores)

    def zRevRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRevRange", _key, _start, _end, _scores)

    def zRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRangeByScore", _key, _start, _end, _options)

    def zRevRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRevRangeByScore", _key, _start, _end, _options)

    def zRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRangeByLex", _key, _min, _max, _offset, _limit)

    def zRevRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRevRangeByLex", _key, _min, _max, _offset, _limit)

    def zInter(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zInter", _key, _keys, _weights, _aggregate)

    def zinterstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zinterstore", _key, _keys, _weights, _aggregate)

    def zUnion(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zUnion", _key, _keys, _weights, _aggregate)

    def zunionstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zunionstore", _key, _keys, _weights, _aggregate)

    def incrBy(self, _key, _value):
        return self.__this.call(f"incrBy", _key, _value)

    def hIncrBy(self, _key, _member, _value):
        return self.__this.call(f"hIncrBy", _key, _member, _value)

    def incr(self, _key):
        return self.__this.call(f"incr", _key)

    def decrBy(self, _key, _value):
        return self.__this.call(f"decrBy", _key, _value)

    def decr(self, _key):
        return self.__this.call(f"decr", _key)

    def getBit(self, _key, _offset):
        return self.__this.call(f"getBit", _key, _offset)

    def lInsert(self, _key, _position, _pivot, _value):
        return self.__this.call(f"lInsert", _key, _position, _pivot, _value)

    def lGet(self, _key, _index):
        return self.__this.call(f"lGet", _key, _index)

    def lIndex(self, _key, _integer):
        return self.__this.call(f"lIndex", _key, _integer)

    def setTimeout(self, _key, _timeout):
        return self.__this.call(f"setTimeout", _key, _timeout)

    def expire(self, _key, _integer):
        return self.__this.call(f"expire", _key, _integer)

    def pexpire(self, _key, _timestamp):
        return self.__this.call(f"pexpire", _key, _timestamp)

    def expireAt(self, _key, _timestamp):
        return self.__this.call(f"expireAt", _key, _timestamp)

    def pexpireAt(self, _key, _timestamp):
        return self.__this.call(f"pexpireAt", _key, _timestamp)

    def move(self, _key, _dbindex):
        return self.__this.call(f"move", _key, _dbindex)

    def select(self, _dbindex):
        return self.__this.call(f"select", _dbindex)

    def getRange(self, _key, _start, _end):
        return self.__this.call(f"getRange", _key, _start, _end)

    def listTrim(self, _key, _start, _stop):
        return self.__this.call(f"listTrim", _key, _start, _stop)

    def ltrim(self, _key, _start, _stop):
        return self.__this.call(f"ltrim", _key, _start, _stop)

    def lGetRange(self, _key, _start, _end):
        return self.__this.call(f"lGetRange", _key, _start, _end)

    def lRange(self, _key, _start, _end):
        return self.__this.call(f"lRange", _key, _start, _end)

    def lRem(self, _key, _value, _count):
        return self.__this.call(f"lRem", _key, _value, _count)

    def lRemove(self, _key, _value, _count):
        return self.__this.call(f"lRemove", _key, _value, _count)

    def zDeleteRangeByRank(self, _key, _start, _end):
        return self.__this.call(f"zDeleteRangeByRank", _key, _start, _end)

    def zRemRangeByRank(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByRank", _key, _min, _max)

    def incrByFloat(self, _key, _value):
        return self.__this.call(f"incrByFloat", _key, _value)

    def hIncrByFloat(self, _key, _member, _value):
        return self.__this.call(f"hIncrByFloat", _key, _member, _value)

    def bitCount(self, _key):
        return self.__this.call(f"bitCount", _key)

    def bitOp(self, _operation, _ret_key, _key, _other_keys=None):
        return self.__this.call(f"bitOp", _operation, _ret_key, _key, _other_keys)

    def sAdd(self, _key, _value):
        return self.__this.call(f"sAdd", _key, _value)

    def sMove(self, _src, _dst, _value):
        return self.__this.call(f"sMove", _src, _dst, _value)

    def sDiff(self, _key, _other_keys=None):
        return self.__this.call(f"sDiff", _key, _other_keys)

    def sDiffStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sDiffStore", _dst, _key, _other_keys)

    def sUnion(self, _key, _other_keys=None):
        return self.__this.call(f"sUnion", _key, _other_keys)

    def sUnionStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sUnionStore", _dst, _key, _other_keys)

    def sInter(self, _key, _other_keys=None):
        return self.__this.call(f"sInter", _key, _other_keys)

    def sInterStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sInterStore", _dst, _key, _other_keys)

    def sRemove(self, _key, _value):
        return self.__this.call(f"sRemove", _key, _value)

    def srem(self, _key, _value):
        return self.__this.call(f"srem", _key, _value)

    def zDelete(self, _key, _member, _other_members=None):
        return self.__this.call(f"zDelete", _key, _member, _other_members)

    def zRemove(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRemove", _key, _member, _other_members)

    def zRem(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRem", _key, _member, _other_members)

    def pSubscribe(self, _patterns):
        return self.__this.call(f"pSubscribe", _patterns)

    def subscribe(self, _channels):
        return self.__this.call(f"subscribe", _channels)

    def unsubscribe(self, _channels):
        return self.__this.call(f"unsubscribe", _channels)

    def pUnSubscribe(self, _patterns):
        return self.__this.call(f"pUnSubscribe", _patterns)

    def multi(self):
        return self.__this.call(f"multi", )

    def exec(self):
        return self.__this.call(f"exec", )

    def eval(self, _script, _args=None, _num_keys=None):
        return self.__this.call(f"eval", _script, _args, _num_keys)

    def evalSha(self, _script_sha, _args=None, _num_keys=None):
        return self.__this.call(f"evalSha", _script_sha, _args, _num_keys)

    def script(self, _cmd, _args=None):
        return self.__this.call(f"script", _cmd, _args)

    def xLen(self, _key):
        return self.__this.call(f"xLen", _key)

    def xAdd(self, _key, _id, _pairs, _options=None):
        return self.__this.call(f"xAdd", _key, _id, _pairs, _options)

    def xRead(self, _streams, _options=None):
        return self.__this.call(f"xRead", _streams, _options)

    def xDel(self, _key, _id):
        return self.__this.call(f"xDel", _key, _id)

    def xRange(self, _key, _start, _end, _count=None):
        return self.__this.call(f"xRange", _key, _start, _end, _count)

    def xRevRange(self, _key, _start, _end, _count=None):
        return self.__this.call(f"xRevRange", _key, _start, _end, _count)

    def xTrim(self, _key, _options=None):
        return self.__this.call(f"xTrim", _key, _options)

    def xGroupCreate(self, _key, _group_name, _id, _mkstream=None):
        return self.__this.call(f"xGroupCreate", _key, _group_name, _id, _mkstream)

    def xGroupSetId(self, _key, _group_name, _id):
        return self.__this.call(f"xGroupSetId", _key, _group_name, _id)

    def xGroupDestroy(self, _key, _group_name):
        return self.__this.call(f"xGroupDestroy", _key, _group_name)

    def xGroupCreateConsumer(self, _key, _group_name, _consumer_name):
        return self.__this.call(f"xGroupCreateConsumer", _key, _group_name, _consumer_name)

    def xGroupDelConsumer(self, _key, _group_name, _consumer_name):
        return self.__this.call(f"xGroupDelConsumer", _key, _group_name, _consumer_name)

    def xReadGroup(self, _group_name, _consumer_name, _streams, _options=None):
        return self.__this.call(f"xReadGroup", _group_name, _consumer_name, _streams, _options)

    def xPending(self, _key, _group_name, _options=None):
        return self.__this.call(f"xPending", _key, _group_name, _options)

    def xAck(self, _key, _group_name, _id):
        return self.__this.call(f"xAck", _key, _group_name, _id)

    def xClaim(self, _key, _group_name, _consumer_name, _min_idle_time, _id, _options=None):
        return self.__this.call(f"xClaim", _key, _group_name, _consumer_name, _min_idle_time, _id, _options)

    def xAutoClaim(self, _key, _group_name, _consumer_name, _min_idle_time, _start, _options=None):
        return self.__this.call(f"xAutoClaim", _key, _group_name, _consumer_name, _min_idle_time, _start, _options)

    def xInfoConsumers(self, _key, _group_name):
        return self.__this.call(f"xInfoConsumers", _key, _group_name)

    def xInfoGroups(self, _key):
        return self.__this.call(f"xInfoGroups", _key)

    def xInfoStream(self, _key):
        return self.__this.call(f"xInfoStream", _key)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class redis():

    def __init__(self, _config=None):
        self.__this = phpy.Object(f'co\\redis', _config)

    def connect(self, _host, _port=None, _serialize=None):
        return self.__this.call(f"connect", _host, _port, _serialize)

    def getAuth(self):
        return self.__this.call(f"getAuth", )

    def getDBNum(self):
        return self.__this.call(f"getDBNum", )

    def getOptions(self):
        return self.__this.call(f"getOptions", )

    def setOptions(self, _options):
        return self.__this.call(f"setOptions", _options)

    def getDefer(self):
        return self.__this.call(f"getDefer", )

    def setDefer(self, _defer):
        return self.__this.call(f"setDefer", _defer)

    def recv(self):
        return self.__this.call(f"recv", )

    def request(self, _params):
        return self.__this.call(f"request", _params)

    def close(self):
        return self.__this.call(f"close", )

    def set(self, _key, _value, _timeout=None, _opt=None):
        return self.__this.call(f"set", _key, _value, _timeout, _opt)

    def setBit(self, _key, _offset, _value):
        return self.__this.call(f"setBit", _key, _offset, _value)

    def setEx(self, _key, _expire, _value):
        return self.__this.call(f"setEx", _key, _expire, _value)

    def psetEx(self, _key, _expire, _value):
        return self.__this.call(f"psetEx", _key, _expire, _value)

    def lSet(self, _key, _index, _value):
        return self.__this.call(f"lSet", _key, _index, _value)

    def get(self, _key):
        return self.__this.call(f"get", _key)

    def mGet(self, _keys):
        return self.__this.call(f"mGet", _keys)

    def _del(self, _key, _other_keys=None):
        return self.__this.call(f"del", _key, _other_keys)

    def hDel(self, _key, _member, _other_members=None):
        return self.__this.call(f"hDel", _key, _member, _other_members)

    def hSet(self, _key, _member, _value):
        return self.__this.call(f"hSet", _key, _member, _value)

    def hMSet(self, _key, _pairs):
        return self.__this.call(f"hMSet", _key, _pairs)

    def hSetNx(self, _key, _member, _value):
        return self.__this.call(f"hSetNx", _key, _member, _value)

    def delete(self, _key, _other_keys=None):
        return self.__this.call(f"delete", _key, _other_keys)

    def mSet(self, _pairs):
        return self.__this.call(f"mSet", _pairs)

    def mSetNx(self, _pairs):
        return self.__this.call(f"mSetNx", _pairs)

    def getKeys(self, _pattern):
        return self.__this.call(f"getKeys", _pattern)

    def keys(self, _pattern):
        return self.__this.call(f"keys", _pattern)

    def exists(self, _key, _other_keys=None):
        return self.__this.call(f"exists", _key, _other_keys)

    def type(self, _key):
        return self.__this.call(f"type", _key)

    def strLen(self, _key):
        return self.__this.call(f"strLen", _key)

    def lPop(self, _key):
        return self.__this.call(f"lPop", _key)

    def blPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"blPop", _key, _timeout_or_key, _extra_args)

    def rPop(self, _key):
        return self.__this.call(f"rPop", _key)

    def brPop(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"brPop", _key, _timeout_or_key, _extra_args)

    def bRPopLPush(self, _src, _dst, _timeout):
        return self.__this.call(f"bRPopLPush", _src, _dst, _timeout)

    def lSize(self, _key):
        return self.__this.call(f"lSize", _key)

    def lLen(self, _key):
        return self.__this.call(f"lLen", _key)

    def sSize(self, _key):
        return self.__this.call(f"sSize", _key)

    def scard(self, _key):
        return self.__this.call(f"scard", _key)

    def sPop(self, _key):
        return self.__this.call(f"sPop", _key)

    def sMembers(self, _key):
        return self.__this.call(f"sMembers", _key)

    def sGetMembers(self, _key):
        return self.__this.call(f"sGetMembers", _key)

    def sRandMember(self, _key, _count=None):
        return self.__this.call(f"sRandMember", _key, _count)

    def persist(self, _key):
        return self.__this.call(f"persist", _key)

    def ttl(self, _key):
        return self.__this.call(f"ttl", _key)

    def pttl(self, _key):
        return self.__this.call(f"pttl", _key)

    def zCard(self, _key):
        return self.__this.call(f"zCard", _key)

    def zSize(self, _key):
        return self.__this.call(f"zSize", _key)

    def hLen(self, _key):
        return self.__this.call(f"hLen", _key)

    def hKeys(self, _key):
        return self.__this.call(f"hKeys", _key)

    def hVals(self, _key):
        return self.__this.call(f"hVals", _key)

    def hGetAll(self, _key):
        return self.__this.call(f"hGetAll", _key)

    def debug(self, _key):
        return self.__this.call(f"debug", _key)

    def restore(self, _ttl, _key, _value):
        return self.__this.call(f"restore", _ttl, _key, _value)

    def dump(self, _key):
        return self.__this.call(f"dump", _key)

    def renameKey(self, _key, _newkey):
        return self.__this.call(f"renameKey", _key, _newkey)

    def rename(self, _key, _newkey):
        return self.__this.call(f"rename", _key, _newkey)

    def renameNx(self, _key, _newkey):
        return self.__this.call(f"renameNx", _key, _newkey)

    def rpoplpush(self, _src, _dst):
        return self.__this.call(f"rpoplpush", _src, _dst)

    def randomKey(self):
        return self.__this.call(f"randomKey", )

    def pfadd(self, _key, _elements):
        return self.__this.call(f"pfadd", _key, _elements)

    def pfcount(self, _key):
        return self.__this.call(f"pfcount", _key)

    def pfmerge(self, _dstkey, _keys):
        return self.__this.call(f"pfmerge", _dstkey, _keys)

    def ping(self):
        return self.__this.call(f"ping", )

    def auth(self, _password):
        return self.__this.call(f"auth", _password)

    def unwatch(self):
        return self.__this.call(f"unwatch", )

    def watch(self, _key, _other_keys=None):
        return self.__this.call(f"watch", _key, _other_keys)

    def save(self):
        return self.__this.call(f"save", )

    def bgSave(self):
        return self.__this.call(f"bgSave", )

    def lastSave(self):
        return self.__this.call(f"lastSave", )

    def flushDB(self):
        return self.__this.call(f"flushDB", )

    def flushAll(self):
        return self.__this.call(f"flushAll", )

    def dbSize(self):
        return self.__this.call(f"dbSize", )

    def bgrewriteaof(self):
        return self.__this.call(f"bgrewriteaof", )

    def time(self):
        return self.__this.call(f"time", )

    def role(self):
        return self.__this.call(f"role", )

    def setRange(self, _key, _offset, _value):
        return self.__this.call(f"setRange", _key, _offset, _value)

    def setNx(self, _key, _value):
        return self.__this.call(f"setNx", _key, _value)

    def getSet(self, _key, _value):
        return self.__this.call(f"getSet", _key, _value)

    def append(self, _key, _value):
        return self.__this.call(f"append", _key, _value)

    def lPushx(self, _key, _value):
        return self.__this.call(f"lPushx", _key, _value)

    def lPush(self, _key, _value):
        return self.__this.call(f"lPush", _key, _value)

    def rPush(self, _key, _value):
        return self.__this.call(f"rPush", _key, _value)

    def rPushx(self, _key, _value):
        return self.__this.call(f"rPushx", _key, _value)

    def sContains(self, _key, _value):
        return self.__this.call(f"sContains", _key, _value)

    def sismember(self, _key, _value):
        return self.__this.call(f"sismember", _key, _value)

    def zScore(self, _key, _member):
        return self.__this.call(f"zScore", _key, _member)

    def zRank(self, _key, _member):
        return self.__this.call(f"zRank", _key, _member)

    def zRevRank(self, _key, _member):
        return self.__this.call(f"zRevRank", _key, _member)

    def hGet(self, _key, _member):
        return self.__this.call(f"hGet", _key, _member)

    def hMGet(self, _key, _keys):
        return self.__this.call(f"hMGet", _key, _keys)

    def hExists(self, _key, _member):
        return self.__this.call(f"hExists", _key, _member)

    def publish(self, _channel, _message):
        return self.__this.call(f"publish", _channel, _message)

    def zIncrBy(self, _key, _value, _member):
        return self.__this.call(f"zIncrBy", _key, _value, _member)

    def zAdd(self, _key, _score, _value):
        return self.__this.call(f"zAdd", _key, _score, _value)

    def zPopMin(self, _key, _count):
        return self.__this.call(f"zPopMin", _key, _count)

    def zPopMax(self, _key, _count):
        return self.__this.call(f"zPopMax", _key, _count)

    def bzPopMin(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMin", _key, _timeout_or_key, _extra_args)

    def bzPopMax(self, _key, _timeout_or_key, _extra_args=None):
        return self.__this.call(f"bzPopMax", _key, _timeout_or_key, _extra_args)

    def zDeleteRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zDeleteRangeByScore", _key, _min, _max)

    def zRemRangeByScore(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByScore", _key, _min, _max)

    def zCount(self, _key, _min, _max):
        return self.__this.call(f"zCount", _key, _min, _max)

    def zRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRange", _key, _start, _end, _scores)

    def zRevRange(self, _key, _start, _end, _scores=None):
        return self.__this.call(f"zRevRange", _key, _start, _end, _scores)

    def zRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRangeByScore", _key, _start, _end, _options)

    def zRevRangeByScore(self, _key, _start, _end, _options=None):
        return self.__this.call(f"zRevRangeByScore", _key, _start, _end, _options)

    def zRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRangeByLex", _key, _min, _max, _offset, _limit)

    def zRevRangeByLex(self, _key, _min, _max, _offset=None, _limit=None):
        return self.__this.call(f"zRevRangeByLex", _key, _min, _max, _offset, _limit)

    def zInter(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zInter", _key, _keys, _weights, _aggregate)

    def zinterstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zinterstore", _key, _keys, _weights, _aggregate)

    def zUnion(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zUnion", _key, _keys, _weights, _aggregate)

    def zunionstore(self, _key, _keys, _weights=None, _aggregate=None):
        return self.__this.call(f"zunionstore", _key, _keys, _weights, _aggregate)

    def incrBy(self, _key, _value):
        return self.__this.call(f"incrBy", _key, _value)

    def hIncrBy(self, _key, _member, _value):
        return self.__this.call(f"hIncrBy", _key, _member, _value)

    def incr(self, _key):
        return self.__this.call(f"incr", _key)

    def decrBy(self, _key, _value):
        return self.__this.call(f"decrBy", _key, _value)

    def decr(self, _key):
        return self.__this.call(f"decr", _key)

    def getBit(self, _key, _offset):
        return self.__this.call(f"getBit", _key, _offset)

    def lInsert(self, _key, _position, _pivot, _value):
        return self.__this.call(f"lInsert", _key, _position, _pivot, _value)

    def lGet(self, _key, _index):
        return self.__this.call(f"lGet", _key, _index)

    def lIndex(self, _key, _integer):
        return self.__this.call(f"lIndex", _key, _integer)

    def setTimeout(self, _key, _timeout):
        return self.__this.call(f"setTimeout", _key, _timeout)

    def expire(self, _key, _integer):
        return self.__this.call(f"expire", _key, _integer)

    def pexpire(self, _key, _timestamp):
        return self.__this.call(f"pexpire", _key, _timestamp)

    def expireAt(self, _key, _timestamp):
        return self.__this.call(f"expireAt", _key, _timestamp)

    def pexpireAt(self, _key, _timestamp):
        return self.__this.call(f"pexpireAt", _key, _timestamp)

    def move(self, _key, _dbindex):
        return self.__this.call(f"move", _key, _dbindex)

    def select(self, _dbindex):
        return self.__this.call(f"select", _dbindex)

    def getRange(self, _key, _start, _end):
        return self.__this.call(f"getRange", _key, _start, _end)

    def listTrim(self, _key, _start, _stop):
        return self.__this.call(f"listTrim", _key, _start, _stop)

    def ltrim(self, _key, _start, _stop):
        return self.__this.call(f"ltrim", _key, _start, _stop)

    def lGetRange(self, _key, _start, _end):
        return self.__this.call(f"lGetRange", _key, _start, _end)

    def lRange(self, _key, _start, _end):
        return self.__this.call(f"lRange", _key, _start, _end)

    def lRem(self, _key, _value, _count):
        return self.__this.call(f"lRem", _key, _value, _count)

    def lRemove(self, _key, _value, _count):
        return self.__this.call(f"lRemove", _key, _value, _count)

    def zDeleteRangeByRank(self, _key, _start, _end):
        return self.__this.call(f"zDeleteRangeByRank", _key, _start, _end)

    def zRemRangeByRank(self, _key, _min, _max):
        return self.__this.call(f"zRemRangeByRank", _key, _min, _max)

    def incrByFloat(self, _key, _value):
        return self.__this.call(f"incrByFloat", _key, _value)

    def hIncrByFloat(self, _key, _member, _value):
        return self.__this.call(f"hIncrByFloat", _key, _member, _value)

    def bitCount(self, _key):
        return self.__this.call(f"bitCount", _key)

    def bitOp(self, _operation, _ret_key, _key, _other_keys=None):
        return self.__this.call(f"bitOp", _operation, _ret_key, _key, _other_keys)

    def sAdd(self, _key, _value):
        return self.__this.call(f"sAdd", _key, _value)

    def sMove(self, _src, _dst, _value):
        return self.__this.call(f"sMove", _src, _dst, _value)

    def sDiff(self, _key, _other_keys=None):
        return self.__this.call(f"sDiff", _key, _other_keys)

    def sDiffStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sDiffStore", _dst, _key, _other_keys)

    def sUnion(self, _key, _other_keys=None):
        return self.__this.call(f"sUnion", _key, _other_keys)

    def sUnionStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sUnionStore", _dst, _key, _other_keys)

    def sInter(self, _key, _other_keys=None):
        return self.__this.call(f"sInter", _key, _other_keys)

    def sInterStore(self, _dst, _key, _other_keys=None):
        return self.__this.call(f"sInterStore", _dst, _key, _other_keys)

    def sRemove(self, _key, _value):
        return self.__this.call(f"sRemove", _key, _value)

    def srem(self, _key, _value):
        return self.__this.call(f"srem", _key, _value)

    def zDelete(self, _key, _member, _other_members=None):
        return self.__this.call(f"zDelete", _key, _member, _other_members)

    def zRemove(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRemove", _key, _member, _other_members)

    def zRem(self, _key, _member, _other_members=None):
        return self.__this.call(f"zRem", _key, _member, _other_members)

    def pSubscribe(self, _patterns):
        return self.__this.call(f"pSubscribe", _patterns)

    def subscribe(self, _channels):
        return self.__this.call(f"subscribe", _channels)

    def unsubscribe(self, _channels):
        return self.__this.call(f"unsubscribe", _channels)

    def pUnSubscribe(self, _patterns):
        return self.__this.call(f"pUnSubscribe", _patterns)

    def multi(self):
        return self.__this.call(f"multi", )

    def exec(self):
        return self.__this.call(f"exec", )

    def eval(self, _script, _args=None, _num_keys=None):
        return self.__this.call(f"eval", _script, _args, _num_keys)

    def evalSha(self, _script_sha, _args=None, _num_keys=None):
        return self.__this.call(f"evalSha", _script_sha, _args, _num_keys)

    def script(self, _cmd, _args=None):
        return self.__this.call(f"script", _cmd, _args)

    def xLen(self, _key):
        return self.__this.call(f"xLen", _key)

    def xAdd(self, _key, _id, _pairs, _options=None):
        return self.__this.call(f"xAdd", _key, _id, _pairs, _options)

    def xRead(self, _streams, _options=None):
        return self.__this.call(f"xRead", _streams, _options)

    def xDel(self, _key, _id):
        return self.__this.call(f"xDel", _key, _id)

    def xRange(self, _key, _start, _end, _count=None):
        return self.__this.call(f"xRange", _key, _start, _end, _count)

    def xRevRange(self, _key, _start, _end, _count=None):
        return self.__this.call(f"xRevRange", _key, _start, _end, _count)

    def xTrim(self, _key, _options=None):
        return self.__this.call(f"xTrim", _key, _options)

    def xGroupCreate(self, _key, _group_name, _id, _mkstream=None):
        return self.__this.call(f"xGroupCreate", _key, _group_name, _id, _mkstream)

    def xGroupSetId(self, _key, _group_name, _id):
        return self.__this.call(f"xGroupSetId", _key, _group_name, _id)

    def xGroupDestroy(self, _key, _group_name):
        return self.__this.call(f"xGroupDestroy", _key, _group_name)

    def xGroupCreateConsumer(self, _key, _group_name, _consumer_name):
        return self.__this.call(f"xGroupCreateConsumer", _key, _group_name, _consumer_name)

    def xGroupDelConsumer(self, _key, _group_name, _consumer_name):
        return self.__this.call(f"xGroupDelConsumer", _key, _group_name, _consumer_name)

    def xReadGroup(self, _group_name, _consumer_name, _streams, _options=None):
        return self.__this.call(f"xReadGroup", _group_name, _consumer_name, _streams, _options)

    def xPending(self, _key, _group_name, _options=None):
        return self.__this.call(f"xPending", _key, _group_name, _options)

    def xAck(self, _key, _group_name, _id):
        return self.__this.call(f"xAck", _key, _group_name, _id)

    def xClaim(self, _key, _group_name, _consumer_name, _min_idle_time, _id, _options=None):
        return self.__this.call(f"xClaim", _key, _group_name, _consumer_name, _min_idle_time, _id, _options)

    def xAutoClaim(self, _key, _group_name, _consumer_name, _min_idle_time, _start, _options=None):
        return self.__this.call(f"xAutoClaim", _key, _group_name, _consumer_name, _min_idle_time, _start, _options)

    def xInfoConsumers(self, _key, _group_name):
        return self.__this.call(f"xInfoConsumers", _key, _group_name)

    def xInfoGroups(self, _key):
        return self.__this.call(f"xInfoGroups", _key)

    def xInfoStream(self, _key):
        return self.__this.call(f"xInfoStream", _key)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Server():

    def __init__(self, _host="0.0.0.0", _port=0, _mode=1, _sock_type=1):
        self.__this = phpy.Object(f'Swoole\\Server', _host, _port, _mode, _sock_type)

    def listen(self, _host, _port, _sock_type):
        return self.__this.call(f"listen", _host, _port, _sock_type)

    def addlistener(self, _host, _port, _sock_type):
        return self.__this.call(f"addlistener", _host, _port, _sock_type)

    def on(self, _event_name, _callback):
        return self.__this.call(f"on", _event_name, _callback)

    def getCallback(self, _event_name):
        return self.__this.call(f"getCallback", _event_name)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def start(self):
        return self.__this.call(f"start", )

    def send(self, _fd, _send_data, _server_socket=-1):
        return self.__this.call(f"send", _fd, _send_data, _server_socket)

    def sendto(self, _ip, _port, _send_data, _server_socket=-1):
        return self.__this.call(f"sendto", _ip, _port, _send_data, _server_socket)

    def sendwait(self, _conn_fd, _send_data):
        return self.__this.call(f"sendwait", _conn_fd, _send_data)

    def exists(self, _fd):
        return self.__this.call(f"exists", _fd)

    def exist(self, _fd):
        return self.__this.call(f"exist", _fd)

    def protect(self, _fd, _is_protected=True):
        return self.__this.call(f"protect", _fd, _is_protected)

    def sendfile(self, _conn_fd, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _conn_fd, _filename, _offset, _length)

    def close(self, _fd, _reset=False):
        return self.__this.call(f"close", _fd, _reset)

    def confirm(self, _fd):
        return self.__this.call(f"confirm", _fd)

    def pause(self, _fd):
        return self.__this.call(f"pause", _fd)

    def resume(self, _fd):
        return self.__this.call(f"resume", _fd)

    def task(self, _data, _task_worker_index=-1, _finish_callback=None):
        return self.__this.call(f"task", _data, _task_worker_index, _finish_callback)

    def taskwait(self, _data, _timeout=0.5, _task_worker_index=-1):
        return self.__this.call(f"taskwait", _data, _timeout, _task_worker_index)

    def taskWaitMulti(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskWaitMulti", _tasks, _timeout)

    def taskCo(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskCo", _tasks, _timeout)

    def finish(self, _data):
        return self.__this.call(f"finish", _data)

    def reload(self, _only_reload_taskworker=False):
        return self.__this.call(f"reload", _only_reload_taskworker)

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def stop(self, _worker_id=-1, _wait_event=False):
        return self.__this.call(f"stop", _worker_id, _wait_event)

    def getLastError(self):
        return self.__this.call(f"getLastError", )

    def heartbeat(self, _if_close_connection=True):
        return self.__this.call(f"heartbeat", _if_close_connection)

    def getClientInfo(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"getClientInfo", _fd, _reactor_id, _ignore_error)

    def getClientList(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"getClientList", _start_fd, _find_count)

    def getWorkerId(self):
        return self.__this.call(f"getWorkerId", )

    def getWorkerPid(self, _worker_id=-1):
        return self.__this.call(f"getWorkerPid", _worker_id)

    def getWorkerStatus(self, _worker_id=-1):
        return self.__this.call(f"getWorkerStatus", _worker_id)

    def getManagerPid(self):
        return self.__this.call(f"getManagerPid", )

    def getMasterPid(self):
        return self.__this.call(f"getMasterPid", )

    def connection_info(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"connection_info", _fd, _reactor_id, _ignore_error)

    def connection_list(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"connection_list", _start_fd, _find_count)

    def sendMessage(self, _message, _dst_worker_id):
        return self.__this.call(f"sendMessage", _message, _dst_worker_id)

    def command(self, _name, _process_id, _process_type, _data, _json_decode=True):
        return self.__this.call(f"command", _name, _process_id, _process_type, _data, _json_decode)

    def addCommand(self, _name, _accepted_process_types, _callback):
        return self.__this.call(f"addCommand", _name, _accepted_process_types, _callback)

    def addProcess(self, _process):
        return self.__this.call(f"addProcess", _process)

    def stats(self):
        return self.__this.call(f"stats", )

    def getSocket(self, _port=0):
        return self.__this.call(f"getSocket", _port)

    def bind(self, _fd, _uid):
        return self.__this.call(f"bind", _fd, _uid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerTask():

    def finish(self, _data):
        return self.__this.call(f"finish", _data)

    def pack(_data):
        return phpy.call(f"Swoole\\Server\\Task::pack", _data)

    def unpack(_data):
        return phpy.call(f"Swoole\\Server\\Task::unpack", _data)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\Task')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerEvent():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\Event')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerPacket():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\Packet')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerPipeMessage():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\PipeMessage')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerStatusInfo():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\StatusInfo')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerTaskResult():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\TaskResult')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ConnectionIterator():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Connection\\Iterator', )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def valid(self):
        return self.__this.call(f"valid", )

    def count(self):
        return self.__this.call(f"count", )

    def offsetExists(self, _fd):
        return self.__this.call(f"offsetExists", _fd)

    def offsetGet(self, _fd):
        return self.__this.call(f"offsetGet", _fd)

    def offsetSet(self, _fd, _value):
        return self.__this.call(f"offsetSet", _fd, _value)

    def offsetUnset(self, _fd):
        return self.__this.call(f"offsetUnset", _fd)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ServerPort():

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def on(self, _event_name, _callback):
        return self.__this.call(f"on", _event_name, _callback)

    def getCallback(self, _event_name):
        return self.__this.call(f"getCallback", _event_name)

    def getSocket(self):
        return self.__this.call(f"getSocket", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Server\\Port')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class HttpRequest():

    def getContent(self):
        return self.__this.call(f"getContent", )

    def rawContent(self):
        return self.__this.call(f"rawContent", )

    def getData(self):
        return self.__this.call(f"getData", )

    def create(_options=[]):
        return phpy.call(f"Swoole\\Http\\Request::create", _options)

    def parse(self, _data):
        return self.__this.call(f"parse", _data)

    def isCompleted(self):
        return self.__this.call(f"isCompleted", )

    def getMethod(self):
        return self.__this.call(f"getMethod", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Http\\Request')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class HttpResponse():

    def initHeader(self):
        return self.__this.call(f"initHeader", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def cookie(self, _name, _value="", _expires=0, _path="/", _domain="", _secure=False, _httponly=False, _samesite="", _priority=""):
        return self.__this.call(f"cookie", _name, _value, _expires, _path, _domain, _secure, _httponly, _samesite, _priority)

    def setCookie(self, _name, _value="", _expires=0, _path="/", _domain="", _secure=False, _httponly=False, _samesite="", _priority=""):
        return self.__this.call(f"setCookie", _name, _value, _expires, _path, _domain, _secure, _httponly, _samesite, _priority)

    def rawcookie(self, _name, _value="", _expires=0, _path="/", _domain="", _secure=False, _httponly=False, _samesite="", _priority=""):
        return self.__this.call(f"rawcookie", _name, _value, _expires, _path, _domain, _secure, _httponly, _samesite, _priority)

    def status(self, _http_code, _reason=""):
        return self.__this.call(f"status", _http_code, _reason)

    def setStatusCode(self, _http_code, _reason=""):
        return self.__this.call(f"setStatusCode", _http_code, _reason)

    def header(self, _key, _value, _format=True):
        return self.__this.call(f"header", _key, _value, _format)

    def setHeader(self, _key, _value, _format=True):
        return self.__this.call(f"setHeader", _key, _value, _format)

    def trailer(self, _key, _value):
        return self.__this.call(f"trailer", _key, _value)

    def ping(self):
        return self.__this.call(f"ping", )

    def goaway(self, _error_code=0, _debug_data=""):
        return self.__this.call(f"goaway", _error_code, _debug_data)

    def write(self, _content):
        return self.__this.call(f"write", _content)

    def end(self, _content=None):
        return self.__this.call(f"end", _content)

    def sendfile(self, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _filename, _offset, _length)

    def redirect(self, _location, _http_code=302):
        return self.__this.call(f"redirect", _location, _http_code)

    def detach(self):
        return self.__this.call(f"detach", )

    def create(_server=-1, _fd=-1):
        return phpy.call(f"Swoole\\Http\\Response::create", _server, _fd)

    def upgrade(self):
        return self.__this.call(f"upgrade", )

    def push(self, _data, _opcode=1, _flags=1):
        return self.__this.call(f"push", _data, _opcode, _flags)

    def recv(self, _timeout=0):
        return self.__this.call(f"recv", _timeout)

    def close(self):
        return self.__this.call(f"close", )

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Http\\Response')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class HttpServer():

    def __init__(self, _host="0.0.0.0", _port=0, _mode=1, _sock_type=1):
        self.__this = phpy.Object(f'Swoole\\Http\\Server', _host, _port, _mode, _sock_type)

    def listen(self, _host, _port, _sock_type):
        return self.__this.call(f"listen", _host, _port, _sock_type)

    def addlistener(self, _host, _port, _sock_type):
        return self.__this.call(f"addlistener", _host, _port, _sock_type)

    def on(self, _event_name, _callback):
        return self.__this.call(f"on", _event_name, _callback)

    def getCallback(self, _event_name):
        return self.__this.call(f"getCallback", _event_name)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def start(self):
        return self.__this.call(f"start", )

    def send(self, _fd, _send_data, _server_socket=-1):
        return self.__this.call(f"send", _fd, _send_data, _server_socket)

    def sendto(self, _ip, _port, _send_data, _server_socket=-1):
        return self.__this.call(f"sendto", _ip, _port, _send_data, _server_socket)

    def sendwait(self, _conn_fd, _send_data):
        return self.__this.call(f"sendwait", _conn_fd, _send_data)

    def exists(self, _fd):
        return self.__this.call(f"exists", _fd)

    def exist(self, _fd):
        return self.__this.call(f"exist", _fd)

    def protect(self, _fd, _is_protected=True):
        return self.__this.call(f"protect", _fd, _is_protected)

    def sendfile(self, _conn_fd, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _conn_fd, _filename, _offset, _length)

    def close(self, _fd, _reset=False):
        return self.__this.call(f"close", _fd, _reset)

    def confirm(self, _fd):
        return self.__this.call(f"confirm", _fd)

    def pause(self, _fd):
        return self.__this.call(f"pause", _fd)

    def resume(self, _fd):
        return self.__this.call(f"resume", _fd)

    def task(self, _data, _task_worker_index=-1, _finish_callback=None):
        return self.__this.call(f"task", _data, _task_worker_index, _finish_callback)

    def taskwait(self, _data, _timeout=0.5, _task_worker_index=-1):
        return self.__this.call(f"taskwait", _data, _timeout, _task_worker_index)

    def taskWaitMulti(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskWaitMulti", _tasks, _timeout)

    def taskCo(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskCo", _tasks, _timeout)

    def finish(self, _data):
        return self.__this.call(f"finish", _data)

    def reload(self, _only_reload_taskworker=False):
        return self.__this.call(f"reload", _only_reload_taskworker)

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def stop(self, _worker_id=-1, _wait_event=False):
        return self.__this.call(f"stop", _worker_id, _wait_event)

    def getLastError(self):
        return self.__this.call(f"getLastError", )

    def heartbeat(self, _if_close_connection=True):
        return self.__this.call(f"heartbeat", _if_close_connection)

    def getClientInfo(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"getClientInfo", _fd, _reactor_id, _ignore_error)

    def getClientList(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"getClientList", _start_fd, _find_count)

    def getWorkerId(self):
        return self.__this.call(f"getWorkerId", )

    def getWorkerPid(self, _worker_id=-1):
        return self.__this.call(f"getWorkerPid", _worker_id)

    def getWorkerStatus(self, _worker_id=-1):
        return self.__this.call(f"getWorkerStatus", _worker_id)

    def getManagerPid(self):
        return self.__this.call(f"getManagerPid", )

    def getMasterPid(self):
        return self.__this.call(f"getMasterPid", )

    def connection_info(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"connection_info", _fd, _reactor_id, _ignore_error)

    def connection_list(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"connection_list", _start_fd, _find_count)

    def sendMessage(self, _message, _dst_worker_id):
        return self.__this.call(f"sendMessage", _message, _dst_worker_id)

    def command(self, _name, _process_id, _process_type, _data, _json_decode=True):
        return self.__this.call(f"command", _name, _process_id, _process_type, _data, _json_decode)

    def addCommand(self, _name, _accepted_process_types, _callback):
        return self.__this.call(f"addCommand", _name, _accepted_process_types, _callback)

    def addProcess(self, _process):
        return self.__this.call(f"addProcess", _process)

    def stats(self):
        return self.__this.call(f"stats", )

    def getSocket(self, _port=0):
        return self.__this.call(f"getSocket", _port)

    def bind(self, _fd, _uid):
        return self.__this.call(f"bind", _fd, _uid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutineHttpServer():

    def __init__(self, _host, _port=0, _ssl=False, _reuse_port=False):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\Http\\Server', _host, _port, _ssl, _reuse_port)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def handle(self, _pattern, _callback):
        return self.__this.call(f"handle", _pattern, _callback)

    def start(self):
        return self.__this.call(f"start", )

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class httpserver():

    def __init__(self, _host, _port=0, _ssl=False, _reuse_port=False):
        self.__this = phpy.Object(f'co\\http\\server', _host, _port, _ssl, _reuse_port)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def handle(self, _pattern, _callback):
        return self.__this.call(f"handle", _pattern, _callback)

    def start(self):
        return self.__this.call(f"start", )

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class WebSocketServer():

    def push(self, _fd, _data, _opcode=1, _flags=1):
        return self.__this.call(f"push", _fd, _data, _opcode, _flags)

    def disconnect(self, _fd, _code=1000, _reason=""):
        return self.__this.call(f"disconnect", _fd, _code, _reason)

    def isEstablished(self, _fd):
        return self.__this.call(f"isEstablished", _fd)

    def pack(_data, _opcode=1, _flags=1):
        return phpy.call(f"Swoole\\WebSocket\\Server::pack", _data, _opcode, _flags)

    def unpack(_data):
        return phpy.call(f"Swoole\\WebSocket\\Server::unpack", _data)

    def __init__(self, _host="0.0.0.0", _port=0, _mode=1, _sock_type=1):
        self.__this = phpy.Object(f'Swoole\\WebSocket\\Server', _host, _port, _mode, _sock_type)

    def listen(self, _host, _port, _sock_type):
        return self.__this.call(f"listen", _host, _port, _sock_type)

    def addlistener(self, _host, _port, _sock_type):
        return self.__this.call(f"addlistener", _host, _port, _sock_type)

    def on(self, _event_name, _callback):
        return self.__this.call(f"on", _event_name, _callback)

    def getCallback(self, _event_name):
        return self.__this.call(f"getCallback", _event_name)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def start(self):
        return self.__this.call(f"start", )

    def send(self, _fd, _send_data, _server_socket=-1):
        return self.__this.call(f"send", _fd, _send_data, _server_socket)

    def sendto(self, _ip, _port, _send_data, _server_socket=-1):
        return self.__this.call(f"sendto", _ip, _port, _send_data, _server_socket)

    def sendwait(self, _conn_fd, _send_data):
        return self.__this.call(f"sendwait", _conn_fd, _send_data)

    def exists(self, _fd):
        return self.__this.call(f"exists", _fd)

    def exist(self, _fd):
        return self.__this.call(f"exist", _fd)

    def protect(self, _fd, _is_protected=True):
        return self.__this.call(f"protect", _fd, _is_protected)

    def sendfile(self, _conn_fd, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _conn_fd, _filename, _offset, _length)

    def close(self, _fd, _reset=False):
        return self.__this.call(f"close", _fd, _reset)

    def confirm(self, _fd):
        return self.__this.call(f"confirm", _fd)

    def pause(self, _fd):
        return self.__this.call(f"pause", _fd)

    def resume(self, _fd):
        return self.__this.call(f"resume", _fd)

    def task(self, _data, _task_worker_index=-1, _finish_callback=None):
        return self.__this.call(f"task", _data, _task_worker_index, _finish_callback)

    def taskwait(self, _data, _timeout=0.5, _task_worker_index=-1):
        return self.__this.call(f"taskwait", _data, _timeout, _task_worker_index)

    def taskWaitMulti(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskWaitMulti", _tasks, _timeout)

    def taskCo(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskCo", _tasks, _timeout)

    def finish(self, _data):
        return self.__this.call(f"finish", _data)

    def reload(self, _only_reload_taskworker=False):
        return self.__this.call(f"reload", _only_reload_taskworker)

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def stop(self, _worker_id=-1, _wait_event=False):
        return self.__this.call(f"stop", _worker_id, _wait_event)

    def getLastError(self):
        return self.__this.call(f"getLastError", )

    def heartbeat(self, _if_close_connection=True):
        return self.__this.call(f"heartbeat", _if_close_connection)

    def getClientInfo(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"getClientInfo", _fd, _reactor_id, _ignore_error)

    def getClientList(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"getClientList", _start_fd, _find_count)

    def getWorkerId(self):
        return self.__this.call(f"getWorkerId", )

    def getWorkerPid(self, _worker_id=-1):
        return self.__this.call(f"getWorkerPid", _worker_id)

    def getWorkerStatus(self, _worker_id=-1):
        return self.__this.call(f"getWorkerStatus", _worker_id)

    def getManagerPid(self):
        return self.__this.call(f"getManagerPid", )

    def getMasterPid(self):
        return self.__this.call(f"getMasterPid", )

    def connection_info(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"connection_info", _fd, _reactor_id, _ignore_error)

    def connection_list(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"connection_list", _start_fd, _find_count)

    def sendMessage(self, _message, _dst_worker_id):
        return self.__this.call(f"sendMessage", _message, _dst_worker_id)

    def command(self, _name, _process_id, _process_type, _data, _json_decode=True):
        return self.__this.call(f"command", _name, _process_id, _process_type, _data, _json_decode)

    def addCommand(self, _name, _accepted_process_types, _callback):
        return self.__this.call(f"addCommand", _name, _accepted_process_types, _callback)

    def addProcess(self, _process):
        return self.__this.call(f"addProcess", _process)

    def stats(self):
        return self.__this.call(f"stats", )

    def getSocket(self, _port=0):
        return self.__this.call(f"getSocket", _port)

    def bind(self, _fd, _uid):
        return self.__this.call(f"bind", _fd, _uid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class WebSocketFrame():

    def __str__(self):
        return self.__this.call(f"__toString", )

    def pack(_data, _opcode=1, _flags=1):
        return phpy.call(f"Swoole\\WebSocket\\Frame::pack", _data, _opcode, _flags)

    def unpack(_data):
        return phpy.call(f"Swoole\\WebSocket\\Frame::unpack", _data)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\WebSocket\\Frame')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class WebSocketCloseFrame():

    def __str__(self):
        return self.__this.call(f"__toString", )

    def pack(_data, _opcode=1, _flags=1):
        return phpy.call(f"Swoole\\WebSocket\\CloseFrame::pack", _data, _opcode, _flags)

    def unpack(_data):
        return phpy.call(f"Swoole\\WebSocket\\CloseFrame::unpack", _data)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\WebSocket\\CloseFrame')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RedisServer():
    NIL = 1
    ERROR = 0
    STATUS = 2
    INT = 3
    STRING = 4
    SET = 5
    MAP = 6

    def setHandler(self, _command, _callback):
        return self.__this.call(f"setHandler", _command, _callback)

    def getHandler(self, _command):
        return self.__this.call(f"getHandler", _command)

    def format(_type, _value=None):
        return phpy.call(f"Swoole\\Redis\\Server::format", _type, _value)

    def __init__(self, _host="0.0.0.0", _port=0, _mode=1, _sock_type=1):
        self.__this = phpy.Object(f'Swoole\\Redis\\Server', _host, _port, _mode, _sock_type)

    def listen(self, _host, _port, _sock_type):
        return self.__this.call(f"listen", _host, _port, _sock_type)

    def addlistener(self, _host, _port, _sock_type):
        return self.__this.call(f"addlistener", _host, _port, _sock_type)

    def on(self, _event_name, _callback):
        return self.__this.call(f"on", _event_name, _callback)

    def getCallback(self, _event_name):
        return self.__this.call(f"getCallback", _event_name)

    def set(self, _settings):
        return self.__this.call(f"set", _settings)

    def start(self):
        return self.__this.call(f"start", )

    def send(self, _fd, _send_data, _server_socket=-1):
        return self.__this.call(f"send", _fd, _send_data, _server_socket)

    def sendto(self, _ip, _port, _send_data, _server_socket=-1):
        return self.__this.call(f"sendto", _ip, _port, _send_data, _server_socket)

    def sendwait(self, _conn_fd, _send_data):
        return self.__this.call(f"sendwait", _conn_fd, _send_data)

    def exists(self, _fd):
        return self.__this.call(f"exists", _fd)

    def exist(self, _fd):
        return self.__this.call(f"exist", _fd)

    def protect(self, _fd, _is_protected=True):
        return self.__this.call(f"protect", _fd, _is_protected)

    def sendfile(self, _conn_fd, _filename, _offset=0, _length=0):
        return self.__this.call(f"sendfile", _conn_fd, _filename, _offset, _length)

    def close(self, _fd, _reset=False):
        return self.__this.call(f"close", _fd, _reset)

    def confirm(self, _fd):
        return self.__this.call(f"confirm", _fd)

    def pause(self, _fd):
        return self.__this.call(f"pause", _fd)

    def resume(self, _fd):
        return self.__this.call(f"resume", _fd)

    def task(self, _data, _task_worker_index=-1, _finish_callback=None):
        return self.__this.call(f"task", _data, _task_worker_index, _finish_callback)

    def taskwait(self, _data, _timeout=0.5, _task_worker_index=-1):
        return self.__this.call(f"taskwait", _data, _timeout, _task_worker_index)

    def taskWaitMulti(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskWaitMulti", _tasks, _timeout)

    def taskCo(self, _tasks, _timeout=0.5):
        return self.__this.call(f"taskCo", _tasks, _timeout)

    def finish(self, _data):
        return self.__this.call(f"finish", _data)

    def reload(self, _only_reload_taskworker=False):
        return self.__this.call(f"reload", _only_reload_taskworker)

    def shutdown(self):
        return self.__this.call(f"shutdown", )

    def stop(self, _worker_id=-1, _wait_event=False):
        return self.__this.call(f"stop", _worker_id, _wait_event)

    def getLastError(self):
        return self.__this.call(f"getLastError", )

    def heartbeat(self, _if_close_connection=True):
        return self.__this.call(f"heartbeat", _if_close_connection)

    def getClientInfo(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"getClientInfo", _fd, _reactor_id, _ignore_error)

    def getClientList(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"getClientList", _start_fd, _find_count)

    def getWorkerId(self):
        return self.__this.call(f"getWorkerId", )

    def getWorkerPid(self, _worker_id=-1):
        return self.__this.call(f"getWorkerPid", _worker_id)

    def getWorkerStatus(self, _worker_id=-1):
        return self.__this.call(f"getWorkerStatus", _worker_id)

    def getManagerPid(self):
        return self.__this.call(f"getManagerPid", )

    def getMasterPid(self):
        return self.__this.call(f"getMasterPid", )

    def connection_info(self, _fd, _reactor_id=-1, _ignore_error=False):
        return self.__this.call(f"connection_info", _fd, _reactor_id, _ignore_error)

    def connection_list(self, _start_fd=0, _find_count=10):
        return self.__this.call(f"connection_list", _start_fd, _find_count)

    def sendMessage(self, _message, _dst_worker_id):
        return self.__this.call(f"sendMessage", _message, _dst_worker_id)

    def command(self, _name, _process_id, _process_type, _data, _json_decode=True):
        return self.__this.call(f"command", _name, _process_id, _process_type, _data, _json_decode)

    def addCommand(self, _name, _accepted_process_types, _callback):
        return self.__this.call(f"addCommand", _name, _accepted_process_types, _callback)

    def addProcess(self, _process):
        return self.__this.call(f"addProcess", _process)

    def stats(self):
        return self.__this.call(f"stats", )

    def getSocket(self, _port=0):
        return self.__this.call(f"getSocket", _port)

    def bind(self, _fd, _uid):
        return self.__this.call(f"bind", _fd, _uid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class NameResolverContext():

    def __init__(self, _family=2, _with_port=False):
        self.__this = phpy.Object(f'Swoole\\NameResolver\\Context', _family, _with_port)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutinePostgreSQL():

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\PostgreSQL', )

    def connect(self, _conninfo, _timeout=2):
        return self.__this.call(f"connect", _conninfo, _timeout)

    def query(self, _query):
        return self.__this.call(f"query", _query)

    def prepare(self, _query):
        return self.__this.call(f"prepare", _query)

    def metaData(self, _table_name):
        return self.__this.call(f"metaData", _table_name)

    def escape(self, _string):
        return self.__this.call(f"escape", _string)

    def escapeLiteral(self, _string):
        return self.__this.call(f"escapeLiteral", _string)

    def escapeIdentifier(self, _string):
        return self.__this.call(f"escapeIdentifier", _string)

    def createLOB(self):
        return self.__this.call(f"createLOB", )

    def openLOB(self, _oid, _mode="rb"):
        return self.__this.call(f"openLOB", _oid, _mode)

    def unlinkLOB(self, _oid):
        return self.__this.call(f"unlinkLOB", _oid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class postgresql():

    def __init__(self):
        self.__this = phpy.Object(f'co\\postgresql', )

    def connect(self, _conninfo, _timeout=2):
        return self.__this.call(f"connect", _conninfo, _timeout)

    def query(self, _query):
        return self.__this.call(f"query", _query)

    def prepare(self, _query):
        return self.__this.call(f"prepare", _query)

    def metaData(self, _table_name):
        return self.__this.call(f"metaData", _table_name)

    def escape(self, _string):
        return self.__this.call(f"escape", _string)

    def escapeLiteral(self, _string):
        return self.__this.call(f"escapeLiteral", _string)

    def escapeIdentifier(self, _string):
        return self.__this.call(f"escapeIdentifier", _string)

    def createLOB(self):
        return self.__this.call(f"createLOB", )

    def openLOB(self, _oid, _mode="rb"):
        return self.__this.call(f"openLOB", _oid, _mode)

    def unlinkLOB(self, _oid):
        return self.__this.call(f"unlinkLOB", _oid)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CoroutinePostgreSQLStatement():

    def execute(self, _params=[]):
        return self.__this.call(f"execute", _params)

    def fetchAll(self, _result_type=1):
        return self.__this.call(f"fetchAll", _result_type)

    def affectedRows(self):
        return self.__this.call(f"affectedRows", )

    def numRows(self):
        return self.__this.call(f"numRows", )

    def fieldCount(self):
        return self.__this.call(f"fieldCount", )

    def fetchObject(self, _row=0, _class_name=None, _ctor_params=[]):
        return self.__this.call(f"fetchObject", _row, _class_name, _ctor_params)

    def fetchAssoc(self, _row=0, _result_type=1):
        return self.__this.call(f"fetchAssoc", _row, _result_type)

    def fetchArray(self, _row=0, _result_type=3):
        return self.__this.call(f"fetchArray", _row, _result_type)

    def fetchRow(self, _row=0, _result_type=2):
        return self.__this.call(f"fetchRow", _row, _result_type)

    def __init__(self):
        self.__this = phpy.Object(f'Swoole\\Coroutine\\PostgreSQLStatement')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

