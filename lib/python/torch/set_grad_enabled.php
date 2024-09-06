<?php
namespace python\torch;

/**
*/
class set_grad_enabled
{
    private $_self;

    public function __construct($mode)
    {
        $this->_self = \PyCore::import('torch')->set_grad_enabled($mode);
    }

    public function clone()
    {
        return $this->_self->clone();
    }

}
