<?php
namespace python\torch;

/**
*/
class SymInt
{
    private $_self;

    public function __construct($node)
    {
        $this->_self = \PyCore::import('torch')->SymInt($node);
    }

}
