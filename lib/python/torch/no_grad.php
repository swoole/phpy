<?php
namespace python\torch;

/**
*/
class no_grad
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->no_grad();
    }

    public function clone()
    {
        return $this->_self->clone();
    }

}
