<?php
namespace python\ast;

/**
*/
class Raise
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Raise();
    }

}
