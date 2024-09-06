<?php
namespace python\ast;

/**
*/
class operator
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->operator();
    }

}
