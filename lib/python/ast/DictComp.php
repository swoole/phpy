<?php
namespace python\ast;

/**
*/
class DictComp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->DictComp();
    }

}
