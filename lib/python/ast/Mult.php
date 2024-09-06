<?php
namespace python\ast;

/**
*/
class Mult
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Mult();
    }

}
