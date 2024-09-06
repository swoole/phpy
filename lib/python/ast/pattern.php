<?php
namespace python\ast;

/**
*/
class pattern
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->pattern();
    }

}
