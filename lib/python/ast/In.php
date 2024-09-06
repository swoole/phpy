<?php
namespace python\ast;

/**
*/
class In
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->In();
    }

}
