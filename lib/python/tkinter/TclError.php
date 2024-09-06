<?php
namespace python\tkinter;

/**
*/
class TclError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->TclError();
    }

}
