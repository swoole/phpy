<?php
namespace python;

use \PyModule;
use \PyCore;

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
class uuid{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('uuid');
            self::$Enum = self::$__module->Enum;
            self::$NAMESPACE_DNS = self::$__module->NAMESPACE_DNS;
            self::$NAMESPACE_OID = self::$__module->NAMESPACE_OID;
            self::$NAMESPACE_URL = self::$__module->NAMESPACE_URL;
            self::$NAMESPACE_X500 = self::$__module->NAMESPACE_X500;
            self::$SafeUUID = self::$__module->SafeUUID;
            self::$UUID = self::$__module->UUID;
            self::$_GETTERS = self::$__module->_GETTERS;
            self::$_OS_GETTERS = self::$__module->_OS_GETTERS;
            self::$__spec__ = self::$__module->__spec__;
            self::$_uuid = self::$__module->_uuid;
            self::$bytes_ = self::$__module->bytes_;
            self::$int_ = self::$__module->int_;
            self::$os = self::$__module->os;
            self::$platform = self::$__module->platform;
            self::$sys = self::$__module->sys;
        }
    }

    public const _has_uuid_generate_time_safe = 1;

    public static $RESERVED_FUTURE = "reserved for future definition";
    public static $RESERVED_MICROSOFT = "reserved for Microsoft compatibility";
    public static $RESERVED_NCS = "reserved for NCS compatibility";
    public static $RFC_4122 = "specified in RFC 4122";
    public static $_AIX = false;
    public static $_LINUX = true;
    public static $_MAC_DELIM = ":";
    public static $_MAC_OMITS_LEADING_ZEROES = false;
    public static $_UuidCreate = null;
    public static $__author__ = "Ka-Ping Yee <ping@zesty.ca>";
    public static $__cached__ = "/opt/anaconda3/lib/python3.11/__pycache__/uuid.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/uuid.py";
    public static $__name__ = "uuid";
    public static $__package__ = "";
    public static $_last_timestamp = null;
    public static $_node = null;
    public static $_platform_system = "Linux";

    public static $Enum = null;
    public static $NAMESPACE_DNS = null;
    public static $NAMESPACE_OID = null;
    public static $NAMESPACE_URL = null;
    public static $NAMESPACE_X500 = null;
    public static $SafeUUID = null;
    public static $UUID = null;
    public static $_GETTERS = null;
    public static $_OS_GETTERS = null;
    public static $__spec__ = null;
    public static $_uuid = null;
    public static $bytes_ = null;
    public static $int_ = null;
    public static $os = null;
    public static $platform = null;
    public static $sys = null;

    public static function _arp_getnode()
    {
        return self::$__module->_arp_getnode();
    }
    public static function _find_mac_near_keyword($command, $args, $keywords, $get_word_index)
    {
        return self::$__module->_find_mac_near_keyword($command, $args, $keywords, $get_word_index);
    }
    public static function _find_mac_under_heading($command, $args, $heading)
    {
        return self::$__module->_find_mac_under_heading($command, $args, $heading);
    }
    public static function _get_command_stdout($command)
    {
        return self::$__module->_get_command_stdout($command);
    }
    public static function _ifconfig_getnode()
    {
        return self::$__module->_ifconfig_getnode();
    }
    public static function _ip_getnode()
    {
        return self::$__module->_ip_getnode();
    }
    public static function _ipconfig_getnode()
    {
        return self::$__module->_ipconfig_getnode();
    }
    public static function _is_universal($mac)
    {
        return self::$__module->_is_universal($mac);
    }
    public static function _lanscan_getnode()
    {
        return self::$__module->_lanscan_getnode();
    }
    public static function _load_system_functions()
    {
        return self::$__module->_load_system_functions();
    }
    public static function _netbios_getnode()
    {
        return self::$__module->_netbios_getnode();
    }
    public static function _netstat_getnode()
    {
        return self::$__module->_netstat_getnode();
    }
    public static function _parse_mac($word)
    {
        return self::$__module->_parse_mac($word);
    }
    public static function _random_getnode()
    {
        return self::$__module->_random_getnode();
    }
    public static function _simple_enum($etype=array (
))
    {
        return self::$__module->_simple_enum($etype);
    }
    public static function _unix_getnode()
    {
        return self::$__module->_unix_getnode();
    }
    public static function _windll_getnode()
    {
        return self::$__module->_windll_getnode();
    }
    public static function getnode()
    {
        return self::$__module->getnode();
    }
    public static function uuid1($node=null, $clock_seq=null)
    {
        return self::$__module->uuid1($node, $clock_seq);
    }
    public static function uuid3($namespace, $name)
    {
        return self::$__module->uuid3($namespace, $name);
    }
    public static function uuid4()
    {
        return self::$__module->uuid4();
    }
    public static function uuid5($namespace, $name)
    {
        return self::$__module->uuid5($namespace, $name);
    }
}

uuid::__init();
