<?php
namespace python\tkinter;

/**
*/
class DoubleVar
{
    private $_self;

    public function __construct($master = null, $value = null, $name = null)
    {
        $this->_self = \PyCore::import('tkinter')->DoubleVar($master, $value, $name);
    }

    public function get()
    {
        return $this->_self->get();
    }

    public function initialize($value)
    {
        return $this->_self->initialize($value);
    }

    public function set($value)
    {
        return $this->_self->set($value);
    }

    public function trace($mode, $callback)
    {
        return $this->_self->trace($mode, $callback);
    }

    public function trace_add($mode, $callback)
    {
        return $this->_self->trace_add($mode, $callback);
    }

    public function trace_info()
    {
        return $this->_self->trace_info();
    }

    public function trace_remove($mode, $cbname)
    {
        return $this->_self->trace_remove($mode, $cbname);
    }

    public function trace_variable($mode, $callback)
    {
        return $this->_self->trace_variable($mode, $callback);
    }

    public function trace_vdelete($mode, $cbname)
    {
        return $this->_self->trace_vdelete($mode, $cbname);
    }

    public function trace_vinfo()
    {
        return $this->_self->trace_vinfo();
    }

}
