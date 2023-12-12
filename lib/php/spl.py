import phpy



def class_implements(_object_or_class, _autoload=True):
    return phpy.call('class_implements', _object_or_class, _autoload)


def class_parents(_object_or_class, _autoload=True):
    return phpy.call('class_parents', _object_or_class, _autoload)


def class_uses(_object_or_class, _autoload=True):
    return phpy.call('class_uses', _object_or_class, _autoload)


def spl_autoload(_class, _file_extensions=None):
    return phpy.call('spl_autoload', _class, _file_extensions)


def spl_autoload_call(_class):
    return phpy.call('spl_autoload_call', _class)


def spl_autoload_extensions(_file_extensions=None):
    return phpy.call('spl_autoload_extensions', _file_extensions)


def spl_autoload_functions():
    return phpy.call('spl_autoload_functions', )


def spl_autoload_register(_callback=None, _throw=True, _prepend=False):
    return phpy.call('spl_autoload_register', _callback, _throw, _prepend)


def spl_autoload_unregister(_callback):
    return phpy.call('spl_autoload_unregister', _callback)


def spl_classes():
    return phpy.call('spl_classes', )


def spl_object_hash(_object):
    return phpy.call('spl_object_hash', _object)


def spl_object_id(_object):
    return phpy.call('spl_object_id', _object)


def iterator_apply(_iterator, _callback, _args=None):
    return phpy.call('iterator_apply', _iterator, _callback, _args)


def iterator_count(_iterator):
    return phpy.call('iterator_count', _iterator)


def iterator_to_array(_iterator, _preserve_keys=True):
    return phpy.call('iterator_to_array', _iterator, _preserve_keys)




class LogicException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'LogicException', _message, _code, _previous)

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

class BadFunctionCallException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'BadFunctionCallException', _message, _code, _previous)

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

class BadMethodCallException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'BadMethodCallException', _message, _code, _previous)

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

class DomainException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'DomainException', _message, _code, _previous)

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

class InvalidArgumentException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'InvalidArgumentException', _message, _code, _previous)

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

class LengthException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'LengthException', _message, _code, _previous)

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

class OutOfRangeException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'OutOfRangeException', _message, _code, _previous)

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

class RuntimeException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'RuntimeException', _message, _code, _previous)

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

class OutOfBoundsException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'OutOfBoundsException', _message, _code, _previous)

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

class OverflowException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'OverflowException', _message, _code, _previous)

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

class RangeException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'RangeException', _message, _code, _previous)

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

class UnderflowException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'UnderflowException', _message, _code, _previous)

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

class UnexpectedValueException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'UnexpectedValueException', _message, _code, _previous)

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

class RecursiveIterator():

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def key(self):
        return self.__this.call(f"key", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def __init__(self):
        self.__this = phpy.Object(f'RecursiveIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class OuterIterator():

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def key(self):
        return self.__this.call(f"key", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def __init__(self):
        self.__this = phpy.Object(f'OuterIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveIteratorIterator():
    LEAVES_ONLY = 0
    SELF_FIRST = 1
    CHILD_FIRST = 2
    CATCH_GET_CHILD = 16

    def __init__(self, _iterator, _mode=0, _flags=0):
        self.__this = phpy.Object(f'RecursiveIteratorIterator', _iterator, _mode, _flags)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def getDepth(self):
        return self.__this.call(f"getDepth", )

    def getSubIterator(self, _level=None):
        return self.__this.call(f"getSubIterator", _level)

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def beginIteration(self):
        return self.__this.call(f"beginIteration", )

    def endIteration(self):
        return self.__this.call(f"endIteration", )

    def callHasChildren(self):
        return self.__this.call(f"callHasChildren", )

    def callGetChildren(self):
        return self.__this.call(f"callGetChildren", )

    def beginChildren(self):
        return self.__this.call(f"beginChildren", )

    def endChildren(self):
        return self.__this.call(f"endChildren", )

    def nextElement(self):
        return self.__this.call(f"nextElement", )

    def setMaxDepth(self, _max_depth=-1):
        return self.__this.call(f"setMaxDepth", _max_depth)

    def getMaxDepth(self):
        return self.__this.call(f"getMaxDepth", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IteratorIterator():

    def __init__(self, _iterator, _class=None):
        self.__this = phpy.Object(f'IteratorIterator', _iterator, _class)

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class FilterIterator():

    def accept(self):
        return self.__this.call(f"accept", )

    def __init__(self, _iterator):
        self.__this = phpy.Object(f'FilterIterator', _iterator)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveFilterIterator():

    def __init__(self, _iterator):
        self.__this = phpy.Object(f'RecursiveFilterIterator', _iterator)

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def accept(self):
        return self.__this.call(f"accept", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CallbackFilterIterator():

    def __init__(self, _iterator, _callback):
        self.__this = phpy.Object(f'CallbackFilterIterator', _iterator, _callback)

    def accept(self):
        return self.__this.call(f"accept", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveCallbackFilterIterator():

    def __init__(self, _iterator, _callback):
        self.__this = phpy.Object(f'RecursiveCallbackFilterIterator', _iterator, _callback)

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def accept(self):
        return self.__this.call(f"accept", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ParentIterator():

    def __init__(self, _iterator):
        self.__this = phpy.Object(f'ParentIterator', _iterator)

    def accept(self):
        return self.__this.call(f"accept", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SeekableIterator():

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def key(self):
        return self.__this.call(f"key", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def __init__(self):
        self.__this = phpy.Object(f'SeekableIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class LimitIterator():

    def __init__(self, _iterator, _offset=0, _limit=-1):
        self.__this = phpy.Object(f'LimitIterator', _iterator, _offset, _limit)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def getPosition(self):
        return self.__this.call(f"getPosition", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class CachingIterator():
    CALL_TOSTRING = 1
    CATCH_GET_CHILD = 16
    TOSTRING_USE_KEY = 2
    TOSTRING_USE_CURRENT = 4
    TOSTRING_USE_INNER = 8
    FULL_CACHE = 256

    def __init__(self, _iterator, _flags=1):
        self.__this = phpy.Object(f'CachingIterator', _iterator, _flags)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def hasNext(self):
        return self.__this.call(f"hasNext", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def getCache(self):
        return self.__this.call(f"getCache", )

    def count(self):
        return self.__this.call(f"count", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveCachingIterator():
    CALL_TOSTRING = 1
    CATCH_GET_CHILD = 16
    TOSTRING_USE_KEY = 2
    TOSTRING_USE_CURRENT = 4
    TOSTRING_USE_INNER = 8
    FULL_CACHE = 256

    def __init__(self, _iterator, _flags=1):
        self.__this = phpy.Object(f'RecursiveCachingIterator', _iterator, _flags)

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def hasNext(self):
        return self.__this.call(f"hasNext", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def offsetGet(self, _key):
        return self.__this.call(f"offsetGet", _key)

    def offsetSet(self, _key, _value):
        return self.__this.call(f"offsetSet", _key, _value)

    def offsetUnset(self, _key):
        return self.__this.call(f"offsetUnset", _key)

    def offsetExists(self, _key):
        return self.__this.call(f"offsetExists", _key)

    def getCache(self):
        return self.__this.call(f"getCache", )

    def count(self):
        return self.__this.call(f"count", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class NoRewindIterator():

    def __init__(self, _iterator):
        self.__this = phpy.Object(f'NoRewindIterator', _iterator)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class AppendIterator():

    def __init__(self):
        self.__this = phpy.Object(f'AppendIterator', )

    def append(self, _iterator):
        return self.__this.call(f"append", _iterator)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def getIteratorIndex(self):
        return self.__this.call(f"getIteratorIndex", )

    def getArrayIterator(self):
        return self.__this.call(f"getArrayIterator", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def key(self):
        return self.__this.call(f"key", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class InfiniteIterator():

    def __init__(self, _iterator):
        self.__this = phpy.Object(f'InfiniteIterator', _iterator)

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RegexIterator():
    USE_KEY = 1
    INVERT_MATCH = 2
    MATCH = 0
    GET_MATCH = 1
    ALL_MATCHES = 2
    SPLIT = 3
    REPLACE = 4

    def __init__(self, _iterator, _pattern, _mode=0, _flags=0, _preg_flags=0):
        self.__this = phpy.Object(f'RegexIterator', _iterator, _pattern, _mode, _flags, _preg_flags)

    def accept(self):
        return self.__this.call(f"accept", )

    def getMode(self):
        return self.__this.call(f"getMode", )

    def setMode(self, _mode):
        return self.__this.call(f"setMode", _mode)

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getRegex(self):
        return self.__this.call(f"getRegex", )

    def getPregFlags(self):
        return self.__this.call(f"getPregFlags", )

    def setPregFlags(self, _preg_flags):
        return self.__this.call(f"setPregFlags", _preg_flags)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveRegexIterator():
    USE_KEY = 1
    INVERT_MATCH = 2
    MATCH = 0
    GET_MATCH = 1
    ALL_MATCHES = 2
    SPLIT = 3
    REPLACE = 4

    def __init__(self, _iterator, _pattern, _mode=0, _flags=0, _preg_flags=0):
        self.__this = phpy.Object(f'RecursiveRegexIterator', _iterator, _pattern, _mode, _flags, _preg_flags)

    def accept(self):
        return self.__this.call(f"accept", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def getMode(self):
        return self.__this.call(f"getMode", )

    def setMode(self, _mode):
        return self.__this.call(f"setMode", _mode)

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getRegex(self):
        return self.__this.call(f"getRegex", )

    def getPregFlags(self):
        return self.__this.call(f"getPregFlags", )

    def setPregFlags(self, _preg_flags):
        return self.__this.call(f"setPregFlags", _preg_flags)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def next(self):
        return self.__this.call(f"next", )

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class EmptyIterator():

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def key(self):
        return self.__this.call(f"key", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def __init__(self):
        self.__this = phpy.Object(f'EmptyIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveTreeIterator():
    LEAVES_ONLY = 0
    SELF_FIRST = 1
    CHILD_FIRST = 2
    CATCH_GET_CHILD = 16
    BYPASS_CURRENT = 4
    BYPASS_KEY = 8
    PREFIX_LEFT = 0
    PREFIX_MID_HAS_NEXT = 1
    PREFIX_MID_LAST = 2
    PREFIX_END_HAS_NEXT = 3
    PREFIX_END_LAST = 4
    PREFIX_RIGHT = 5

    def __init__(self, _iterator, _flags=8, _caching_iterator_flags=16, _mode=1):
        self.__this = phpy.Object(f'RecursiveTreeIterator', _iterator, _flags, _caching_iterator_flags, _mode)

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getPrefix(self):
        return self.__this.call(f"getPrefix", )

    def setPostfix(self, _postfix):
        return self.__this.call(f"setPostfix", _postfix)

    def setPrefixPart(self, _part, _value):
        return self.__this.call(f"setPrefixPart", _part, _value)

    def getEntry(self):
        return self.__this.call(f"getEntry", )

    def getPostfix(self):
        return self.__this.call(f"getPostfix", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def getDepth(self):
        return self.__this.call(f"getDepth", )

    def getSubIterator(self, _level=None):
        return self.__this.call(f"getSubIterator", _level)

    def getInnerIterator(self):
        return self.__this.call(f"getInnerIterator", )

    def beginIteration(self):
        return self.__this.call(f"beginIteration", )

    def endIteration(self):
        return self.__this.call(f"endIteration", )

    def callHasChildren(self):
        return self.__this.call(f"callHasChildren", )

    def callGetChildren(self):
        return self.__this.call(f"callGetChildren", )

    def beginChildren(self):
        return self.__this.call(f"beginChildren", )

    def endChildren(self):
        return self.__this.call(f"endChildren", )

    def nextElement(self):
        return self.__this.call(f"nextElement", )

    def setMaxDepth(self, _max_depth=-1):
        return self.__this.call(f"setMaxDepth", _max_depth)

    def getMaxDepth(self):
        return self.__this.call(f"getMaxDepth", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ArrayObject():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0, _iterator_class="ArrayIterator"):
        self.__this = phpy.Object(f'ArrayObject', _array, _flags, _iterator_class)

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

class ArrayIterator():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2

    def __init__(self, _array=[], _flags=0):
        self.__this = phpy.Object(f'ArrayIterator', _array, _flags)

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

class RecursiveArrayIterator():
    STD_PROP_LIST = 1
    ARRAY_AS_PROPS = 2
    CHILD_ARRAYS_ONLY = 4

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def __init__(self, _array=[], _flags=0):
        self.__this = phpy.Object(f'RecursiveArrayIterator', _array, _flags)

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

class SplFileInfo():

    def __init__(self, _filename):
        self.__this = phpy.Object(f'SplFileInfo', _filename)

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class DirectoryIterator():

    def __init__(self, _directory):
        self.__this = phpy.Object(f'DirectoryIterator', _directory)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class FilesystemIterator():
    CURRENT_MODE_MASK = 240
    CURRENT_AS_PATHNAME = 32
    CURRENT_AS_FILEINFO = 0
    CURRENT_AS_SELF = 16
    KEY_MODE_MASK = 3840
    KEY_AS_PATHNAME = 0
    FOLLOW_SYMLINKS = 16384
    KEY_AS_FILENAME = 256
    NEW_CURRENT_AND_KEY = 256
    OTHER_MODE_MASK = 28672
    SKIP_DOTS = 4096
    UNIX_PATHS = 8192

    def __init__(self, _directory, _flags=4096):
        self.__this = phpy.Object(f'FilesystemIterator', _directory, _flags)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class RecursiveDirectoryIterator():
    CURRENT_MODE_MASK = 240
    CURRENT_AS_PATHNAME = 32
    CURRENT_AS_FILEINFO = 0
    CURRENT_AS_SELF = 16
    KEY_MODE_MASK = 3840
    KEY_AS_PATHNAME = 0
    FOLLOW_SYMLINKS = 16384
    KEY_AS_FILENAME = 256
    NEW_CURRENT_AND_KEY = 256
    OTHER_MODE_MASK = 28672
    SKIP_DOTS = 4096
    UNIX_PATHS = 8192

    def __init__(self, _directory, _flags=0):
        self.__this = phpy.Object(f'RecursiveDirectoryIterator', _directory, _flags)

    def hasChildren(self, _allow_links=False):
        return self.__this.call(f"hasChildren", _allow_links)

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def getSubPath(self):
        return self.__this.call(f"getSubPath", )

    def getSubPathname(self):
        return self.__this.call(f"getSubPathname", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class GlobIterator():
    CURRENT_MODE_MASK = 240
    CURRENT_AS_PATHNAME = 32
    CURRENT_AS_FILEINFO = 0
    CURRENT_AS_SELF = 16
    KEY_MODE_MASK = 3840
    KEY_AS_PATHNAME = 0
    FOLLOW_SYMLINKS = 16384
    KEY_AS_FILENAME = 256
    NEW_CURRENT_AND_KEY = 256
    OTHER_MODE_MASK = 28672
    SKIP_DOTS = 4096
    UNIX_PATHS = 8192

    def __init__(self, _pattern, _flags=0):
        self.__this = phpy.Object(f'GlobIterator', _pattern, _flags)

    def count(self):
        return self.__this.call(f"count", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplFileObject():
    DROP_NEW_LINE = 1
    READ_AHEAD = 2
    SKIP_EMPTY = 4
    READ_CSV = 8

    def __init__(self, _filename, _mode="r", _use_include_path=False, _context=None):
        self.__this = phpy.Object(f'SplFileObject', _filename, _mode, _use_include_path, _context)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def eof(self):
        return self.__this.call(f"eof", )

    def valid(self):
        return self.__this.call(f"valid", )

    def fgets(self):
        return self.__this.call(f"fgets", )

    def fread(self, _length):
        return self.__this.call(f"fread", _length)

    def fgetcsv(self, _separator=",", _enclosure="\"", _escape="\\"):
        return self.__this.call(f"fgetcsv", _separator, _enclosure, _escape)

    def fputcsv(self, _fields, _separator=",", _enclosure="\"", _escape="\\", _eol="\n"):
        return self.__this.call(f"fputcsv", _fields, _separator, _enclosure, _escape, _eol)

    def setCsvControl(self, _separator=",", _enclosure="\"", _escape="\\"):
        return self.__this.call(f"setCsvControl", _separator, _enclosure, _escape)

    def getCsvControl(self):
        return self.__this.call(f"getCsvControl", )

    def flock(self, _operation, _would_block=None):
        return self.__this.call(f"flock", _operation, _would_block)

    def fflush(self):
        return self.__this.call(f"fflush", )

    def ftell(self):
        return self.__this.call(f"ftell", )

    def fseek(self, _offset, _whence=0):
        return self.__this.call(f"fseek", _offset, _whence)

    def fgetc(self):
        return self.__this.call(f"fgetc", )

    def fpassthru(self):
        return self.__this.call(f"fpassthru", )

    def fscanf(self, _format, _vars=None):
        return self.__this.call(f"fscanf", _format, _vars)

    def fwrite(self, _data, _length=0):
        return self.__this.call(f"fwrite", _data, _length)

    def fstat(self):
        return self.__this.call(f"fstat", )

    def ftruncate(self, _size):
        return self.__this.call(f"ftruncate", _size)

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setMaxLineLen(self, _max_length):
        return self.__this.call(f"setMaxLineLen", _max_length)

    def getMaxLineLen(self):
        return self.__this.call(f"getMaxLineLen", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def seek(self, _line):
        return self.__this.call(f"seek", _line)

    def getCurrentLine(self):
        return self.__this.call(f"getCurrentLine", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplTempFileObject():
    DROP_NEW_LINE = 1
    READ_AHEAD = 2
    SKIP_EMPTY = 4
    READ_CSV = 8

    def __init__(self, _max_memory=2097152):
        self.__this = phpy.Object(f'SplTempFileObject', _max_memory)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def eof(self):
        return self.__this.call(f"eof", )

    def valid(self):
        return self.__this.call(f"valid", )

    def fgets(self):
        return self.__this.call(f"fgets", )

    def fread(self, _length):
        return self.__this.call(f"fread", _length)

    def fgetcsv(self, _separator=",", _enclosure="\"", _escape="\\"):
        return self.__this.call(f"fgetcsv", _separator, _enclosure, _escape)

    def fputcsv(self, _fields, _separator=",", _enclosure="\"", _escape="\\", _eol="\n"):
        return self.__this.call(f"fputcsv", _fields, _separator, _enclosure, _escape, _eol)

    def setCsvControl(self, _separator=",", _enclosure="\"", _escape="\\"):
        return self.__this.call(f"setCsvControl", _separator, _enclosure, _escape)

    def getCsvControl(self):
        return self.__this.call(f"getCsvControl", )

    def flock(self, _operation, _would_block=None):
        return self.__this.call(f"flock", _operation, _would_block)

    def fflush(self):
        return self.__this.call(f"fflush", )

    def ftell(self):
        return self.__this.call(f"ftell", )

    def fseek(self, _offset, _whence=0):
        return self.__this.call(f"fseek", _offset, _whence)

    def fgetc(self):
        return self.__this.call(f"fgetc", )

    def fpassthru(self):
        return self.__this.call(f"fpassthru", )

    def fscanf(self, _format, _vars=None):
        return self.__this.call(f"fscanf", _format, _vars)

    def fwrite(self, _data, _length=0):
        return self.__this.call(f"fwrite", _data, _length)

    def fstat(self):
        return self.__this.call(f"fstat", )

    def ftruncate(self, _size):
        return self.__this.call(f"ftruncate", _size)

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setMaxLineLen(self, _max_length):
        return self.__this.call(f"setMaxLineLen", _max_length)

    def getMaxLineLen(self):
        return self.__this.call(f"getMaxLineLen", )

    def hasChildren(self):
        return self.__this.call(f"hasChildren", )

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def seek(self, _line):
        return self.__this.call(f"seek", _line)

    def getCurrentLine(self):
        return self.__this.call(f"getCurrentLine", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplDoublyLinkedList():
    IT_MODE_LIFO = 2
    IT_MODE_FIFO = 0
    IT_MODE_DELETE = 1
    IT_MODE_KEEP = 0

    def add(self, _index, _value):
        return self.__this.call(f"add", _index, _value)

    def pop(self):
        return self.__this.call(f"pop", )

    def shift(self):
        return self.__this.call(f"shift", )

    def push(self, _value):
        return self.__this.call(f"push", _value)

    def unshift(self, _value):
        return self.__this.call(f"unshift", _value)

    def top(self):
        return self.__this.call(f"top", )

    def bottom(self):
        return self.__this.call(f"bottom", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def setIteratorMode(self, _mode):
        return self.__this.call(f"setIteratorMode", _mode)

    def getIteratorMode(self):
        return self.__this.call(f"getIteratorMode", )

    def offsetExists(self, _index):
        return self.__this.call(f"offsetExists", _index)

    def offsetGet(self, _index):
        return self.__this.call(f"offsetGet", _index)

    def offsetSet(self, _index, _value):
        return self.__this.call(f"offsetSet", _index, _value)

    def offsetUnset(self, _index):
        return self.__this.call(f"offsetUnset", _index)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def prev(self):
        return self.__this.call(f"prev", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def __init__(self):
        self.__this = phpy.Object(f'SplDoublyLinkedList')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplQueue():
    IT_MODE_LIFO = 2
    IT_MODE_FIFO = 0
    IT_MODE_DELETE = 1
    IT_MODE_KEEP = 0

    def enqueue(self, _value):
        return self.__this.call(f"enqueue", _value)

    def dequeue(self):
        return self.__this.call(f"dequeue", )

    def add(self, _index, _value):
        return self.__this.call(f"add", _index, _value)

    def pop(self):
        return self.__this.call(f"pop", )

    def shift(self):
        return self.__this.call(f"shift", )

    def push(self, _value):
        return self.__this.call(f"push", _value)

    def unshift(self, _value):
        return self.__this.call(f"unshift", _value)

    def top(self):
        return self.__this.call(f"top", )

    def bottom(self):
        return self.__this.call(f"bottom", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def setIteratorMode(self, _mode):
        return self.__this.call(f"setIteratorMode", _mode)

    def getIteratorMode(self):
        return self.__this.call(f"getIteratorMode", )

    def offsetExists(self, _index):
        return self.__this.call(f"offsetExists", _index)

    def offsetGet(self, _index):
        return self.__this.call(f"offsetGet", _index)

    def offsetSet(self, _index, _value):
        return self.__this.call(f"offsetSet", _index, _value)

    def offsetUnset(self, _index):
        return self.__this.call(f"offsetUnset", _index)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def prev(self):
        return self.__this.call(f"prev", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def __init__(self):
        self.__this = phpy.Object(f'SplQueue')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplStack():
    IT_MODE_LIFO = 2
    IT_MODE_FIFO = 0
    IT_MODE_DELETE = 1
    IT_MODE_KEEP = 0

    def add(self, _index, _value):
        return self.__this.call(f"add", _index, _value)

    def pop(self):
        return self.__this.call(f"pop", )

    def shift(self):
        return self.__this.call(f"shift", )

    def push(self, _value):
        return self.__this.call(f"push", _value)

    def unshift(self, _value):
        return self.__this.call(f"unshift", _value)

    def top(self):
        return self.__this.call(f"top", )

    def bottom(self):
        return self.__this.call(f"bottom", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

    def setIteratorMode(self, _mode):
        return self.__this.call(f"setIteratorMode", _mode)

    def getIteratorMode(self):
        return self.__this.call(f"getIteratorMode", )

    def offsetExists(self, _index):
        return self.__this.call(f"offsetExists", _index)

    def offsetGet(self, _index):
        return self.__this.call(f"offsetGet", _index)

    def offsetSet(self, _index, _value):
        return self.__this.call(f"offsetSet", _index, _value)

    def offsetUnset(self, _index):
        return self.__this.call(f"offsetUnset", _index)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def prev(self):
        return self.__this.call(f"prev", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def __init__(self):
        self.__this = phpy.Object(f'SplStack')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplHeap():

    def extract(self):
        return self.__this.call(f"extract", )

    def insert(self, _value):
        return self.__this.call(f"insert", _value)

    def top(self):
        return self.__this.call(f"top", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

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

    def recoverFromCorruption(self):
        return self.__this.call(f"recoverFromCorruption", )

    def isCorrupted(self):
        return self.__this.call(f"isCorrupted", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __init__(self):
        self.__this = phpy.Object(f'SplHeap')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplMinHeap():

    def extract(self):
        return self.__this.call(f"extract", )

    def insert(self, _value):
        return self.__this.call(f"insert", _value)

    def top(self):
        return self.__this.call(f"top", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

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

    def recoverFromCorruption(self):
        return self.__this.call(f"recoverFromCorruption", )

    def isCorrupted(self):
        return self.__this.call(f"isCorrupted", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __init__(self):
        self.__this = phpy.Object(f'SplMinHeap')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplMaxHeap():

    def extract(self):
        return self.__this.call(f"extract", )

    def insert(self, _value):
        return self.__this.call(f"insert", _value)

    def top(self):
        return self.__this.call(f"top", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

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

    def recoverFromCorruption(self):
        return self.__this.call(f"recoverFromCorruption", )

    def isCorrupted(self):
        return self.__this.call(f"isCorrupted", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __init__(self):
        self.__this = phpy.Object(f'SplMaxHeap')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplPriorityQueue():
    EXTR_BOTH = 3
    EXTR_PRIORITY = 2
    EXTR_DATA = 1

    def compare(self, _priority1, _priority2):
        return self.__this.call(f"compare", _priority1, _priority2)

    def insert(self, _value, _priority):
        return self.__this.call(f"insert", _value, _priority)

    def setExtractFlags(self, _flags):
        return self.__this.call(f"setExtractFlags", _flags)

    def top(self):
        return self.__this.call(f"top", )

    def extract(self):
        return self.__this.call(f"extract", )

    def count(self):
        return self.__this.call(f"count", )

    def isEmpty(self):
        return self.__this.call(f"isEmpty", )

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

    def recoverFromCorruption(self):
        return self.__this.call(f"recoverFromCorruption", )

    def isCorrupted(self):
        return self.__this.call(f"isCorrupted", )

    def getExtractFlags(self):
        return self.__this.call(f"getExtractFlags", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __init__(self):
        self.__this = phpy.Object(f'SplPriorityQueue')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplFixedArray():

    def __init__(self, _size=0):
        self.__this = phpy.Object(f'SplFixedArray', _size)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def count(self):
        return self.__this.call(f"count", )

    def toArray(self):
        return self.__this.call(f"toArray", )

    def fromArray(_array, _preserve_keys=True):
        return phpy.call(f"SplFixedArray::fromArray", _array, _preserve_keys)

    def getSize(self):
        return self.__this.call(f"getSize", )

    def setSize(self, _size):
        return self.__this.call(f"setSize", _size)

    def offsetExists(self, _index):
        return self.__this.call(f"offsetExists", _index)

    def offsetGet(self, _index):
        return self.__this.call(f"offsetGet", _index)

    def offsetSet(self, _index, _value):
        return self.__this.call(f"offsetSet", _index, _value)

    def offsetUnset(self, _index):
        return self.__this.call(f"offsetUnset", _index)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def jsonSerialize(self):
        return self.__this.call(f"jsonSerialize", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplObserver():

    def update(self, _subject):
        return self.__this.call(f"update", _subject)

    def __init__(self):
        self.__this = phpy.Object(f'SplObserver')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplSubject():

    def attach(self, _observer):
        return self.__this.call(f"attach", _observer)

    def detach(self, _observer):
        return self.__this.call(f"detach", _observer)

    def notify(self):
        return self.__this.call(f"notify", )

    def __init__(self):
        self.__this = phpy.Object(f'SplSubject')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class SplObjectStorage():

    def attach(self, _object, _info=None):
        return self.__this.call(f"attach", _object, _info)

    def detach(self, _object):
        return self.__this.call(f"detach", _object)

    def contains(self, _object):
        return self.__this.call(f"contains", _object)

    def addAll(self, _storage):
        return self.__this.call(f"addAll", _storage)

    def removeAll(self, _storage):
        return self.__this.call(f"removeAll", _storage)

    def removeAllExcept(self, _storage):
        return self.__this.call(f"removeAllExcept", _storage)

    def getInfo(self):
        return self.__this.call(f"getInfo", )

    def setInfo(self, _info):
        return self.__this.call(f"setInfo", _info)

    def count(self, _mode=0):
        return self.__this.call(f"count", _mode)

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)

    def serialize(self):
        return self.__this.call(f"serialize", )

    def offsetExists(self, _object):
        return self.__this.call(f"offsetExists", _object)

    def offsetGet(self, _object):
        return self.__this.call(f"offsetGet", _object)

    def offsetSet(self, _object, _info=None):
        return self.__this.call(f"offsetSet", _object, _info)

    def offsetUnset(self, _object):
        return self.__this.call(f"offsetUnset", _object)

    def getHash(self, _object):
        return self.__this.call(f"getHash", _object)

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __init__(self):
        self.__this = phpy.Object(f'SplObjectStorage')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class MultipleIterator():
    MIT_NEED_ANY = 0
    MIT_NEED_ALL = 1
    MIT_KEYS_NUMERIC = 0
    MIT_KEYS_ASSOC = 2

    def __init__(self, _flags=1):
        self.__this = phpy.Object(f'MultipleIterator', _flags)

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def attachIterator(self, _iterator, _info=None):
        return self.__this.call(f"attachIterator", _iterator, _info)

    def detachIterator(self, _iterator):
        return self.__this.call(f"detachIterator", _iterator)

    def containsIterator(self, _iterator):
        return self.__this.call(f"containsIterator", _iterator)

    def countIterators(self):
        return self.__this.call(f"countIterators", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def next(self):
        return self.__this.call(f"next", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

