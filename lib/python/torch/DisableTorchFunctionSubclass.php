<?php
namespace python\torch;

/**
*/
class DisableTorchFunctionSubclass
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->DisableTorchFunctionSubclass();
    }

}
