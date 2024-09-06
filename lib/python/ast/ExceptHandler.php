<?php
namespace python\ast;

/**
*/
class ExceptHandler
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->ExceptHandler();
    }

}
