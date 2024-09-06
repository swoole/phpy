<?php
namespace python\ast;

/**
*/
class NotEq
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->NotEq();
    }

}
