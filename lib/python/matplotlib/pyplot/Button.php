<?php
namespace python\matplotlib\pyplot;

/**
* @property $active
*/
class Button
{
    private $_self;

    public function __construct($ax, $label, $image = null, $color = "0.85", $hovercolor = "0.95")
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Button($ax, $label, $image, $color, $hovercolor);
    }

    public function connect_event($event, $callback)
    {
        return $this->_self->connect_event($event, $callback);
    }

    public function disconnect($cid)
    {
        return $this->_self->disconnect($cid);
    }

    public function disconnect_events()
    {
        return $this->_self->disconnect_events();
    }

    public function get_active()
    {
        return $this->_self->get_active();
    }

    public function ignore($event)
    {
        return $this->_self->ignore($event);
    }

    public function on_clicked($func)
    {
        return $this->_self->on_clicked($func);
    }

    public function set_active($active)
    {
        return $this->_self->set_active($active);
    }

}
