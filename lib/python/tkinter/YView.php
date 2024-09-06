<?php
namespace python\tkinter;

/**
*/
class YView
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->YView();
    }

    public function yview()
    {
        return $this->_self->yview();
    }

    public function yview_moveto($fraction)
    {
        return $this->_self->yview_moveto($fraction);
    }

    public function yview_scroll($number, $what)
    {
        return $this->_self->yview_scroll($number, $what);
    }

}
