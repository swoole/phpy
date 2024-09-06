<?php
namespace python\ast;

/**
*/
class cmpop
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->cmpop();
    }

}
