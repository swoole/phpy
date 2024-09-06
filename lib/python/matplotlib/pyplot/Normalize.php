<?php
namespace python\matplotlib\pyplot;

/**
* @property $clip
* @property $vmax
* @property $vmin
*/
class Normalize
{
    private $_self;

    public function __construct($vmin = null, $vmax = null, $clip = false)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Normalize($vmin, $vmax, $clip);
    }

    public function autoscale($A)
    {
        return $this->_self->autoscale($A);
    }

    public function autoscale_None($A)
    {
        return $this->_self->autoscale_None($A);
    }

    public function inverse($value)
    {
        return $this->_self->inverse($value);
    }

    public function process_value()
    {
        return $this->_self->process_value();
    }

    public function scaled()
    {
        return $this->_self->scaled();
    }

}
