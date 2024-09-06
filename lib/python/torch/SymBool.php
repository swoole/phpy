<?php
namespace python\torch;

/**
*/
class SymBool
{
    private $_self;

    public function __construct($node)
    {
        $this->_self = \PyCore::import('torch')->SymBool($node);
    }

}
