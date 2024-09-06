<?php
namespace python\pickle;

/**
*/
class PicklingError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->PicklingError();
    }

}
