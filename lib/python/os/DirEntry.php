<?php
namespace python\os;

/**
*/
class DirEntry
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->DirEntry();
    }

}
