<?php
namespace python\threading;

/**
*/
class local
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->local();
    }

}
