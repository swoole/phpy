<?php
namespace python\ast;

/**
*/
class _Yield
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Yield();
    }

}
