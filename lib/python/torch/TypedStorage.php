<?php
namespace python\torch;

/**
* @property $device
* @property $filename
* @property $is_cuda
* @property $is_hpu
*/
class TypedStorage
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->TypedStorage();
    }

    public function bfloat16()
    {
        return $this->_self->bfloat16();
    }

    public function bool()
    {
        return $this->_self->bool();
    }

    public function byte()
    {
        return $this->_self->byte();
    }

    public function char()
    {
        return $this->_self->char();
    }

    public function clone()
    {
        return $this->_self->clone();
    }

    public function complex_double()
    {
        return $this->_self->complex_double();
    }

    public function complex_float()
    {
        return $this->_self->complex_float();
    }

    public function copy_($source, $non_blocking = null)
    {
        return $this->_self->copy_($source, $non_blocking);
    }

    public function cpu()
    {
        return $this->_self->cpu();
    }

    public function cuda($device = null, $non_blocking = false)
    {
        return $this->_self->cuda($device, $non_blocking);
    }

    public function data_ptr()
    {
        return $this->_self->data_ptr();
    }

    public function double()
    {
        return $this->_self->double();
    }

    public function element_size()
    {
        return $this->_self->element_size();
    }

    public function fill_($value)
    {
        return $this->_self->fill_($value);
    }

    public function float()
    {
        return $this->_self->float();
    }

    public function float8_e4m3fn()
    {
        return $this->_self->float8_e4m3fn();
    }

    public function float8_e4m3fnuz()
    {
        return $this->_self->float8_e4m3fnuz();
    }

    public function float8_e5m2()
    {
        return $this->_self->float8_e5m2();
    }

    public function float8_e5m2fnuz()
    {
        return $this->_self->float8_e5m2fnuz();
    }

    public function get_device()
    {
        return $this->_self->get_device();
    }

    public function half()
    {
        return $this->_self->half();
    }

    public function hpu($device = null, $non_blocking = false)
    {
        return $this->_self->hpu($device, $non_blocking);
    }

    public function int()
    {
        return $this->_self->int();
    }

    public function is_pinned($device = "cuda")
    {
        return $this->_self->is_pinned($device);
    }

    public function is_shared()
    {
        return $this->_self->is_shared();
    }

    public function long()
    {
        return $this->_self->long();
    }

    public function nbytes()
    {
        return $this->_self->nbytes();
    }

    public function pickle_storage_type()
    {
        return $this->_self->pickle_storage_type();
    }

    public function pin_memory($device = "cuda")
    {
        return $this->_self->pin_memory($device);
    }

    public function resizable()
    {
        return $this->_self->resizable();
    }

    public function resize_($size)
    {
        return $this->_self->resize_($size);
    }

    public function share_memory_()
    {
        return $this->_self->share_memory_();
    }

    public function short()
    {
        return $this->_self->short();
    }

    public function size()
    {
        return $this->_self->size();
    }

    public function to()
    {
        return $this->_self->to();
    }

    public function tolist()
    {
        return $this->_self->tolist();
    }

    public function type($dtype = null, $non_blocking = false)
    {
        return $this->_self->type($dtype, $non_blocking);
    }

    public function untyped()
    {
        return $this->_self->untyped();
    }

}
