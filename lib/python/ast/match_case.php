<?php
namespace python\ast;

/**
*/
class match_case
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->match_case();
    }

}
