<?php
namespace python\ast;

/**
*/
class LShift
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->LShift();
    }

}
