<?php
namespace python\ast;

/**
*/
class Match
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Match();
    }

}
