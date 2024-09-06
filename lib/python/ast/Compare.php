<?php
namespace python\ast;

/**
*/
class Compare
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Compare();
    }

}
