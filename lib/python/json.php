<?php
namespace python;

use \PyModule;
use \PyCore;

/**
JSON (JavaScript Object Notation) <https://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import json
    >>> mydict = {'4': 5, '6': 7}
    >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import json
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import json
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> json.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using json.tool from the shell to validate and pretty-print::

    $ echo '{"json":"obj"}' | python -m json.tool
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json.tool
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
*/
class json{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('json');
            self::$JSONDecodeError = self::$__module->JSONDecodeError;
            self::$JSONDecoder = self::$__module->JSONDecoder;
            self::$JSONEncoder = self::$__module->JSONEncoder;
            self::$__path__ = self::$__module->__path__;
            self::$_default_decoder = self::$__module->_default_decoder;
            self::$_default_encoder = self::$__module->_default_encoder;
            self::$codecs = self::$__module->codecs;
            self::$decoder = self::$__module->decoder;
            self::$encoder = self::$__module->encoder;
            self::$scanner = self::$__module->scanner;
        }
    }


    public static $__author__ = "Bob Ippolito <bob@redivi.com>";
    public static $__name__ = "json";
    public static $__package__ = "json";
    public static $__version__ = "2.0.9";

    public static $JSONDecodeError = null;
    public static $JSONDecoder = null;
    public static $JSONEncoder = null;
    public static $__path__ = null;
    public static $_default_decoder = null;
    public static $_default_encoder = null;
    public static $codecs = null;
    public static $decoder = null;
    public static $encoder = null;
    public static $scanner = null;

    public static function detect_encoding($b)
    {
        return self::$__module->detect_encoding($b);
    }
    public static function dump($obj, $fp)
    {
        return self::$__module->dump($obj, $fp);
    }
    public static function dumps($obj)
    {
        return self::$__module->dumps($obj);
    }
    public static function load($fp)
    {
        return self::$__module->load($fp);
    }
    public static function loads($s)
    {
        return self::$__module->loads($s);
    }
}

json::__init();
