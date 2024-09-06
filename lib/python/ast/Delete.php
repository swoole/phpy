<?php
namespace python\ast;

/**
*/
class Delete
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Delete();
    }

}
