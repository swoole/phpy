<?php
namespace python\ast;

/**
*/
class Try
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Try();
    }

}
