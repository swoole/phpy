<?php
namespace python\ast;

/**
*/
class Assert
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Assert();
    }

}
