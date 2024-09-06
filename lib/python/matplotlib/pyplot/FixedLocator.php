<?php
namespace python\matplotlib\pyplot;

/**
*/
class FixedLocator
{
    private $_self;

    public function __construct($locs, $nbins = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->FixedLocator($locs, $nbins);
    }

    public function create_dummy_axis()
    {
        return $this->_self->create_dummy_axis();
    }

    public function nonsingular($v0, $v1)
    {
        return $this->_self->nonsingular($v0, $v1);
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

    public function set_params($nbins = null)
    {
        return $this->_self->set_params($nbins);
    }

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
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
