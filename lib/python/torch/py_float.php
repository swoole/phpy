<?php
namespace python\torch;

/**
*/
class py_float
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->py_float();
    }

}
