<?php
namespace python\os;

/**
*/
class times_result
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->times_result();
    }

}
