<?php
namespace python\ast;

/**
*/
class _While
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_While();
    }

}
