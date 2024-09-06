<?php
namespace python\os;

/**
*/
class statvfs_result
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->statvfs_result();
    }

}
