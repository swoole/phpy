<?php
namespace python\matplotlib\pyplot;

/**
* @property $ncols
* @property $nrows
*/
class GridSpec
{
    private $_self;

    public function __construct($nrows, $ncols, $figure = null, $left = null, $bottom = null, $right = null, $top = null, $wspace = null, $hspace = null, $width_ratios = null, $height_ratios = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->GridSpec($nrows, $ncols, $figure, $left, $bottom, $right, $top, $wspace, $hspace, $width_ratios, $height_ratios);
    }

    public function get_geometry()
    {
        return $this->_self->get_geometry();
    }

    public function get_grid_positions($fig, $raw = false)
    {
        return $this->_self->get_grid_positions($fig, $raw);
    }

    public function get_height_ratios()
    {
        return $this->_self->get_height_ratios();
    }

    public function get_subplot_params($figure = null)
    {
        return $this->_self->get_subplot_params($figure);
    }

    public function get_width_ratios()
    {
        return $this->_self->get_width_ratios();
    }

    public function locally_modified_subplot_params()
    {
        return $this->_self->locally_modified_subplot_params();
    }

    public function new_subplotspec($loc, $rowspan = 1, $colspan = 1)
    {
        return $this->_self->new_subplotspec($loc, $rowspan, $colspan);
    }

    public function set_height_ratios($height_ratios)
    {
        return $this->_self->set_height_ratios($height_ratios);
    }

    public function set_width_ratios($width_ratios)
    {
        return $this->_self->set_width_ratios($width_ratios);
    }

    public function subplots()
    {
        return $this->_self->subplots();
    }

    public function tight_layout($figure, $renderer = null, $pad = 1.08, $h_pad = null, $w_pad = null, $rect = null)
    {
        return $this->_self->tight_layout($figure, $renderer, $pad, $h_pad, $w_pad, $rect);
    }

    public function update()
    {
        return $this->_self->update();
    }

}
