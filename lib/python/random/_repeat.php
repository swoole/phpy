<?php
namespace python\random;

/**
*/
class _repeat
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('random')->_repeat();
    }

}
