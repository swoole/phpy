<?php
namespace python\ast;

/**
*/
class Or
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Or();
    }

}
