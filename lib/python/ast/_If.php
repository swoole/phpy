<?php
namespace python\ast;

/**
*/
class _If
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->_If();
    }

}
