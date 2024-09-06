<?php
namespace python\ast;

/**
*/
class _List
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_List();
    }

}
