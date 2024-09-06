<?php
namespace python\ast;

/**
*/
class Pow
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Pow();
    }

}
