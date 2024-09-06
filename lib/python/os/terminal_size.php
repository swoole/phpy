<?php
namespace python\os;

/**
*/
class terminal_size
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->terminal_size();
    }

}
