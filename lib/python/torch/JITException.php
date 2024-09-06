<?php
namespace python\torch;

/**
*/
class JITException
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->JITException();
    }

}
