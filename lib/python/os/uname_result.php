<?php
namespace python\os;

/**
*/
class uname_result
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->uname_result();
    }

}
