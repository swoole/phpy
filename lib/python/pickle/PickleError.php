<?php
namespace python\pickle;

/**
*/
class PickleError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->PickleError();
    }

}
