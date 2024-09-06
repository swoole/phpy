<?php
namespace python\subprocess;

/**
*/
class CompletedProcess
{
    private $_self;

    public function __construct($args, $returncode, $stdout = null, $stderr = null)
    {
        $this->_self = \PyCore::import('subprocess')->CompletedProcess($args, $returncode, $stdout, $stderr);
    }

    public function check_returncode()
    {
        return $this->_self->check_returncode();
    }

}
