<?php
namespace python\ast;

/**
*/
class _And
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_And();
    }

}
