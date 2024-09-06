<?php
namespace python;

/**
UUID objects (universally unique identifiers) according to RFC 4122.

This module provides immutable UUID objects (class UUID) and the functions
uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
UUIDs as specified in RFC 4122.

If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.

Typical usage:

    >>> import uuid

    # make a UUID based on the host ID and current time
    >>> uuid.uuid1()    # doctest: +SKIP
    UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

    # make a UUID using an MD5 hash of a namespace UUID and a name
    >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

    # make a random UUID
    >>> uuid.uuid4()    # doctest: +SKIP
    UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

    # make a UUID using a SHA-1 hash of a namespace UUID and a name
    >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

    # make a UUID from a string of hex digits (braces and hyphens ignored)
    >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

    # convert a UUID to a string of hex digits in standard form
    >>> str(x)
    '00010203-0405-0607-0809-0a0b0c0d0e0f'

    # get the raw 16 bytes of the UUID
    >>> x.bytes
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    # make a UUID from a 16-byte string
    >>> uuid.UUID(bytes=x.bytes)
    UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')
*/
class uuid
{
    /**
    * @return uuid
    */
    public static function import()
    {
        return \PyCore::import('uuid');
    }

    public $_has_uuid_generate_time_safe = 1;

    public $RESERVED_FUTURE = "reserved for future definition";
    public $RESERVED_MICROSOFT = "reserved for Microsoft compatibility";
    public $RESERVED_NCS = "reserved for NCS compatibility";
    public $RFC_4122 = "specified in RFC 4122";
    public $_AIX = false;
    public $_LINUX = true;
    public $_MAC_OMITS_LEADING_ZEROES = false;
    public $_UuidCreate = null;
    public $__author__ = "Ka-Ping Yee <ping@zesty.ca>";
    public $__name__ = "uuid";
    public $__package__ = "";
    public $_last_timestamp = null;
    public $_node = null;
    public $_platform_system = "Linux";

    public $Enum = null;
    public $NAMESPACE_DNS = null;
    public $NAMESPACE_OID = null;
    public $NAMESPACE_URL = null;
    public $NAMESPACE_X500 = null;
    public $SafeUUID = null;
    public $_GETTERS = null;
    public $_MAC_DELIM = null;
    public $_OS_GETTERS = null;
    public $_uuid = null;
    public $os = null;
    public $platform = null;
    public $sys = null;

    /**
    * @return mixed
    */
    public function _arp_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _find_mac_near_keyword($command, $args, $keywords, $get_word_index)
    {
    }

    /**
    * @return mixed
    */
    public function _find_mac_under_heading($command, $args, $heading)
    {
    }

    /**
    * @return mixed
    */
    public function _get_command_stdout($command)
    {
    }

    /**
    * @return mixed
    */
    public function _ifconfig_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _ip_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _ipconfig_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _is_universal($mac)
    {
    }

    /**
    * @return mixed
    */
    public function _lanscan_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _load_system_functions()
    {
    }

    /**
    * @return mixed
    */
    public function _netbios_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _netstat_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _parse_mac($word)
    {
    }

    /**
    * @return mixed
    */
    public function _random_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _unix_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function _windll_getnode()
    {
    }

    /**
    * @return mixed
    */
    public function getnode()
    {
    }

    /**
    * @return mixed
    */
    public function uuid1($node = null, $clock_seq = null)
    {
    }

    /**
    * @return mixed
    */
    public function uuid3($namespace, $name)
    {
    }

    /**
    * @return mixed
    */
    public function uuid4()
    {
    }

    /**
    * @return mixed
    */
    public function uuid5($namespace, $name)
    {
    }

}
