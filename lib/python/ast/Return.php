<?php
namespace python\ast;

/**
*/
class Return
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Return();
    }

}
