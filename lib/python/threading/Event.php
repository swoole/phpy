<?php
namespace python\threading;

/**
*/
class Event
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->Event();
    }

    public function clear()
    {
        return $this->_self->clear();
    }

    public function isSet()
    {
        return $this->_self->isSet();
    }

    public function is_set()
    {
        return $this->_self->is_set();
    }

    public function set()
    {
        return $this->_self->set();
    }

    public function wait($timeout = null)
    {
        return $this->_self->wait($timeout);
    }

}
