<?php
namespace python\ast;

/**
*/
class expr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->expr();
    }

}
