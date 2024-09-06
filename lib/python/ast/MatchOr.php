<?php
namespace python\ast;

/**
*/
class MatchOr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchOr();
    }

}
