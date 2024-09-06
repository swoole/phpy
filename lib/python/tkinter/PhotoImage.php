<?php
namespace python\tkinter;

/**
*/
class PhotoImage
{
    private $_self;

    public function __construct($name = null, $cnf = [], $master = null)
    {
        $this->_self = \PyCore::import('tkinter')->PhotoImage($name, $cnf, $master);
    }

    public function blank()
    {
        return $this->_self->blank();
    }

    public function cget($option)
    {
        return $this->_self->cget($option);
    }

    public function config()
    {
        return $this->_self->config();
    }

    public function configure()
    {
        return $this->_self->configure();
    }

    public function copy()
    {
        return $this->_self->copy();
    }

    public function get($x, $y)
    {
        return $this->_self->get($x, $y);
    }

    public function height()
    {
        return $this->_self->height();
    }

    public function put($data, $to = null)
    {
        return $this->_self->put($data, $to);
    }

    public function subsample($x, $y = "")
    {
        return $this->_self->subsample($x, $y);
    }

    public function transparency_get($x, $y)
    {
        return $this->_self->transparency_get($x, $y);
    }

    public function transparency_set($x, $y, $boolean)
    {
        return $this->_self->transparency_set($x, $y, $boolean);
    }

    public function type()
    {
        return $this->_self->type();
    }

    public function width()
    {
        return $this->_self->width();
    }

    public function write($filename, $format = null, $from_coords = null)
    {
        return $this->_self->write($filename, $format, $from_coords);
    }

    public function zoom($x, $y = "")
    {
        return $this->_self->zoom($x, $y);
    }

}
