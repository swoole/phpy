<?php
namespace python;

use \PyModule;
use \PyCore;

/**
A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

*/
class string{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('string');
            self::$Formatter = self::$__module->Formatter;
            self::$Template = self::$__module->Template;
            self::$_ChainMap = self::$__module->_ChainMap;
            self::$_re = self::$__module->_re;
            self::$_sentinel_dict = self::$__module->_sentinel_dict;
            self::$_string = self::$__module->_string;
        }
    }


    public static $__name__ = "string";
    public static $__package__ = "";
    public static $ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static $ascii_lowercase = "abcdefghijklmnopqrstuvwxyz";
    public static $ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static $digits = "0123456789";
    public static $hexdigits = "0123456789abcdefABCDEF";
    public static $octdigits = "01234567";
    public static $printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	\n";
    public static $punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~";
    public static $whitespace = " 	\n";

    public static $Formatter = null;
    public static $Template = null;
    public static $_ChainMap = null;
    public static $_re = null;
    public static $_sentinel_dict = null;
    public static $_string = null;

    public static function capwords($s, $sep=null)
    {
        return self::$__module->capwords($s, $sep);
    }
}

string::__init();
