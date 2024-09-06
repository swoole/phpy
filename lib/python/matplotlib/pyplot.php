<?php
namespace python\matplotlib;

/**

`matplotlib.pyplot` is a state-based interface to matplotlib. It provides
an implicit,  MATLAB-like, way of plotting.  It also opens figures on your
screen, and acts as the figure GUI manager.

pyplot is mainly intended for interactive plots and simple cases of
programmatic plot generation::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)

The explicit (object-oriented) API is recommended for complex plots, though
pyplot is still usually used to create the figure and often the axes in the
figure. See `.pyplot.figure`, `.pyplot.subplots`, and
`.pyplot.subplot_mosaic` to create figures, and
:doc:`Axes API <../axes_api>` for the plotting methods on an axes::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
*/
class pyplot
{
    /**
    * @return pyplot
    */
    public static function import()
    {
        return \PyCore::import('matplotlib.pyplot');
    }


    public $_INSTALL_FIG_OBSERVER = true;
    public $_IP_REGISTERED = null;
    public $__name__ = "matplotlib.pyplot";
    public $__package__ = "matplotlib";

    public $MouseButton = null;
    public $Number = null;
    public $_api = null;
    public $_interactive_bk = null;
    public $_log = null;
    public $_pylab_helpers = null;
    public $cbook = null;
    public $cm = null;
    public $colormaps = null;
    public $docstring = null;
    public $draw_all = null;
    public $functools = null;
    public $importlib = null;
    public $inspect = null;
    public $logging = null;
    public $matplotlib = null;
    public $mlab = null;
    public $np = null;
    public $rcParams = null;
    public $rcParamsDefault = null;
    public $rcParamsOrig = null;
    public $rcsetup = null;
    public $re = null;
    public $style = null;
    public $sys = null;
    public $threading = null;
    public $time = null;

    /**
    * @return mixed
    */
    public function _auto_draw_if_interactive($fig, $val)
    {
    }

    /**
    * @return mixed
    */
    public function _copy_docstring_and_deprecators($method, $func = null)
    {
    }

    /**
    * @return mixed
    */
    public function _get_required_interactive_framework($backend_mod)
    {
    }

    /**
    * @return mixed
    */
    public function _setup_pyplot_info_docstrings()
    {
    }

    /**
    * @return mixed
    */
    public function _warn_if_gui_out_of_main_thread()
    {
    }

    /**
    * @return mixed
    */
    public function acorr($x)
    {
    }

    /**
    * @return mixed
    */
    public function angle_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
    }

    /**
    * @return mixed
    */
    public function annotate($text, $xy)
    {
    }

    /**
    * @return mixed
    */
    public function arrow($x, $y, $dx, $dy)
    {
    }

    /**
    * @return mixed
    */
    public function autoscale($enable = true, $axis = "both", $tight = null)
    {
    }

    /**
    * @return mixed
    */
    public function autumn()
    {
    }

    /**
    * @return mixed
    */
    public function axes($arg = null)
    {
    }

    /**
    * @return mixed
    */
    public function axhline($y = 0, $xmin = 0, $xmax = 1)
    {
    }

    /**
    * @return mixed
    */
    public function axhspan($ymin, $ymax, $xmin = 0, $xmax = 1)
    {
    }

    /**
    * @return mixed
    */
    public function axis()
    {
    }

    /**
    * @return mixed
    */
    public function axline($xy1, $xy2 = null)
    {
    }

    /**
    * @return mixed
    */
    public function axvline($x = 0, $ymin = 0, $ymax = 1)
    {
    }

    /**
    * @return mixed
    */
    public function axvspan($xmin, $xmax, $ymin = 0, $ymax = 1)
    {
    }

    /**
    * @return mixed
    */
    public function bar($x, $height, $width = 0.8, $bottom = null)
    {
    }

    /**
    * @return mixed
    */
    public function bar_label($container, $labels = null)
    {
    }

    /**
    * @return mixed
    */
    public function barbs()
    {
    }

    /**
    * @return mixed
    */
    public function barh($y, $width, $height = 0.8, $left = null)
    {
    }

    /**
    * @return mixed
    */
    public function bone()
    {
    }

    /**
    * @return mixed
    */
    public function box($on = null)
    {
    }

    /**
    * @return mixed
    */
    public function boxplot($x, $notch = null, $sym = null, $vert = null, $whis = null, $positions = null, $widths = null, $patch_artist = null, $bootstrap = null, $usermedians = null, $conf_intervals = null, $meanline = null, $showmeans = null, $showcaps = null, $showbox = null, $showfliers = null, $boxprops = null, $labels = null, $flierprops = null, $medianprops = null, $meanprops = null, $capprops = null, $whiskerprops = null, $manage_ticks = true, $autorange = false, $zorder = null)
    {
    }

    /**
    * @return mixed
    */
    public function broken_barh($xranges, $yrange)
    {
    }

    /**
    * @return mixed
    */
    public function cla()
    {
    }

    /**
    * @return mixed
    */
    public function clabel($CS, $levels = null)
    {
    }

    /**
    * @return mixed
    */
    public function clf()
    {
    }

    /**
    * @return mixed
    */
    public function clim($vmin = null, $vmax = null)
    {
    }

    /**
    * @return mixed
    */
    public function close($fig = null)
    {
    }

    /**
    * @return mixed
    */
    public function cohere($x, $y, $NFFT = 256, $Fs = 2, $Fc = 0, $detrend = null, $window = null, $noverlap = 0, $pad_to = null, $sides = "default", $scale_by_freq = null)
    {
    }

    /**
    * @return mixed
    */
    public function colorbar($mappable = null, $cax = null, $ax = null)
    {
    }

    /**
    * @return mixed
    */
    public function connect($s, $func)
    {
    }

    /**
    * @return mixed
    */
    public function contour()
    {
    }

    /**
    * @return mixed
    */
    public function contourf()
    {
    }

    /**
    * @return mixed
    */
    public function cool()
    {
    }

    /**
    * @return mixed
    */
    public function copper()
    {
    }

    /**
    * @return mixed
    */
    public function csd($x, $y, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
    }

    /**
    * @return mixed
    */
    public function cycler()
    {
    }

    /**
    * @return mixed
    */
    public function delaxes($ax = null)
    {
    }

    /**
    * @return mixed
    */
    public function disconnect($cid)
    {
    }

    /**
    * @return mixed
    */
    public function draw()
    {
    }

    /**
    * @return mixed
    */
    public function draw_if_interactive()
    {
    }

    /**
    * @return mixed
    */
    public function errorbar($x, $y, $yerr = null, $xerr = null, $fmt = "", $ecolor = null, $elinewidth = null, $capsize = null, $barsabove = false, $lolims = false, $uplims = false, $xlolims = false, $xuplims = false, $errorevery = 1, $capthick = null)
    {
    }

    /**
    * @return mixed
    */
    public function eventplot($positions, $orientation = "horizontal", $lineoffsets = 1, $linelengths = 1, $linewidths = null, $colors = null, $linestyles = "solid")
    {
    }

    /**
    * @return mixed
    */
    public function figaspect($arg)
    {
    }

    /**
    * @return mixed
    */
    public function figimage($X, $xo = 0, $yo = 0, $alpha = null, $norm = null, $cmap = null, $vmin = null, $vmax = null, $origin = null, $resize = false)
    {
    }

    /**
    * @return mixed
    */
    public function figlegend()
    {
    }

    /**
    * @return mixed
    */
    public function fignum_exists($num)
    {
    }

    /**
    * @return mixed
    */
    public function figtext($x, $y, $s, $fontdict = null)
    {
    }

    /**
    * @return mixed
    */
    public function figure($num = null, $figsize = null, $dpi = null, $facecolor = null, $edgecolor = null, $frameon = true, $FigureClass = null, $clear = false)
    {
    }

    /**
    * @return mixed
    */
    public function fill()
    {
    }

    /**
    * @return mixed
    */
    public function fill_between($x, $y1, $y2 = 0, $where = null, $interpolate = false, $step = null)
    {
    }

    /**
    * @return mixed
    */
    public function fill_betweenx($y, $x1, $x2 = 0, $where = null, $step = null, $interpolate = false)
    {
    }

    /**
    * @return mixed
    */
    public function findobj($o = null, $match = null, $include_self = true)
    {
    }

    /**
    * @return mixed
    */
    public function flag()
    {
    }

    /**
    * @return mixed
    */
    public function gca()
    {
    }

    /**
    * @return mixed
    */
    public function gcf()
    {
    }

    /**
    * @return mixed
    */
    public function gci()
    {
    }

    /**
    * @return mixed
    */
    public function get($obj)
    {
    }

    /**
    * @return mixed
    */
    public function get_backend()
    {
    }

    /**
    * @return mixed
    */
    public function get_cmap($name = null, $lut = null)
    {
    }

    /**
    * @return mixed
    */
    public function get_current_fig_manager()
    {
    }

    /**
    * @return mixed
    */
    public function get_figlabels()
    {
    }

    /**
    * @return mixed
    */
    public function get_fignums()
    {
    }

    /**
    * @return mixed
    */
    public function get_plot_commands()
    {
    }

    /**
    * @return mixed
    */
    public function get_scale_names()
    {
    }

    /**
    * @return mixed
    */
    public function getp($obj)
    {
    }

    /**
    * @return mixed
    */
    public function ginput($n = 1, $timeout = 30, $show_clicks = true, $mouse_add = null, $mouse_pop = null, $mouse_stop = null)
    {
    }

    /**
    * @return mixed
    */
    public function gray()
    {
    }

    /**
    * @return mixed
    */
    public function grid()
    {
    }

    /**
    * @return mixed
    */
    public function hexbin($x, $y, $C = null, $gridsize = 100, $bins = null, $xscale = "linear", $yscale = "linear", $extent = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null, $edgecolors = "face", $reduce_C_function = null, $mincnt = null, $marginals = false)
    {
    }

    /**
    * @return mixed
    */
    public function hist($x, $bins = null, $range = null, $density = false, $weights = null, $cumulative = false, $bottom = null, $histtype = "bar", $align = "mid", $orientation = "vertical", $rwidth = null, $log = false, $color = null, $label = null, $stacked = false)
    {
    }

    /**
    * @return mixed
    */
    public function hist2d($x, $y, $bins = 10, $range = null, $density = false, $weights = null, $cmin = null, $cmax = null)
    {
    }

    /**
    * @return mixed
    */
    public function hlines($y, $xmin, $xmax, $colors = null, $linestyles = "solid", $label = "")
    {
    }

    /**
    * @return mixed
    */
    public function hot()
    {
    }

    /**
    * @return mixed
    */
    public function hsv()
    {
    }

    /**
    * @return mixed
    */
    public function imread($fname, $format = null)
    {
    }

    /**
    * @return mixed
    */
    public function imsave($fname, $arr)
    {
    }

    /**
    * @return mixed
    */
    public function imshow($X, $cmap = null, $norm = null)
    {
    }

    /**
    * @return mixed
    */
    public function inferno()
    {
    }

    /**
    * @return mixed
    */
    public function install_repl_displayhook()
    {
    }

    /**
    * @return mixed
    */
    public function interactive($b)
    {
    }

    /**
    * @return mixed
    */
    public function ioff()
    {
    }

    /**
    * @return mixed
    */
    public function ion()
    {
    }

    /**
    * @return mixed
    */
    public function isinteractive()
    {
    }

    /**
    * @return mixed
    */
    public function jet()
    {
    }

    /**
    * @return mixed
    */
    public function legend()
    {
    }

    /**
    * @return mixed
    */
    public function locator_params($axis = "both", $tight = null)
    {
    }

    /**
    * @return mixed
    */
    public function loglog()
    {
    }

    /**
    * @return mixed
    */
    public function magma()
    {
    }

    /**
    * @return mixed
    */
    public function magnitude_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null, $scale = null)
    {
    }

    /**
    * @return mixed
    */
    public function margins()
    {
    }

    /**
    * @return mixed
    */
    public function matshow($A, $fignum = null)
    {
    }

    /**
    * @return mixed
    */
    public function minorticks_off()
    {
    }

    /**
    * @return mixed
    */
    public function minorticks_on()
    {
    }

    /**
    * @return mixed
    */
    public function new_figure_manager($num)
    {
    }

    /**
    * @return mixed
    */
    public function nipy_spectral()
    {
    }

    /**
    * @return mixed
    */
    public function pause($interval)
    {
    }

    /**
    * @return mixed
    */
    public function pcolor()
    {
    }

    /**
    * @return mixed
    */
    public function pcolormesh()
    {
    }

    /**
    * @return mixed
    */
    public function phase_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
    }

    /**
    * @return mixed
    */
    public function pie($x, $explode = null, $labels = null, $colors = null, $autopct = null, $pctdistance = 0.6, $shadow = false, $labeldistance = 1.1, $startangle = 0, $radius = 1, $counterclock = true, $wedgeprops = null, $textprops = null, $center = array (
  0 => 0,
  1 => 0,
), $frame = false, $rotatelabels = false)
    {
    }

    /**
    * @return mixed
    */
    public function pink()
    {
    }

    /**
    * @return mixed
    */
    public function plasma()
    {
    }

    /**
    * @return mixed
    */
    public function plot()
    {
    }

    /**
    * @return mixed
    */
    public function plot_date($x, $y, $fmt = "o", $tz = null, $xdate = true, $ydate = false)
    {
    }

    /**
    * @return mixed
    */
    public function plotting()
    {
    }

    /**
    * @return mixed
    */
    public function polar()
    {
    }

    /**
    * @return mixed
    */
    public function prism()
    {
    }

    /**
    * @return mixed
    */
    public function psd($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
    }

    /**
    * @return mixed
    */
    public function quiver()
    {
    }

    /**
    * @return mixed
    */
    public function quiverkey($Q, $X, $Y, $U, $label)
    {
    }

    /**
    * @return mixed
    */
    public function rc($group)
    {
    }

    /**
    * @return mixed
    */
    public function rc_context($rc = null, $fname = null)
    {
    }

    /**
    * @return mixed
    */
    public function rcdefaults()
    {
    }

    /**
    * @return mixed
    */
    public function register_cmap($name = null, $cmap = null)
    {
    }

    /**
    * @return mixed
    */
    public function rgrids($radii = null, $labels = null, $angle = null, $fmt = null)
    {
    }

    /**
    * @return mixed
    */
    public function savefig()
    {
    }

    /**
    * @return mixed
    */
    public function sca($ax)
    {
    }

    /**
    * @return mixed
    */
    public function scatter($x, $y, $s = null, $c = null, $marker = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null)
    {
    }

    /**
    * @return mixed
    */
    public function sci($im)
    {
    }

    /**
    * @return mixed
    */
    public function semilogx()
    {
    }

    /**
    * @return mixed
    */
    public function semilogy()
    {
    }

    /**
    * @return mixed
    */
    public function set_cmap($cmap)
    {
    }

    /**
    * @return mixed
    */
    public function set_loglevel()
    {
    }

    /**
    * @return mixed
    */
    public function setp($obj)
    {
    }

    /**
    * @return mixed
    */
    public function show()
    {
    }

    /**
    * @return mixed
    */
    public function specgram($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $cmap = null, $xextent = null, $pad_to = null, $sides = null, $scale_by_freq = null, $mode = null, $scale = null, $vmin = null, $vmax = null)
    {
    }

    /**
    * @return mixed
    */
    public function spring()
    {
    }

    /**
    * @return mixed
    */
    public function spy($Z, $precision = 0, $marker = null, $markersize = null, $aspect = "equal", $origin = "upper")
    {
    }

    /**
    * @return mixed
    */
    public function stackplot($x)
    {
    }

    /**
    * @return mixed
    */
    public function stairs($values, $edges = null)
    {
    }

    /**
    * @return mixed
    */
    public function stem()
    {
    }

    /**
    * @return mixed
    */
    public function step($x, $y)
    {
    }

    /**
    * @return mixed
    */
    public function streamplot($x, $y, $u, $v, $density = 1, $linewidth = null, $color = null, $cmap = null, $norm = null, $arrowsize = 1, $arrowstyle = "-|>", $minlength = 0.1, $transform = null, $zorder = null, $start_points = null, $maxlength = 4, $integration_direction = "both")
    {
    }

    /**
    * @return mixed
    */
    public function subplot()
    {
    }

    /**
    * @return mixed
    */
    public function subplot2grid($shape, $loc, $rowspan = 1, $colspan = 1, $fig = null)
    {
    }

    /**
    * @return mixed
    */
    public function subplot_mosaic($mosaic)
    {
    }

    /**
    * @return mixed
    */
    public function subplot_tool($targetfig = null)
    {
    }

    /**
    * @return mixed
    */
    public function subplots($nrows = 1, $ncols = 1)
    {
    }

    /**
    * @return mixed
    */
    public function subplots_adjust($left = null, $bottom = null, $right = null, $top = null, $wspace = null, $hspace = null)
    {
    }

    /**
    * @return mixed
    */
    public function summer()
    {
    }

    /**
    * @return mixed
    */
    public function suptitle($t)
    {
    }

    /**
    * @return mixed
    */
    public function switch_backend($newbackend)
    {
    }

    /**
    * @return mixed
    */
    public function table($cellText = null, $cellColours = null, $cellLoc = "right", $colWidths = null, $rowLabels = null, $rowColours = null, $rowLoc = "left", $colLabels = null, $colColours = null, $colLoc = "center", $loc = "bottom", $bbox = null, $edges = "closed")
    {
    }

    /**
    * @return mixed
    */
    public function text($x, $y, $s, $fontdict = null)
    {
    }

    /**
    * @return mixed
    */
    public function thetagrids($angles = null, $labels = null, $fmt = null)
    {
    }

    /**
    * @return mixed
    */
    public function tick_params($axis = "both")
    {
    }

    /**
    * @return mixed
    */
    public function ticklabel_format()
    {
    }

    /**
    * @return mixed
    */
    public function tight_layout()
    {
    }

    /**
    * @return mixed
    */
    public function title($label, $fontdict = null, $loc = null, $pad = null)
    {
    }

    /**
    * @return mixed
    */
    public function tricontour()
    {
    }

    /**
    * @return mixed
    */
    public function tricontourf()
    {
    }

    /**
    * @return mixed
    */
    public function tripcolor()
    {
    }

    /**
    * @return mixed
    */
    public function triplot()
    {
    }

    /**
    * @return mixed
    */
    public function twinx($ax = null)
    {
    }

    /**
    * @return mixed
    */
    public function twiny($ax = null)
    {
    }

    /**
    * @return mixed
    */
    public function uninstall_repl_displayhook()
    {
    }

    /**
    * @return mixed
    */
    public function violinplot($dataset, $positions = null, $vert = true, $widths = 0.5, $showmeans = false, $showextrema = true, $showmedians = false, $quantiles = null, $points = 100, $bw_method = null)
    {
    }

    /**
    * @return mixed
    */
    public function viridis()
    {
    }

    /**
    * @return mixed
    */
    public function vlines($x, $ymin, $ymax, $colors = null, $linestyles = "solid", $label = "")
    {
    }

    /**
    * @return mixed
    */
    public function waitforbuttonpress($timeout = -1)
    {
    }

    /**
    * @return mixed
    */
    public function winter()
    {
    }

    /**
    * @return mixed
    */
    public function xcorr($x, $y, $normed = true, $detrend = null, $usevlines = true, $maxlags = 10)
    {
    }

    /**
    * @return mixed
    */
    public function xkcd($scale = 1, $length = 100, $randomness = 2)
    {
    }

    /**
    * @return mixed
    */
    public function xlabel($xlabel, $fontdict = null, $labelpad = null)
    {
    }

    /**
    * @return mixed
    */
    public function xlim()
    {
    }

    /**
    * @return mixed
    */
    public function xscale($value)
    {
    }

    /**
    * @return mixed
    */
    public function xticks($ticks = null, $labels = null)
    {
    }

    /**
    * @return mixed
    */
    public function ylabel($ylabel, $fontdict = null, $labelpad = null)
    {
    }

    /**
    * @return mixed
    */
    public function ylim()
    {
    }

    /**
    * @return mixed
    */
    public function yscale($value)
    {
    }

    /**
    * @return mixed
    */
    public function yticks($ticks = null, $labels = null)
    {
    }

}
