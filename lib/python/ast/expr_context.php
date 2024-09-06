<?php
namespace python\ast;

/**
*/
class expr_context
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->expr_context();
    }

}
