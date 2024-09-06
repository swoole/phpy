<?php
namespace python\ast;

/**
*/
class AugLoad
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AugLoad();
    }

}
