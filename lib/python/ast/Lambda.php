<?php
namespace python\ast;

/**
*/
class Lambda
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Lambda();
    }

}
