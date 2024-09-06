<?php
namespace python\ast;

/**
*/
class Is
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->Is();
    }

}
