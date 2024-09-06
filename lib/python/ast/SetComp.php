<?php
namespace python\ast;

/**
*/
class SetComp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->SetComp();
    }

}
