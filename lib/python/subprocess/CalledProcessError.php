<?php
namespace python\subprocess;

/**
* @property $stdout
*/
class CalledProcessError
{
    private $_self;

    public function __construct($returncode, $cmd, $output = null, $stderr = null)
    {
        $this->_self = \PyCore::import('subprocess')->CalledProcessError($returncode, $cmd, $output, $stderr);
    }

}
