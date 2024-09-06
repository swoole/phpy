<?php
namespace python\ast;

/**
*/
class NamedExpr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->NamedExpr();
    }

}
