<?php
namespace python\ast;

/**
*/
class Del
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Del();
    }

}
