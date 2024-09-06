<?php
namespace python\ast;

/**
*/
class FloorDiv
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->FloorDiv();
    }

}
