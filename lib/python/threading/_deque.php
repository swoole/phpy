<?php
namespace python\threading;

/**
*/
class _deque
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_deque();
    }

}
