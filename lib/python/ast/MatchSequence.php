<?php
namespace python\ast;

/**
*/
class MatchSequence
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->MatchSequence();
    }

}
