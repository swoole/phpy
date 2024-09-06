<?php
namespace python\ast;

/**
*/
class TypeIgnore
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->TypeIgnore();
    }

}
