<?php
namespace python\ast;

/**
*/
class UAdd
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->UAdd();
    }

}
