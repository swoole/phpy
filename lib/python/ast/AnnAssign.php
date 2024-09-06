<?php
namespace python\ast;

/**
*/
class AnnAssign
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AnnAssign();
    }

}
