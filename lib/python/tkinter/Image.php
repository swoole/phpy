<?php
namespace python\tkinter;

/**
*/
class Image
{
    private $_self;

    public function __construct($imgtype, $name = null, $cnf = [], $master = null)
    {
        $this->_self = \PyCore::import('tkinter')->Image($imgtype, $name, $cnf, $master);
    }

    public function config()
    {
        return $this->_self->config();
    }

    public function configure()
    {
        return $this->_self->configure();
    }

    public function height()
    {
        return $this->_self->height();
    }

    public function type()
    {
        return $this->_self->type();
    }

    public function width()
    {
        return $this->_self->width();
    }

}
