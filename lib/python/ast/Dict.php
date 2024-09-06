<?php
namespace python\ast;

/**
*/
class Dict
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Dict();
    }

}
