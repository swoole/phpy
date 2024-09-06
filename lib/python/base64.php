<?php
namespace python;

/**
Base16, Base32, Base64 (RFC 3548), Base85 and Ascii85 data encodings*/
class base64
{
    /**
    * @return base64
    */
    public static function import()
    {
        return \PyCore::import('base64');
    }

    public $MAXBINSIZE = 57;
    public $MAXLINESIZE = 76;

    public $_B32_DECODE_DOCSTRING = "\nDecode the {encoding} encoded bytes-like object or ASCII string s.\n\nOptional casefold is a flag specifying whether a lowercase alphabet is\nacceptable as input.  For security purposes, the default is False.\n{extra_args}\nThe result is returned as a bytes object.  A binascii.Error is raised if\nthe input is incorrectly padded or if there are non-alphabet\ncharacters present in the input.\n";
    public $_B32_DECODE_MAP01_DOCSTRING = "\nRFC 3548 allows for optional mapping of the digit 0 (zero) to the\nletter O (oh), and for optional mapping of the digit 1 (one) to\neither the letter I (eye) or letter L (el).  The optional argument\nmap01 when not None, specifies which letter the digit 1 should be\nmapped to (when map01 is not None, the digit 0 is always mapped to\nthe letter O).  For security purposes the default is None, so that\n0 and 1 are not allowed in the input.\n";
    public $_B32_ENCODE_DOCSTRING = "\nEncode the bytes-like objects using {encoding} and return a bytes object.\n";
    public $__name__ = "base64";
    public $__package__ = "";
    public $_a85chars = null;
    public $_a85chars2 = null;
    public $_b85chars = null;
    public $_b85chars2 = null;
    public $_b85dec = null;

    public $_A85END = null;
    public $_A85START = null;
    public $_b32alphabet = null;
    public $_b32hexalphabet = null;
    public $_b32rev = null;
    public $_b32tab2 = null;
    public $_b85alphabet = null;
    public $_urlsafe_decode_translation = null;
    public $_urlsafe_encode_translation = null;
    public $binascii = null;
    public $bytes_types = null;
    public $re = null;
    public $struct = null;

    /**
    * @return mixed
    */
    public function _85encode($b, $chars, $chars2, $pad = false, $foldnuls = false, $foldspaces = false)
    {
    }

    /**
    * @return mixed
    */
    public function _b32decode($alphabet, $s, $casefold = false, $map01 = null)
    {
    }

    /**
    * @return mixed
    */
    public function _b32encode($alphabet, $s)
    {
    }

    /**
    * @return mixed
    */
    public function _bytes_from_decode_data($s)
    {
    }

    /**
    * @return mixed
    */
    public function _input_type_check($s)
    {
    }

    /**
    * @return mixed
    */
    public function a85decode($b)
    {
    }

    /**
    * @return mixed
    */
    public function a85encode($b)
    {
    }

    /**
    * @return mixed
    */
    public function b16decode($s, $casefold = false)
    {
    }

    /**
    * @return mixed
    */
    public function b16encode($s)
    {
    }

    /**
    * @return mixed
    */
    public function b32decode($s, $casefold = false, $map01 = null)
    {
    }

    /**
    * @return mixed
    */
    public function b32encode($s)
    {
    }

    /**
    * @return mixed
    */
    public function b32hexdecode($s, $casefold = false)
    {
    }

    /**
    * @return mixed
    */
    public function b32hexencode($s)
    {
    }

    /**
    * @return mixed
    */
    public function b64decode($s, $altchars = null, $validate = false)
    {
    }

    /**
    * @return mixed
    */
    public function b64encode($s, $altchars = null)
    {
    }

    /**
    * @return mixed
    */
    public function b85decode($b)
    {
    }

    /**
    * @return mixed
    */
    public function b85encode($b, $pad = false)
    {
    }

    /**
    * @return mixed
    */
    public function decode($input, $output)
    {
    }

    /**
    * @return mixed
    */
    public function decodebytes($s)
    {
    }

    /**
    * @return mixed
    */
    public function encode($input, $output)
    {
    }

    /**
    * @return mixed
    */
    public function encodebytes($s)
    {
    }

    /**
    * @return mixed
    */
    public function main()
    {
    }

    /**
    * @return mixed
    */
    public function standard_b64decode($s)
    {
    }

    /**
    * @return mixed
    */
    public function standard_b64encode($s)
    {
    }

    /**
    * @return mixed
    */
    public function test()
    {
    }

    /**
    * @return mixed
    */
    public function urlsafe_b64decode($s)
    {
    }

    /**
    * @return mixed
    */
    public function urlsafe_b64encode($s)
    {
    }

}
