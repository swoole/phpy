<?php
namespace python\ast;

/**
*/
class Starred
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Starred();
    }

}
