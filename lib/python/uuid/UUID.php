<?php
namespace python\uuid;

/**
* @property $bytes
* @property $bytes_le
* @property $clock_seq
* @property $clock_seq_hi_variant
* @property $clock_seq_low
* @property $fields
* @property $hex
* @property $node
* @property $time
* @property $time_hi_version
* @property $time_low
* @property $time_mid
* @property $urn
* @property $variant
* @property $version
*/
class UUID
{
    private $_self;

    public function __construct($hex = null, $bytes = null, $bytes_le = null, $fields = null, $int = null, $version = null)
    {
        $this->_self = \PyCore::import('uuid')->UUID($hex, $bytes, $bytes_le, $fields, $int, $version);
    }

}
