<?php
namespace python\ast;

/**
*/
class Subscript
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Subscript();
    }

}
