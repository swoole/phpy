<?php
namespace python\threading;

/**
*/
class _RLock
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_RLock();
    }

    public function acquire($blocking = true, $timeout = -1)
    {
        return $this->_self->acquire($blocking, $timeout);
    }

    public function release()
    {
        return $this->_self->release();
    }

}
