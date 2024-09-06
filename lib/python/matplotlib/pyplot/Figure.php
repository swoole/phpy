<?php
namespace python\matplotlib\pyplot;

/**
* @property $axes
* @property $dpi
* @property $frameon
* @property $mouseover
* @property $stale
* @property $sticky_edges
*/
class Figure
{
    private $_self;

    public function __construct($figsize = null, $dpi = null, $facecolor = null, $edgecolor = null, $linewidth = 0, $frameon = null, $subplotpars = null, $tight_layout = null, $constrained_layout = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Figure($figsize, $dpi, $facecolor, $edgecolor, $linewidth, $frameon, $subplotpars, $tight_layout, $constrained_layout);
    }

    public function add_artist($artist, $clip = false)
    {
        return $this->_self->add_artist($artist, $clip);
    }

    public function add_axes()
    {
        return $this->_self->add_axes();
    }

    public function add_axobserver($func)
    {
        return $this->_self->add_axobserver($func);
    }

    public function add_callback($func)
    {
        return $this->_self->add_callback($func);
    }

    public function add_gridspec($nrows = 1, $ncols = 1)
    {
        return $this->_self->add_gridspec($nrows, $ncols);
    }

    public function add_subfigure($subplotspec)
    {
        return $this->_self->add_subfigure($subplotspec);
    }

    public function add_subplot()
    {
        return $this->_self->add_subplot();
    }

    public function align_labels($axs = null)
    {
        return $this->_self->align_labels($axs);
    }

    public function align_xlabels($axs = null)
    {
        return $this->_self->align_xlabels($axs);
    }

    public function align_ylabels($axs = null)
    {
        return $this->_self->align_ylabels($axs);
    }

    public function autofmt_xdate($bottom = 0.2, $rotation = 30, $ha = "right", $which = "major")
    {
        return $this->_self->autofmt_xdate($bottom, $rotation, $ha, $which);
    }

    public function clear($keep_observers = false)
    {
        return $this->_self->clear($keep_observers);
    }

    public function clf($keep_observers = false)
    {
        return $this->_self->clf($keep_observers);
    }

    public function colorbar($mappable, $cax = null, $ax = null, $use_gridspec = true)
    {
        return $this->_self->colorbar($mappable, $cax, $ax, $use_gridspec);
    }

    public function contains($mouseevent)
    {
        return $this->_self->contains($mouseevent);
    }

    public function convert_xunits($x)
    {
        return $this->_self->convert_xunits($x);
    }

    public function convert_yunits($y)
    {
        return $this->_self->convert_yunits($y);
    }

    public function delaxes($ax)
    {
        return $this->_self->delaxes($ax);
    }

    public function draw($renderer)
    {
        return $this->_self->draw($renderer);
    }

    public function draw_artist($a)
    {
        return $this->_self->draw_artist($a);
    }

    public function draw_without_rendering()
    {
        return $this->_self->draw_without_rendering();
    }

    public function execute_constrained_layout($renderer = null)
    {
        return $this->_self->execute_constrained_layout($renderer);
    }

    public function figimage($X, $xo = 0, $yo = 0, $alpha = null, $norm = null, $cmap = null, $vmin = null, $vmax = null, $origin = null, $resize = false)
    {
        return $this->_self->figimage($X, $xo, $yo, $alpha, $norm, $cmap, $vmin, $vmax, $origin, $resize);
    }

    public function findobj($match = null, $include_self = true)
    {
        return $this->_self->findobj($match, $include_self);
    }

    public function format_cursor_data($data)
    {
        return $this->_self->format_cursor_data($data);
    }

    public function gca()
    {
        return $this->_self->gca();
    }

    public function get_agg_filter()
    {
        return $this->_self->get_agg_filter();
    }

    public function get_alpha()
    {
        return $this->_self->get_alpha();
    }

    public function get_animated()
    {
        return $this->_self->get_animated();
    }

    public function get_axes()
    {
        return $this->_self->get_axes();
    }

    public function get_children()
    {
        return $this->_self->get_children();
    }

    public function get_clip_box()
    {
        return $this->_self->get_clip_box();
    }

    public function get_clip_on()
    {
        return $this->_self->get_clip_on();
    }

    public function get_clip_path()
    {
        return $this->_self->get_clip_path();
    }

    public function get_constrained_layout()
    {
        return $this->_self->get_constrained_layout();
    }

    public function get_constrained_layout_pads($relative = false)
    {
        return $this->_self->get_constrained_layout_pads($relative);
    }

    public function get_cursor_data($event)
    {
        return $this->_self->get_cursor_data($event);
    }

    public function get_default_bbox_extra_artists()
    {
        return $this->_self->get_default_bbox_extra_artists();
    }

    public function get_dpi()
    {
        return $this->_self->get_dpi();
    }

    public function get_edgecolor()
    {
        return $this->_self->get_edgecolor();
    }

    public function get_facecolor()
    {
        return $this->_self->get_facecolor();
    }

    public function get_figheight()
    {
        return $this->_self->get_figheight();
    }

    public function get_figure()
    {
        return $this->_self->get_figure();
    }

    public function get_figwidth()
    {
        return $this->_self->get_figwidth();
    }

    public function get_frameon()
    {
        return $this->_self->get_frameon();
    }

    public function get_gid()
    {
        return $this->_self->get_gid();
    }

    public function get_in_layout()
    {
        return $this->_self->get_in_layout();
    }

    public function get_label()
    {
        return $this->_self->get_label();
    }

    public function get_linewidth()
    {
        return $this->_self->get_linewidth();
    }

    public function get_path_effects()
    {
        return $this->_self->get_path_effects();
    }

    public function get_picker()
    {
        return $this->_self->get_picker();
    }

    public function get_rasterized()
    {
        return $this->_self->get_rasterized();
    }

    public function get_size_inches()
    {
        return $this->_self->get_size_inches();
    }

    public function get_sketch_params()
    {
        return $this->_self->get_sketch_params();
    }

    public function get_snap()
    {
        return $this->_self->get_snap();
    }

    public function get_tight_layout()
    {
        return $this->_self->get_tight_layout();
    }

    public function get_tightbbox($renderer, $bbox_extra_artists = null)
    {
        return $this->_self->get_tightbbox($renderer, $bbox_extra_artists);
    }

    public function get_transform()
    {
        return $this->_self->get_transform();
    }

    public function get_transformed_clip_path_and_affine()
    {
        return $this->_self->get_transformed_clip_path_and_affine();
    }

    public function get_url()
    {
        return $this->_self->get_url();
    }

    public function get_visible()
    {
        return $this->_self->get_visible();
    }

    public function get_window_extent()
    {
        return $this->_self->get_window_extent();
    }

    public function get_zorder()
    {
        return $this->_self->get_zorder();
    }

    public function ginput($n = 1, $timeout = 30, $show_clicks = true, $mouse_add = null, $mouse_pop = null, $mouse_stop = null)
    {
        return $this->_self->ginput($n, $timeout, $show_clicks, $mouse_add, $mouse_pop, $mouse_stop);
    }

    public function have_units()
    {
        return $this->_self->have_units();
    }

    public function is_transform_set()
    {
        return $this->_self->is_transform_set();
    }

    public function legend()
    {
        return $this->_self->legend();
    }

    public function pchanged()
    {
        return $this->_self->pchanged();
    }

    public function pick($mouseevent)
    {
        return $this->_self->pick($mouseevent);
    }

    public function pickable()
    {
        return $this->_self->pickable();
    }

    public function properties()
    {
        return $this->_self->properties();
    }

    public function remove()
    {
        return $this->_self->remove();
    }

    public function remove_callback($oid)
    {
        return $this->_self->remove_callback($oid);
    }

    public function savefig($fname)
    {
        return $this->_self->savefig($fname);
    }

    public function sca($a)
    {
        return $this->_self->sca($a);
    }

    public function set()
    {
        return $this->_self->set();
    }

    public function set_agg_filter($filter_func)
    {
        return $this->_self->set_agg_filter($filter_func);
    }

    public function set_alpha($alpha)
    {
        return $this->_self->set_alpha($alpha);
    }

    public function set_animated($b)
    {
        return $this->_self->set_animated($b);
    }

    public function set_canvas($canvas)
    {
        return $this->_self->set_canvas($canvas);
    }

    public function set_clip_box($clipbox)
    {
        return $this->_self->set_clip_box($clipbox);
    }

    public function set_clip_on($b)
    {
        return $this->_self->set_clip_on($b);
    }

    public function set_clip_path($path, $transform = null)
    {
        return $this->_self->set_clip_path($path, $transform);
    }

    public function set_constrained_layout($constrained)
    {
        return $this->_self->set_constrained_layout($constrained);
    }

    public function set_constrained_layout_pads()
    {
        return $this->_self->set_constrained_layout_pads();
    }

    public function set_dpi($val)
    {
        return $this->_self->set_dpi($val);
    }

    public function set_edgecolor($color)
    {
        return $this->_self->set_edgecolor($color);
    }

    public function set_facecolor($color)
    {
        return $this->_self->set_facecolor($color);
    }

    public function set_figheight($val, $forward = true)
    {
        return $this->_self->set_figheight($val, $forward);
    }

    public function set_figure($fig)
    {
        return $this->_self->set_figure($fig);
    }

    public function set_figwidth($val, $forward = true)
    {
        return $this->_self->set_figwidth($val, $forward);
    }

    public function set_frameon($b)
    {
        return $this->_self->set_frameon($b);
    }

    public function set_gid($gid)
    {
        return $this->_self->set_gid($gid);
    }

    public function set_in_layout($in_layout)
    {
        return $this->_self->set_in_layout($in_layout);
    }

    public function set_label($s)
    {
        return $this->_self->set_label($s);
    }

    public function set_linewidth($linewidth)
    {
        return $this->_self->set_linewidth($linewidth);
    }

    public function set_path_effects($path_effects)
    {
        return $this->_self->set_path_effects($path_effects);
    }

    public function set_picker($picker)
    {
        return $this->_self->set_picker($picker);
    }

    public function set_rasterized($rasterized)
    {
        return $this->_self->set_rasterized($rasterized);
    }

    public function set_size_inches($w, $h = null, $forward = true)
    {
        return $this->_self->set_size_inches($w, $h, $forward);
    }

    public function set_sketch_params($scale = null, $length = null, $randomness = null)
    {
        return $this->_self->set_sketch_params($scale, $length, $randomness);
    }

    public function set_snap($snap)
    {
        return $this->_self->set_snap($snap);
    }

    public function set_tight_layout($tight)
    {
        return $this->_self->set_tight_layout($tight);
    }

    public function set_transform($t)
    {
        return $this->_self->set_transform($t);
    }

    public function set_url($url)
    {
        return $this->_self->set_url($url);
    }

    public function set_visible($b)
    {
        return $this->_self->set_visible($b);
    }

    public function set_zorder($level)
    {
        return $this->_self->set_zorder($level);
    }

    public function show($warn = true)
    {
        return $this->_self->show($warn);
    }

    public function subfigures($nrows = 1, $ncols = 1, $squeeze = true, $wspace = null, $hspace = null, $width_ratios = null, $height_ratios = null)
    {
        return $this->_self->subfigures($nrows, $ncols, $squeeze, $wspace, $hspace, $width_ratios, $height_ratios);
    }

    public function subplot_mosaic($mosaic)
    {
        return $this->_self->subplot_mosaic($mosaic);
    }

    public function subplots($nrows = 1, $ncols = 1)
    {
        return $this->_self->subplots($nrows, $ncols);
    }

    public function subplots_adjust($left = null, $bottom = null, $right = null, $top = null, $wspace = null, $hspace = null)
    {
        return $this->_self->subplots_adjust($left, $bottom, $right, $top, $wspace, $hspace);
    }

    public function suptitle($t)
    {
        return $this->_self->suptitle($t);
    }

    public function supxlabel($t)
    {
        return $this->_self->supxlabel($t);
    }

    public function supylabel($t)
    {
        return $this->_self->supylabel($t);
    }

    public function text($x, $y, $s, $fontdict = null)
    {
        return $this->_self->text($x, $y, $s, $fontdict);
    }

    public function tight_layout()
    {
        return $this->_self->tight_layout();
    }

    public function update($props)
    {
        return $this->_self->update($props);
    }

    public function update_from($other)
    {
        return $this->_self->update_from($other);
    }

    public function waitforbuttonpress($timeout = -1)
    {
        return $this->_self->waitforbuttonpress($timeout);
    }

}
