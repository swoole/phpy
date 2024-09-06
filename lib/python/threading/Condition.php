<?php
namespace python\threading;

/**
*/
class Condition
{
    private $_self;

    public function __construct($lock = null)
    {
        $this->_self = \PyCore::import('threading')->Condition($lock);
    }

    public function notify($n = 1)
    {
        return $this->_self->notify($n);
    }

    public function notifyAll()
    {
        return $this->_self->notifyAll();
    }

    public function notify_all()
    {
        return $this->_self->notify_all();
    }

    public function wait($timeout = null)
    {
        return $this->_self->wait($timeout);
    }

    public function wait_for($predicate, $timeout = null)
    {
        return $this->_self->wait_for($predicate, $timeout);
    }

}
