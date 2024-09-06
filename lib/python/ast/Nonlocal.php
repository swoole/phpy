<?php
namespace python\ast;

/**
*/
class Nonlocal
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Nonlocal();
    }

}
