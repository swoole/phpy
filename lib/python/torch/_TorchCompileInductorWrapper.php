<?php
namespace python\torch;

/**
*/
class _TorchCompileInductorWrapper
{
    private $_self;

    public function __construct($mode, $options, $dynamic)
    {
        $this->_self = \PyCore::import('torch')->_TorchCompileInductorWrapper($mode, $options, $dynamic);
    }

    public function apply_mode($mode)
    {
        return $this->_self->apply_mode($mode);
    }

    public function apply_options($options)
    {
        return $this->_self->apply_options($options);
    }

    public function get_compiler_config()
    {
        return $this->_self->get_compiler_config();
    }

    public function reset()
    {
        return $this->_self->reset();
    }

}
