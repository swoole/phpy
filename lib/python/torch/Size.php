<?php
namespace python\torch;

/**
*/
class Size
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->Size();
    }

}
