<?php
namespace python\ast;

/**
*/
class arguments
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->arguments();
    }

}
