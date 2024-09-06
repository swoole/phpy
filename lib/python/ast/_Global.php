<?php
namespace python\ast;

/**
*/
class _Global
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Global();
    }

}
