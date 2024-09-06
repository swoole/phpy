<?php
namespace python\ast;

/**
*/
class AugStore
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AugStore();
    }

}
