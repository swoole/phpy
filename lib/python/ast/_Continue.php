<?php
namespace python\ast;

/**
*/
class _Continue
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Continue();
    }

}
