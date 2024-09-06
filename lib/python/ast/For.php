<?php
namespace python\ast;

/**
*/
class For
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->For();
    }

}
