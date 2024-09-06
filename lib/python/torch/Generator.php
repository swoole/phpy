<?php
namespace python\torch;

/**
*/
class Generator
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->Generator();
    }

}
