<?php
namespace python\ast;

/**
*/
class ListComp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->ListComp();
    }

}
