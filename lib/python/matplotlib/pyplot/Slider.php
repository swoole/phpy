<?php
namespace python\matplotlib\pyplot;

/**
* @property $active
*/
class Slider
{
    private $_self;

    public function __construct($ax, $label, $valmin, $valmax, $valinit = 0.5, $valfmt = null, $closedmin = true, $closedmax = true, $slidermin = null, $slidermax = null, $dragging = true, $valstep = null, $orientation = "horizontal")
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Slider($ax, $label, $valmin, $valmax, $valinit, $valfmt, $closedmin, $closedmax, $slidermin, $slidermax, $dragging, $valstep, $orientation);
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

    public function on_changed($func)
    {
        return $this->_self->on_changed($func);
    }

    public function reset()
    {
        return $this->_self->reset();
    }

    public function set_active($active)
    {
        return $this->_self->set_active($active);
    }

    public function set_val($val)
    {
        return $this->_self->set_val($val);
    }

}
