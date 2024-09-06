<?php
namespace python\ast;

/**
*/
class Not
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Not();
    }

}
