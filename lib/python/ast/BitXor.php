<?php
namespace python\ast;

/**
*/
class BitXor
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->BitXor();
    }

}
