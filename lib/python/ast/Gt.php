<?php
namespace python\ast;

/**
*/
class Gt
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Gt();
    }

}
