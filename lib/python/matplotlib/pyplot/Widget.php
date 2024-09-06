<?php
namespace python\matplotlib\pyplot;

/**
* @property $active
*/
class Widget
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Widget();
    }

    public function get_active()
    {
        return $this->_self->get_active();
    }

    public function ignore($event)
    {
        return $this->_self->ignore($event);
    }

    public function set_active($active)
    {
        return $this->_self->set_active($active);
    }

}
