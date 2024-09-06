<?php
namespace python\ast;

/**
*/
class If
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->If();
    }

}
