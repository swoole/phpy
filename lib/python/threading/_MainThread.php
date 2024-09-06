<?php
namespace python\threading;

/**
* @property $daemon
* @property $ident
* @property $name
* @property $native_id
*/
class _MainThread
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_MainThread();
    }

    public function getName()
    {
        return $this->_self->getName();
    }

    public function isDaemon()
    {
        return $this->_self->isDaemon();
    }

    public function is_alive()
    {
        return $this->_self->is_alive();
    }

    public function join($timeout = null)
    {
        return $this->_self->join($timeout);
    }

    public function run()
    {
        return $this->_self->run();
    }

    public function setDaemon($daemonic)
    {
        return $this->_self->setDaemon($daemonic);
    }

    public function setName($name)
    {
        return $this->_self->setName($name);
    }

    public function start()
    {
        return $this->_self->start();
    }

}
