<?php
namespace python\ast;

/**
*/
class AsyncWith
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AsyncWith();
    }

}
