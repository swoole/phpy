<?php
namespace python\subprocess;

/**
*/
class SubprocessError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('subprocess')->SubprocessError();
    }

}
