<?php
namespace python\ast;

/**
*/
class _Return
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Return();
    }

}
