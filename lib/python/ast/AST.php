<?php
namespace python\ast;

/**
*/
class AST
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AST();
    }

}
