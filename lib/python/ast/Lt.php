<?php
namespace python\ast;

/**
*/
class Lt
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Lt();
    }

}
