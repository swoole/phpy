<?php
namespace python\ast;

/**
*/
class type_ignore
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->type_ignore();
    }

}
