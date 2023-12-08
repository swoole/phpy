<?php
namespace python\matplotlib;

use \PyModule;
use \PyCore;

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
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('matplotlib.pyplot');
            self::$Annotation = self::$__module->Annotation;
            self::$Arrow = self::$__module->Arrow;
            self::$Artist = self::$__module->Artist;
            self::$AutoLocator = self::$__module->AutoLocator;
            self::$Axes = self::$__module->Axes;
            self::$Button = self::$__module->Button;
            self::$Circle = self::$__module->Circle;
            self::$Enum = self::$__module->Enum;
            self::$ExitStack = self::$__module->ExitStack;
            self::$Figure = self::$__module->Figure;
            self::$FigureBase = self::$__module->FigureBase;
            self::$FigureCanvasBase = self::$__module->FigureCanvasBase;
            self::$FigureManagerBase = self::$__module->FigureManagerBase;
            self::$FixedFormatter = self::$__module->FixedFormatter;
            self::$FixedLocator = self::$__module->FixedLocator;
            self::$FormatStrFormatter = self::$__module->FormatStrFormatter;
            self::$Formatter = self::$__module->Formatter;
            self::$FuncFormatter = self::$__module->FuncFormatter;
            self::$GridSpec = self::$__module->GridSpec;
            self::$IndexLocator = self::$__module->IndexLocator;
            self::$Line2D = self::$__module->Line2D;
            self::$LinearLocator = self::$__module->LinearLocator;
            self::$Locator = self::$__module->Locator;
            self::$LogFormatter = self::$__module->LogFormatter;
            self::$LogFormatterExponent = self::$__module->LogFormatterExponent;
            self::$LogFormatterMathtext = self::$__module->LogFormatterMathtext;
            self::$LogLocator = self::$__module->LogLocator;
            self::$MaxNLocator = self::$__module->MaxNLocator;
            self::$MouseButton = self::$__module->MouseButton;
            self::$MultipleLocator = self::$__module->MultipleLocator;
            self::$Normalize = self::$__module->Normalize;
            self::$NullFormatter = self::$__module->NullFormatter;
            self::$NullLocator = self::$__module->NullLocator;
            self::$Number = self::$__module->Number;
            self::$PolarAxes = self::$__module->PolarAxes;
            self::$Polygon = self::$__module->Polygon;
            self::$Rectangle = self::$__module->Rectangle;
            self::$ScalarFormatter = self::$__module->ScalarFormatter;
            self::$Slider = self::$__module->Slider;
            self::$Subplot = self::$__module->Subplot;
            self::$SubplotSpec = self::$__module->SubplotSpec;
            self::$Text = self::$__module->Text;
            self::$TickHelper = self::$__module->TickHelper;
            self::$Widget = self::$__module->Widget;
            self::$_REPL_DISPLAYHOOK = self::$__module->_REPL_DISPLAYHOOK;
            self::$_ReplDisplayHook = self::$__module->_ReplDisplayHook;
            self::$_api = self::$__module->_api;
            self::$_docstring = self::$__module->_docstring;
            self::$_interactive_bk = self::$__module->_interactive_bk;
            self::$_log = self::$__module->_log;
            self::$_pylab_helpers = self::$__module->_pylab_helpers;
            self::$cbook = self::$__module->cbook;
            self::$cm = self::$__module->cm;
            self::$color_sequences = self::$__module->color_sequences;
            self::$colormaps = self::$__module->colormaps;
            self::$draw_all = self::$__module->draw_all;
            self::$functools = self::$__module->functools;
            self::$importlib = self::$__module->importlib;
            self::$inspect = self::$__module->inspect;
            self::$logging = self::$__module->logging;
            self::$matplotlib = self::$__module->matplotlib;
            self::$mlab = self::$__module->mlab;
            self::$np = self::$__module->np;
            self::$rcParams = self::$__module->rcParams;
            self::$rcParamsDefault = self::$__module->rcParamsDefault;
            self::$rcParamsOrig = self::$__module->rcParamsOrig;
            self::$rcsetup = self::$__module->rcsetup;
            self::$re = self::$__module->re;
            self::$style = self::$__module->style;
            self::$sys = self::$__module->sys;
            self::$threading = self::$__module->threading;
            self::$time = self::$__module->time;
        }
    }


    public static $__name__ = "matplotlib.pyplot";
    public static $__package__ = "matplotlib";
    public static $_backend_mod = null;

    public static $Annotation = null;
    public static $Arrow = null;
    public static $Artist = null;
    public static $AutoLocator = null;
    public static $Axes = null;
    public static $Button = null;
    public static $Circle = null;
    public static $Enum = null;
    public static $ExitStack = null;
    public static $Figure = null;
    public static $FigureBase = null;
    public static $FigureCanvasBase = null;
    public static $FigureManagerBase = null;
    public static $FixedFormatter = null;
    public static $FixedLocator = null;
    public static $FormatStrFormatter = null;
    public static $Formatter = null;
    public static $FuncFormatter = null;
    public static $GridSpec = null;
    public static $IndexLocator = null;
    public static $Line2D = null;
    public static $LinearLocator = null;
    public static $Locator = null;
    public static $LogFormatter = null;
    public static $LogFormatterExponent = null;
    public static $LogFormatterMathtext = null;
    public static $LogLocator = null;
    public static $MaxNLocator = null;
    public static $MouseButton = null;
    public static $MultipleLocator = null;
    public static $Normalize = null;
    public static $NullFormatter = null;
    public static $NullLocator = null;
    public static $Number = null;
    public static $PolarAxes = null;
    public static $Polygon = null;
    public static $Rectangle = null;
    public static $ScalarFormatter = null;
    public static $Slider = null;
    public static $Subplot = null;
    public static $SubplotSpec = null;
    public static $Text = null;
    public static $TickHelper = null;
    public static $Widget = null;
    public static $_REPL_DISPLAYHOOK = null;
    public static $_ReplDisplayHook = null;
    public static $_api = null;
    public static $_docstring = null;
    public static $_interactive_bk = null;
    public static $_log = null;
    public static $_pylab_helpers = null;
    public static $cbook = null;
    public static $cm = null;
    public static $color_sequences = null;
    public static $colormaps = null;
    public static $draw_all = null;
    public static $functools = null;
    public static $importlib = null;
    public static $inspect = null;
    public static $logging = null;
    public static $matplotlib = null;
    public static $mlab = null;
    public static $np = null;
    public static $rcParams = null;
    public static $rcParamsDefault = null;
    public static $rcParamsOrig = null;
    public static $rcsetup = null;
    public static $re = null;
    public static $style = null;
    public static $sys = null;
    public static $threading = null;
    public static $time = null;

    public static function _auto_draw_if_interactive($fig, $val)
    {
        return self::$__module->_auto_draw_if_interactive($fig, $val);
    }
    public static function _copy_docstring_and_deprecators($method, $func=null)
    {
        return self::$__module->_copy_docstring_and_deprecators($method, $func);
    }
    public static function _draw_all_if_interactive()
    {
        return self::$__module->_draw_all_if_interactive();
    }
    public static function _get_backend_mod()
    {
        return self::$__module->_get_backend_mod();
    }
    public static function _get_pyplot_commands()
    {
        return self::$__module->_get_pyplot_commands();
    }
    public static function _get_required_interactive_framework($backend_mod)
    {
        return self::$__module->_get_required_interactive_framework($backend_mod);
    }
    public static function _warn_if_gui_out_of_main_thread()
    {
        return self::$__module->_warn_if_gui_out_of_main_thread();
    }
    public static function acorr($x)
    {
        return self::$__module->acorr($x);
    }
    public static function angle_spectrum($x, $Fs=null, $Fc=null, $window=null, $pad_to=null, $sides=null)
    {
        return self::$__module->angle_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides);
    }
    public static function annotate($text, $xy, $xytext=null, $xycoords="data", $textcoords=null, $arrowprops=null, $annotation_clip=null)
    {
        return self::$__module->annotate($text, $xy, $xytext, $xycoords, $textcoords, $arrowprops, $annotation_clip);
    }
    public static function arrow($x, $y, $dx, $dy)
    {
        return self::$__module->arrow($x, $y, $dx, $dy);
    }
    public static function autoscale($enable=true, $axis="both", $tight=null)
    {
        return self::$__module->autoscale($enable, $axis, $tight);
    }
    public static function autumn()
    {
        return self::$__module->autumn();
    }
    public static function axes($arg=null)
    {
        return self::$__module->axes($arg);
    }
    public static function axhline($y=0, $xmin=0, $xmax=1)
    {
        return self::$__module->axhline($y, $xmin, $xmax);
    }
    public static function axhspan($ymin, $ymax, $xmin=0, $xmax=1)
    {
        return self::$__module->axhspan($ymin, $ymax, $xmin, $xmax);
    }
    public static function axis($arg=null)
    {
        return self::$__module->axis($arg);
    }
    public static function axline($xy1, $xy2=null)
    {
        return self::$__module->axline($xy1, $xy2);
    }
    public static function axvline($x=0, $ymin=0, $ymax=1)
    {
        return self::$__module->axvline($x, $ymin, $ymax);
    }
    public static function axvspan($xmin, $xmax, $ymin=0, $ymax=1)
    {
        return self::$__module->axvspan($xmin, $xmax, $ymin, $ymax);
    }
    public static function bar($x, $height, $width=0.8, $bottom=null)
    {
        return self::$__module->bar($x, $height, $width, $bottom);
    }
    public static function bar_label($container, $labels=null)
    {
        return self::$__module->bar_label($container, $labels);
    }
    public static function barbs()
    {
        return self::$__module->barbs();
    }
    public static function barh($y, $width, $height=0.8, $left=null)
    {
        return self::$__module->barh($y, $width, $height, $left);
    }
    public static function bone()
    {
        return self::$__module->bone();
    }
    public static function box($on=null)
    {
        return self::$__module->box($on);
    }
    public static function boxplot($x, $notch=null, $sym=null, $vert=null, $whis=null, $positions=null, $widths=null, $patch_artist=null, $bootstrap=null, $usermedians=null, $conf_intervals=null, $meanline=null, $showmeans=null, $showcaps=null, $showbox=null, $showfliers=null, $boxprops=null, $labels=null, $flierprops=null, $medianprops=null, $meanprops=null, $capprops=null, $whiskerprops=null, $manage_ticks=true, $autorange=false, $zorder=null, $capwidths=null)
    {
        return self::$__module->boxplot($x, $notch, $sym, $vert, $whis, $positions, $widths, $patch_artist, $bootstrap, $usermedians, $conf_intervals, $meanline, $showmeans, $showcaps, $showbox, $showfliers, $boxprops, $labels, $flierprops, $medianprops, $meanprops, $capprops, $whiskerprops, $manage_ticks, $autorange, $zorder, $capwidths);
    }
    public static function broken_barh($xranges, $yrange)
    {
        return self::$__module->broken_barh($xranges, $yrange);
    }
    public static function cla()
    {
        return self::$__module->cla();
    }
    public static function clabel($CS, $levels=null)
    {
        return self::$__module->clabel($CS, $levels);
    }
    public static function clf()
    {
        return self::$__module->clf();
    }
    public static function clim($vmin=null, $vmax=null)
    {
        return self::$__module->clim($vmin, $vmax);
    }
    public static function close($fig=null)
    {
        return self::$__module->close($fig);
    }
    public static function cohere($x, $y, $NFFT=256, $Fs=2, $Fc=0, $detrend=null, $window=null, $noverlap=0, $pad_to=null, $sides="default", $scale_by_freq=null)
    {
        return self::$__module->cohere($x, $y, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq);
    }
    public static function colorbar($mappable=null, $cax=null, $ax=null)
    {
        return self::$__module->colorbar($mappable, $cax, $ax);
    }
    public static function connect($s, $func)
    {
        return self::$__module->connect($s, $func);
    }
    public static function contour()
    {
        return self::$__module->contour();
    }
    public static function contourf()
    {
        return self::$__module->contourf();
    }
    public static function cool()
    {
        return self::$__module->cool();
    }
    public static function copper()
    {
        return self::$__module->copper();
    }
    public static function csd($x, $y, $NFFT=null, $Fs=null, $Fc=null, $detrend=null, $window=null, $noverlap=null, $pad_to=null, $sides=null, $scale_by_freq=null, $return_line=null)
    {
        return self::$__module->csd($x, $y, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq, $return_line);
    }
    public static function cycler()
    {
        return self::$__module->cycler();
    }
    public static function delaxes($ax=null)
    {
        return self::$__module->delaxes($ax);
    }
    public static function disconnect($cid)
    {
        return self::$__module->disconnect($cid);
    }
    public static function draw()
    {
        return self::$__module->draw();
    }
    public static function draw_if_interactive()
    {
        return self::$__module->draw_if_interactive();
    }
    public static function errorbar($x, $y, $yerr=null, $xerr=null, $fmt="", $ecolor=null, $elinewidth=null, $capsize=null, $barsabove=false, $lolims=false, $uplims=false, $xlolims=false, $xuplims=false, $errorevery=1, $capthick=null)
    {
        return self::$__module->errorbar($x, $y, $yerr, $xerr, $fmt, $ecolor, $elinewidth, $capsize, $barsabove, $lolims, $uplims, $xlolims, $xuplims, $errorevery, $capthick);
    }
    public static function eventplot($positions, $orientation="horizontal", $lineoffsets=1, $linelengths=1, $linewidths=null, $colors=null, $alpha=null, $linestyles="solid")
    {
        return self::$__module->eventplot($positions, $orientation, $lineoffsets, $linelengths, $linewidths, $colors, $alpha, $linestyles);
    }
    public static function figaspect($arg)
    {
        return self::$__module->figaspect($arg);
    }
    public static function figimage($X, $xo=0, $yo=0, $alpha=null, $norm=null, $cmap=null, $vmin=null, $vmax=null, $origin=null, $resize=false)
    {
        return self::$__module->figimage($X, $xo, $yo, $alpha, $norm, $cmap, $vmin, $vmax, $origin, $resize);
    }
    public static function figlegend()
    {
        return self::$__module->figlegend();
    }
    public static function fignum_exists($num)
    {
        return self::$__module->fignum_exists($num);
    }
    public static function figtext($x, $y, $s, $fontdict=null)
    {
        return self::$__module->figtext($x, $y, $s, $fontdict);
    }
    public static function figure($num=null, $figsize=null, $dpi=null)
    {
        return self::$__module->figure($num, $figsize, $dpi);
    }
    public static function fill()
    {
        return self::$__module->fill();
    }
    public static function fill_between($x, $y1, $y2=0, $where=null, $interpolate=false, $step=null)
    {
        return self::$__module->fill_between($x, $y1, $y2, $where, $interpolate, $step);
    }
    public static function fill_betweenx($y, $x1, $x2=0, $where=null, $step=null, $interpolate=false)
    {
        return self::$__module->fill_betweenx($y, $x1, $x2, $where, $step, $interpolate);
    }
    public static function findobj($o=null, $match=null, $include_self=true)
    {
        return self::$__module->findobj($o, $match, $include_self);
    }
    public static function flag()
    {
        return self::$__module->flag();
    }
    public static function gca()
    {
        return self::$__module->gca();
    }
    public static function gcf()
    {
        return self::$__module->gcf();
    }
    public static function gci()
    {
        return self::$__module->gci();
    }
    public static function get($obj)
    {
        return self::$__module->get($obj);
    }
    public static function get_backend()
    {
        return self::$__module->get_backend();
    }
    public static function get_cmap($name=null, $lut=null)
    {
        return self::$__module->get_cmap($name, $lut);
    }
    public static function get_current_fig_manager()
    {
        return self::$__module->get_current_fig_manager();
    }
    public static function get_figlabels()
    {
        return self::$__module->get_figlabels();
    }
    public static function get_fignums()
    {
        return self::$__module->get_fignums();
    }
    public static function get_plot_commands()
    {
        return self::$__module->get_plot_commands();
    }
    public static function get_scale_names()
    {
        return self::$__module->get_scale_names();
    }
    public static function getp($obj)
    {
        return self::$__module->getp($obj);
    }
    public static function ginput($n=1, $timeout=30, $show_clicks=true, $mouse_add=1, $mouse_pop=3, $mouse_stop=2)
    {
        return self::$__module->ginput($n, $timeout, $show_clicks, $mouse_add, $mouse_pop, $mouse_stop);
    }
    public static function gray()
    {
        return self::$__module->gray();
    }
    public static function grid($visible=null, $which="major", $axis="both")
    {
        return self::$__module->grid($visible, $which, $axis);
    }
    public static function hexbin($x, $y, $C=null, $gridsize=100, $bins=null, $xscale="linear", $yscale="linear", $extent=null, $cmap=null, $norm=null, $vmin=null, $vmax=null, $alpha=null, $linewidths=null, $edgecolors="face", $reduce_C_function=null, $mincnt=null, $marginals=false)
    {
        return self::$__module->hexbin($x, $y, $C, $gridsize, $bins, $xscale, $yscale, $extent, $cmap, $norm, $vmin, $vmax, $alpha, $linewidths, $edgecolors, $reduce_C_function, $mincnt, $marginals);
    }
    public static function hist($x, $bins=null, $range=null, $density=false, $weights=null, $cumulative=false, $bottom=null, $histtype="bar", $align="mid", $orientation="vertical", $rwidth=null, $log=false, $color=null, $label=null, $stacked=false)
    {
        return self::$__module->hist($x, $bins, $range, $density, $weights, $cumulative, $bottom, $histtype, $align, $orientation, $rwidth, $log, $color, $label, $stacked);
    }
    public static function hist2d($x, $y, $bins=10, $range=null, $density=false, $weights=null, $cmin=null, $cmax=null)
    {
        return self::$__module->hist2d($x, $y, $bins, $range, $density, $weights, $cmin, $cmax);
    }
    public static function hlines($y, $xmin, $xmax, $colors=null, $linestyles="solid", $label="")
    {
        return self::$__module->hlines($y, $xmin, $xmax, $colors, $linestyles, $label);
    }
    public static function hot()
    {
        return self::$__module->hot();
    }
    public static function hsv()
    {
        return self::$__module->hsv();
    }
    public static function imread($fname, $format=null)
    {
        return self::$__module->imread($fname, $format);
    }
    public static function imsave($fname, $arr)
    {
        return self::$__module->imsave($fname, $arr);
    }
    public static function imshow($X, $cmap=null, $norm=null)
    {
        return self::$__module->imshow($X, $cmap, $norm);
    }
    public static function inferno()
    {
        return self::$__module->inferno();
    }
    public static function install_repl_displayhook()
    {
        return self::$__module->install_repl_displayhook();
    }
    public static function interactive($b)
    {
        return self::$__module->interactive($b);
    }
    public static function ioff()
    {
        return self::$__module->ioff();
    }
    public static function ion()
    {
        return self::$__module->ion();
    }
    public static function isinteractive()
    {
        return self::$__module->isinteractive();
    }
    public static function jet()
    {
        return self::$__module->jet();
    }
    public static function legend()
    {
        return self::$__module->legend();
    }
    public static function locator_params($axis="both", $tight=null)
    {
        return self::$__module->locator_params($axis, $tight);
    }
    public static function loglog()
    {
        return self::$__module->loglog();
    }
    public static function magma()
    {
        return self::$__module->magma();
    }
    public static function magnitude_spectrum($x, $Fs=null, $Fc=null, $window=null, $pad_to=null, $sides=null, $scale=null)
    {
        return self::$__module->magnitude_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides, $scale);
    }
    public static function margins()
    {
        return self::$__module->margins();
    }
    public static function matshow($A, $fignum=null)
    {
        return self::$__module->matshow($A, $fignum);
    }
    public static function minorticks_off()
    {
        return self::$__module->minorticks_off();
    }
    public static function minorticks_on()
    {
        return self::$__module->minorticks_on();
    }
    public static function new_figure_manager()
    {
        return self::$__module->new_figure_manager();
    }
    public static function nipy_spectral()
    {
        return self::$__module->nipy_spectral();
    }
    public static function pause($interval)
    {
        return self::$__module->pause($interval);
    }
    public static function pcolor()
    {
        return self::$__module->pcolor();
    }
    public static function pcolormesh()
    {
        return self::$__module->pcolormesh();
    }
    public static function phase_spectrum($x, $Fs=null, $Fc=null, $window=null, $pad_to=null, $sides=null)
    {
        return self::$__module->phase_spectrum($x, $Fs, $Fc, $window, $pad_to, $sides);
    }
    public static function pie($x, $explode=null, $labels=null, $colors=null, $autopct=null, $pctdistance=0.6, $shadow=false, $labeldistance=1.1, $startangle=0, $radius=1, $counterclock=true, $wedgeprops=null, $textprops=null, $center=array (
  0 => 0,
  1 => 0,
), $frame=false, $rotatelabels=false)
    {
        return self::$__module->pie($x, $explode, $labels, $colors, $autopct, $pctdistance, $shadow, $labeldistance, $startangle, $radius, $counterclock, $wedgeprops, $textprops, $center, $frame, $rotatelabels);
    }
    public static function pink()
    {
        return self::$__module->pink();
    }
    public static function plasma()
    {
        return self::$__module->plasma();
    }
    public static function plot()
    {
        return self::$__module->plot();
    }
    public static function plot_date($x, $y, $fmt="o", $tz=null, $xdate=true, $ydate=false)
    {
        return self::$__module->plot_date($x, $y, $fmt, $tz, $xdate, $ydate);
    }
    public static function polar()
    {
        return self::$__module->polar();
    }
    public static function prism()
    {
        return self::$__module->prism();
    }
    public static function psd($x, $NFFT=null, $Fs=null, $Fc=null, $detrend=null, $window=null, $noverlap=null, $pad_to=null, $sides=null, $scale_by_freq=null, $return_line=null)
    {
        return self::$__module->psd($x, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $pad_to, $sides, $scale_by_freq, $return_line);
    }
    public static function quiver()
    {
        return self::$__module->quiver();
    }
    public static function quiverkey($Q, $X, $Y, $U, $label)
    {
        return self::$__module->quiverkey($Q, $X, $Y, $U, $label);
    }
    public static function rc($group)
    {
        return self::$__module->rc($group);
    }
    public static function rc_context($rc=null, $fname=null)
    {
        return self::$__module->rc_context($rc, $fname);
    }
    public static function rcdefaults()
    {
        return self::$__module->rcdefaults();
    }
    public static function register_cmap()
    {
        return self::$__module->register_cmap();
    }
    public static function rgrids($radii=null, $labels=null, $angle=null, $fmt=null)
    {
        return self::$__module->rgrids($radii, $labels, $angle, $fmt);
    }
    public static function savefig()
    {
        return self::$__module->savefig();
    }
    public static function sca($ax)
    {
        return self::$__module->sca($ax);
    }
    public static function scatter($x, $y, $s=null, $c=null, $marker=null, $cmap=null, $norm=null, $vmin=null, $vmax=null, $alpha=null, $linewidths=null)
    {
        return self::$__module->scatter($x, $y, $s, $c, $marker, $cmap, $norm, $vmin, $vmax, $alpha, $linewidths);
    }
    public static function sci($im)
    {
        return self::$__module->sci($im);
    }
    public static function semilogx()
    {
        return self::$__module->semilogx();
    }
    public static function semilogy()
    {
        return self::$__module->semilogy();
    }
    public static function set_cmap($cmap)
    {
        return self::$__module->set_cmap($cmap);
    }
    public static function set_loglevel()
    {
        return self::$__module->set_loglevel();
    }
    public static function setp($obj)
    {
        return self::$__module->setp($obj);
    }
    public static function show()
    {
        return self::$__module->show();
    }
    public static function specgram($x, $NFFT=null, $Fs=null, $Fc=null, $detrend=null, $window=null, $noverlap=null, $cmap=null, $xextent=null, $pad_to=null, $sides=null, $scale_by_freq=null, $mode=null, $scale=null, $vmin=null, $vmax=null)
    {
        return self::$__module->specgram($x, $NFFT, $Fs, $Fc, $detrend, $window, $noverlap, $cmap, $xextent, $pad_to, $sides, $scale_by_freq, $mode, $scale, $vmin, $vmax);
    }
    public static function spring()
    {
        return self::$__module->spring();
    }
    public static function spy($Z, $precision=0, $marker=null, $markersize=null, $aspect="equal", $origin="upper")
    {
        return self::$__module->spy($Z, $precision, $marker, $markersize, $aspect, $origin);
    }
    public static function stackplot($x)
    {
        return self::$__module->stackplot($x);
    }
    public static function stairs($values, $edges=null)
    {
        return self::$__module->stairs($values, $edges);
    }
    public static function stem()
    {
        return self::$__module->stem();
    }
    public static function step($x, $y)
    {
        return self::$__module->step($x, $y);
    }
    public static function streamplot($x, $y, $u, $v, $density=1, $linewidth=null, $color=null, $cmap=null, $norm=null, $arrowsize=1, $arrowstyle="-|>", $minlength=0.1, $transform=null, $zorder=null, $start_points=null, $maxlength=4, $integration_direction="both", $broken_streamlines=true)
    {
        return self::$__module->streamplot($x, $y, $u, $v, $density, $linewidth, $color, $cmap, $norm, $arrowsize, $arrowstyle, $minlength, $transform, $zorder, $start_points, $maxlength, $integration_direction, $broken_streamlines);
    }
    public static function subplot()
    {
        return self::$__module->subplot();
    }
    public static function subplot2grid($shape, $loc, $rowspan=1, $colspan=1, $fig=null)
    {
        return self::$__module->subplot2grid($shape, $loc, $rowspan, $colspan, $fig);
    }
    public static function subplot_mosaic($mosaic)
    {
        return self::$__module->subplot_mosaic($mosaic);
    }
    public static function subplot_tool($targetfig=null)
    {
        return self::$__module->subplot_tool($targetfig);
    }
    public static function subplots($nrows=1, $ncols=1)
    {
        return self::$__module->subplots($nrows, $ncols);
    }
    public static function subplots_adjust($left=null, $bottom=null, $right=null, $top=null, $wspace=null, $hspace=null)
    {
        return self::$__module->subplots_adjust($left, $bottom, $right, $top, $wspace, $hspace);
    }
    public static function summer()
    {
        return self::$__module->summer();
    }
    public static function suptitle($t)
    {
        return self::$__module->suptitle($t);
    }
    public static function switch_backend($newbackend)
    {
        return self::$__module->switch_backend($newbackend);
    }
    public static function table($cellText=null, $cellColours=null, $cellLoc="right", $colWidths=null, $rowLabels=null, $rowColours=null, $rowLoc="left", $colLabels=null, $colColours=null, $colLoc="center", $loc="bottom", $bbox=null, $edges="closed")
    {
        return self::$__module->table($cellText, $cellColours, $cellLoc, $colWidths, $rowLabels, $rowColours, $rowLoc, $colLabels, $colColours, $colLoc, $loc, $bbox, $edges);
    }
    public static function text($x, $y, $s, $fontdict=null)
    {
        return self::$__module->text($x, $y, $s, $fontdict);
    }
    public static function thetagrids($angles=null, $labels=null, $fmt=null)
    {
        return self::$__module->thetagrids($angles, $labels, $fmt);
    }
    public static function tick_params($axis="both")
    {
        return self::$__module->tick_params($axis);
    }
    public static function ticklabel_format()
    {
        return self::$__module->ticklabel_format();
    }
    public static function tight_layout()
    {
        return self::$__module->tight_layout();
    }
    public static function title($label, $fontdict=null, $loc=null, $pad=null)
    {
        return self::$__module->title($label, $fontdict, $loc, $pad);
    }
    public static function tricontour()
    {
        return self::$__module->tricontour();
    }
    public static function tricontourf()
    {
        return self::$__module->tricontourf();
    }
    public static function tripcolor()
    {
        return self::$__module->tripcolor();
    }
    public static function triplot()
    {
        return self::$__module->triplot();
    }
    public static function twinx($ax=null)
    {
        return self::$__module->twinx($ax);
    }
    public static function twiny($ax=null)
    {
        return self::$__module->twiny($ax);
    }
    public static function uninstall_repl_displayhook()
    {
        return self::$__module->uninstall_repl_displayhook();
    }
    public static function violinplot($dataset, $positions=null, $vert=true, $widths=0.5, $showmeans=false, $showextrema=true, $showmedians=false, $quantiles=null, $points=100, $bw_method=null)
    {
        return self::$__module->violinplot($dataset, $positions, $vert, $widths, $showmeans, $showextrema, $showmedians, $quantiles, $points, $bw_method);
    }
    public static function viridis()
    {
        return self::$__module->viridis();
    }
    public static function vlines($x, $ymin, $ymax, $colors=null, $linestyles="solid", $label="")
    {
        return self::$__module->vlines($x, $ymin, $ymax, $colors, $linestyles, $label);
    }
    public static function waitforbuttonpress($timeout=-1)
    {
        return self::$__module->waitforbuttonpress($timeout);
    }
    public static function winter()
    {
        return self::$__module->winter();
    }
    public static function xcorr($x, $y, $normed=true, $detrend=null, $usevlines=true, $maxlags=10)
    {
        return self::$__module->xcorr($x, $y, $normed, $detrend, $usevlines, $maxlags);
    }
    public static function xkcd($scale=1, $length=100, $randomness=2)
    {
        return self::$__module->xkcd($scale, $length, $randomness);
    }
    public static function xlabel($xlabel, $fontdict=null, $labelpad=null)
    {
        return self::$__module->xlabel($xlabel, $fontdict, $labelpad);
    }
    public static function xlim()
    {
        return self::$__module->xlim();
    }
    public static function xscale($value)
    {
        return self::$__module->xscale($value);
    }
    public static function xticks($ticks=null, $labels=null)
    {
        return self::$__module->xticks($ticks, $labels);
    }
    public static function ylabel($ylabel, $fontdict=null, $labelpad=null)
    {
        return self::$__module->ylabel($ylabel, $fontdict, $labelpad);
    }
    public static function ylim()
    {
        return self::$__module->ylim();
    }
    public static function yscale($value)
    {
        return self::$__module->yscale($value);
    }
    public static function yticks($ticks=null, $labels=null)
    {
        return self::$__module->yticks($ticks, $labels);
    }
}

pyplot::__init();
