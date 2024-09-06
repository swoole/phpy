<?php
namespace python\tkinter;

/**
*/
class Place
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->Place();
    }

    public function config($cnf = [])
    {
        return $this->_self->config($cnf);
    }

    public function configure($cnf = [])
    {
        return $this->_self->configure($cnf);
    }

    public function forget()
    {
        return $this->_self->forget();
    }

    public function info()
    {
        return $this->_self->info();
    }

    public function place($cnf = [])
    {
        return $this->_self->place($cnf);
    }

    public function place_configure($cnf = [])
    {
        return $this->_self->place_configure($cnf);
    }

    public function place_forget()
    {
        return $this->_self->place_forget();
    }

    public function place_info()
    {
        return $this->_self->place_info();
    }

    public function place_slaves()
    {
        return $this->_self->place_slaves();
    }

    public function slaves()
    {
        return $this->_self->slaves();
    }

}
