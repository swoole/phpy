<?php
namespace python\ast;

/**
*/
class Expression
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Expression();
    }

}
