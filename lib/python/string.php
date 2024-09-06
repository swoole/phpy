<?php
namespace python;

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
class string
{
    /**
    * @return string
    */
    public static function import()
    {
        return \PyCore::import('string');
    }


    public $__name__ = "string";
    public $__package__ = "";
    public $ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public $ascii_lowercase = "abcdefghijklmnopqrstuvwxyz";
    public $ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public $digits = "0123456789";
    public $hexdigits = "0123456789abcdefABCDEF";
    public $octdigits = "01234567";
    public $printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\v";
    public $punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
    public $whitespace = " \t\n\r\v";

    public $_ChainMap = null;
    public $_re = null;
    public $_sentinel_dict = null;
    public $_string = null;

    /**
    * @return mixed
    */
    public function capwords($s, $sep = null)
    {
    }

}
