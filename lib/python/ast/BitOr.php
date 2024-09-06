<?php
namespace python\ast;

/**
*/
class BitOr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->BitOr();
    }

}
