<?php
namespace python\ast;

/**
*/
class Yield
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Yield();
    }

}
