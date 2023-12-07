<?php
namespace python;

use \PyModule;
use \PyCore;

/**
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
*/
class sys{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('sys');
            self::$__spec__ = self::$__module->__spec__;
            self::$__stderr__ = self::$__module->__stderr__;
            self::$__stdin__ = self::$__module->__stdin__;
            self::$__stdout__ = self::$__module->__stdout__;
            self::$_git = self::$__module->_git;
            self::$_xoptions = self::$__module->_xoptions;
            self::$argv = self::$__module->argv;
            self::$builtin_module_names = self::$__module->builtin_module_names;
            self::$flags = self::$__module->flags;
            self::$float_info = self::$__module->float_info;
            self::$hash_info = self::$__module->hash_info;
            self::$implementation = self::$__module->implementation;
            self::$int_info = self::$__module->int_info;
            self::$meta_path = self::$__module->meta_path;
            self::$modules = self::$__module->modules;
            self::$orig_argv = self::$__module->orig_argv;
            self::$path = self::$__module->path;
            self::$path_hooks = self::$__module->path_hooks;
            self::$path_importer_cache = self::$__module->path_importer_cache;
            self::$stderr = self::$__module->stderr;
            self::$stdin = self::$__module->stdin;
            self::$stdlib_module_names = self::$__module->stdlib_module_names;
            self::$stdout = self::$__module->stdout;
            self::$thread_info = self::$__module->thread_info;
            self::$version_info = self::$__module->version_info;
            self::$warnoptions = self::$__module->warnoptions;
        }
    }

    public const api_version = 1013;
    public const hexversion = 51054064;
    public const maxsize = 9223372036854775807;
    public const maxunicode = 1114111;

    public static $__name__ = "sys";
    public static $__package__ = "";
    public static $_base_executable = "/opt/anaconda3/bin/python3";
    public static $_framework = "";
    public static $_home = null;
    public static $_stdlib_dir = "/opt/anaconda3/lib/python3.11";
    public static $abiflags = "";
    public static $base_exec_prefix = "/opt/anaconda3";
    public static $base_prefix = "/opt/anaconda3";
    public static $byteorder = "little";
    public static $copyright = "Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.";
    public static $dont_write_bytecode = false;
    public static $exec_prefix = "/opt/anaconda3";
    public static $executable = "/opt/anaconda3/bin/python3";
    public static $float_repr_style = "short";
    public static $platform = "linux";
    public static $platlibdir = "lib";
    public static $prefix = "/opt/anaconda3";
    public static $pycache_prefix = null;
    public static $version = "3.11.5 (main, Sep 11 2023, 14:07:11) [GCC 11.2.0]";

    public static $__spec__ = null;
    public static $__stderr__ = null;
    public static $__stdin__ = null;
    public static $__stdout__ = null;
    public static $_git = null;
    public static $_xoptions = null;
    public static $argv = null;
    public static $builtin_module_names = null;
    public static $flags = null;
    public static $float_info = null;
    public static $hash_info = null;
    public static $implementation = null;
    public static $int_info = null;
    public static $meta_path = null;
    public static $modules = null;
    public static $orig_argv = null;
    public static $path = null;
    public static $path_hooks = null;
    public static $path_importer_cache = null;
    public static $stderr = null;
    public static $stdin = null;
    public static $stdlib_module_names = null;
    public static $stdout = null;
    public static $thread_info = null;
    public static $version_info = null;
    public static $warnoptions = null;

    public static function __displayhook__($object)
    {
        return self::$__module->__displayhook__($object);
    }
    public static function __excepthook__($exctype, $value, $traceback)
    {
        return self::$__module->__excepthook__($exctype, $value, $traceback);
    }
    public static function __interactivehook__()
    {
        return self::$__module->__interactivehook__();
    }
    public static function __unraisablehook__($unraisable)
    {
        return self::$__module->__unraisablehook__($unraisable);
    }
    public static function _clear_type_cache()
    {
        return self::$__module->_clear_type_cache();
    }
    public static function _current_exceptions()
    {
        return self::$__module->_current_exceptions();
    }
    public static function _current_frames()
    {
        return self::$__module->_current_frames();
    }
    public static function _debugmallocstats()
    {
        return self::$__module->_debugmallocstats();
    }
    public static function _getframe($depth=0)
    {
        return self::$__module->_getframe($depth);
    }
    public static function _getquickenedcount()
    {
        return self::$__module->_getquickenedcount();
    }
    public static function addaudithook($hook)
    {
        return self::$__module->addaudithook($hook);
    }
    public static function call_tracing($func, $args)
    {
        return self::$__module->call_tracing($func, $args);
    }
    public static function displayhook($object)
    {
        return self::$__module->displayhook($object);
    }
    public static function exc_info()
    {
        return self::$__module->exc_info();
    }
    public static function excepthook($exctype, $value, $traceback)
    {
        return self::$__module->excepthook($exctype, $value, $traceback);
    }
    public static function exception()
    {
        return self::$__module->exception();
    }
    public static function exit($status=null)
    {
        return self::$__module->exit($status);
    }
    public static function get_asyncgen_hooks()
    {
        return self::$__module->get_asyncgen_hooks();
    }
    public static function get_coroutine_origin_tracking_depth()
    {
        return self::$__module->get_coroutine_origin_tracking_depth();
    }
    public static function get_int_max_str_digits()
    {
        return self::$__module->get_int_max_str_digits();
    }
    public static function getallocatedblocks()
    {
        return self::$__module->getallocatedblocks();
    }
    public static function getdefaultencoding()
    {
        return self::$__module->getdefaultencoding();
    }
    public static function getdlopenflags()
    {
        return self::$__module->getdlopenflags();
    }
    public static function getfilesystemencodeerrors()
    {
        return self::$__module->getfilesystemencodeerrors();
    }
    public static function getfilesystemencoding()
    {
        return self::$__module->getfilesystemencoding();
    }
    public static function getprofile()
    {
        return self::$__module->getprofile();
    }
    public static function getrecursionlimit()
    {
        return self::$__module->getrecursionlimit();
    }
    public static function getrefcount($object)
    {
        return self::$__module->getrefcount($object);
    }
    public static function getswitchinterval()
    {
        return self::$__module->getswitchinterval();
    }
    public static function gettrace()
    {
        return self::$__module->gettrace();
    }
    public static function intern($string)
    {
        return self::$__module->intern($string);
    }
    public static function is_finalizing()
    {
        return self::$__module->is_finalizing();
    }
    public static function set_coroutine_origin_tracking_depth($depth)
    {
        return self::$__module->set_coroutine_origin_tracking_depth($depth);
    }
    public static function set_int_max_str_digits($maxdigits)
    {
        return self::$__module->set_int_max_str_digits($maxdigits);
    }
    public static function setdlopenflags($flags)
    {
        return self::$__module->setdlopenflags($flags);
    }
    public static function setrecursionlimit($limit)
    {
        return self::$__module->setrecursionlimit($limit);
    }
    public static function setswitchinterval($interval)
    {
        return self::$__module->setswitchinterval($interval);
    }
    public static function unraisablehook($unraisable)
    {
        return self::$__module->unraisablehook($unraisable);
    }
}

sys::__init();
