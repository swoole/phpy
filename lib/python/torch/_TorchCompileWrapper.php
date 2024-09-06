<?php
namespace python\torch;

/**
*/
class _TorchCompileWrapper
{
    private $_self;

    public function __construct($backend, $mode, $options, $dynamic)
    {
        $this->_self = \PyCore::import('torch')->_TorchCompileWrapper($backend, $mode, $options, $dynamic);
    }

    public function reset()
    {
        return $this->_self->reset();
    }

}
