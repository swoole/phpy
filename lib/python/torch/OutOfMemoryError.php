<?php
namespace python\torch;

/**
*/
class OutOfMemoryError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->OutOfMemoryError();
    }

}
