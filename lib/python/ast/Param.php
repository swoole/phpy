<?php
namespace python\ast;

/**
*/
class Param
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Param();
    }

}
