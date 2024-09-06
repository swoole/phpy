<?php
namespace python\ast;

/**
*/
class BinOp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->BinOp();
    }

}
