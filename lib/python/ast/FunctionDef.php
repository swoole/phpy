<?php
namespace python\ast;

/**
*/
class FunctionDef
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->FunctionDef();
    }

}
