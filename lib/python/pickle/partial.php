<?php
namespace python\pickle;

/**
*/
class partial
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->partial();
    }

}
