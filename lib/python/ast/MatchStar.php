<?php
namespace python\ast;

/**
*/
class MatchStar
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchStar();
    }

}
