<?php
namespace python\ast;

/**
*/
class keyword
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->keyword();
    }

}
