<?php
namespace python\ast;

/**
*/
class MatchAs
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchAs();
    }

}
