<?php
namespace python\ast;

/**
*/
class FunctionType
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->FunctionType();
    }

}
