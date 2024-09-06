<?php
namespace python\tkinter;

/**
*/
class BitmapImage
{
    private $_self;

    public function __construct($name = null, $cnf = [], $master = null)
    {
        $this->_self = \PyCore::import('tkinter')->BitmapImage($name, $cnf, $master);
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
