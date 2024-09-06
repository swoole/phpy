<?php
namespace python\matplotlib\pyplot;

/**
* @property $axes
* @property $mouseover
* @property $pickradius
* @property $stale
* @property $sticky_edges
*/
class Line2D
{
    private $_self;

    public function __construct($xdata, $ydata, $linewidth = null, $linestyle = null, $color = null, $marker = null, $markersize = null, $markeredgewidth = null, $markeredgecolor = null, $markerfacecolor = null, $markerfacecoloralt = "none", $fillstyle = null, $antialiased = null, $dash_capstyle = null, $solid_capstyle = null, $dash_joinstyle = null, $solid_joinstyle = null, $pickradius = 5, $drawstyle = null, $markevery = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Line2D($xdata, $ydata, $linewidth, $linestyle, $color, $marker, $markersize, $markeredgewidth, $markeredgecolor, $markerfacecolor, $markerfacecoloralt, $fillstyle, $antialiased, $dash_capstyle, $solid_capstyle, $dash_joinstyle, $solid_joinstyle, $pickradius, $drawstyle, $markevery);
    }

    public function add_callback($func)
    {
        return $this->_self->add_callback($func);
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

    public function draw($renderer)
    {
        return $this->_self->draw($renderer);
    }

    public function findobj($match = null, $include_self = true)
    {
        return $this->_self->findobj($match, $include_self);
    }

    public function format_cursor_data($data)
    {
        return $this->_self->format_cursor_data($data);
    }

    public function get_aa()
    {
        return $this->_self->get_aa();
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

    public function get_antialiased()
    {
        return $this->_self->get_antialiased();
    }

    public function get_c()
    {
        return $this->_self->get_c();
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

    public function get_color()
    {
        return $this->_self->get_color();
    }

    public function get_cursor_data($event)
    {
        return $this->_self->get_cursor_data($event);
    }

    public function get_dash_capstyle()
    {
        return $this->_self->get_dash_capstyle();
    }

    public function get_dash_joinstyle()
    {
        return $this->_self->get_dash_joinstyle();
    }

    public function get_data($orig = true)
    {
        return $this->_self->get_data($orig);
    }

    public function get_drawstyle()
    {
        return $this->_self->get_drawstyle();
    }

    public function get_ds()
    {
        return $this->_self->get_ds();
    }

    public function get_figure()
    {
        return $this->_self->get_figure();
    }

    public function get_fillstyle()
    {
        return $this->_self->get_fillstyle();
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

    public function get_linestyle()
    {
        return $this->_self->get_linestyle();
    }

    public function get_linewidth()
    {
        return $this->_self->get_linewidth();
    }

    public function get_ls()
    {
        return $this->_self->get_ls();
    }

    public function get_lw()
    {
        return $this->_self->get_lw();
    }

    public function get_marker()
    {
        return $this->_self->get_marker();
    }

    public function get_markeredgecolor()
    {
        return $this->_self->get_markeredgecolor();
    }

    public function get_markeredgewidth()
    {
        return $this->_self->get_markeredgewidth();
    }

    public function get_markerfacecolor()
    {
        return $this->_self->get_markerfacecolor();
    }

    public function get_markerfacecoloralt()
    {
        return $this->_self->get_markerfacecoloralt();
    }

    public function get_markersize()
    {
        return $this->_self->get_markersize();
    }

    public function get_markevery()
    {
        return $this->_self->get_markevery();
    }

    public function get_mec()
    {
        return $this->_self->get_mec();
    }

    public function get_mew()
    {
        return $this->_self->get_mew();
    }

    public function get_mfc()
    {
        return $this->_self->get_mfc();
    }

    public function get_mfcalt()
    {
        return $this->_self->get_mfcalt();
    }

    public function get_ms()
    {
        return $this->_self->get_ms();
    }

    public function get_path()
    {
        return $this->_self->get_path();
    }

    public function get_path_effects()
    {
        return $this->_self->get_path_effects();
    }

    public function get_picker()
    {
        return $this->_self->get_picker();
    }

    public function get_pickradius()
    {
        return $this->_self->get_pickradius();
    }

    public function get_rasterized()
    {
        return $this->_self->get_rasterized();
    }

    public function get_sketch_params()
    {
        return $this->_self->get_sketch_params();
    }

    public function get_snap()
    {
        return $this->_self->get_snap();
    }

    public function get_solid_capstyle()
    {
        return $this->_self->get_solid_capstyle();
    }

    public function get_solid_joinstyle()
    {
        return $this->_self->get_solid_joinstyle();
    }

    public function get_tightbbox($renderer)
    {
        return $this->_self->get_tightbbox($renderer);
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

    public function get_window_extent($renderer)
    {
        return $this->_self->get_window_extent($renderer);
    }

    public function get_xdata($orig = true)
    {
        return $this->_self->get_xdata($orig);
    }

    public function get_xydata()
    {
        return $this->_self->get_xydata();
    }

    public function get_ydata($orig = true)
    {
        return $this->_self->get_ydata($orig);
    }

    public function get_zorder()
    {
        return $this->_self->get_zorder();
    }

    public function have_units()
    {
        return $this->_self->have_units();
    }

    public function is_dashed()
    {
        return $this->_self->is_dashed();
    }

    public function is_transform_set()
    {
        return $this->_self->is_transform_set();
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

    public function recache($always = false)
    {
        return $this->_self->recache($always);
    }

    public function recache_always()
    {
        return $this->_self->recache_always();
    }

    public function remove()
    {
        return $this->_self->remove();
    }

    public function remove_callback($oid)
    {
        return $this->_self->remove_callback($oid);
    }

    public function set()
    {
        return $this->_self->set();
    }

    public function set_aa()
    {
        return $this->_self->set_aa();
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

    public function set_antialiased($b)
    {
        return $this->_self->set_antialiased($b);
    }

    public function set_c()
    {
        return $this->_self->set_c();
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

    public function set_color($color)
    {
        return $this->_self->set_color($color);
    }

    public function set_dash_capstyle($s)
    {
        return $this->_self->set_dash_capstyle($s);
    }

    public function set_dash_joinstyle($s)
    {
        return $this->_self->set_dash_joinstyle($s);
    }

    public function set_dashes($seq)
    {
        return $this->_self->set_dashes($seq);
    }

    public function set_data()
    {
        return $this->_self->set_data();
    }

    public function set_drawstyle($drawstyle)
    {
        return $this->_self->set_drawstyle($drawstyle);
    }

    public function set_ds()
    {
        return $this->_self->set_ds();
    }

    public function set_figure($fig)
    {
        return $this->_self->set_figure($fig);
    }

    public function set_fillstyle($fs)
    {
        return $this->_self->set_fillstyle($fs);
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

    public function set_linestyle($ls)
    {
        return $this->_self->set_linestyle($ls);
    }

    public function set_linewidth($w)
    {
        return $this->_self->set_linewidth($w);
    }

    public function set_ls()
    {
        return $this->_self->set_ls();
    }

    public function set_lw()
    {
        return $this->_self->set_lw();
    }

    public function set_marker($marker)
    {
        return $this->_self->set_marker($marker);
    }

    public function set_markeredgecolor($ec)
    {
        return $this->_self->set_markeredgecolor($ec);
    }

    public function set_markeredgewidth($ew)
    {
        return $this->_self->set_markeredgewidth($ew);
    }

    public function set_markerfacecolor($fc)
    {
        return $this->_self->set_markerfacecolor($fc);
    }

    public function set_markerfacecoloralt($fc)
    {
        return $this->_self->set_markerfacecoloralt($fc);
    }

    public function set_markersize($sz)
    {
        return $this->_self->set_markersize($sz);
    }

    public function set_markevery($every)
    {
        return $this->_self->set_markevery($every);
    }

    public function set_mec()
    {
        return $this->_self->set_mec();
    }

    public function set_mew()
    {
        return $this->_self->set_mew();
    }

    public function set_mfc()
    {
        return $this->_self->set_mfc();
    }

    public function set_mfcalt()
    {
        return $this->_self->set_mfcalt();
    }

    public function set_ms()
    {
        return $this->_self->set_ms();
    }

    public function set_path_effects($path_effects)
    {
        return $this->_self->set_path_effects($path_effects);
    }

    public function set_picker($p)
    {
        return $this->_self->set_picker($p);
    }

    public function set_pickradius($d)
    {
        return $this->_self->set_pickradius($d);
    }

    public function set_rasterized($rasterized)
    {
        return $this->_self->set_rasterized($rasterized);
    }

    public function set_sketch_params($scale = null, $length = null, $randomness = null)
    {
        return $this->_self->set_sketch_params($scale, $length, $randomness);
    }

    public function set_snap($snap)
    {
        return $this->_self->set_snap($snap);
    }

    public function set_solid_capstyle($s)
    {
        return $this->_self->set_solid_capstyle($s);
    }

    public function set_solid_joinstyle($s)
    {
        return $this->_self->set_solid_joinstyle($s);
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

    public function set_xdata($x)
    {
        return $this->_self->set_xdata($x);
    }

    public function set_ydata($y)
    {
        return $this->_self->set_ydata($y);
    }

    public function set_zorder($level)
    {
        return $this->_self->set_zorder($level);
    }

    public function update($props)
    {
        return $this->_self->update($props);
    }

    public function update_from($other)
    {
        return $this->_self->update_from($other);
    }

}
