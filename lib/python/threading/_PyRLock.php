<?php
namespace python\threading;

/**
*/
class _PyRLock
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_PyRLock();
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
