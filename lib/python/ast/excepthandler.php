<?php
namespace python\ast;

/**
*/
class excepthandler
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->excepthandler();
    }

}
