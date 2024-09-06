<?php
namespace python\tkinter;

/**
*/
class Pack
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->Pack();
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

    public function pack($cnf = [])
    {
        return $this->_self->pack($cnf);
    }

    public function pack_configure($cnf = [])
    {
        return $this->_self->pack_configure($cnf);
    }

    public function pack_forget()
    {
        return $this->_self->pack_forget();
    }

    public function pack_info()
    {
        return $this->_self->pack_info();
    }

    public function pack_propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->pack_propagate($flag);
    }

    public function pack_slaves()
    {
        return $this->_self->pack_slaves();
    }

    public function propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->propagate($flag);
    }

    public function slaves()
    {
        return $this->_self->slaves();
    }

}
