<?php
namespace python\pickle;

/**
*/
class Unpickler
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->Unpickler();
    }

}
