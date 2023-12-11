<?php
namespace python;

/**
Wrapper functions for Tcl/Tk.

Tkinter provides classes which allow the display, positioning and
control of widgets. Toplevel widgets are Tk and Toplevel. Other
widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
LabelFrame and PanedWindow.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under Tk.

Widgets are positioned with one of the geometry managers Place, Pack
or Grid. These managers can be called with methods place, pack, grid
available in every Widget.

Actions are bound to events by resources (e.g. keyword argument
command) or with the method bind.

Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
*/
class tkinter{
    /**
    * @return tkinter 
    */
    public static function import()
    {
        return \PyCore::import('tkinter');
    }
    public $EXCEPTION = 8;
    public $FALSE = 0;
    public $NO = 0;
    public $OFF = 0;
    public $ON = 1;
    public $READABLE = 2;
    public $TRUE = 1;
    public $TclVersion = 8.6;
    public $TkVersion = 8.6;
    public $WRITABLE = 4;
    public $YES = 1;
    public $_checkbutton_count = 0;
    public $_varnum = 0;
    public $wantobjects = 1;

    public $ACTIVE = "active";
    public $ALL = "all";
    public $ANCHOR = "anchor";
    public $ARC = "arc";
    public $BASELINE = "baseline";
    public $BEVEL = "bevel";
    public $BOTH = "both";
    public $BOTTOM = "bottom";
    public $BROWSE = "browse";
    public $BUTT = "butt";
    public $CASCADE = "cascade";
    public $CENTER = "center";
    public $CHAR = "char";
    public $CHECKBUTTON = "checkbutton";
    public $CHORD = "chord";
    public $COMMAND = "command";
    public $CURRENT = "current";
    public $DISABLED = "disabled";
    public $DOTBOX = "dotbox";
    public $E = "e";
    public $END = "end";
    public $EW = "ew";
    public $EXTENDED = "extended";
    public $FIRST = "first";
    public $FLAT = "flat";
    public $GROOVE = "groove";
    public $HIDDEN = "hidden";
    public $HORIZONTAL = "horizontal";
    public $INSERT = "insert";
    public $INSIDE = "inside";
    public $LAST = "last";
    public $LEFT = "left";
    public $MITER = "miter";
    public $MOVETO = "moveto";
    public $MULTIPLE = "multiple";
    public $N = "n";
    public $NE = "ne";
    public $NONE = "none";
    public $NORMAL = "normal";
    public $NS = "ns";
    public $NSEW = "nsew";
    public $NUMERIC = "numeric";
    public $NW = "nw";
    public $OUTSIDE = "outside";
    public $PAGES = "pages";
    public $PIESLICE = "pieslice";
    public $PROJECTING = "projecting";
    public $RADIOBUTTON = "radiobutton";
    public $RAISED = "raised";
    public $RIDGE = "ridge";
    public $RIGHT = "right";
    public $ROUND = "round";
    public $S = "s";
    public $SCROLL = "scroll";
    public $SE = "se";
    public $SEL = "sel";
    public $SEL_FIRST = "sel.first";
    public $SEL_LAST = "sel.last";
    public $SEPARATOR = "separator";
    public $SINGLE = "single";
    public $SOLID = "solid";
    public $SUNKEN = "sunken";
    public $SW = "sw";
    public $TOP = "top";
    public $UNDERLINE = "underline";
    public $UNITS = "units";
    public $VERTICAL = "vertical";
    public $W = "w";
    public $WORD = "word";
    public $X = "x";
    public $Y = "y";
    public $__name__ = "tkinter";
    public $__package__ = "tkinter";
    public $_default_root = null;
    public $_support_default_root = true;

    public $BaseWidget = null;
    public $BitmapImage = null;
    public $BooleanVar = null;
    public $Button = null;
    public $CallWrapper = null;
    public $Canvas = null;
    public $Checkbutton = null;
    public $DoubleVar = null;
    public $Entry = null;
    public $Event = null;
    public $EventType = null;
    public $Frame = null;
    public $Grid = null;
    public $Image = null;
    public $IntVar = null;
    public $Label = null;
    public $LabelFrame = null;
    public $Listbox = null;
    public $Menu = null;
    public $Menubutton = null;
    public $Message = null;
    public $Misc = null;
    public $OptionMenu = null;
    public $Pack = null;
    public $PanedWindow = null;
    public $PhotoImage = null;
    public $Place = null;
    public $Radiobutton = null;
    public $Scale = null;
    public $Scrollbar = null;
    public $Spinbox = null;
    public $StringVar = null;
    public $TclError = null;
    public $Text = null;
    public $Tk = null;
    public $Toplevel = null;
    public $Variable = null;
    public $Widget = null;
    public $Wm = null;
    public $XView = null;
    public $YView = null;
    public $_VersionInfoType = null;
    public $__path__ = null;
    public $_magic_re = null;
    public $_setit = null;
    public $_space_re = null;
    public $_tkinter = null;
    public $collections = null;
    public $constants = null;
    public $enum = null;
    public $getdouble = null;
    public $getint = null;
    public $re = null;
    public $sys = null;
    public $types = null;

    public function NoDefaultRoot()
    {
    }

    public function Tcl($screenName = null, $baseName = null, $className = "Tk", $useTk = false)
    {
    }

    public function _cnfmerge($cnfs)
    {
    }

    public function _destroy_temp_root($master)
    {
    }

    public function _exit($code = 0)
    {
    }

    public function _flatten($item)
    {
    }

    public function _get_default_root($what = null)
    {
    }

    public function _get_temp_root()
    {
    }

    public function _join($value)
    {
    }

    public function _parse_version($version)
    {
    }

    public function _splitdict($tk, $v, $cut_minus = true, $conv = null)
    {
    }

    public function _stringify($value)
    {
    }

    public function _test()
    {
    }

    public function _tkerror($err)
    {
    }

    public function getboolean($s)
    {
    }

    public function image_names()
    {
    }

    public function image_types()
    {
    }

    public function mainloop($n = 0)
    {
    }

}
