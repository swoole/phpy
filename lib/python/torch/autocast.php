<?php
namespace python\torch;

/**
*/
class autocast
{
    private $_self;

    public function __construct($device_type, $dtype = null, $enabled = true, $cache_enabled = null)
    {
        $this->_self = \PyCore::import('torch')->autocast($device_type, $dtype, $enabled, $cache_enabled);
    }

}
