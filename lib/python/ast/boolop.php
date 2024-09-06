<?php
namespace python\ast;

/**
*/
class boolop
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->boolop();
    }

}
