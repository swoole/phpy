<?php
namespace python\ast;

/**
*/
class UnaryOp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->UnaryOp();
    }

}
