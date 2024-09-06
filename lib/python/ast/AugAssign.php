<?php
namespace python\ast;

/**
*/
class AugAssign
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AugAssign();
    }

}
