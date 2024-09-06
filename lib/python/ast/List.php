<?php
namespace python\ast;

/**
*/
class List
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->List();
    }

}
