<?php
namespace python\matplotlib\pyplot;

/**
* @property $axes
* @property $fill
* @property $mouseover
* @property $stale
* @property $sticky_edges
* @property $xy
*/
class Polygon
{
    private $_self;

    public function __construct($xy, $closed = true)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Polygon($xy, $closed);
    }

    public function add_callback($func)
    {
        return $this->_self->add_callback($func);
    }

    public function contains($mouseevent, $radius = null)
    {
        return $this->_self->contains($mouseevent, $radius);
    }

    public function contains_point($point, $radius = null)
    {
        return $this->_self->contains_point($point, $radius);
    }

    public function contains_points($points, $radius = null)
    {
        return $this->_self->contains_points($points, $radius);
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

    public function get_capstyle()
    {
        return $this->_self->get_capstyle();
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

    public function get_closed()
    {
        return $this->_self->get_closed();
    }

    public function get_cursor_data($event)
    {
        return $this->_self->get_cursor_data($event);
    }

    public function get_data_transform()
    {
        return $this->_self->get_data_transform();
    }

    public function get_ec()
    {
        return $this->_self->get_ec();
    }

    public function get_edgecolor()
    {
        return $this->_self->get_edgecolor();
    }

    public function get_extents()
    {
        return $this->_self->get_extents();
    }

    public function get_facecolor()
    {
        return $this->_self->get_facecolor();
    }

    public function get_fc()
    {
        return $this->_self->get_fc();
    }

    public function get_figure()
    {
        return $this->_self->get_figure();
    }

    public function get_fill()
    {
        return $this->_self->get_fill();
    }

    public function get_gid()
    {
        return $this->_self->get_gid();
    }

    public function get_hatch()
    {
        return $this->_self->get_hatch();
    }

    public function get_in_layout()
    {
        return $this->_self->get_in_layout();
    }

    public function get_joinstyle()
    {
        return $this->_self->get_joinstyle();
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

    public function get_patch_transform()
    {
        return $this->_self->get_patch_transform();
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

    public function get_verts()
    {
        return $this->_self->get_verts();
    }

    public function get_visible()
    {
        return $this->_self->get_visible();
    }

    public function get_window_extent($renderer = null)
    {
        return $this->_self->get_window_extent($renderer);
    }

    public function get_xy()
    {
        return $this->_self->get_xy();
    }

    public function get_zorder()
    {
        return $this->_self->get_zorder();
    }

    public function have_units()
    {
        return $this->_self->have_units();
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

    public function set_antialiased($aa)
    {
        return $this->_self->set_antialiased($aa);
    }

    public function set_capstyle($s)
    {
        return $this->_self->set_capstyle($s);
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

    public function set_closed($closed)
    {
        return $this->_self->set_closed($closed);
    }

    public function set_color($c)
    {
        return $this->_self->set_color($c);
    }

    public function set_ec()
    {
        return $this->_self->set_ec();
    }

    public function set_edgecolor($color)
    {
        return $this->_self->set_edgecolor($color);
    }

    public function set_facecolor($color)
    {
        return $this->_self->set_facecolor($color);
    }

    public function set_fc()
    {
        return $this->_self->set_fc();
    }

    public function set_figure($fig)
    {
        return $this->_self->set_figure($fig);
    }

    public function set_fill($b)
    {
        return $this->_self->set_fill($b);
    }

    public function set_gid($gid)
    {
        return $this->_self->set_gid($gid);
    }

    public function set_hatch($hatch)
    {
        return $this->_self->set_hatch($hatch);
    }

    public function set_in_layout($in_layout)
    {
        return $this->_self->set_in_layout($in_layout);
    }

    public function set_joinstyle($s)
    {
        return $this->_self->set_joinstyle($s);
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

    public function set_sketch_params($scale = null, $length = null, $randomness = null)
    {
        return $this->_self->set_sketch_params($scale, $length, $randomness);
    }

    public function set_snap($snap)
    {
        return $this->_self->set_snap($snap);
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

    public function set_xy($xy)
    {
        return $this->_self->set_xy($xy);
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
