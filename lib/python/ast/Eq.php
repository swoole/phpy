<?php
namespace python\ast;

/**
*/
class Eq
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Eq();
    }

}
