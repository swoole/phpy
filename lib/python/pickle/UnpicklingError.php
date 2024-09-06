<?php
namespace python\pickle;

/**
*/
class UnpicklingError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->UnpicklingError();
    }

}
