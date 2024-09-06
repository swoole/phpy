<?php
namespace python\ast;

/**
*/
class Suite
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Suite();
    }

}
