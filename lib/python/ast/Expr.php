<?php
namespace python\ast;

/**
*/
class Expr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Expr();
    }

}
