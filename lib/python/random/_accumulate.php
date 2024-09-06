<?php
namespace python\random;

/**
*/
class _accumulate
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('random')->_accumulate();
    }

}
