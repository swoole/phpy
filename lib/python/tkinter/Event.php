<?php
namespace python\tkinter;

/**
*/
class Event
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->Event();
    }

}
