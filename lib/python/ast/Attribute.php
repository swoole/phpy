<?php
namespace python\ast;

/**
*/
class Attribute
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Attribute();
    }

}
