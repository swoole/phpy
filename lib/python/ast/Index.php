<?php
namespace python\ast;

/**
*/
class Index
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Index();
    }

}
