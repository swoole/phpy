<?php
namespace python\os;

/**
*/
class sched_param
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->sched_param();
    }

}
