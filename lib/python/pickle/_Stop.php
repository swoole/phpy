<?php
namespace python\pickle;

/**
*/
class _Stop
{
    private $_self;

    public function __construct($value)
    {
        $this->_self = \PyCore::import('pickle')->_Stop($value);
    }

}
