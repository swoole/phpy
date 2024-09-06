<?php
namespace python\ast;

/**
*/
class stmt
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->stmt();
    }

}
