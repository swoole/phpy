<?php
namespace python\ast;

/**
*/
class alias
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->alias();
    }

}
