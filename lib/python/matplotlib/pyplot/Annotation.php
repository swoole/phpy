<?php
namespace python\matplotlib\pyplot;

/**
* @property $anncoords
* @property $axes
* @property $mouseover
* @property $stale
* @property $sticky_edges
* @property $xyann
* @property $xycoords
*/
class Annotation
{
    private $_self;

    public function __construct($text, $xy, $xytext = null, $xycoords = "data", $textcoords = null, $arrowprops = null, $annotation_clip = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Annotation($text, $xy, $xytext, $xycoords, $textcoords, $arrowprops, $annotation_clip);
    }

    public function add_callback($func)
    {
        return $this->_self->add_callback($func);
    }

    public function contains($event)
    {
        return $this->_self->contains($event);
    }

    public function convert_xunits($x)
    {
        return $this->_self->convert_xunits($x);
    }

    public function convert_yunits($y)
    {
        return $this->_self->convert_yunits($y);
    }

    public function draggable($state = null, $use_blit = false)
    {
        return $this->_self->draggable($state, $use_blit);
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

    public function get_anncoords()
    {
        return $this->_self->get_anncoords();
    }

    public function get_annotation_clip()
    {
        return $this->_self->get_annotation_clip();
    }

    public function get_bbox_patch()
    {
        return $this->_self->get_bbox_patch();
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

    public function get_family()
    {
        return $this->_self->get_family();
    }

    public function get_figure()
    {
        return $this->_self->get_figure();
    }

    public function get_font()
    {
        return $this->_self->get_font();
    }

    public function get_font_properties()
    {
        return $this->_self->get_font_properties();
    }

    public function get_fontfamily()
    {
        return $this->_self->get_fontfamily();
    }

    public function get_fontname()
    {
        return $this->_self->get_fontname();
    }

    public function get_fontproperties()
    {
        return $this->_self->get_fontproperties();
    }

    public function get_fontsize()
    {
        return $this->_self->get_fontsize();
    }

    public function get_fontstyle()
    {
        return $this->_self->get_fontstyle();
    }

    public function get_fontvariant()
    {
        return $this->_self->get_fontvariant();
    }

    public function get_fontweight()
    {
        return $this->_self->get_fontweight();
    }

    public function get_gid()
    {
        return $this->_self->get_gid();
    }

    public function get_ha()
    {
        return $this->_self->get_ha();
    }

    public function get_horizontalalignment()
    {
        return $this->_self->get_horizontalalignment();
    }

    public function get_in_layout()
    {
        return $this->_self->get_in_layout();
    }

    public function get_label()
    {
        return $this->_self->get_label();
    }

    public function get_math_fontfamily()
    {
        return $this->_self->get_math_fontfamily();
    }

    public function get_name()
    {
        return $this->_self->get_name();
    }

    public function get_parse_math()
    {
        return $this->_self->get_parse_math();
    }

    public function get_path_effects()
    {
        return $this->_self->get_path_effects();
    }

    public function get_picker()
    {
        return $this->_self->get_picker();
    }

    public function get_position()
    {
        return $this->_self->get_position();
    }

    public function get_prop_tup()
    {
        return $this->_self->get_prop_tup();
    }

    public function get_rasterized()
    {
        return $this->_self->get_rasterized();
    }

    public function get_rotation()
    {
        return $this->_self->get_rotation();
    }

    public function get_rotation_mode()
    {
        return $this->_self->get_rotation_mode();
    }

    public function get_size()
    {
        return $this->_self->get_size();
    }

    public function get_sketch_params()
    {
        return $this->_self->get_sketch_params();
    }

    public function get_snap()
    {
        return $this->_self->get_snap();
    }

    public function get_stretch()
    {
        return $this->_self->get_stretch();
    }

    public function get_style()
    {
        return $this->_self->get_style();
    }

    public function get_text()
    {
        return $this->_self->get_text();
    }

    public function get_tightbbox($renderer)
    {
        return $this->_self->get_tightbbox($renderer);
    }

    public function get_transform()
    {
        return $this->_self->get_transform();
    }

    public function get_transform_rotates_text()
    {
        return $this->_self->get_transform_rotates_text();
    }

    public function get_transformed_clip_path_and_affine()
    {
        return $this->_self->get_transformed_clip_path_and_affine();
    }

    public function get_unitless_position()
    {
        return $this->_self->get_unitless_position();
    }

    public function get_url()
    {
        return $this->_self->get_url();
    }

    public function get_usetex()
    {
        return $this->_self->get_usetex();
    }

    public function get_va()
    {
        return $this->_self->get_va();
    }

    public function get_variant()
    {
        return $this->_self->get_variant();
    }

    public function get_verticalalignment()
    {
        return $this->_self->get_verticalalignment();
    }

    public function get_visible()
    {
        return $this->_self->get_visible();
    }

    public function get_weight()
    {
        return $this->_self->get_weight();
    }

    public function get_window_extent($renderer = null)
    {
        return $this->_self->get_window_extent($renderer);
    }

    public function get_wrap()
    {
        return $this->_self->get_wrap();
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

    public function set_anncoords($coords)
    {
        return $this->_self->set_anncoords($coords);
    }

    public function set_annotation_clip($b)
    {
        return $this->_self->set_annotation_clip($b);
    }

    public function set_backgroundcolor($color)
    {
        return $this->_self->set_backgroundcolor($color);
    }

    public function set_bbox($rectprops)
    {
        return $this->_self->set_bbox($rectprops);
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

    public function set_family()
    {
        return $this->_self->set_family();
    }

    public function set_figure($fig)
    {
        return $this->_self->set_figure($fig);
    }

    public function set_font()
    {
        return $this->_self->set_font();
    }

    public function set_font_properties()
    {
        return $this->_self->set_font_properties();
    }

    public function set_fontfamily($fontname)
    {
        return $this->_self->set_fontfamily($fontname);
    }

    public function set_fontname($fontname)
    {
        return $this->_self->set_fontname($fontname);
    }

    public function set_fontproperties($fp)
    {
        return $this->_self->set_fontproperties($fp);
    }

    public function set_fontsize($fontsize)
    {
        return $this->_self->set_fontsize($fontsize);
    }

    public function set_fontstretch($stretch)
    {
        return $this->_self->set_fontstretch($stretch);
    }

    public function set_fontstyle($fontstyle)
    {
        return $this->_self->set_fontstyle($fontstyle);
    }

    public function set_fontvariant($variant)
    {
        return $this->_self->set_fontvariant($variant);
    }

    public function set_fontweight($weight)
    {
        return $this->_self->set_fontweight($weight);
    }

    public function set_gid($gid)
    {
        return $this->_self->set_gid($gid);
    }

    public function set_ha()
    {
        return $this->_self->set_ha();
    }

    public function set_horizontalalignment($align)
    {
        return $this->_self->set_horizontalalignment($align);
    }

    public function set_in_layout($in_layout)
    {
        return $this->_self->set_in_layout($in_layout);
    }

    public function set_label($s)
    {
        return $this->_self->set_label($s);
    }

    public function set_linespacing($spacing)
    {
        return $this->_self->set_linespacing($spacing);
    }

    public function set_ma()
    {
        return $this->_self->set_ma();
    }

    public function set_math_fontfamily($fontfamily)
    {
        return $this->_self->set_math_fontfamily($fontfamily);
    }

    public function set_multialignment($align)
    {
        return $this->_self->set_multialignment($align);
    }

    public function set_name()
    {
        return $this->_self->set_name();
    }

    public function set_parse_math($parse_math)
    {
        return $this->_self->set_parse_math($parse_math);
    }

    public function set_path_effects($path_effects)
    {
        return $this->_self->set_path_effects($path_effects);
    }

    public function set_picker($picker)
    {
        return $this->_self->set_picker($picker);
    }

    public function set_position($xy)
    {
        return $this->_self->set_position($xy);
    }

    public function set_rasterized($rasterized)
    {
        return $this->_self->set_rasterized($rasterized);
    }

    public function set_rotation($s)
    {
        return $this->_self->set_rotation($s);
    }

    public function set_rotation_mode($m)
    {
        return $this->_self->set_rotation_mode($m);
    }

    public function set_size()
    {
        return $this->_self->set_size();
    }

    public function set_sketch_params($scale = null, $length = null, $randomness = null)
    {
        return $this->_self->set_sketch_params($scale, $length, $randomness);
    }

    public function set_snap($snap)
    {
        return $this->_self->set_snap($snap);
    }

    public function set_stretch()
    {
        return $this->_self->set_stretch();
    }

    public function set_style()
    {
        return $this->_self->set_style();
    }

    public function set_text($s)
    {
        return $this->_self->set_text($s);
    }

    public function set_transform($t)
    {
        return $this->_self->set_transform($t);
    }

    public function set_transform_rotates_text($t)
    {
        return $this->_self->set_transform_rotates_text($t);
    }

    public function set_url($url)
    {
        return $this->_self->set_url($url);
    }

    public function set_usetex($usetex)
    {
        return $this->_self->set_usetex($usetex);
    }

    public function set_va()
    {
        return $this->_self->set_va();
    }

    public function set_variant()
    {
        return $this->_self->set_variant();
    }

    public function set_verticalalignment($align)
    {
        return $this->_self->set_verticalalignment($align);
    }

    public function set_visible($b)
    {
        return $this->_self->set_visible($b);
    }

    public function set_weight()
    {
        return $this->_self->set_weight();
    }

    public function set_wrap($wrap)
    {
        return $this->_self->set_wrap($wrap);
    }

    public function set_x($x)
    {
        return $this->_self->set_x($x);
    }

    public function set_y($y)
    {
        return $this->_self->set_y($y);
    }

    public function set_zorder($level)
    {
        return $this->_self->set_zorder($level);
    }

    public function update($kwargs)
    {
        return $this->_self->update($kwargs);
    }

    public function update_bbox_position_size($renderer)
    {
        return $this->_self->update_bbox_position_size($renderer);
    }

    public function update_from($other)
    {
        return $this->_self->update_from($other);
    }

    public function update_positions($renderer)
    {
        return $this->_self->update_positions($renderer);
    }

}
