<?php
namespace python\pickle;

/**
*/
class islice
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('pickle')->islice();
    }

}
