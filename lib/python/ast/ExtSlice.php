<?php
namespace python\ast;

/**
*/
class ExtSlice
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->ExtSlice();
    }

}
