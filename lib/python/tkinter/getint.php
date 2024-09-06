<?php
namespace python\tkinter;

/**
*/
class getint
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->getint();
    }

}
