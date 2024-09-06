<?php
namespace python\ast;

/**
*/
class RShift
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->RShift();
    }

}
