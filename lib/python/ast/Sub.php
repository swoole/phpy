<?php
namespace python\ast;

/**
*/
class Sub
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Sub();
    }

}
