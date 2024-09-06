<?php
namespace python\matplotlib\pyplot;

/**
* @property $colspan
* @property $num2
* @property $rowspan
*/
class SubplotSpec
{
    private $_self;

    public function __construct($gridspec, $num1, $num2 = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->SubplotSpec($gridspec, $num1, $num2);
    }

    public function get_geometry()
    {
        return $this->_self->get_geometry();
    }

    public function get_gridspec()
    {
        return $this->_self->get_gridspec();
    }

    public function get_position($figure, $return_all = null)
    {
        return $this->_self->get_position($figure, $return_all);
    }

    public function get_topmost_subplotspec()
    {
        return $this->_self->get_topmost_subplotspec();
    }

    public function is_first_col()
    {
        return $this->_self->is_first_col();
    }

    public function is_first_row()
    {
        return $this->_self->is_first_row();
    }

    public function is_last_col()
    {
        return $this->_self->is_last_col();
    }

    public function is_last_row()
    {
        return $this->_self->is_last_row();
    }

    public function subgridspec($nrows, $ncols)
    {
        return $this->_self->subgridspec($nrows, $ncols);
    }

}
