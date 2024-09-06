<?php
namespace python\ast;

/**
*/
class Load
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Load();
    }

}
