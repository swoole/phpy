<?php
namespace python\ast;

/**
*/
class Module
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Module();
    }

}
