<?php
namespace python\ast;

/**
*/
class ClassDef
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->ClassDef();
    }

}
