<?php
namespace python\ast;

/**
*/
class comprehension
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->comprehension();
    }

}
