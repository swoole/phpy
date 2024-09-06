<?php
namespace python\ast;

/**
* @property $dims
*/
class Tuple
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Tuple();
    }

}
