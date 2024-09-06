<?php
namespace python\torch;

/**
*/
class dtype
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->dtype();
    }

}
