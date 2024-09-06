<?php
namespace python\ast;

/**
*/
class Await
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Await();
    }

}
