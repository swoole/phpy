<?php
namespace python\pickle;

/**
*/
class PickleBuffer
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->PickleBuffer();
    }

}
