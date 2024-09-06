<?php
namespace python\torch;

/**
*/
class inference_mode
{
    private $_self;

    public function __construct($mode = true)
    {
        $this->_self = \PyCore::import('torch')->inference_mode($mode);
    }

    public function clone()
    {
        return $this->_self->clone();
    }

}
