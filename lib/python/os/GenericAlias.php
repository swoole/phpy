<?php
namespace python\os;

/**
*/
class GenericAlias
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('os')->GenericAlias();
    }

}
