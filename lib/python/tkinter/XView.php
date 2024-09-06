<?php
namespace python\tkinter;

/**
*/
class XView
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->XView();
    }

    public function xview()
    {
        return $this->_self->xview();
    }

    public function xview_moveto($fraction)
    {
        return $this->_self->xview_moveto($fraction);
    }

    public function xview_scroll($number, $what)
    {
        return $this->_self->xview_scroll($number, $what);
    }

}
