<?php
namespace python\ast;

/**
*/
class arg
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->arg();
    }

}
