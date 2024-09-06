<?php
namespace python\torch;

/**
*/
class SymFloat
{
    private $_self;

    public function __construct($node)
    {
        $this->_self = \PyCore::import('torch')->SymFloat($node);
    }

    public function is_integer()
    {
        return $this->_self->is_integer();
    }

}
