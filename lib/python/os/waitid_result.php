<?php
namespace python\os;

/**
*/
class waitid_result
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->waitid_result();
    }

}
