<?php
namespace python\ast;

/**
*/
class _Match
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_Match();
    }

}
