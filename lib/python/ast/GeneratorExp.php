<?php
namespace python\ast;

/**
*/
class GeneratorExp
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->GeneratorExp();
    }

}
