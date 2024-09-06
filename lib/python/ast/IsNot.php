<?php
namespace python\ast;

/**
*/
class IsNot
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->IsNot();
    }

}
