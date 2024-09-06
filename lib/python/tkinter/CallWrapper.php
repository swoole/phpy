<?php
namespace python\tkinter;

/**
*/
class CallWrapper
{
    private $_self;

    public function __construct($func, $subst, $widget)
    {
        $this->_self = \PyCore::import('tkinter')->CallWrapper($func, $subst, $widget);
    }

}
