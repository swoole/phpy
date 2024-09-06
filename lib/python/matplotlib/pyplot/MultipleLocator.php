<?php
namespace python\matplotlib\pyplot;

/**
*/
class MultipleLocator
{
    private $_self;

    public function __construct($base = 1)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->MultipleLocator($base);
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

    public function set_params($base)
    {
        return $this->_self->set_params($base);
    }

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
    }

    public function tick_values($vmin, $vmax)
    {
        return $this->_self->tick_values($vmin, $vmax);
    }

    public function view_limits($dmin, $dmax)
    {
        return $this->_self->view_limits($dmin, $dmax);
    }

}
