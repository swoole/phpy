<?php
namespace python\ast;

/**
*/
class MatMult
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatMult();
    }

}
