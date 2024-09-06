<?php
namespace python\ast;

/**
*/
class Pass
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Pass();
    }

}
