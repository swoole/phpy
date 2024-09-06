<?php
namespace python\ast;

/**
*/
class auto
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->auto();
    }

}
