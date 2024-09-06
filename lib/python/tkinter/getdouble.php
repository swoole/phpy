<?php
namespace python\tkinter;

/**
*/
class getdouble
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->getdouble();
    }

}
