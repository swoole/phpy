<?php
namespace python\ast;

/**
*/
class Div
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Div();
    }

}
