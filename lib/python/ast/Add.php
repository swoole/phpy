<?php
namespace python\ast;

/**
*/
class Add
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Add();
    }

}
