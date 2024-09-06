<?php
namespace python\ast;

/**
*/
class Name
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Name();
    }

}
