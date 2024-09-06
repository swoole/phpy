<?php
namespace python\matplotlib\pyplot;

/**
* @property $artists
* @property $axes
* @property $collections
* @property $images
* @property $lines
* @property $mouseover
* @property $patches
* @property $stale
* @property $sticky_edges
* @property $tables
* @property $texts
* @property $use_sticky_edges
* @property $viewLim
*/
class Axes
{
    private $_self;

    public function __construct($fig, $rect)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->Axes($fig, $rect);
    }

    public function acorr($x)
    {
        return $this->_self->acorr($x);
    }

    public function add_artist($a)
    {
        return $this->_self->add_artist($a);
    }

    public function add_callback($func)
    {
        return $this->_self->add_callback($func);
    }

    public function add_child_axes($ax)
    {
        return $this->_self->add_child_axes($ax);
    }

    public function add_collection($collection, $autolim = true)
    {
        return $this->_self->add_collection($collection, $autolim);
    }

    public function add_container($container)
    {
        return $this->_self->add_container($container);
    }

    public function add_image($image)
    {
        return $this->_self->add_image($image);
    }

    public function add_line($line)
    {
        return $this->_self->add_line($line);
    }

    public function add_patch($p)
    {
        return $this->_self->add_patch($p);
    }

    public function add_table($tab)
    {
        return $this->_self->add_table($tab);
    }

    public function angle_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
        return $this->_self->angle_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides);
    }

    public function annotate($text, $xy)
    {
        return $this->_self->annotate($text, $xy);
    }

    public function apply_aspect($position = null)
    {
        return $this->_self->apply_aspect($position);
    }

    public function arrow($x, $y, $dx, $dy)
    {
        return $this->_self->arrow($x, $y, $dx, $dy);
    }

    public function autoscale($enable = true, $axis = "both", $tight = null)
    {
        return $this->_self->autoscale($enable, $axis, $tight);
    }

    public function autoscale_view($tight = null, $scalex = true, $scaley = true)
    {
        return $this->_self->autoscale_view($tight, $scalex, $scaley);
    }

    public function axhline($y = 0, $xmin = 0, $xmax = 1)
    {
        return $this->_self->axhline($y, $xmin, $xmax);
    }

    public function axhspan($ymin, $ymax, $xmin = 0, $xmax = 1)
    {
        return $this->_self->axhspan($ymin, $ymax, $xmin, $xmax);
    }

    public function axis()
    {
        return $this->_self->axis();
    }

    public function axline($xy1, $xy2 = null)
    {
        return $this->_self->axline($xy1, $xy2);
    }

    public function axvline($x = 0, $ymin = 0, $ymax = 1)
    {
        return $this->_self->axvline($x, $ymin, $ymax);
    }

    public function axvspan($xmin, $xmax, $ymin = 0, $ymax = 1)
    {
        return $this->_self->axvspan($xmin, $xmax, $ymin, $ymax);
    }

    public function bar($x, $height, $width = 0.8, $bottom = null)
    {
        return $this->_self->bar($x, $height, $width, $bottom);
    }

    public function bar_label($container, $labels = null)
    {
        return $this->_self->bar_label($container, $labels);
    }

    public function barbs()
    {
        return $this->_self->barbs();
    }

    public function barh($y, $width, $height = 0.8, $left = null)
    {
        return $this->_self->barh($y, $width, $height, $left);
    }

    public function boxplot($x, $notch = null, $sym = null, $vert = null, $whis = null, $positions = null, $widths = null, $patch_artist = null, $bootstrap = null, $usermedians = null, $conf_intervals = null, $meanline = null, $showmeans = null, $showcaps = null, $showbox = null, $showfliers = null, $boxprops = null, $labels = null, $flierprops = null, $medianprops = null, $meanprops = null, $capprops = null, $whiskerprops = null, $manage_ticks = true, $autorange = false, $zorder = null)
    {
        return $this->_self->boxplot($x, $notch, $sym, $vert, $whis, $positions, $widths, $patch_artist, $bootstrap, $usermedians, $conf_intervals, $meanline, $showmeans, $showcaps, $showbox, $showfliers, $boxprops, $labels, $flierprops, $medianprops, $meanprops, $capprops, $whiskerprops, $manage_ticks, $autorange, $zorder);
    }

    public function broken_barh($xranges, $yrange)
    {
        return $this->_self->broken_barh($xranges, $yrange);
    }

    public function bxp($bxpstats, $positions = null, $widths = null, $vert = true, $patch_artist = false, $shownotches = false, $showmeans = false, $showcaps = true, $showbox = true, $showfliers = true, $boxprops = null, $whiskerprops = null, $flierprops = null, $medianprops = null, $capprops = null, $meanprops = null, $meanline = false, $manage_ticks = true, $zorder = null)
    {
        return $this->_self->bxp($bxpstats, $positions, $widths, $vert, $patch_artist, $shownotches, $showmeans, $showcaps, $showbox, $showfliers, $boxprops, $whiskerprops, $flierprops, $medianprops, $capprops, $meanprops, $meanline, $manage_ticks, $zorder);
    }

    public function can_pan()
    {
        return $this->_self->can_pan();
    }

    public function can_zoom()
    {
        return $this->_self->can_zoom();
    }

    public function cla()
    {
        return $this->_self->cla();
    }

    public function clabel($CS, $levels = null)
    {
        return $this->_self->clabel($CS, $levels);
    }

    public function clear()
    {
        return $this->_self->clear();
    }

    public function cohere($x, $y, $NFFT = 256, $Fs = 2, $Fc = 0, $detrend = null, $window = null, $noverlap = 0, $pad_to = null, $sides = "default", $scale_by_freq = null)
    {
        return $this->_self->cohere($x, $y, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq);
    }

    public function contains($mouseevent)
    {
        return $this->_self->contains($mouseevent);
    }

    public function contains_point($point)
    {
        return $this->_self->contains_point($point);
    }

    public function contour()
    {
        return $this->_self->contour();
    }

    public function contourf()
    {
        return $this->_self->contourf();
    }

    public function convert_xunits($x)
    {
        return $this->_self->convert_xunits($x);
    }

    public function convert_yunits($y)
    {
        return $this->_self->convert_yunits($y);
    }

    public function csd($x, $y, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
        return $this->_self->csd($x, $y, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq, $return_line);
    }

    public function drag_pan($button, $key, $x, $y)
    {
        return $this->_self->drag_pan($button, $key, $x, $y);
    }

    public function draw($renderer)
    {
        return $this->_self->draw($renderer);
    }

    public function draw_artist($a)
    {
        return $this->_self->draw_artist($a);
    }

    public function end_pan()
    {
        return $this->_self->end_pan();
    }

    public function errorbar($x, $y, $yerr = null, $xerr = null, $fmt = "", $ecolor = null, $elinewidth = null, $capsize = null, $barsabove = false, $lolims = false, $uplims = false, $xlolims = false, $xuplims = false, $errorevery = 1, $capthick = null)
    {
        return $this->_self->errorbar($x, $y, $yerr, $xerr, $fmt, $ecolor, $elinewidth, $capsize, $barsabove, $lolims, $uplims, $xlolims, $xuplims, $errorevery, $capthick);
    }

    public function eventplot($positions, $orientation = "horizontal", $lineoffsets = 1, $linelengths = 1, $linewidths = null, $colors = null, $linestyles = "solid")
    {
        return $this->_self->eventplot($positions, $orientation, $lineoffsets, $linelengths, $linewidths, $colors, $linestyles);
    }

    public function fill()
    {
        return $this->_self->fill();
    }

    public function fill_between($x, $y1, $y2 = 0, $where = null, $interpolate = false, $step = null)
    {
        return $this->_self->fill_between($x, $y1, $y2, $where, $interpolate, $step);
    }

    public function fill_betweenx($y, $x1, $x2 = 0, $where = null, $step = null, $interpolate = false)
    {
        return $this->_self->fill_betweenx($y, $x1, $x2, $where, $step, $interpolate);
    }

    public function findobj($match = null, $include_self = true)
    {
        return $this->_self->findobj($match, $include_self);
    }

    public function format_coord($x, $y)
    {
        return $this->_self->format_coord($x, $y);
    }

    public function format_cursor_data($data)
    {
        return $this->_self->format_cursor_data($data);
    }

    public function format_xdata($x)
    {
        return $this->_self->format_xdata($x);
    }

    public function format_ydata($y)
    {
        return $this->_self->format_ydata($y);
    }

    public function get_adjustable()
    {
        return $this->_self->get_adjustable();
    }

    public function get_agg_filter()
    {
        return $this->_self->get_agg_filter();
    }

    public function get_alpha()
    {
        return $this->_self->get_alpha();
    }

    public function get_anchor()
    {
        return $this->_self->get_anchor();
    }

    public function get_animated()
    {
        return $this->_self->get_animated();
    }

    public function get_aspect()
    {
        return $this->_self->get_aspect();
    }

    public function get_autoscale_on()
    {
        return $this->_self->get_autoscale_on();
    }

    public function get_autoscalex_on()
    {
        return $this->_self->get_autoscalex_on();
    }

    public function get_autoscaley_on()
    {
        return $this->_self->get_autoscaley_on();
    }

    public function get_axes_locator()
    {
        return $this->_self->get_axes_locator();
    }

    public function get_axisbelow()
    {
        return $this->_self->get_axisbelow();
    }

    public function get_box_aspect()
    {
        return $this->_self->get_box_aspect();
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

    public function get_cursor_data($event)
    {
        return $this->_self->get_cursor_data($event);
    }

    public function get_data_ratio()
    {
        return $this->_self->get_data_ratio();
    }

    public function get_default_bbox_extra_artists()
    {
        return $this->_self->get_default_bbox_extra_artists();
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

    public function get_frame_on()
    {
        return $this->_self->get_frame_on();
    }

    public function get_gid()
    {
        return $this->_self->get_gid();
    }

    public function get_images()
    {
        return $this->_self->get_images();
    }

    public function get_in_layout()
    {
        return $this->_self->get_in_layout();
    }

    public function get_label()
    {
        return $this->_self->get_label();
    }

    public function get_legend()
    {
        return $this->_self->get_legend();
    }

    public function get_legend_handles_labels($legend_handler_map = null)
    {
        return $this->_self->get_legend_handles_labels($legend_handler_map);
    }

    public function get_lines()
    {
        return $this->_self->get_lines();
    }

    public function get_navigate()
    {
        return $this->_self->get_navigate();
    }

    public function get_navigate_mode()
    {
        return $this->_self->get_navigate_mode();
    }

    public function get_path_effects()
    {
        return $this->_self->get_path_effects();
    }

    public function get_picker()
    {
        return $this->_self->get_picker();
    }

    public function get_position($original = false)
    {
        return $this->_self->get_position($original);
    }

    public function get_rasterization_zorder()
    {
        return $this->_self->get_rasterization_zorder();
    }

    public function get_rasterized()
    {
        return $this->_self->get_rasterized();
    }

    public function get_renderer_cache()
    {
        return $this->_self->get_renderer_cache();
    }

    public function get_shared_x_axes()
    {
        return $this->_self->get_shared_x_axes();
    }

    public function get_shared_y_axes()
    {
        return $this->_self->get_shared_y_axes();
    }

    public function get_sketch_params()
    {
        return $this->_self->get_sketch_params();
    }

    public function get_snap()
    {
        return $this->_self->get_snap();
    }

    public function get_tightbbox($renderer, $call_axes_locator = true, $bbox_extra_artists = null)
    {
        return $this->_self->get_tightbbox($renderer, $call_axes_locator, $bbox_extra_artists);
    }

    public function get_title($loc = "center")
    {
        return $this->_self->get_title($loc);
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

    public function get_xaxis()
    {
        return $this->_self->get_xaxis();
    }

    public function get_xaxis_text1_transform($pad_points)
    {
        return $this->_self->get_xaxis_text1_transform($pad_points);
    }

    public function get_xaxis_text2_transform($pad_points)
    {
        return $this->_self->get_xaxis_text2_transform($pad_points);
    }

    public function get_xaxis_transform($which = "grid")
    {
        return $this->_self->get_xaxis_transform($which);
    }

    public function get_xbound()
    {
        return $this->_self->get_xbound();
    }

    public function get_xgridlines()
    {
        return $this->_self->get_xgridlines();
    }

    public function get_xlabel()
    {
        return $this->_self->get_xlabel();
    }

    public function get_xlim()
    {
        return $this->_self->get_xlim();
    }

    public function get_xmajorticklabels()
    {
        return $this->_self->get_xmajorticklabels();
    }

    public function get_xminorticklabels()
    {
        return $this->_self->get_xminorticklabels();
    }

    public function get_xscale()
    {
        return $this->_self->get_xscale();
    }

    public function get_xticklabels($minor = false, $which = null)
    {
        return $this->_self->get_xticklabels($minor, $which);
    }

    public function get_xticklines($minor = false)
    {
        return $this->_self->get_xticklines($minor);
    }

    public function get_xticks()
    {
        return $this->_self->get_xticks();
    }

    public function get_yaxis()
    {
        return $this->_self->get_yaxis();
    }

    public function get_yaxis_text1_transform($pad_points)
    {
        return $this->_self->get_yaxis_text1_transform($pad_points);
    }

    public function get_yaxis_text2_transform($pad_points)
    {
        return $this->_self->get_yaxis_text2_transform($pad_points);
    }

    public function get_yaxis_transform($which = "grid")
    {
        return $this->_self->get_yaxis_transform($which);
    }

    public function get_ybound()
    {
        return $this->_self->get_ybound();
    }

    public function get_ygridlines()
    {
        return $this->_self->get_ygridlines();
    }

    public function get_ylabel()
    {
        return $this->_self->get_ylabel();
    }

    public function get_ylim()
    {
        return $this->_self->get_ylim();
    }

    public function get_ymajorticklabels()
    {
        return $this->_self->get_ymajorticklabels();
    }

    public function get_yminorticklabels()
    {
        return $this->_self->get_yminorticklabels();
    }

    public function get_yscale()
    {
        return $this->_self->get_yscale();
    }

    public function get_yticklabels($minor = false, $which = null)
    {
        return $this->_self->get_yticklabels($minor, $which);
    }

    public function get_yticklines($minor = false)
    {
        return $this->_self->get_yticklines($minor);
    }

    public function get_yticks()
    {
        return $this->_self->get_yticks();
    }

    public function get_zorder()
    {
        return $this->_self->get_zorder();
    }

    public function grid()
    {
        return $this->_self->grid();
    }

    public function has_data()
    {
        return $this->_self->has_data();
    }

    public function have_units()
    {
        return $this->_self->have_units();
    }

    public function hexbin($x, $y, $C = null, $gridsize = 100, $bins = null, $xscale = "linear", $yscale = "linear", $extent = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null, $edgecolors = "face", $reduce_C_function = null, $mincnt = null, $marginals = false)
    {
        return $this->_self->hexbin($x, $y, $C, $gridsize, $bins, $xscale, $yscale, $extent, $cmap, $norm, $vmin, $vmax, $alpha, $linewidths, $edgecolors, $reduce_C_function, $mincnt, $marginals);
    }

    public function hist($x, $bins = null, $range = null, $density = false, $weights = null, $cumulative = false, $bottom = null, $histtype = "bar", $align = "mid", $orientation = "vertical", $rwidth = null, $log = false, $color = null, $label = null, $stacked = false)
    {
        return $this->_self->hist($x, $bins, $range, $density, $weights, $cumulative, $bottom, $histtype, $align, $orientation, $rwidth, $log, $color, $label, $stacked);
    }

    public function hist2d($x, $y, $bins = 10, $range = null, $density = false, $weights = null, $cmin = null, $cmax = null)
    {
        return $this->_self->hist2d($x, $y, $bins, $range, $density, $weights, $cmin, $cmax);
    }

    public function hlines($y, $xmin, $xmax, $colors = null, $linestyles = "solid", $label = "")
    {
        return $this->_self->hlines($y, $xmin, $xmax, $colors, $linestyles, $label);
    }

    public function imshow($X, $cmap = null, $norm = null)
    {
        return $this->_self->imshow($X, $cmap, $norm);
    }

    public function in_axes($mouseevent)
    {
        return $this->_self->in_axes($mouseevent);
    }

    public function indicate_inset($bounds, $inset_ax = null)
    {
        return $this->_self->indicate_inset($bounds, $inset_ax);
    }

    public function indicate_inset_zoom($inset_ax)
    {
        return $this->_self->indicate_inset_zoom($inset_ax);
    }

    public function inset_axes($bounds)
    {
        return $this->_self->inset_axes($bounds);
    }

    public function invert_xaxis()
    {
        return $this->_self->invert_xaxis();
    }

    public function invert_yaxis()
    {
        return $this->_self->invert_yaxis();
    }

    public function is_transform_set()
    {
        return $this->_self->is_transform_set();
    }

    public function legend()
    {
        return $this->_self->legend();
    }

    public function locator_params($axis = "both", $tight = null)
    {
        return $this->_self->locator_params($axis, $tight);
    }

    public function loglog()
    {
        return $this->_self->loglog();
    }

    public function magnitude_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null, $scale = null)
    {
        return $this->_self->magnitude_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides, $scale);
    }

    public function margins()
    {
        return $this->_self->margins();
    }

    public function matshow($Z)
    {
        return $this->_self->matshow($Z);
    }

    public function minorticks_off()
    {
        return $this->_self->minorticks_off();
    }

    public function minorticks_on()
    {
        return $this->_self->minorticks_on();
    }

    public function pchanged()
    {
        return $this->_self->pchanged();
    }

    public function pcolor()
    {
        return $this->_self->pcolor();
    }

    public function pcolorfast()
    {
        return $this->_self->pcolorfast();
    }

    public function pcolormesh()
    {
        return $this->_self->pcolormesh();
    }

    public function phase_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
        return $this->_self->phase_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides);
    }

    public function pick($mouseevent)
    {
        return $this->_self->pick($mouseevent);
    }

    public function pickable()
    {
        return $this->_self->pickable();
    }

    public function pie($x, $explode = null, $labels = null, $colors = null, $autopct = null, $pctdistance = 0.6, $shadow = false, $labeldistance = 1.1, $startangle = 0, $radius = 1, $counterclock = true, $wedgeprops = null, $textprops = null, $center = array (
  0 => 0,
  1 => 0,
), $frame = false, $rotatelabels = false)
    {
        return $this->_self->pie($x, $explode, $labels, $colors, $autopct, $pctdistance, $shadow, $labeldistance, $startangle, $radius, $counterclock, $wedgeprops, $textprops, $center, $frame, $rotatelabels);
    }

    public function plot()
    {
        return $this->_self->plot();
    }

    public function plot_date($x, $y, $fmt = "o", $tz = null, $xdate = true, $ydate = false)
    {
        return $this->_self->plot_date($x, $y, $fmt, $tz, $xdate, $ydate);
    }

    public function properties()
    {
        return $this->_self->properties();
    }

    public function psd($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
        return $this->_self->psd($x, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq, $return_line);
    }

    public function quiver()
    {
        return $this->_self->quiver();
    }

    public function quiverkey($Q, $X, $Y, $U, $label)
    {
        return $this->_self->quiverkey($Q, $X, $Y, $U, $label);
    }

    public function redraw_in_frame()
    {
        return $this->_self->redraw_in_frame();
    }

    public function relim($visible_only = false)
    {
        return $this->_self->relim($visible_only);
    }

    public function remove()
    {
        return $this->_self->remove();
    }

    public function remove_callback($oid)
    {
        return $this->_self->remove_callback($oid);
    }

    public function reset_position()
    {
        return $this->_self->reset_position();
    }

    public function scatter($x, $y, $s = null, $c = null, $marker = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null)
    {
        return $this->_self->scatter($x, $y, $s, $c, $marker, $cmap, $norm, $vmin, $vmax, $alpha, $linewidths);
    }

    public function secondary_xaxis($location)
    {
        return $this->_self->secondary_xaxis($location);
    }

    public function secondary_yaxis($location)
    {
        return $this->_self->secondary_yaxis($location);
    }

    public function semilogx()
    {
        return $this->_self->semilogx();
    }

    public function semilogy()
    {
        return $this->_self->semilogy();
    }

    public function set()
    {
        return $this->_self->set();
    }

    public function set_adjustable($adjustable, $share = false)
    {
        return $this->_self->set_adjustable($adjustable, $share);
    }

    public function set_agg_filter($filter_func)
    {
        return $this->_self->set_agg_filter($filter_func);
    }

    public function set_alpha($alpha)
    {
        return $this->_self->set_alpha($alpha);
    }

    public function set_anchor($anchor, $share = false)
    {
        return $this->_self->set_anchor($anchor, $share);
    }

    public function set_animated($b)
    {
        return $this->_self->set_animated($b);
    }

    public function set_aspect($aspect, $adjustable = null, $anchor = null, $share = false)
    {
        return $this->_self->set_aspect($aspect, $adjustable, $anchor, $share);
    }

    public function set_autoscale_on($b)
    {
        return $this->_self->set_autoscale_on($b);
    }

    public function set_autoscalex_on($b)
    {
        return $this->_self->set_autoscalex_on($b);
    }

    public function set_autoscaley_on($b)
    {
        return $this->_self->set_autoscaley_on($b);
    }

    public function set_axes_locator($locator)
    {
        return $this->_self->set_axes_locator($locator);
    }

    public function set_axis_off()
    {
        return $this->_self->set_axis_off();
    }

    public function set_axis_on()
    {
        return $this->_self->set_axis_on();
    }

    public function set_axisbelow($b)
    {
        return $this->_self->set_axisbelow($b);
    }

    public function set_box_aspect($aspect = null)
    {
        return $this->_self->set_box_aspect($aspect);
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

    public function set_frame_on($b)
    {
        return $this->_self->set_frame_on($b);
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

    public function set_navigate($b)
    {
        return $this->_self->set_navigate($b);
    }

    public function set_navigate_mode($b)
    {
        return $this->_self->set_navigate_mode($b);
    }

    public function set_path_effects($path_effects)
    {
        return $this->_self->set_path_effects($path_effects);
    }

    public function set_picker($picker)
    {
        return $this->_self->set_picker($picker);
    }

    public function set_position($pos, $which = "both")
    {
        return $this->_self->set_position($pos, $which);
    }

    public function set_prop_cycle()
    {
        return $this->_self->set_prop_cycle();
    }

    public function set_rasterization_zorder($z)
    {
        return $this->_self->set_rasterization_zorder($z);
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

    public function set_title($label, $fontdict = null, $loc = null, $pad = null)
    {
        return $this->_self->set_title($label, $fontdict, $loc, $pad);
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

    public function set_xbound($lower = null, $upper = null)
    {
        return $this->_self->set_xbound($lower, $upper);
    }

    public function set_xlabel($xlabel, $fontdict = null, $labelpad = null)
    {
        return $this->_self->set_xlabel($xlabel, $fontdict, $labelpad);
    }

    public function set_xlim($left = null, $right = null, $emit = true, $auto = false)
    {
        return $this->_self->set_xlim($left, $right, $emit, $auto);
    }

    public function set_xmargin($m)
    {
        return $this->_self->set_xmargin($m);
    }

    public function set_xscale($value)
    {
        return $this->_self->set_xscale($value);
    }

    public function set_xticklabels($labels)
    {
        return $this->_self->set_xticklabels($labels);
    }

    public function set_xticks($ticks, $labels = null)
    {
        return $this->_self->set_xticks($ticks, $labels);
    }

    public function set_ybound($lower = null, $upper = null)
    {
        return $this->_self->set_ybound($lower, $upper);
    }

    public function set_ylabel($ylabel, $fontdict = null, $labelpad = null)
    {
        return $this->_self->set_ylabel($ylabel, $fontdict, $labelpad);
    }

    public function set_ylim($bottom = null, $top = null, $emit = true, $auto = false)
    {
        return $this->_self->set_ylim($bottom, $top, $emit, $auto);
    }

    public function set_ymargin($m)
    {
        return $this->_self->set_ymargin($m);
    }

    public function set_yscale($value)
    {
        return $this->_self->set_yscale($value);
    }

    public function set_yticklabels($labels)
    {
        return $this->_self->set_yticklabels($labels);
    }

    public function set_yticks($ticks, $labels = null)
    {
        return $this->_self->set_yticks($ticks, $labels);
    }

    public function set_zorder($level)
    {
        return $this->_self->set_zorder($level);
    }

    public function sharex($other)
    {
        return $this->_self->sharex($other);
    }

    public function sharey($other)
    {
        return $this->_self->sharey($other);
    }

    public function specgram($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $cmap = null, $xextent = null, $pad_to = null, $sides = null, $scale_by_freq = null, $mode = null, $scale = null, $vmin = null, $vmax = null)
    {
        return $this->_self->specgram($x, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $cmap, $xextent, $pad_to, $sides, $scale_by_freq, $mode, $scale, $vmin, $vmax);
    }

    public function spy($Z, $precision = 0, $marker = null, $markersize = null, $aspect = "equal", $origin = "upper")
    {
        return $this->_self->spy($Z, $precision, $marker, $markersize, $aspect, $origin);
    }

    public function stackplot($x)
    {
        return $this->_self->stackplot($x);
    }

    public function stairs($values, $edges = null)
    {
        return $this->_self->stairs($values, $edges);
    }

    public function start_pan($x, $y, $button)
    {
        return $this->_self->start_pan($x, $y, $button);
    }

    public function stem()
    {
        return $this->_self->stem();
    }

    public function step($x, $y)
    {
        return $this->_self->step($x, $y);
    }

    public function streamplot($x, $y, $u, $v, $density = 1, $linewidth = null, $color = null, $cmap = null, $norm = null, $arrowsize = 1, $arrowstyle = "-|>", $minlength = 0.1, $transform = null, $zorder = null, $start_points = null, $maxlength = 4, $integration_direction = "both")
    {
        return $this->_self->streamplot($x, $y, $u, $v, $density, $linewidth, $color, $cmap, $norm, $arrowsize, $arrowstyle, $minlength, $transform, $zorder, $start_points, $maxlength, $integration_direction);
    }

    public function table($cellText = null, $cellColours = null, $cellLoc = "right", $colWidths = null, $rowLabels = null, $rowColours = null, $rowLoc = "left", $colLabels = null, $colColours = null, $colLoc = "center", $loc = "bottom", $bbox = null, $edges = "closed")
    {
        return $this->_self->table($cellText, $cellColours, $cellLoc, $colWidths, $rowLabels, $rowColours, $rowLoc, $colLabels, $colColours, $colLoc, $loc, $bbox, $edges);
    }

    public function text($x, $y, $s, $fontdict = null)
    {
        return $this->_self->text($x, $y, $s, $fontdict);
    }

    public function tick_params($axis = "both")
    {
        return $this->_self->tick_params($axis);
    }

    public function ticklabel_format()
    {
        return $this->_self->ticklabel_format();
    }

    public function tricontour()
    {
        return $this->_self->tricontour();
    }

    public function tricontourf()
    {
        return $this->_self->tricontourf();
    }

    public function tripcolor()
    {
        return $this->_self->tripcolor();
    }

    public function triplot()
    {
        return $this->_self->triplot();
    }

    public function twinx()
    {
        return $this->_self->twinx();
    }

    public function twiny()
    {
        return $this->_self->twiny();
    }

    public function update($props)
    {
        return $this->_self->update($props);
    }

    public function update_datalim($xys, $updatex = true, $updatey = true)
    {
        return $this->_self->update_datalim($xys, $updatex, $updatey);
    }

    public function update_from($other)
    {
        return $this->_self->update_from($other);
    }

    public function violin($vpstats, $positions = null, $vert = true, $widths = 0.5, $showmeans = false, $showextrema = true, $showmedians = false)
    {
        return $this->_self->violin($vpstats, $positions, $vert, $widths, $showmeans, $showextrema, $showmedians);
    }

    public function violinplot($dataset, $positions = null, $vert = true, $widths = 0.5, $showmeans = false, $showextrema = true, $showmedians = false, $quantiles = null, $points = 100, $bw_method = null)
    {
        return $this->_self->violinplot($dataset, $positions, $vert, $widths, $showmeans, $showextrema, $showmedians, $quantiles, $points, $bw_method);
    }

    public function vlines($x, $ymin, $ymax, $colors = null, $linestyles = "solid", $label = "")
    {
        return $this->_self->vlines($x, $ymin, $ymax, $colors, $linestyles, $label);
    }

    public function xaxis_date($tz = null)
    {
        return $this->_self->xaxis_date($tz);
    }

    public function xaxis_inverted()
    {
        return $this->_self->xaxis_inverted();
    }

    public function xcorr($x, $y, $normed = true, $detrend = null, $usevlines = true, $maxlags = 10)
    {
        return $this->_self->xcorr($x, $y, $normed, $detrend, $usevlines, $maxlags);
    }

    public function yaxis_date($tz = null)
    {
        return $this->_self->yaxis_date($tz);
    }

    public function yaxis_inverted()
    {
        return $this->_self->yaxis_inverted();
    }

}
