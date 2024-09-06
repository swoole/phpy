<?php
namespace python\ast;

/**
* @property $n
* @property $s
*/
class Constant
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Constant();
    }

}
