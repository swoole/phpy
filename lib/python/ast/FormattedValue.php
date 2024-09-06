<?php
namespace python\ast;

/**
*/
class FormattedValue
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->FormattedValue();
    }

}
