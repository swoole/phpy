<?php
namespace python\pickle;

/**
*/
class FunctionType
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->FunctionType();
    }

}
