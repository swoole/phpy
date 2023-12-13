import phpy



def pdo_drivers():
    return phpy.call('pdo_drivers', )




class PDOException():

    errorInfo = None

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'PDOException', _message, _code, _previous)

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


class PDO():
    PARAM_BOOL = 5
    PARAM_NULL = 0
    PARAM_INT = 1
    PARAM_STR = 2
    PARAM_LOB = 3
    PARAM_STMT = 4
    PARAM_INPUT_OUTPUT = 2147483648
    PARAM_STR_NATL = 1073741824
    PARAM_STR_CHAR = 536870912
    PARAM_EVT_ALLOC = 0
    PARAM_EVT_FREE = 1
    PARAM_EVT_EXEC_PRE = 2
    PARAM_EVT_EXEC_POST = 3
    PARAM_EVT_FETCH_PRE = 4
    PARAM_EVT_FETCH_POST = 5
    PARAM_EVT_NORMALIZE = 6
    FETCH_DEFAULT = 0
    FETCH_LAZY = 1
    FETCH_ASSOC = 2
    FETCH_NUM = 3
    FETCH_BOTH = 4
    FETCH_OBJ = 5
    FETCH_BOUND = 6
    FETCH_COLUMN = 7
    FETCH_CLASS = 8
    FETCH_INTO = 9
    FETCH_FUNC = 10
    FETCH_GROUP = 65536
    FETCH_UNIQUE = 196608
    FETCH_KEY_PAIR = 12
    FETCH_CLASSTYPE = 262144
    FETCH_SERIALIZE = 524288
    FETCH_PROPS_LATE = 1048576
    FETCH_NAMED = 11
    ATTR_AUTOCOMMIT = 0
    ATTR_PREFETCH = 1
    ATTR_TIMEOUT = 2
    ATTR_ERRMODE = 3
    ATTR_SERVER_VERSION = 4
    ATTR_CLIENT_VERSION = 5
    ATTR_SERVER_INFO = 6
    ATTR_CONNECTION_STATUS = 7
    ATTR_CASE = 8
    ATTR_CURSOR_NAME = 9
    ATTR_CURSOR = 10
    ATTR_ORACLE_NULLS = 11
    ATTR_PERSISTENT = 12
    ATTR_STATEMENT_CLASS = 13
    ATTR_FETCH_TABLE_NAMES = 14
    ATTR_FETCH_CATALOG_NAMES = 15
    ATTR_DRIVER_NAME = 16
    ATTR_STRINGIFY_FETCHES = 17
    ATTR_MAX_COLUMN_LEN = 18
    ATTR_EMULATE_PREPARES = 20
    ATTR_DEFAULT_FETCH_MODE = 19
    ATTR_DEFAULT_STR_PARAM = 21
    ERRMODE_SILENT = 0
    ERRMODE_WARNING = 1
    ERRMODE_EXCEPTION = 2
    CASE_NATURAL = 0
    CASE_LOWER = 2
    CASE_UPPER = 1
    NULL_NATURAL = 0
    NULL_EMPTY_STRING = 1
    NULL_TO_STRING = 2
    ERR_NONE = "00000"
    FETCH_ORI_NEXT = 0
    FETCH_ORI_PRIOR = 1
    FETCH_ORI_FIRST = 2
    FETCH_ORI_LAST = 3
    FETCH_ORI_ABS = 4
    FETCH_ORI_REL = 5
    CURSOR_FWDONLY = 0
    CURSOR_SCROLL = 1
    MYSQL_ATTR_USE_BUFFERED_QUERY = 1000
    MYSQL_ATTR_LOCAL_INFILE = 1001
    MYSQL_ATTR_INIT_COMMAND = 1002
    MYSQL_ATTR_COMPRESS = 1003
    MYSQL_ATTR_DIRECT_QUERY = 1004
    MYSQL_ATTR_FOUND_ROWS = 1005
    MYSQL_ATTR_IGNORE_SPACE = 1006
    MYSQL_ATTR_SSL_KEY = 1007
    MYSQL_ATTR_SSL_CERT = 1008
    MYSQL_ATTR_SSL_CA = 1009
    MYSQL_ATTR_SSL_CAPATH = 1010
    MYSQL_ATTR_SSL_CIPHER = 1011
    MYSQL_ATTR_SERVER_PUBLIC_KEY = 1012
    MYSQL_ATTR_MULTI_STATEMENTS = 1013
    MYSQL_ATTR_SSL_VERIFY_SERVER_CERT = 1014
    MYSQL_ATTR_LOCAL_INFILE_DIRECTORY = 1015
    SQLITE_DETERMINISTIC = 2048
    SQLITE_ATTR_OPEN_FLAGS = 1000
    SQLITE_OPEN_READONLY = 1
    SQLITE_OPEN_READWRITE = 2
    SQLITE_OPEN_CREATE = 4
    SQLITE_ATTR_READONLY_STATEMENT = 1001
    SQLITE_ATTR_EXTENDED_RESULT_CODES = 1002
    PGSQL_ATTR_DISABLE_PREPARES = 1000
    PGSQL_TRANSACTION_IDLE = 0
    PGSQL_TRANSACTION_ACTIVE = 1
    PGSQL_TRANSACTION_INTRANS = 2
    PGSQL_TRANSACTION_INERROR = 3
    PGSQL_TRANSACTION_UNKNOWN = 4


    def __init__(self, _dsn, _username=None, _password=None, _options=None):
        self.__this = phpy.Object(f'PDO', _dsn, _username, _password, _options)

    def beginTransaction(self):
        return self.__this.call(f"beginTransaction", )

    def commit(self):
        return self.__this.call(f"commit", )

    def errorCode(self):
        return self.__this.call(f"errorCode", )

    def errorInfo(self):
        return self.__this.call(f"errorInfo", )

    def exec(self, _statement):
        return self.__this.call(f"exec", _statement)

    def getAttribute(self, _attribute):
        return self.__this.call(f"getAttribute", _attribute)

    def getAvailableDrivers():
        return phpy.call(f"PDO::getAvailableDrivers", )

    def inTransaction(self):
        return self.__this.call(f"inTransaction", )

    def lastInsertId(self, _name=None):
        return self.__this.call(f"lastInsertId", _name)

    def prepare(self, _query, _options=[]):
        return self.__this.call(f"prepare", _query, _options)

    def query(self, _query, _fetch_mode=None, _fetch_mode_args=None):
        return self.__this.call(f"query", _query, _fetch_mode, _fetch_mode_args)

    def quote(self, _string, _type=2):
        return self.__this.call(f"quote", _string, _type)

    def rollBack(self):
        return self.__this.call(f"rollBack", )

    def setAttribute(self, _attribute, _value):
        return self.__this.call(f"setAttribute", _attribute, _value)


class PDOStatement():

    queryString = None

    def bindColumn(self, _column, _var, _type=2, _max_length=0, _driver_options=None):
        return self.__this.call(f"bindColumn", _column, _var, _type, _max_length, _driver_options)

    def bindParam(self, _param, _var, _type=2, _max_length=0, _driver_options=None):
        return self.__this.call(f"bindParam", _param, _var, _type, _max_length, _driver_options)

    def bindValue(self, _param, _value, _type=2):
        return self.__this.call(f"bindValue", _param, _value, _type)

    def closeCursor(self):
        return self.__this.call(f"closeCursor", )

    def columnCount(self):
        return self.__this.call(f"columnCount", )

    def debugDumpParams(self):
        return self.__this.call(f"debugDumpParams", )

    def errorCode(self):
        return self.__this.call(f"errorCode", )

    def errorInfo(self):
        return self.__this.call(f"errorInfo", )

    def execute(self, _params=None):
        return self.__this.call(f"execute", _params)

    def fetch(self, _mode=0, _cursor_orientation=0, _cursor_offset=0):
        return self.__this.call(f"fetch", _mode, _cursor_orientation, _cursor_offset)

    def fetchAll(self, _mode=0, _args=None):
        return self.__this.call(f"fetchAll", _mode, _args)

    def fetchColumn(self, _column=0):
        return self.__this.call(f"fetchColumn", _column)

    def fetchObject(self, _class="stdClass", _constructor_args=[]):
        return self.__this.call(f"fetchObject", _class, _constructor_args)

    def getAttribute(self, _name):
        return self.__this.call(f"getAttribute", _name)

    def getColumnMeta(self, _column):
        return self.__this.call(f"getColumnMeta", _column)

    def nextRowset(self):
        return self.__this.call(f"nextRowset", )

    def rowCount(self):
        return self.__this.call(f"rowCount", )

    def setAttribute(self, _attribute, _value):
        return self.__this.call(f"setAttribute", _attribute, _value)

    def setFetchMode(self, _mode, _args=None):
        return self.__this.call(f"setFetchMode", _mode, _args)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __init__(self):
        self.__this = phpy.Object(f'PDOStatement')


class PDORow():

    queryString = None

    def __init__(self):
        self.__this = phpy.Object(f'PDORow')


