<?php
namespace python\torch;

/**
*/
class device
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->device();
    }

}
