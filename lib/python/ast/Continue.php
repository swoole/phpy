<?php
namespace python\ast;

/**
*/
class Continue
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Continue();
    }

}
