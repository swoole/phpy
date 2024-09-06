<?php
namespace python\threading;

/**
* @property $broken
* @property $n_waiting
* @property $parties
*/
class Barrier
{
    private $_self;

    public function __construct($parties, $action = null, $timeout = null)
    {
        $this->_self = \PyCore::import('threading')->Barrier($parties, $action, $timeout);
    }

    public function abort()
    {
        return $this->_self->abort();
    }

    public function reset()
    {
        return $this->_self->reset();
    }

    public function wait($timeout = null)
    {
        return $this->_self->wait($timeout);
    }

}
