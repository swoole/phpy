<?php
namespace python\os;

/**
*/
class stat_result
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->stat_result();
    }

}
