<?php
namespace python\ast;

/**
*/
class _Break
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Break();
    }

}
