<?php
namespace python\torch;

/**
*/
class DisableTorchFunction
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->DisableTorchFunction();
    }

}
