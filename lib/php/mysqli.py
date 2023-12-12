import phpy

READ_DEFAULT_GROUP = 5
READ_DEFAULT_FILE = 4
OPT_CONNECT_TIMEOUT = 0
OPT_LOCAL_INFILE = 8
OPT_LOAD_DATA_LOCAL_DIR = 43
INIT_COMMAND = 3
OPT_READ_TIMEOUT = 11
OPT_NET_CMD_BUFFER_SIZE = 202
OPT_NET_READ_BUFFER_SIZE = 203
OPT_INT_AND_FLOAT_NATIVE = 201
OPT_SSL_VERIFY_SERVER_CERT = 21
SERVER_PUBLIC_KEY = 35
CLIENT_SSL = 2048
CLIENT_COMPRESS = 32
CLIENT_INTERACTIVE = 1024
CLIENT_IGNORE_SPACE = 256
CLIENT_NO_SCHEMA = 16
CLIENT_FOUND_ROWS = 2
CLIENT_SSL_VERIFY_SERVER_CERT = 1073741824
CLIENT_SSL_DONT_VERIFY_SERVER_CERT = 64
CLIENT_CAN_HANDLE_EXPIRED_PASSWORDS = 4194304
OPT_CAN_HANDLE_EXPIRED_PASSWORDS = 37
STORE_RESULT = 0
USE_RESULT = 1
ASYNC = 8
STORE_RESULT_COPY_DATA = 16
ASSOC = 1
NUM = 2
BOTH = 3
STMT_ATTR_UPDATE_MAX_LENGTH = 0
STMT_ATTR_CURSOR_TYPE = 1
CURSOR_TYPE_NO_CURSOR = 0
CURSOR_TYPE_READ_ONLY = 1
CURSOR_TYPE_FOR_UPDATE = 2
CURSOR_TYPE_SCROLLABLE = 4
STMT_ATTR_PREFETCH_ROWS = 2
NOT_NULL_FLAG = 1
PRI_KEY_FLAG = 2
UNIQUE_KEY_FLAG = 4
MULTIPLE_KEY_FLAG = 8
BLOB_FLAG = 16
UNSIGNED_FLAG = 32
ZEROFILL_FLAG = 64
AUTO_INCREMENT_FLAG = 512
TIMESTAMP_FLAG = 1024
SET_FLAG = 2048
NUM_FLAG = 32768
PART_KEY_FLAG = 16384
GROUP_FLAG = 32768
ENUM_FLAG = 256
BINARY_FLAG = 128
NO_DEFAULT_VALUE_FLAG = 4096
ON_UPDATE_NOW_FLAG = 8192
TYPE_DECIMAL = 0
TYPE_TINY = 1
TYPE_SHORT = 2
TYPE_LONG = 3
TYPE_FLOAT = 4
TYPE_DOUBLE = 5
TYPE_NULL = 6
TYPE_TIMESTAMP = 7
TYPE_LONGLONG = 8
TYPE_INT24 = 9
TYPE_DATE = 10
TYPE_TIME = 11
TYPE_DATETIME = 12
TYPE_YEAR = 13
TYPE_NEWDATE = 14
TYPE_ENUM = 247
TYPE_SET = 248
TYPE_TINY_BLOB = 249
TYPE_MEDIUM_BLOB = 250
TYPE_LONG_BLOB = 251
TYPE_BLOB = 252
TYPE_VAR_STRING = 253
TYPE_STRING = 254
TYPE_CHAR = 1
TYPE_INTERVAL = 247
TYPE_GEOMETRY = 255
TYPE_JSON = 245
TYPE_NEWDECIMAL = 246
TYPE_BIT = 16
SET_CHARSET_NAME = 7
SET_CHARSET_DIR = 6
NO_DATA = 100
DATA_TRUNCATED = 101
REPORT_INDEX = 4
REPORT_ERROR = 1
REPORT_STRICT = 2
REPORT_ALL = 255
REPORT_OFF = 0
DEBUG_TRACE_ENABLED = 0
SERVER_QUERY_NO_GOOD_INDEX_USED = 16
SERVER_QUERY_NO_INDEX_USED = 32
SERVER_QUERY_WAS_SLOW = 2048
SERVER_PS_OUT_PARAMS = 4096
REFRESH_GRANT = 1
REFRESH_LOG = 2
REFRESH_TABLES = 4
REFRESH_HOSTS = 8
REFRESH_STATUS = 16
REFRESH_THREADS = 32
REFRESH_REPLICA = 64
REFRESH_SLAVE = 64
REFRESH_MASTER = 128
REFRESH_BACKUP_LOG = 2097152
TRANS_START_WITH_CONSISTENT_SNAPSHOT = 1
TRANS_START_READ_WRITE = 2
TRANS_START_READ_ONLY = 4
TRANS_COR_AND_CHAIN = 1
TRANS_COR_AND_NO_CHAIN = 2
TRANS_COR_RELEASE = 4
TRANS_COR_NO_RELEASE = 8
IS_MARIADB = False


def affected_rows(_mysql):
    return phpy.call('mysqli_affected_rows', _mysql)


def autocommit(_mysql, _enable):
    return phpy.call('mysqli_autocommit', _mysql, _enable)


def begin_transaction(_mysql, _flags=0, _name=None):
    return phpy.call('mysqli_begin_transaction', _mysql, _flags, _name)


def change_user(_mysql, _username, _password, _database):
    return phpy.call('mysqli_change_user', _mysql, _username, _password, _database)


def character_set_name(_mysql):
    return phpy.call('mysqli_character_set_name', _mysql)


def close(_mysql):
    return phpy.call('mysqli_close', _mysql)


def commit(_mysql, _flags=0, _name=None):
    return phpy.call('mysqli_commit', _mysql, _flags, _name)


def connect(_hostname=None, _username=None, _password=None, _database=None, _port=None, _socket=None):
    return phpy.call('mysqli_connect', _hostname, _username, _password, _database, _port, _socket)


def connect_errno():
    return phpy.call('mysqli_connect_errno', )


def connect_error():
    return phpy.call('mysqli_connect_error', )


def data_seek(_result, _offset):
    return phpy.call('mysqli_data_seek', _result, _offset)


def dump_debug_info(_mysql):
    return phpy.call('mysqli_dump_debug_info', _mysql)


def debug(_options):
    return phpy.call('mysqli_debug', _options)


def errno(_mysql):
    return phpy.call('mysqli_errno', _mysql)


def error(_mysql):
    return phpy.call('mysqli_error', _mysql)


def error_list(_mysql):
    return phpy.call('mysqli_error_list', _mysql)


def stmt_execute(_statement, _params=None):
    return phpy.call('mysqli_stmt_execute', _statement, _params)


def execute(_statement, _params=None):
    return phpy.call('mysqli_execute', _statement, _params)


def fetch_field(_result):
    return phpy.call('mysqli_fetch_field', _result)


def fetch_fields(_result):
    return phpy.call('mysqli_fetch_fields', _result)


def fetch_field_direct(_result, _index):
    return phpy.call('mysqli_fetch_field_direct', _result, _index)


def fetch_lengths(_result):
    return phpy.call('mysqli_fetch_lengths', _result)


def fetch_all(_result, _mode=2):
    return phpy.call('mysqli_fetch_all', _result, _mode)


def fetch_array(_result, _mode=3):
    return phpy.call('mysqli_fetch_array', _result, _mode)


def fetch_assoc(_result):
    return phpy.call('mysqli_fetch_assoc', _result)


def fetch_object(_result, _class="stdClass", _constructor_args=[]):
    return phpy.call('mysqli_fetch_object', _result, _class, _constructor_args)


def fetch_row(_result):
    return phpy.call('mysqli_fetch_row', _result)


def fetch_column(_result, _column=0):
    return phpy.call('mysqli_fetch_column', _result, _column)


def field_count(_mysql):
    return phpy.call('mysqli_field_count', _mysql)


def field_seek(_result, _index):
    return phpy.call('mysqli_field_seek', _result, _index)


def field_tell(_result):
    return phpy.call('mysqli_field_tell', _result)


def free_result(_result):
    return phpy.call('mysqli_free_result', _result)


def get_connection_stats(_mysql):
    return phpy.call('mysqli_get_connection_stats', _mysql)


def get_client_stats():
    return phpy.call('mysqli_get_client_stats', )


def get_charset(_mysql):
    return phpy.call('mysqli_get_charset', _mysql)


def get_client_info(_mysql=None):
    return phpy.call('mysqli_get_client_info', _mysql)


def get_client_version():
    return phpy.call('mysqli_get_client_version', )


def get_links_stats():
    return phpy.call('mysqli_get_links_stats', )


def get_host_info(_mysql):
    return phpy.call('mysqli_get_host_info', _mysql)


def get_proto_info(_mysql):
    return phpy.call('mysqli_get_proto_info', _mysql)


def get_server_info(_mysql):
    return phpy.call('mysqli_get_server_info', _mysql)


def get_server_version(_mysql):
    return phpy.call('mysqli_get_server_version', _mysql)


def get_warnings(_mysql):
    return phpy.call('mysqli_get_warnings', _mysql)


def init():
    return phpy.call('mysqli_init', )


def info(_mysql):
    return phpy.call('mysqli_info', _mysql)


def insert_id(_mysql):
    return phpy.call('mysqli_insert_id', _mysql)


def kill(_mysql, _process_id):
    return phpy.call('mysqli_kill', _mysql, _process_id)


def more_results(_mysql):
    return phpy.call('mysqli_more_results', _mysql)


def multi_query(_mysql, _query):
    return phpy.call('mysqli_multi_query', _mysql, _query)


def next_result(_mysql):
    return phpy.call('mysqli_next_result', _mysql)


def num_fields(_result):
    return phpy.call('mysqli_num_fields', _result)


def num_rows(_result):
    return phpy.call('mysqli_num_rows', _result)


def options(_mysql, _option, _value):
    return phpy.call('mysqli_options', _mysql, _option, _value)


def set_opt(_mysql, _option, _value):
    return phpy.call('mysqli_set_opt', _mysql, _option, _value)


def ping(_mysql):
    return phpy.call('mysqli_ping', _mysql)


def poll(_read, _error, _reject, _seconds, _microseconds=0):
    return phpy.call('mysqli_poll', _read, _error, _reject, _seconds, _microseconds)


def prepare(_mysql, _query):
    return phpy.call('mysqli_prepare', _mysql, _query)


def report(_flags):
    return phpy.call('mysqli_report', _flags)


def query(_mysql, _query, _result_mode=0):
    return phpy.call('mysqli_query', _mysql, _query, _result_mode)


def real_connect(_mysql, _hostname=None, _username=None, _password=None, _database=None, _port=None, _socket=None, _flags=0):
    return phpy.call('mysqli_real_connect', _mysql, _hostname, _username, _password, _database, _port, _socket, _flags)


def real_escape_string(_mysql, _string):
    return phpy.call('mysqli_real_escape_string', _mysql, _string)


def escape_string(_mysql, _string):
    return phpy.call('mysqli_escape_string', _mysql, _string)


def real_query(_mysql, _query):
    return phpy.call('mysqli_real_query', _mysql, _query)


def reap_async_query(_mysql):
    return phpy.call('mysqli_reap_async_query', _mysql)


def release_savepoint(_mysql, _name):
    return phpy.call('mysqli_release_savepoint', _mysql, _name)


def rollback(_mysql, _flags=0, _name=None):
    return phpy.call('mysqli_rollback', _mysql, _flags, _name)


def savepoint(_mysql, _name):
    return phpy.call('mysqli_savepoint', _mysql, _name)


def select_db(_mysql, _database):
    return phpy.call('mysqli_select_db', _mysql, _database)


def set_charset(_mysql, _charset):
    return phpy.call('mysqli_set_charset', _mysql, _charset)


def stmt_affected_rows(_statement):
    return phpy.call('mysqli_stmt_affected_rows', _statement)


def stmt_attr_get(_statement, _attribute):
    return phpy.call('mysqli_stmt_attr_get', _statement, _attribute)


def stmt_attr_set(_statement, _attribute, _value):
    return phpy.call('mysqli_stmt_attr_set', _statement, _attribute, _value)


def stmt_bind_param(_statement, _types, _vars=None):
    return phpy.call('mysqli_stmt_bind_param', _statement, _types, _vars)


def stmt_bind_result(_statement, _vars=None):
    return phpy.call('mysqli_stmt_bind_result', _statement, _vars)


def stmt_close(_statement):
    return phpy.call('mysqli_stmt_close', _statement)


def stmt_data_seek(_statement, _offset):
    return phpy.call('mysqli_stmt_data_seek', _statement, _offset)


def stmt_errno(_statement):
    return phpy.call('mysqli_stmt_errno', _statement)


def stmt_error(_statement):
    return phpy.call('mysqli_stmt_error', _statement)


def stmt_error_list(_statement):
    return phpy.call('mysqli_stmt_error_list', _statement)


def stmt_fetch(_statement):
    return phpy.call('mysqli_stmt_fetch', _statement)


def stmt_field_count(_statement):
    return phpy.call('mysqli_stmt_field_count', _statement)


def stmt_free_result(_statement):
    return phpy.call('mysqli_stmt_free_result', _statement)


def stmt_get_result(_statement):
    return phpy.call('mysqli_stmt_get_result', _statement)


def stmt_get_warnings(_statement):
    return phpy.call('mysqli_stmt_get_warnings', _statement)


def stmt_init(_mysql):
    return phpy.call('mysqli_stmt_init', _mysql)


def stmt_insert_id(_statement):
    return phpy.call('mysqli_stmt_insert_id', _statement)


def stmt_more_results(_statement):
    return phpy.call('mysqli_stmt_more_results', _statement)


def stmt_next_result(_statement):
    return phpy.call('mysqli_stmt_next_result', _statement)


def stmt_num_rows(_statement):
    return phpy.call('mysqli_stmt_num_rows', _statement)


def stmt_param_count(_statement):
    return phpy.call('mysqli_stmt_param_count', _statement)


def stmt_prepare(_statement, _query):
    return phpy.call('mysqli_stmt_prepare', _statement, _query)


def stmt_reset(_statement):
    return phpy.call('mysqli_stmt_reset', _statement)


def stmt_result_metadata(_statement):
    return phpy.call('mysqli_stmt_result_metadata', _statement)


def stmt_send_long_data(_statement, _param_num, _data):
    return phpy.call('mysqli_stmt_send_long_data', _statement, _param_num, _data)


def stmt_store_result(_statement):
    return phpy.call('mysqli_stmt_store_result', _statement)


def stmt_sqlstate(_statement):
    return phpy.call('mysqli_stmt_sqlstate', _statement)


def sqlstate(_mysql):
    return phpy.call('mysqli_sqlstate', _mysql)


def ssl_set(_mysql, _key, _certificate, _ca_certificate, _ca_path, _cipher_algos):
    return phpy.call('mysqli_ssl_set', _mysql, _key, _certificate, _ca_certificate, _ca_path, _cipher_algos)


def stat(_mysql):
    return phpy.call('mysqli_stat', _mysql)


def store_result(_mysql, _mode=0):
    return phpy.call('mysqli_store_result', _mysql, _mode)


def thread_id(_mysql):
    return phpy.call('mysqli_thread_id', _mysql)


def thread_safe():
    return phpy.call('mysqli_thread_safe', )


def use_result(_mysql):
    return phpy.call('mysqli_use_result', _mysql)


def warning_count(_mysql):
    return phpy.call('mysqli_warning_count', _mysql)


def refresh(_mysql, _flags):
    return phpy.call('mysqli_refresh', _mysql, _flags)




def mysqli_sql_exception():

    def getSqlState(self):
        return self.__this.call(f"getSqlState", )

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'mysqli_sql_exception', _message, _code, _previous)

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

    def __toString(self):
        return self.__this.call(f"__toString", )


def mysqli():

    def __init__(self, _hostname=None, _username=None, _password=None, _database=None, _port=None, _socket=None):
        self.__this = phpy.Object(f'mysqli', _hostname, _username, _password, _database, _port, _socket)

    def autocommit(self, _enable):
        return self.__this.call(f"autocommit", _enable)

    def begin_transaction(self, _flags=0, _name=None):
        return self.__this.call(f"begin_transaction", _flags, _name)

    def change_user(self, _username, _password, _database):
        return self.__this.call(f"change_user", _username, _password, _database)

    def character_set_name(self):
        return self.__this.call(f"character_set_name", )

    def close(self):
        return self.__this.call(f"close", )

    def commit(self, _flags=0, _name=None):
        return self.__this.call(f"commit", _flags, _name)

    def connect(self, _hostname=None, _username=None, _password=None, _database=None, _port=None, _socket=None):
        return self.__this.call(f"connect", _hostname, _username, _password, _database, _port, _socket)

    def dump_debug_info(self):
        return self.__this.call(f"dump_debug_info", )

    def debug(self, _options):
        return self.__this.call(f"debug", _options)

    def get_charset(self):
        return self.__this.call(f"get_charset", )

    def get_client_info(self):
        return self.__this.call(f"get_client_info", )

    def get_connection_stats(self):
        return self.__this.call(f"get_connection_stats", )

    def get_server_info(self):
        return self.__this.call(f"get_server_info", )

    def get_warnings(self):
        return self.__this.call(f"get_warnings", )

    def init(self):
        return self.__this.call(f"init", )

    def kill(self, _process_id):
        return self.__this.call(f"kill", _process_id)

    def multi_query(self, _query):
        return self.__this.call(f"multi_query", _query)

    def more_results(self):
        return self.__this.call(f"more_results", )

    def next_result(self):
        return self.__this.call(f"next_result", )

    def ping(self):
        return self.__this.call(f"ping", )

    def poll(_read, _error, _reject, _seconds, _microseconds=0):
        return phpy.call(f"mysqli::poll", _read, _error, _reject, _seconds, _microseconds)

    def prepare(self, _query):
        return self.__this.call(f"prepare", _query)

    def query(self, _query, _result_mode=0):
        return self.__this.call(f"query", _query, _result_mode)

    def real_connect(self, _hostname=None, _username=None, _password=None, _database=None, _port=None, _socket=None, _flags=0):
        return self.__this.call(f"real_connect", _hostname, _username, _password, _database, _port, _socket, _flags)

    def real_escape_string(self, _string):
        return self.__this.call(f"real_escape_string", _string)

    def reap_async_query(self):
        return self.__this.call(f"reap_async_query", )

    def escape_string(self, _string):
        return self.__this.call(f"escape_string", _string)

    def real_query(self, _query):
        return self.__this.call(f"real_query", _query)

    def release_savepoint(self, _name):
        return self.__this.call(f"release_savepoint", _name)

    def rollback(self, _flags=0, _name=None):
        return self.__this.call(f"rollback", _flags, _name)

    def savepoint(self, _name):
        return self.__this.call(f"savepoint", _name)

    def select_db(self, _database):
        return self.__this.call(f"select_db", _database)

    def set_charset(self, _charset):
        return self.__this.call(f"set_charset", _charset)

    def options(self, _option, _value):
        return self.__this.call(f"options", _option, _value)

    def set_opt(self, _option, _value):
        return self.__this.call(f"set_opt", _option, _value)

    def ssl_set(self, _key, _certificate, _ca_certificate, _ca_path, _cipher_algos):
        return self.__this.call(f"ssl_set", _key, _certificate, _ca_certificate, _ca_path, _cipher_algos)

    def stat(self):
        return self.__this.call(f"stat", )

    def stmt_init(self):
        return self.__this.call(f"stmt_init", )

    def store_result(self, _mode=0):
        return self.__this.call(f"store_result", _mode)

    def thread_safe(self):
        return self.__this.call(f"thread_safe", )

    def use_result(self):
        return self.__this.call(f"use_result", )

    def refresh(self, _flags):
        return self.__this.call(f"refresh", _flags)


def mysqli_warning():

    def next(self):
        return self.__this.call(f"next", )


def mysqli_result():

    def __init__(self, _mysql, _result_mode=0):
        self.__this = phpy.Object(f'mysqli_result', _mysql, _result_mode)

    def close(self):
        return self.__this.call(f"close", )

    def free(self):
        return self.__this.call(f"free", )

    def data_seek(self, _offset):
        return self.__this.call(f"data_seek", _offset)

    def fetch_field(self):
        return self.__this.call(f"fetch_field", )

    def fetch_fields(self):
        return self.__this.call(f"fetch_fields", )

    def fetch_field_direct(self, _index):
        return self.__this.call(f"fetch_field_direct", _index)

    def fetch_all(self, _mode=2):
        return self.__this.call(f"fetch_all", _mode)

    def fetch_array(self, _mode=3):
        return self.__this.call(f"fetch_array", _mode)

    def fetch_assoc(self):
        return self.__this.call(f"fetch_assoc", )

    def fetch_object(self, _class="stdClass", _constructor_args=[]):
        return self.__this.call(f"fetch_object", _class, _constructor_args)

    def fetch_row(self):
        return self.__this.call(f"fetch_row", )

    def fetch_column(self, _column=0):
        return self.__this.call(f"fetch_column", _column)

    def field_seek(self, _index):
        return self.__this.call(f"field_seek", _index)

    def free_result(self):
        return self.__this.call(f"free_result", )

    def getIterator(self):
        return self.__this.call(f"getIterator", )


def mysqli_stmt():

    def __init__(self, _mysql, _query=None):
        self.__this = phpy.Object(f'mysqli_stmt', _mysql, _query)

    def attr_get(self, _attribute):
        return self.__this.call(f"attr_get", _attribute)

    def attr_set(self, _attribute, _value):
        return self.__this.call(f"attr_set", _attribute, _value)

    def bind_param(self, _types, _vars=None):
        return self.__this.call(f"bind_param", _types, _vars)

    def bind_result(self, _vars=None):
        return self.__this.call(f"bind_result", _vars)

    def close(self):
        return self.__this.call(f"close", )

    def data_seek(self, _offset):
        return self.__this.call(f"data_seek", _offset)

    def execute(self, _params=None):
        return self.__this.call(f"execute", _params)

    def fetch(self):
        return self.__this.call(f"fetch", )

    def get_warnings(self):
        return self.__this.call(f"get_warnings", )

    def result_metadata(self):
        return self.__this.call(f"result_metadata", )

    def more_results(self):
        return self.__this.call(f"more_results", )

    def next_result(self):
        return self.__this.call(f"next_result", )

    def num_rows(self):
        return self.__this.call(f"num_rows", )

    def send_long_data(self, _param_num, _data):
        return self.__this.call(f"send_long_data", _param_num, _data)

    def free_result(self):
        return self.__this.call(f"free_result", )

    def reset(self):
        return self.__this.call(f"reset", )

    def prepare(self, _query):
        return self.__this.call(f"prepare", _query)

    def store_result(self):
        return self.__this.call(f"store_result", )

    def get_result(self):
        return self.__this.call(f"get_result", )


