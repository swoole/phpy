<?php
namespace python\torch;

/**
*/
class FatalError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->FatalError();
    }

}
