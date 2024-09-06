<?php
namespace python\matplotlib\pyplot;

/**
*/
class TickHelper
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->TickHelper();
    }

    public function create_dummy_axis()
    {
        return $this->_self->create_dummy_axis();
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

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
    }

}
