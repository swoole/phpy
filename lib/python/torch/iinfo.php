<?php
namespace python\torch;

/**
*/
class iinfo
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->iinfo();
    }

}
