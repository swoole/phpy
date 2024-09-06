<?php
namespace python\ast;

/**
*/
class mod
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->mod();
    }

}
