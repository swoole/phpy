<?php
namespace python\ast;

/**
*/
class IfExp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->IfExp();
    }

}
