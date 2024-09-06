<?php
namespace python\ast;

/**
*/
class And
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->And();
    }

}
