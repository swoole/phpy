<?php
namespace python\ast;

/**
*/
class _For
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_For();
    }

}