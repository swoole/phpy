<?php
namespace python\ast;

/**
*/
class MatchSingleton
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchSingleton();
    }

}
