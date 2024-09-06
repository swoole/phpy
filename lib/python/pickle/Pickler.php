<?php
namespace python\pickle;

/**
*/
class Pickler
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->Pickler();
    }

}
