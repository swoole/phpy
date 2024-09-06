<?php
namespace python\ast;

/**
*/
class Call
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Call();
    }

}
