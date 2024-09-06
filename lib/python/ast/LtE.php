<?php
namespace python\ast;

/**
*/
class LtE
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->LtE();
    }

}
