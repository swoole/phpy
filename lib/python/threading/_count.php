<?php
namespace python\threading;

/**
*/
class _count
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_count();
    }

}
