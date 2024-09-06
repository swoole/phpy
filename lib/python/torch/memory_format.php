<?php
namespace python\torch;

/**
*/
class memory_format
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->memory_format();
    }

}
