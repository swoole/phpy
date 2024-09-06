<?php
namespace python\matplotlib\pyplot;

/**
*/
class LogLocator
{
    private $_self;

    public function __construct($base = 10, $subs = array (
  0 => 1.0,
), $numdecs = 4, $numticks = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->LogLocator($base, $subs, $numdecs, $numticks);
    }

    public function base($base)
    {
        return $this->_self->base($base);
    }

    public function create_dummy_axis()
    {
        return $this->_self->create_dummy_axis();
    }

    public function nonsingular($vmin, $vmax)
    {
        return $this->_self->nonsingular($vmin, $vmax);
    }

    public function raise_if_exceeds($locs)
    {
        return $this->_self->raise_if_exceeds($locs);
    }

    public function set_axis($axis)
    {
        return $this->_self->set_axis($axis);
    }

    public function set_bounds()
    {
        return $this->_self->set_bounds();
    }

    public function set_data_interval()
    {
        return $this->_self->set_data_interval();
    }

    public function set_params($base = null, $subs = null, $numdecs = null, $numticks = null)
    {
        return $this->_self->set_params($base, $subs, $numdecs, $numticks);
    }

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
    }

    public function subs($subs)
    {
        return $this->_self->subs($subs);
    }

    public function tick_values($vmin, $vmax)
    {
        return $this->_self->tick_values($vmin, $vmax);
    }

    public function view_limits($vmin, $vmax)
    {
        return $this->_self->view_limits($vmin, $vmax);
    }

}
