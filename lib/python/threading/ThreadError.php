<?php
namespace python\threading;

/**
*/
class ThreadError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->ThreadError();
    }

}
