<?php
namespace python\ast;

/**
*/
class MatchClass
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchClass();
    }

}
