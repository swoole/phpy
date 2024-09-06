<?php
namespace python;

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
class pickle
{
    /**
    * @return pickle
    */
    public static function import()
    {
        return \PyCore::import('pickle');
    }

    public $DEFAULT_PROTOCOL = 4;
    public $HIGHEST_PROTOCOL = 5;
    public $maxsize = 9223372036854775807;

    public $PyStringMap = null;
    public $_HAVE_PICKLE_BUFFER = true;
    public $__name__ = "pickle";
    public $__package__ = "";
    public $format_version = "4.0";

    public $ADDITEMS = null;
    public $APPEND = null;
    public $APPENDS = null;
    public $BINBYTES = null;
    public $BINBYTES8 = null;
    public $BINFLOAT = null;
    public $BINGET = null;
    public $BININT = null;
    public $BININT1 = null;
    public $BININT2 = null;
    public $BINPERSID = null;
    public $BINPUT = null;
    public $BINSTRING = null;
    public $BINUNICODE = null;
    public $BINUNICODE8 = null;
    public $BUILD = null;
    public $BYTEARRAY8 = null;
    public $DICT = null;
    public $DUP = null;
    public $EMPTY_DICT = null;
    public $EMPTY_LIST = null;
    public $EMPTY_SET = null;
    public $EMPTY_TUPLE = null;
    public $EXT1 = null;
    public $EXT2 = null;
    public $EXT4 = null;
    public $FALSE = null;
    public $FLOAT = null;
    public $FRAME = null;
    public $FROZENSET = null;
    public $GET = null;
    public $GLOBAL = null;
    public $INST = null;
    public $INT = null;
    public $LIST = null;
    public $LONG = null;
    public $LONG1 = null;
    public $LONG4 = null;
    public $LONG_BINGET = null;
    public $LONG_BINPUT = null;
    public $MARK = null;
    public $MEMOIZE = null;
    public $NEWFALSE = null;
    public $NEWOBJ = null;
    public $NEWOBJ_EX = null;
    public $NEWTRUE = null;
    public $NEXT_BUFFER = null;
    public $NONE = null;
    public $OBJ = null;
    public $PERSID = null;
    public $POP = null;
    public $POP_MARK = null;
    public $PROTO = null;
    public $PUT = null;
    public $READONLY_BUFFER = null;
    public $REDUCE = null;
    public $SETITEM = null;
    public $SETITEMS = null;
    public $SHORT_BINBYTES = null;
    public $SHORT_BINSTRING = null;
    public $SHORT_BINUNICODE = null;
    public $STACK_GLOBAL = null;
    public $STOP = null;
    public $STRING = null;
    public $TRUE = null;
    public $TUPLE = null;
    public $TUPLE1 = null;
    public $TUPLE2 = null;
    public $TUPLE3 = null;
    public $UNICODE = null;
    public $_compat_pickle = null;
    public $_extension_cache = null;
    public $_extension_registry = null;
    public $_inverted_registry = null;
    public $_tuplesize2code = null;
    public $bytes_types = null;
    public $codecs = null;
    public $compatible_formats = null;
    public $dispatch_table = null;
    public $io = null;
    public $re = null;
    public $sys = null;

    /**
    * @return mixed
    */
    public function _dump($obj, $file, $protocol = null)
    {
    }

    /**
    * @return mixed
    */
    public function _dumps($obj, $protocol = null)
    {
    }

    /**
    * @return mixed
    */
    public function _getattribute($obj, $name)
    {
    }

    /**
    * @return mixed
    */
    public function _load($file)
    {
    }

    /**
    * @return mixed
    */
    public function _loads($s)
    {
    }

    /**
    * @return mixed
    */
    public function _test()
    {
    }

    /**
    * @return mixed
    */
    public function decode_long($data)
    {
    }

    /**
    * @return mixed
    */
    public function dump($obj, $file, $protocol = null)
    {
    }

    /**
    * @return mixed
    */
    public function dumps($obj, $protocol = null)
    {
    }

    /**
    * @return mixed
    */
    public function encode_long($x)
    {
    }

    /**
    * @return mixed
    */
    public function load($file)
    {
    }

    /**
    * @return mixed
    */
    public function loads($data)
    {
    }

    /**
    * @return mixed
    */
    public function unpack($format, $buffer)
    {
    }

    /**
    * @return mixed
    */
    public function whichmodule($obj, $name)
    {
    }

}
