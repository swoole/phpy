<?php
namespace python\ast;

/**
*/
class AsyncFor
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->AsyncFor();
    }

}
