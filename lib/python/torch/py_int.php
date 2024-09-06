<?php
namespace python\torch;

/**
*/
class py_int
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->py_int();
    }

}
