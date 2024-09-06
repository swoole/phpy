<?php
namespace python\ast;

/**
*/
class While
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->While();
    }

}
