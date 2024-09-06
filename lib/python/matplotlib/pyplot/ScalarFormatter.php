<?php
namespace python\matplotlib\pyplot;

/**
* @property $useLocale
* @property $useMathText
* @property $useOffset
*/
class ScalarFormatter
{
    private $_self;

    public function __construct($useOffset = null, $useMathText = null, $useLocale = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->ScalarFormatter($useOffset, $useMathText, $useLocale);
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

    public function get_useLocale()
    {
        return $this->_self->get_useLocale();
    }

    public function get_useMathText()
    {
        return $this->_self->get_useMathText();
    }

    public function get_useOffset()
    {
        return $this->_self->get_useOffset();
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

    public function set_powerlimits($lims)
    {
        return $this->_self->set_powerlimits($lims);
    }

    public function set_scientific($b)
    {
        return $this->_self->set_scientific($b);
    }

    public function set_useLocale($val)
    {
        return $this->_self->set_useLocale($val);
    }

    public function set_useMathText($val)
    {
        return $this->_self->set_useMathText($val);
    }

    public function set_useOffset($val)
    {
        return $this->_self->set_useOffset($val);
    }

    public function set_view_interval()
    {
        return $this->_self->set_view_interval();
    }

}
