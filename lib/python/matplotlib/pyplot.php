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

The explicit object-oriented API is recommended for complex plots, though
pyplot is still usually used to create the figure and often the axes in the
figure. See `.pyplot.figure`, `.pyplot.subplots`, and
`.pyplot.subplot_mosaic` to create figures, and
:doc:`Axes API </api/axes_api>` for the plotting methods on an Axes::

    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)


See :ref:`api_interfaces` for an explanation of the tradeoffs between the
implicit and explicit interfaces.
*/
class pyplot{
    /**
    * @return pyplot 
    */
    public static function import()
    {
        return \PyCore::import('matplotlib.pyplot');
    }

    public $__name__ = "matplotlib.pyplot";
    public $__package__ = "matplotlib";
    public $_backend_mod = null;

    public $Annotation = null;
    public $Arrow = null;
    public $Artist = null;
    public $AutoLocator = null;
    public $Axes = null;
    public $Button = null;
    public $Circle = null;
    public $Enum = null;
    public $ExitStack = null;
    public $Figure = null;
    public $FigureBase = null;
    public $FigureCanvasBase = null;
    public $FigureManagerBase = null;
    public $FixedFormatter = null;
    public $FixedLocator = null;
    public $FormatStrFormatter = null;
    public $Formatter = null;
    public $FuncFormatter = null;
    public $GridSpec = null;
    public $IndexLocator = null;
    public $Line2D = null;
    public $LinearLocator = null;
    public $Locator = null;
    public $LogFormatter = null;
    public $LogFormatterExponent = null;
    public $LogFormatterMathtext = null;
    public $LogLocator = null;
    public $MaxNLocator = null;
    public $MouseButton = null;
    public $MultipleLocator = null;
    public $Normalize = null;
    public $NullFormatter = null;
    public $NullLocator = null;
    public $Number = null;
    public $PolarAxes = null;
    public $Polygon = null;
    public $Rectangle = null;
    public $ScalarFormatter = null;
    public $Slider = null;
    public $Subplot = null;
    public $SubplotSpec = null;
    public $Text = null;
    public $TickHelper = null;
    public $Widget = null;
    public $_REPL_DISPLAYHOOK = null;
    public $_ReplDisplayHook = null;
    public $_api = null;
    public $_docstring = null;
    public $_interactive_bk = null;
    public $_log = null;
    public $_pylab_helpers = null;
    public $cbook = null;
    public $cm = null;
    public $color_sequences = null;
    public $colormaps = null;
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

    public function _auto_draw_if_interactive($fig, $val)
    {
    }

    public function _copy_docstring_and_deprecators($method, $func = null)
    {
    }

    public function _draw_all_if_interactive()
    {
    }

    public function _get_backend_mod()
    {
    }

    public function _get_pyplot_commands()
    {
    }

    public function _get_required_interactive_framework($backend_mod)
    {
    }

    public function _warn_if_gui_out_of_main_thread()
    {
    }

    public function acorr($x)
    {
    }

    public function angle_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
    }

    public function annotate($text, $xy, $xytext = null, $xycoords = "data", $textcoords = null, $arrowprops = null, $annotation_clip = null)
    {
    }

    public function arrow($x, $y, $dx, $dy)
    {
    }

    public function autoscale($enable = true, $axis = "both", $tight = null)
    {
    }

    public function autumn()
    {
    }

    public function axes($arg = null)
    {
    }

    public function axhline($y = 0, $xmin = 0, $xmax = 1)
    {
    }

    public function axhspan($ymin, $ymax, $xmin = 0, $xmax = 1)
    {
    }

    public function axis($arg = null)
    {
    }

    public function axline($xy1, $xy2 = null)
    {
    }

    public function axvline($x = 0, $ymin = 0, $ymax = 1)
    {
    }

    public function axvspan($xmin, $xmax, $ymin = 0, $ymax = 1)
    {
    }

    public function bar($x, $height, $width = 0.8, $bottom = null)
    {
    }

    public function bar_label($container, $labels = null)
    {
    }

    public function barbs()
    {
    }

    public function barh($y, $width, $height = 0.8, $left = null)
    {
    }

    public function bone()
    {
    }

    public function box($on = null)
    {
    }

    public function boxplot($x, $notch = null, $sym = null, $vert = null, $whis = null, $positions = null, $widths = null, $patch_artist = null, $bootstrap = null, $usermedians = null, $conf_intervals = null, $meanline = null, $showmeans = null, $showcaps = null, $showbox = null, $showfliers = null, $boxprops = null, $labels = null, $flierprops = null, $medianprops = null, $meanprops = null, $capprops = null, $whiskerprops = null, $manage_ticks = true, $autorange = false, $zorder = null, $capwidths = null)
    {
    }

    public function broken_barh($xranges, $yrange)
    {
    }

    public function cla()
    {
    }

    public function clabel($CS, $levels = null)
    {
    }

    public function clf()
    {
    }

    public function clim($vmin = null, $vmax = null)
    {
    }

    public function close($fig = null)
    {
    }

    public function cohere($x, $y, $NFFT = 256, $Fs = 2, $Fc = 0, $detrend = null, $window = null, $noverlap = 0, $pad_to = null, $sides = "default", $scale_by_freq = null)
    {
    }

    public function colorbar($mappable = null, $cax = null, $ax = null)
    {
    }

    public function connect($s, $func)
    {
    }

    public function contour()
    {
    }

    public function contourf()
    {
    }

    public function cool()
    {
    }

    public function copper()
    {
    }

    public function csd($x, $y, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
    }

    public function cycler()
    {
    }

    public function delaxes($ax = null)
    {
    }

    public function disconnect($cid)
    {
    }

    public function draw()
    {
    }

    public function draw_if_interactive()
    {
    }

    public function errorbar($x, $y, $yerr = null, $xerr = null, $fmt = "", $ecolor = null, $elinewidth = null, $capsize = null, $barsabove = false, $lolims = false, $uplims = false, $xlolims = false, $xuplims = false, $errorevery = 1, $capthick = null)
    {
    }

    public function eventplot($positions, $orientation = "horizontal", $lineoffsets = 1, $linelengths = 1, $linewidths = null, $colors = null, $alpha = null, $linestyles = "solid")
    {
    }

    public function figaspect($arg)
    {
    }

    public function figimage($X, $xo = 0, $yo = 0, $alpha = null, $norm = null, $cmap = null, $vmin = null, $vmax = null, $origin = null, $resize = false)
    {
    }

    public function figlegend()
    {
    }

    public function fignum_exists($num)
    {
    }

    public function figtext($x, $y, $s, $fontdict = null)
    {
    }

    public function figure($num = null, $figsize = null, $dpi = null)
    {
    }

    public function fill()
    {
    }

    public function fill_between($x, $y1, $y2 = 0, $where = null, $interpolate = false, $step = null)
    {
    }

    public function fill_betweenx($y, $x1, $x2 = 0, $where = null, $step = null, $interpolate = false)
    {
    }

    public function findobj($o = null, $match = null, $include_self = true)
    {
    }

    public function flag()
    {
    }

    public function gca()
    {
    }

    public function gcf()
    {
    }

    public function gci()
    {
    }

    public function get($obj)
    {
    }

    public function get_backend()
    {
    }

    public function get_cmap($name = null, $lut = null)
    {
    }

    public function get_current_fig_manager()
    {
    }

    public function get_figlabels()
    {
    }

    public function get_fignums()
    {
    }

    public function get_plot_commands()
    {
    }

    public function get_scale_names()
    {
    }

    public function getp($obj)
    {
    }

    public function ginput($n = 1, $timeout = 30, $show_clicks = true, $mouse_add = 1, $mouse_pop = 3, $mouse_stop = 2)
    {
    }

    public function gray()
    {
    }

    public function grid($visible = null, $which = "major", $axis = "both")
    {
    }

    public function hexbin($x, $y, $C = null, $gridsize = 100, $bins = null, $xscale = "linear", $yscale = "linear", $extent = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null, $edgecolors = "face", $reduce_C_function = null, $mincnt = null, $marginals = false)
    {
    }

    public function hist($x, $bins = null, $range = null, $density = false, $weights = null, $cumulative = false, $bottom = null, $histtype = "bar", $align = "mid", $orientation = "vertical", $rwidth = null, $log = false, $color = null, $label = null, $stacked = false)
    {
    }

    public function hist2d($x, $y, $bins = 10, $range = null, $density = false, $weights = null, $cmin = null, $cmax = null)
    {
    }

    public function hlines($y, $xmin, $xmax, $colors = null, $linestyles = "solid", $label = "")
    {
    }

    public function hot()
    {
    }

    public function hsv()
    {
    }

    public function imread($fname, $format = null)
    {
    }

    public function imsave($fname, $arr)
    {
    }

    public function imshow($X, $cmap = null, $norm = null)
    {
    }

    public function inferno()
    {
    }

    public function install_repl_displayhook()
    {
    }

    public function interactive($b)
    {
    }

    public function ioff()
    {
    }

    public function ion()
    {
    }

    public function isinteractive()
    {
    }

    public function jet()
    {
    }

    public function legend()
    {
    }

    public function locator_params($axis = "both", $tight = null)
    {
    }

    public function loglog()
    {
    }

    public function magma()
    {
    }

    public function magnitude_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null, $scale = null)
    {
    }

    public function margins()
    {
    }

    public function matshow($A, $fignum = null)
    {
    }

    public function minorticks_off()
    {
    }

    public function minorticks_on()
    {
    }

    public function new_figure_manager()
    {
    }

    public function nipy_spectral()
    {
    }

    public function pause($interval)
    {
    }

    public function pcolor()
    {
    }

    public function pcolormesh()
    {
    }

    public function phase_spectrum($x, $Fs = null, $Fc = null, $window = null, $pad_to = null, $sides = null)
    {
    }

    public function pie($x, $explode = null, $labels = null, $colors = null, $autopct = null, $pctdistance = 0.6, $shadow = false, $labeldistance = 1.1, $startangle = 0, $radius = 1, $counterclock = true, $wedgeprops = null, $textprops = null, $center = array (
  0 => 0,
  1 => 0,
), $frame = false, $rotatelabels = false)
    {
    }

    public function pink()
    {
    }

    public function plasma()
    {
    }

    public function plot()
    {
    }

    public function plot_date($x, $y, $fmt = "o", $tz = null, $xdate = true, $ydate = false)
    {
    }

    public function polar()
    {
    }

    public function prism()
    {
    }

    public function psd($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $pad_to = null, $sides = null, $scale_by_freq = null, $return_line = null)
    {
    }

    public function quiver()
    {
    }

    public function quiverkey($Q, $X, $Y, $U, $label)
    {
    }

    public function rc($group)
    {
    }

    public function rc_context($rc = null, $fname = null)
    {
    }

    public function rcdefaults()
    {
    }

    public function register_cmap()
    {
    }

    public function rgrids($radii = null, $labels = null, $angle = null, $fmt = null)
    {
    }

    public function savefig()
    {
    }

    public function sca($ax)
    {
    }

    public function scatter($x, $y, $s = null, $c = null, $marker = null, $cmap = null, $norm = null, $vmin = null, $vmax = null, $alpha = null, $linewidths = null)
    {
    }

    public function sci($im)
    {
    }

    public function semilogx()
    {
    }

    public function semilogy()
    {
    }

    public function set_cmap($cmap)
    {
    }

    public function set_loglevel()
    {
    }

    public function setp($obj)
    {
    }

    public function show()
    {
    }

    public function specgram($x, $NFFT = null, $Fs = null, $Fc = null, $detrend = null, $window = null, $noverlap = null, $cmap = null, $xextent = null, $pad_to = null, $sides = null, $scale_by_freq = null, $mode = null, $scale = null, $vmin = null, $vmax = null)
    {
    }

    public function spring()
    {
    }

    public function spy($Z, $precision = 0, $marker = null, $markersize = null, $aspect = "equal", $origin = "upper")
    {
    }

    public function stackplot($x)
    {
    }

    public function stairs($values, $edges = null)
    {
    }

    public function stem()
    {
    }

    public function step($x, $y)
    {
    }

    public function streamplot($x, $y, $u, $v, $density = 1, $linewidth = null, $color = null, $cmap = null, $norm = null, $arrowsize = 1, $arrowstyle = "-|>", $minlength = 0.1, $transform = null, $zorder = null, $start_points = null, $maxlength = 4, $integration_direction = "both", $broken_streamlines = true)
    {
    }

    public function subplot()
    {
    }

    public function subplot2grid($shape, $loc, $rowspan = 1, $colspan = 1, $fig = null)
    {
    }

    public function subplot_mosaic($mosaic)
    {
    }

    public function subplot_tool($targetfig = null)
    {
    }

    public function subplots($nrows = 1, $ncols = 1)
    {
    }

    public function subplots_adjust($left = null, $bottom = null, $right = null, $top = null, $wspace = null, $hspace = null)
    {
    }

    public function summer()
    {
    }

    public function suptitle($t)
    {
    }

    public function switch_backend($newbackend)
    {
    }

    public function table($cellText = null, $cellColours = null, $cellLoc = "right", $colWidths = null, $rowLabels = null, $rowColours = null, $rowLoc = "left", $colLabels = null, $colColours = null, $colLoc = "center", $loc = "bottom", $bbox = null, $edges = "closed")
    {
    }

    public function text($x, $y, $s, $fontdict = null)
    {
    }

    public function thetagrids($angles = null, $labels = null, $fmt = null)
    {
    }

    public function tick_params($axis = "both")
    {
    }

    public function ticklabel_format()
    {
    }

    public function tight_layout()
    {
    }

    public function title($label, $fontdict = null, $loc = null, $pad = null)
    {
    }

    public function tricontour()
    {
    }

    public function tricontourf()
    {
    }

    public function tripcolor()
    {
    }

    public function triplot()
    {
    }

    public function twinx($ax = null)
    {
    }

    public function twiny($ax = null)
    {
    }

    public function uninstall_repl_displayhook()
    {
    }

    public function violinplot($dataset, $positions = null, $vert = true, $widths = 0.5, $showmeans = false, $showextrema = true, $showmedians = false, $quantiles = null, $points = 100, $bw_method = null)
    {
    }

    public function viridis()
    {
    }

    public function vlines($x, $ymin, $ymax, $colors = null, $linestyles = "solid", $label = "")
    {
    }

    public function waitforbuttonpress($timeout = -1)
    {
    }

    public function winter()
    {
    }

    public function xcorr($x, $y, $normed = true, $detrend = null, $usevlines = true, $maxlags = 10)
    {
    }

    public function xkcd($scale = 1, $length = 100, $randomness = 2)
    {
    }

    public function xlabel($xlabel, $fontdict = null, $labelpad = null)
    {
    }

    public function xlim()
    {
    }

    public function xscale($value)
    {
    }

    public function xticks($ticks = null, $labels = null)
    {
    }

    public function ylabel($ylabel, $fontdict = null, $labelpad = null)
    {
    }

    public function ylim()
    {
    }

    public function yscale($value)
    {
    }

    public function yticks($ticks = null, $labels = null)
    {
    }

}
