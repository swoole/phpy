<?php
namespace python\ast;

/**
*/
class Global
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Global();
    }

}
