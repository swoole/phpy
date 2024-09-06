<?php
namespace python\torch;

/**
*/
class finfo
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->finfo();
    }

}
