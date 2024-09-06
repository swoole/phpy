<?php
namespace python\threading;

/**
*/
class Semaphore
{
    private $_self;

    public function __construct($value = 1)
    {
        $this->_self = \PyCore::import('threading')->Semaphore($value);
    }

    public function acquire($blocking = true, $timeout = null)
    {
        return $this->_self->acquire($blocking, $timeout);
    }

    public function release($n = 1)
    {
        return $this->_self->release($n);
    }

}
