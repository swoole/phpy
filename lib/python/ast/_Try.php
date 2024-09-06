<?php
namespace python\ast;

/**
*/
class _Try
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Try();
    }

}
