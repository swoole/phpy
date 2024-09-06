<?php
namespace python\ast;

/**
*/
class BitAnd
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->BitAnd();
    }

}
