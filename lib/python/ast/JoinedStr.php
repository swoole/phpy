<?php
namespace python\ast;

/**
*/
class JoinedStr
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->JoinedStr();
    }

}
