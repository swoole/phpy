<?php
namespace python\ast;

/**
*/
class Invert
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Invert();
    }

}
