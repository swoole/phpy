<?php
namespace python\ast;

/**
*/
class unaryop
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->unaryop();
    }

}
