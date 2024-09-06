<?php
namespace python\tkinter;

/**
*/
class _setit
{
    private $_self;

    public function __construct($var, $value, $callback = null)
    {
        $this->_self = \PyCore::import('tkinter')->_setit($var, $value, $callback);
    }

}
