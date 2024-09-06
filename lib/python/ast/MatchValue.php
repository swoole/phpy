<?php
namespace python\ast;

/**
*/
class MatchValue
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchValue();
    }

}
