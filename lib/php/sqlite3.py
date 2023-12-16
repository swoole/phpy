import phpy

ASSOC = 1
NUM = 2
BOTH = 3
INTEGER = 1
FLOAT = 2
TEXT = 3
BLOB = 4
NULL = 5
OPEN_READONLY = 1
OPEN_READWRITE = 2
OPEN_CREATE = 4
DETERMINISTIC = 2048




class SQLite3():
    OK = 0
    DENY = 1
    IGNORE = 2
    CREATE_INDEX = 1
    CREATE_TABLE = 2
    CREATE_TEMP_INDEX = 3
    CREATE_TEMP_TABLE = 4
    CREATE_TEMP_TRIGGER = 5
    CREATE_TEMP_VIEW = 6
    CREATE_TRIGGER = 7
    CREATE_VIEW = 8
    DELETE = 9
    DROP_INDEX = 10
    DROP_TABLE = 11
    DROP_TEMP_INDEX = 12
    DROP_TEMP_TABLE = 13
    DROP_TEMP_TRIGGER = 14
    DROP_TEMP_VIEW = 15
    DROP_TRIGGER = 16
    DROP_VIEW = 17
    INSERT = 18
    PRAGMA = 19
    READ = 20
    SELECT = 21
    TRANSACTION = 22
    UPDATE = 23
    ATTACH = 24
    DETACH = 25
    ALTER_TABLE = 26
    REINDEX = 27
    ANALYZE = 28
    CREATE_VTABLE = 29
    DROP_VTABLE = 30
    FUNCTION = 31
    SAVEPOINT = 32
    COPY = 0
    RECURSIVE = 33

    def __init__(self, _filename, _flags=6, _encryption_key=""):
        self.__this = phpy.Object(f'SQLite3', _filename, _flags, _encryption_key)

    def open(self, _filename, _flags=6, _encryption_key=""):
        return self.__this.call(f"open", _filename, _flags, _encryption_key)

    def close(self):
        return self.__this.call(f"close", )

    def version():
        return phpy.call(f"SQLite3::version", )

    def lastInsertRowID(self):
        return self.__this.call(f"lastInsertRowID", )

    def lastErrorCode(self):
        return self.__this.call(f"lastErrorCode", )

    def lastExtendedErrorCode(self):
        return self.__this.call(f"lastExtendedErrorCode", )

    def lastErrorMsg(self):
        return self.__this.call(f"lastErrorMsg", )

    def changes(self):
        return self.__this.call(f"changes", )

    def busyTimeout(self, _milliseconds):
        return self.__this.call(f"busyTimeout", _milliseconds)

    def loadExtension(self, _name):
        return self.__this.call(f"loadExtension", _name)

    def backup(self, _destination, _source_database="main", _destination_database="main"):
        return self.__this.call(f"backup", _destination, _source_database, _destination_database)

    def escapeString(_string):
        return phpy.call(f"SQLite3::escapeString", _string)

    def prepare(self, _query):
        return self.__this.call(f"prepare", _query)

    def exec(self, _query):
        return self.__this.call(f"exec", _query)

    def query(self, _query):
        return self.__this.call(f"query", _query)

    def querySingle(self, _query, _entire_row=False):
        return self.__this.call(f"querySingle", _query, _entire_row)

    def createFunction(self, _name, _callback, _arg_count=-1, _flags=0):
        return self.__this.call(f"createFunction", _name, _callback, _arg_count, _flags)

    def createAggregate(self, _name, _step_callback, _final_callback, _arg_count=-1):
        return self.__this.call(f"createAggregate", _name, _step_callback, _final_callback, _arg_count)

    def createCollation(self, _name, _callback):
        return self.__this.call(f"createCollation", _name, _callback)

    def openBlob(self, _table, _column, _rowid, _database="main", _flags=1):
        return self.__this.call(f"openBlob", _table, _column, _rowid, _database, _flags)

    def enableExceptions(self, _enable=False):
        return self.__this.call(f"enableExceptions", _enable)

    def enableExtendedResultCodes(self, _enable=True):
        return self.__this.call(f"enableExtendedResultCodes", _enable)

    def setAuthorizer(self, _callback):
        return self.__this.call(f"setAuthorizer", _callback)

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class SQLite3Stmt():

    def bindParam(self, _param, _var, _type=3):
        return self.__this.call(f"bindParam", _param, _var, _type)

    def bindValue(self, _param, _value, _type=3):
        return self.__this.call(f"bindValue", _param, _value, _type)

    def clear(self):
        return self.__this.call(f"clear", )

    def close(self):
        return self.__this.call(f"close", )

    def execute(self):
        return self.__this.call(f"execute", )

    def getSQL(self, _expand=False):
        return self.__this.call(f"getSQL", _expand)

    def paramCount(self):
        return self.__this.call(f"paramCount", )

    def readOnly(self):
        return self.__this.call(f"readOnly", )

    def reset(self):
        return self.__this.call(f"reset", )

    def __init__(self):
        self.__this = phpy.Object(f'SQLite3Stmt')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class SQLite3Result():

    def numColumns(self):
        return self.__this.call(f"numColumns", )

    def columnName(self, _column):
        return self.__this.call(f"columnName", _column)

    def columnType(self, _column):
        return self.__this.call(f"columnType", _column)

    def fetchArray(self, _mode=3):
        return self.__this.call(f"fetchArray", _mode)

    def reset(self):
        return self.__this.call(f"reset", )

    def finalize(self):
        return self.__this.call(f"finalize", )

    def __init__(self):
        self.__this = phpy.Object(f'SQLite3Result')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

