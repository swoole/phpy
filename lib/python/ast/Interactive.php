<?php
namespace python\ast;

/**
*/
class Interactive
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Interactive();
    }

}
