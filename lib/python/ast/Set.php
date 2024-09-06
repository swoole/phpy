<?php
namespace python\ast;

/**
*/
class Set
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Set();
    }

}
