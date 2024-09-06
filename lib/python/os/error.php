<?php
namespace python\os;

/**
*/
class error
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->error();
    }

}
