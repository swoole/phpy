<?php
namespace python\ast;

/**
*/
class ImportFrom
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->ImportFrom();
    }

}
