<?php
namespace python\ast;

/**
*/
class With
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->With();
    }

}
