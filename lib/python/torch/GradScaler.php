<?php
namespace python\torch;

/**
*/
class GradScaler
{
    private $_self;

    public function __construct($device = "cuda", $init_scale = 65536, $growth_factor = 2, $backoff_factor = 0.5, $growth_interval = 2000, $enabled = true)
    {
        $this->_self = \PyCore::import('torch')->GradScaler($device, $init_scale, $growth_factor, $backoff_factor, $growth_interval, $enabled);
    }

    public function get_backoff_factor()
    {
        return $this->_self->get_backoff_factor();
    }

    public function get_growth_factor()
    {
        return $this->_self->get_growth_factor();
    }

    public function get_growth_interval()
    {
        return $this->_self->get_growth_interval();
    }

    public function get_scale()
    {
        return $this->_self->get_scale();
    }

    public function is_enabled()
    {
        return $this->_self->is_enabled();
    }

    public function load_state_dict($state_dict)
    {
        return $this->_self->load_state_dict($state_dict);
    }

    public function scale($outputs)
    {
        return $this->_self->scale($outputs);
    }

    public function set_backoff_factor($new_factor)
    {
        return $this->_self->set_backoff_factor($new_factor);
    }

    public function set_growth_factor($new_factor)
    {
        return $this->_self->set_growth_factor($new_factor);
    }

    public function set_growth_interval($new_interval)
    {
        return $this->_self->set_growth_interval($new_interval);
    }

    public function state_dict()
    {
        return $this->_self->state_dict();
    }

    public function step($optimizer)
    {
        return $this->_self->step($optimizer);
    }

    public function unscale_($optimizer)
    {
        return $this->_self->unscale_($optimizer);
    }

    public function update($new_scale = null)
    {
        return $this->_self->update($new_scale);
    }

}
