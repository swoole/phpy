<?php
namespace python\torch;

/**
*/
class enable_grad
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->enable_grad();
    }

    public function clone()
    {
        return $this->_self->clone();
    }

}
