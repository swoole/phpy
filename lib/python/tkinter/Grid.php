<?php
namespace python\tkinter;

/**
*/
class Grid
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->Grid();
    }

    public function bbox($column = null, $row = null, $col2 = null, $row2 = null)
    {
        return $this->_self->bbox($column, $row, $col2, $row2);
    }

    public function columnconfigure($index, $cnf = [])
    {
        return $this->_self->columnconfigure($index, $cnf);
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

    public function grid($cnf = [])
    {
        return $this->_self->grid($cnf);
    }

    public function grid_bbox($column = null, $row = null, $col2 = null, $row2 = null)
    {
        return $this->_self->grid_bbox($column, $row, $col2, $row2);
    }

    public function grid_columnconfigure($index, $cnf = [])
    {
        return $this->_self->grid_columnconfigure($index, $cnf);
    }

    public function grid_configure($cnf = [])
    {
        return $this->_self->grid_configure($cnf);
    }

    public function grid_forget()
    {
        return $this->_self->grid_forget();
    }

    public function grid_info()
    {
        return $this->_self->grid_info();
    }

    public function grid_location($x, $y)
    {
        return $this->_self->grid_location($x, $y);
    }

    public function grid_propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->grid_propagate($flag);
    }

    public function grid_remove()
    {
        return $this->_self->grid_remove();
    }

    public function grid_rowconfigure($index, $cnf = [])
    {
        return $this->_self->grid_rowconfigure($index, $cnf);
    }

    public function grid_size()
    {
        return $this->_self->grid_size();
    }

    public function grid_slaves($row = null, $column = null)
    {
        return $this->_self->grid_slaves($row, $column);
    }

    public function info()
    {
        return $this->_self->info();
    }

    public function location($x, $y)
    {
        return $this->_self->location($x, $y);
    }

    public function propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->propagate($flag);
    }

    public function rowconfigure($index, $cnf = [])
    {
        return $this->_self->rowconfigure($index, $cnf);
    }

    public function size()
    {
        return $this->_self->size();
    }

    public function slaves($row = null, $column = null)
    {
        return $this->_self->slaves($row, $column);
    }

}
