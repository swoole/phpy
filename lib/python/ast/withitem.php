<?php
namespace python\ast;

/**
*/
class withitem
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->withitem();
    }

}
