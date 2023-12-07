<?php
namespace python;

use \PyModule;
use \PyCore;

/**
Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(bytes) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

*/
class pickle{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('pickle');
            self::$FunctionType = self::$__module->FunctionType;
            self::$PickleBuffer = self::$__module->PickleBuffer;
            self::$PickleError = self::$__module->PickleError;
            self::$Pickler = self::$__module->Pickler;
            self::$PicklingError = self::$__module->PicklingError;
            self::$Unpickler = self::$__module->Unpickler;
            self::$UnpicklingError = self::$__module->UnpicklingError;
            self::$_Framer = self::$__module->_Framer;
            self::$_Pickler = self::$__module->_Pickler;
            self::$_Stop = self::$__module->_Stop;
            self::$_Unframer = self::$__module->_Unframer;
            self::$_Unpickler = self::$__module->_Unpickler;
            self::$__spec__ = self::$__module->__spec__;
            self::$_compat_pickle = self::$__module->_compat_pickle;
            self::$_extension_cache = self::$__module->_extension_cache;
            self::$_extension_registry = self::$__module->_extension_registry;
            self::$_inverted_registry = self::$__module->_inverted_registry;
            self::$_tuplesize2code = self::$__module->_tuplesize2code;
            self::$bytes_types = self::$__module->bytes_types;
            self::$codecs = self::$__module->codecs;
            self::$compatible_formats = self::$__module->compatible_formats;
            self::$dispatch_table = self::$__module->dispatch_table;
            self::$io = self::$__module->io;
            self::$islice = self::$__module->islice;
            self::$partial = self::$__module->partial;
            self::$re = self::$__module->re;
            self::$sys = self::$__module->sys;
        }
    }

    public const DEFAULT_PROTOCOL = 4;
    public const DUP = 2;
    public const HIGHEST_PROTOCOL = 5;
    public const POP = 0;
    public const POP_MARK = 1;
    public const maxsize = 9223372036854775807;

    public static $ADDITEMS = "";
    public static $APPEND = "a";
    public static $APPENDS = "e";
    public static $BINBYTES = "B";
    public static $BINBYTES8 = "Ž";
    public static $BINFLOAT = "G";
    public static $BINGET = "h";
    public static $BININT = "J";
    public static $BININT1 = "K";
    public static $BININT2 = "M";
    public static $BINPERSID = "Q";
    public static $BINPUT = "q";
    public static $BINSTRING = "T";
    public static $BINUNICODE = "X";
    public static $BINUNICODE8 = "";
    public static $BUILD = "b";
    public static $BYTEARRAY8 = "–";
    public static $DICT = "d";
    public static $EMPTY_DICT = "}";
    public static $EMPTY_LIST = "]";
    public static $EMPTY_SET = "";
    public static $EMPTY_TUPLE = ")";
    public static $EXT1 = "‚";
    public static $EXT2 = "ƒ";
    public static $EXT4 = "„";
    public static $FALSE = "I00\n";
    public static $FLOAT = "F";
    public static $FRAME = "•";
    public static $FROZENSET = "‘";
    public static $GET = "g";
    public static $GLOBAL = "c";
    public static $INST = "i";
    public static $INT = "I";
    public static $LIST = "l";
    public static $LONG = "L";
    public static $LONG1 = "Š";
    public static $LONG4 = "‹";
    public static $LONG_BINGET = "j";
    public static $LONG_BINPUT = "r";
    public static $MARK = "(";
    public static $MEMOIZE = "”";
    public static $NEWFALSE = "‰";
    public static $NEWOBJ = "";
    public static $NEWOBJ_EX = "’";
    public static $NEWTRUE = "ˆ";
    public static $NEXT_BUFFER = "—";
    public static $NONE = "N";
    public static $OBJ = "o";
    public static $PERSID = "P";
    public static $PROTO = "€";
    public static $PUT = "p";
    public static $PyStringMap = null;
    public static $READONLY_BUFFER = "˜";
    public static $REDUCE = "R";
    public static $SETITEM = "s";
    public static $SETITEMS = "u";
    public static $SHORT_BINBYTES = "C";
    public static $SHORT_BINSTRING = "U";
    public static $SHORT_BINUNICODE = "Œ";
    public static $STACK_GLOBAL = "“";
    public static $STOP = ".";
    public static $STRING = "S";
    public static $TRUE = "I01\n";
    public static $TUPLE = "t";
    public static $TUPLE1 = "…";
    public static $TUPLE2 = "†";
    public static $TUPLE3 = "‡";
    public static $UNICODE = "V";
    public static $_HAVE_PICKLE_BUFFER = true;
    public static $__cached__ = "/opt/anaconda3/lib/python3.11/__pycache__/pickle.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/pickle.py";
    public static $__name__ = "pickle";
    public static $__package__ = "";
    public static $format_version = "4.0";

    public static $FunctionType = null;
    public static $PickleBuffer = null;
    public static $PickleError = null;
    public static $Pickler = null;
    public static $PicklingError = null;
    public static $Unpickler = null;
    public static $UnpicklingError = null;
    public static $_Framer = null;
    public static $_Pickler = null;
    public static $_Stop = null;
    public static $_Unframer = null;
    public static $_Unpickler = null;
    public static $__spec__ = null;
    public static $_compat_pickle = null;
    public static $_extension_cache = null;
    public static $_extension_registry = null;
    public static $_inverted_registry = null;
    public static $_tuplesize2code = null;
    public static $bytes_types = null;
    public static $codecs = null;
    public static $compatible_formats = null;
    public static $dispatch_table = null;
    public static $io = null;
    public static $islice = null;
    public static $partial = null;
    public static $re = null;
    public static $sys = null;

    public static function _dump($obj, $file, $protocol=null)
    {
        return self::$__module->_dump($obj, $file, $protocol);
    }
    public static function _dumps($obj, $protocol=null)
    {
        return self::$__module->_dumps($obj, $protocol);
    }
    public static function _getattribute($obj, $name)
    {
        return self::$__module->_getattribute($obj, $name);
    }
    public static function _load($file)
    {
        return self::$__module->_load($file);
    }
    public static function _loads($s)
    {
        return self::$__module->_loads($s);
    }
    public static function _test()
    {
        return self::$__module->_test();
    }
    public static function decode_long($data)
    {
        return self::$__module->decode_long($data);
    }
    public static function dump($obj, $file, $protocol=null)
    {
        return self::$__module->dump($obj, $file, $protocol);
    }
    public static function dumps($obj, $protocol=null)
    {
        return self::$__module->dumps($obj, $protocol);
    }
    public static function encode_long($x)
    {
        return self::$__module->encode_long($x);
    }
    public static function load($file)
    {
        return self::$__module->load($file);
    }
    public static function loads($data)
    {
        return self::$__module->loads($data);
    }
    public static function unpack($format, $buffer)
    {
        return self::$__module->unpack($format, $buffer);
    }
    public static function whichmodule($obj, $name)
    {
        return self::$__module->whichmodule($obj, $name);
    }
}

pickle::__init();
