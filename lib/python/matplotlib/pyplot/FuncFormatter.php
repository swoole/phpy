<?php
namespace python\matplotlib\pyplot;

/**
*/
class FuncFormatter
{
    private $_self;

    public function __construct($func)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->FuncFormatter($func);
    }

    public function create_dummy_axis()
    {
        return $this->_self->create_dummy_axis();
    }

    public function fix_minus()
    {
        return $this->_self->fix_minus();
    }

    public function format_data($value)
    {
        return $this->_self->format_data($value);
    }

    public function format_data_short($value)
    {
        return $this->_self->format_data_short($value);
    }

    public function format_ticks($values)
    {
        return $this->_self->format_ticks($values);
    }

    public function get_offset()
    {
        return $this->_self->get_offset();
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

    public function set_locs($locs)
    {
        return $this->_self->set_locs($locs);
    }

    public function set_offset_string($ofs)
    {
        return $this->_self->set_offset_string($ofs);
    }

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
    }

}
