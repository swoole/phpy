<?php
namespace python\ast;

/**
*/
class BoolOp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->BoolOp();
    }

}
