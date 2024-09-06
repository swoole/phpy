<?php
namespace python\ast;

/**
*/
class USub
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->USub();
    }

}
