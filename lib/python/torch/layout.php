<?php
namespace python\torch;

/**
*/
class layout
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->layout();
    }

}
