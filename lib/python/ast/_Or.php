<?php
namespace python\ast;

/**
*/
class _Or
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Or();
    }

}
