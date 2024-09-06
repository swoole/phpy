<?php
namespace python\ast;

/**
*/
class GtE
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->GtE();
    }

}
