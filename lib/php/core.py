import phpy

E_ERROR = 1
E_RECOVERABLE_ERROR = 4096
E_WARNING = 2
E_PARSE = 4
E_NOTICE = 8
E_STRICT = 2048
E_DEPRECATED = 8192
E_CORE_ERROR = 16
E_CORE_WARNING = 32
E_COMPILE_ERROR = 64
E_COMPILE_WARNING = 128
E_USER_ERROR = 256
E_USER_WARNING = 512
E_USER_NOTICE = 1024
E_USER_DEPRECATED = 16384
E_ALL = 32767
DEBUG_BACKTRACE_PROVIDE_OBJECT = 1
DEBUG_BACKTRACE_IGNORE_ARGS = 2
ZEND_THREAD_SAFE = False
ZEND_DEBUG_BUILD = False
TRUE = True
FALSE = False
NULL = None
PHP_VERSION = "8.1.12"
PHP_MAJOR_VERSION = 8
PHP_MINOR_VERSION = 1
PHP_RELEASE_VERSION = 12
PHP_EXTRA_VERSION = ""
PHP_VERSION_ID = 80112
PHP_ZTS = 0
PHP_DEBUG = 0
PHP_OS = "Linux"
PHP_OS_FAMILY = "Linux"
PHP_SAPI = "cli"
DEFAULT_INCLUDE_PATH = ".:"
PEAR_INSTALL_DIR = ""
PEAR_EXTENSION_DIR = "/usr/local/lib/php/extensions/no-debug-non-zts-20210902"
PHP_EXTENSION_DIR = "/usr/local/lib/php/extensions/no-debug-non-zts-20210902"
PHP_PREFIX = "/usr/local"
PHP_BINDIR = "/usr/local/bin"
PHP_MANDIR = "/usr/local/php/man"
PHP_LIBDIR = "/usr/local/lib/php"
PHP_DATADIR = "/usr/local/share/php"
PHP_SYSCONFDIR = "/usr/local/etc"
PHP_LOCALSTATEDIR = "/usr/local/var"
PHP_CONFIG_FILE_PATH = "/usr/local/lib"
PHP_CONFIG_FILE_SCAN_DIR = ""
PHP_SHLIB_SUFFIX = "so"
PHP_EOL = "\n"
PHP_MAXPATHLEN = 4096
PHP_INT_MAX = 9223372036854775807
PHP_INT_MIN = -9223372036854775808
PHP_INT_SIZE = 8
PHP_FD_SETSIZE = 1024
PHP_FLOAT_DIG = 15
PHP_FLOAT_EPSILON = 2.2204460492503E-16
PHP_FLOAT_MAX = 1.7976931348623E+308
PHP_FLOAT_MIN = 2.2250738585072E-308
PHP_BINARY = "/home/htf/bin/swoole-cli"
PHP_OUTPUT_HANDLER_START = 1
PHP_OUTPUT_HANDLER_WRITE = 0
PHP_OUTPUT_HANDLER_FLUSH = 4
PHP_OUTPUT_HANDLER_CLEAN = 2
PHP_OUTPUT_HANDLER_FINAL = 8
PHP_OUTPUT_HANDLER_CONT = 0
PHP_OUTPUT_HANDLER_END = 8
PHP_OUTPUT_HANDLER_CLEANABLE = 16
PHP_OUTPUT_HANDLER_FLUSHABLE = 32
PHP_OUTPUT_HANDLER_REMOVABLE = 64
PHP_OUTPUT_HANDLER_STDFLAGS = 112
PHP_OUTPUT_HANDLER_STARTED = 4096
PHP_OUTPUT_HANDLER_DISABLED = 8192
UPLOAD_ERR_OK = 0
UPLOAD_ERR_INI_SIZE = 1
UPLOAD_ERR_FORM_SIZE = 2
UPLOAD_ERR_PARTIAL = 3
UPLOAD_ERR_NO_FILE = 4
UPLOAD_ERR_NO_TMP_DIR = 6
UPLOAD_ERR_CANT_WRITE = 7
UPLOAD_ERR_EXTENSION = 8
PHP_CLI_PROCESS_TITLE = True
SWOOLE_CLI = True
STDIN = None
STDOUT = None
STDERR = None


def zend_version():
    return phpy.call('zend_version', )


def func_num_args():
    return phpy.call('func_num_args', )


def func_get_arg(_position):
    return phpy.call('func_get_arg', _position)


def func_get_args():
    return phpy.call('func_get_args', )


def strlen(_string):
    return phpy.call('strlen', _string)


def strcmp(_string1, _string2):
    return phpy.call('strcmp', _string1, _string2)


def strncmp(_string1, _string2, _length):
    return phpy.call('strncmp', _string1, _string2, _length)


def strcasecmp(_string1, _string2):
    return phpy.call('strcasecmp', _string1, _string2)


def strncasecmp(_string1, _string2, _length):
    return phpy.call('strncasecmp', _string1, _string2, _length)


def error_reporting(_error_level=None):
    return phpy.call('error_reporting', _error_level)


def define(_constant_name, _value, _case_insensitive=False):
    return phpy.call('define', _constant_name, _value, _case_insensitive)


def defined(_constant_name):
    return phpy.call('defined', _constant_name)


def get_class(_object=None):
    return phpy.call('get_class', _object)


def get_called_class():
    return phpy.call('get_called_class', )


def get_parent_class(_object_or_class=None):
    return phpy.call('get_parent_class', _object_or_class)


def is_subclass_of(_object_or_class, _class, _allow_string=True):
    return phpy.call('is_subclass_of', _object_or_class, _class, _allow_string)


def is_a(_object_or_class, _class, _allow_string=False):
    return phpy.call('is_a', _object_or_class, _class, _allow_string)


def get_class_vars(_class):
    return phpy.call('get_class_vars', _class)


def get_object_vars(_object):
    return phpy.call('get_object_vars', _object)


def get_mangled_object_vars(_object):
    return phpy.call('get_mangled_object_vars', _object)


def get_class_methods(_object_or_class):
    return phpy.call('get_class_methods', _object_or_class)


def method_exists(_object_or_class, _method):
    return phpy.call('method_exists', _object_or_class, _method)


def property_exists(_object_or_class, _property):
    return phpy.call('property_exists', _object_or_class, _property)


def class_exists(_class, _autoload=True):
    return phpy.call('class_exists', _class, _autoload)


def interface_exists(_interface, _autoload=True):
    return phpy.call('interface_exists', _interface, _autoload)


def trait_exists(_trait, _autoload=True):
    return phpy.call('trait_exists', _trait, _autoload)


def enum_exists(_enum, _autoload=True):
    return phpy.call('enum_exists', _enum, _autoload)


def function_exists(_function):
    return phpy.call('function_exists', _function)


def class_alias(_class, _alias, _autoload=True):
    return phpy.call('class_alias', _class, _alias, _autoload)


def get_included_files():
    return phpy.call('get_included_files', )


def get_required_files():
    return phpy.call('get_required_files', )


def trigger_error(_message, _error_level=1024):
    return phpy.call('trigger_error', _message, _error_level)


def user_error(_message, _error_level=1024):
    return phpy.call('user_error', _message, _error_level)


def set_error_handler(_callback, _error_levels=32767):
    return phpy.call('set_error_handler', _callback, _error_levels)


def restore_error_handler():
    return phpy.call('restore_error_handler', )


def set_exception_handler(_callback):
    return phpy.call('set_exception_handler', _callback)


def restore_exception_handler():
    return phpy.call('restore_exception_handler', )


def get_declared_classes():
    return phpy.call('get_declared_classes', )


def get_declared_traits():
    return phpy.call('get_declared_traits', )


def get_declared_interfaces():
    return phpy.call('get_declared_interfaces', )


def get_defined_functions(_exclude_disabled=True):
    return phpy.call('get_defined_functions', _exclude_disabled)


def get_defined_vars():
    return phpy.call('get_defined_vars', )


def get_resource_type(_resource):
    return phpy.call('get_resource_type', _resource)


def get_resource_id(_resource):
    return phpy.call('get_resource_id', _resource)


def get_resources(_type=None):
    return phpy.call('get_resources', _type)


def get_loaded_extensions(_zend_extensions=False):
    return phpy.call('get_loaded_extensions', _zend_extensions)


def get_defined_constants(_categorize=False):
    return phpy.call('get_defined_constants', _categorize)


def debug_backtrace(_options=1, _limit=0):
    return phpy.call('debug_backtrace', _options, _limit)


def debug_print_backtrace(_options=0, _limit=0):
    return phpy.call('debug_print_backtrace', _options, _limit)


def extension_loaded(_extension):
    return phpy.call('extension_loaded', _extension)


def get_extension_funcs(_extension):
    return phpy.call('get_extension_funcs', _extension)


def gc_mem_caches():
    return phpy.call('gc_mem_caches', )


def gc_collect_cycles():
    return phpy.call('gc_collect_cycles', )


def gc_enabled():
    return phpy.call('gc_enabled', )


def gc_enable():
    return phpy.call('gc_enable', )


def gc_disable():
    return phpy.call('gc_disable', )


def gc_status():
    return phpy.call('gc_status', )




def IteratorAggregate():

    def getIterator(self):
        return self.__this.call(f"getIterator", )


def Iterator():

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


def Serializable():

    def serialize(self):
        return self.__this.call(f"serialize", )

    def unserialize(self, _data):
        return self.__this.call(f"unserialize", _data)


def ArrayAccess():

    def offsetExists(self, _offset):
        return self.__this.call(f"offsetExists", _offset)

    def offsetGet(self, _offset):
        return self.__this.call(f"offsetGet", _offset)

    def offsetSet(self, _offset, _value):
        return self.__this.call(f"offsetSet", _offset, _value)

    def offsetUnset(self, _offset):
        return self.__this.call(f"offsetUnset", _offset)


def Countable():

    def count(self):
        return self.__this.call(f"count", )


def Stringable():

    def __toString(self):
        return self.__this.call(f"__toString", )


def InternalIterator():

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def valid(self):
        return self.__this.call(f"valid", )

    def rewind(self):
        return self.__this.call(f"rewind", )


def Throwable():

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


def Exception():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Exception', _message, _code, _previous)

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


def ErrorException():

    def __init__(self, _message="", _code=0, _severity=1, _filename=None, _line=None, _previous=None):
        self.__this = phpy.Object(f'ErrorException', _message, _code, _severity, _filename, _line, _previous)

    def getSeverity(self):
        return self.__this.call(f"getSeverity", )

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


def Error():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'Error', _message, _code, _previous)

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


def CompileError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'CompileError', _message, _code, _previous)

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


def ParseError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ParseError', _message, _code, _previous)

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


def TypeError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'TypeError', _message, _code, _previous)

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


def ArgumentCountError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ArgumentCountError', _message, _code, _previous)

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


def ValueError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ValueError', _message, _code, _previous)

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


def ArithmeticError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ArithmeticError', _message, _code, _previous)

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


def DivisionByZeroError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'DivisionByZeroError', _message, _code, _previous)

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


def UnhandledMatchError():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'UnhandledMatchError', _message, _code, _previous)

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


def Closure():

    def bind(_closure, _new_this, _new_scope="static"):
        return phpy.call(f"Closure::bind", _closure, _new_this, _new_scope)

    def bindTo(self, _new_this, _new_scope="static"):
        return self.__this.call(f"bindTo", _new_this, _new_scope)

    def call(self, _new_this, _args=None):
        return self.__this.call(f"call", _new_this, _args)

    def fromCallable(_callback):
        return phpy.call(f"Closure::fromCallable", _callback)

    def __invoke(self):
        return self.__this.call(f"__invoke", )


def Generator():

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def send(self, _value):
        return self.__this.call(f"send", _value)

    def throw(self, _exception):
        return self.__this.call(f"throw", _exception)

    def getReturn(self):
        return self.__this.call(f"getReturn", )


def ClosedGeneratorException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ClosedGeneratorException', _message, _code, _previous)

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


def WeakReference():

    def __init__(self):
        self.__this = phpy.Object(f'WeakReference', )

    def create(_object):
        return phpy.call(f"WeakReference::create", _object)

    def get(self):
        return self.__this.call(f"get", )


def WeakMap():

    def offsetGet(self, _object):
        return self.__this.call(f"offsetGet", _object)

    def offsetSet(self, _object, _value):
        return self.__this.call(f"offsetSet", _object, _value)

    def offsetExists(self, _object):
        return self.__this.call(f"offsetExists", _object)

    def offsetUnset(self, _object):
        return self.__this.call(f"offsetUnset", _object)

    def count(self):
        return self.__this.call(f"count", )

    def getIterator(self):
        return self.__this.call(f"getIterator", )


def Attribute():
    TARGET_CLASS = 1
    TARGET_FUNCTION = 2
    TARGET_METHOD = 4
    TARGET_PROPERTY = 8
    TARGET_CLASS_CONSTANT = 16
    TARGET_PARAMETER = 32
    TARGET_ALL = 63
    IS_REPEATABLE = 64

    def __init__(self, _flags=63):
        self.__this = phpy.Object(f'Attribute', _flags)


def ReturnTypeWillChange():

    def __init__(self):
        self.__this = phpy.Object(f'ReturnTypeWillChange', )


def UnitEnum():

    def cases():
        return phpy.call(f"UnitEnum::cases", )


def BackedEnum():

    def _from(_value):
        return phpy.call(f"BackedEnum::from", _value)

    def tryFrom(_value):
        return phpy.call(f"BackedEnum::tryFrom", _value)

    def cases():
        return phpy.call(f"BackedEnum::cases", )


def Fiber():

    def __init__(self, _callback):
        self.__this = phpy.Object(f'Fiber', _callback)

    def start(self, _args=None):
        return self.__this.call(f"start", _args)

    def resume(self, _value=None):
        return self.__this.call(f"resume", _value)

    def throw(self, _exception):
        return self.__this.call(f"throw", _exception)

    def isStarted(self):
        return self.__this.call(f"isStarted", )

    def isSuspended(self):
        return self.__this.call(f"isSuspended", )

    def isRunning(self):
        return self.__this.call(f"isRunning", )

    def isTerminated(self):
        return self.__this.call(f"isTerminated", )

    def getReturn(self):
        return self.__this.call(f"getReturn", )

    def getCurrent():
        return phpy.call(f"Fiber::getCurrent", )

    def suspend(_value=None):
        return phpy.call(f"Fiber::suspend", _value)


def FiberError():

    def __init__(self):
        self.__this = phpy.Object(f'FiberError', )

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


