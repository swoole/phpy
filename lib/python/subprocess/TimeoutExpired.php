<?php
namespace python\subprocess;

/**
* @property $stdout
*/
class TimeoutExpired
{
    private $_self;

    public function __construct($cmd, $timeout, $output = null, $stderr = null)
    {
        $this->_self = \PyCore::import('subprocess')->TimeoutExpired($cmd, $timeout, $output, $stderr);
    }

}
