<?php
namespace python\threading;

/**
*/
class _CRLock
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_CRLock();
    }

}
