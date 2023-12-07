<?php
namespace python;

use \PyModule;
use \PyCore;

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
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('tkinter');
            self::$BaseWidget = self::$__module->BaseWidget;
            self::$BitmapImage = self::$__module->BitmapImage;
            self::$BooleanVar = self::$__module->BooleanVar;
            self::$Button = self::$__module->Button;
            self::$CallWrapper = self::$__module->CallWrapper;
            self::$Canvas = self::$__module->Canvas;
            self::$Checkbutton = self::$__module->Checkbutton;
            self::$DoubleVar = self::$__module->DoubleVar;
            self::$Entry = self::$__module->Entry;
            self::$Event = self::$__module->Event;
            self::$EventType = self::$__module->EventType;
            self::$Frame = self::$__module->Frame;
            self::$Grid = self::$__module->Grid;
            self::$Image = self::$__module->Image;
            self::$IntVar = self::$__module->IntVar;
            self::$Label = self::$__module->Label;
            self::$LabelFrame = self::$__module->LabelFrame;
            self::$Listbox = self::$__module->Listbox;
            self::$Menu = self::$__module->Menu;
            self::$Menubutton = self::$__module->Menubutton;
            self::$Message = self::$__module->Message;
            self::$Misc = self::$__module->Misc;
            self::$OptionMenu = self::$__module->OptionMenu;
            self::$Pack = self::$__module->Pack;
            self::$PanedWindow = self::$__module->PanedWindow;
            self::$PhotoImage = self::$__module->PhotoImage;
            self::$Place = self::$__module->Place;
            self::$Radiobutton = self::$__module->Radiobutton;
            self::$Scale = self::$__module->Scale;
            self::$Scrollbar = self::$__module->Scrollbar;
            self::$Spinbox = self::$__module->Spinbox;
            self::$StringVar = self::$__module->StringVar;
            self::$TclError = self::$__module->TclError;
            self::$Text = self::$__module->Text;
            self::$Tk = self::$__module->Tk;
            self::$Toplevel = self::$__module->Toplevel;
            self::$Variable = self::$__module->Variable;
            self::$Widget = self::$__module->Widget;
            self::$Wm = self::$__module->Wm;
            self::$XView = self::$__module->XView;
            self::$YView = self::$__module->YView;
            self::$_VersionInfoType = self::$__module->_VersionInfoType;
            self::$__path__ = self::$__module->__path__;
            self::$__spec__ = self::$__module->__spec__;
            self::$_magic_re = self::$__module->_magic_re;
            self::$_setit = self::$__module->_setit;
            self::$_space_re = self::$__module->_space_re;
            self::$_tkinter = self::$__module->_tkinter;
            self::$collections = self::$__module->collections;
            self::$constants = self::$__module->constants;
            self::$enum = self::$__module->enum;
            self::$getdouble = self::$__module->getdouble;
            self::$getint = self::$__module->getint;
            self::$re = self::$__module->re;
            self::$sys = self::$__module->sys;
            self::$types = self::$__module->types;
        }
    }

    public const EXCEPTION = 8;
    public const FALSE = 0;
    public const NO = 0;
    public const OFF = 0;
    public const ON = 1;
    public const READABLE = 2;
    public const TRUE = 1;
    public const TclVersion = 8.6;
    public const TkVersion = 8.6;
    public const WRITABLE = 4;
    public const YES = 1;
    public const _checkbutton_count = 0;
    public const _varnum = 0;
    public const wantobjects = 1;

    public static $ACTIVE = "active";
    public static $ALL = "all";
    public static $ANCHOR = "anchor";
    public static $ARC = "arc";
    public static $BASELINE = "baseline";
    public static $BEVEL = "bevel";
    public static $BOTH = "both";
    public static $BOTTOM = "bottom";
    public static $BROWSE = "browse";
    public static $BUTT = "butt";
    public static $CASCADE = "cascade";
    public static $CENTER = "center";
    public static $CHAR = "char";
    public static $CHECKBUTTON = "checkbutton";
    public static $CHORD = "chord";
    public static $COMMAND = "command";
    public static $CURRENT = "current";
    public static $DISABLED = "disabled";
    public static $DOTBOX = "dotbox";
    public static $E = "e";
    public static $END = "end";
    public static $EW = "ew";
    public static $EXTENDED = "extended";
    public static $FIRST = "first";
    public static $FLAT = "flat";
    public static $GROOVE = "groove";
    public static $HIDDEN = "hidden";
    public static $HORIZONTAL = "horizontal";
    public static $INSERT = "insert";
    public static $INSIDE = "inside";
    public static $LAST = "last";
    public static $LEFT = "left";
    public static $MITER = "miter";
    public static $MOVETO = "moveto";
    public static $MULTIPLE = "multiple";
    public static $N = "n";
    public static $NE = "ne";
    public static $NONE = "none";
    public static $NORMAL = "normal";
    public static $NS = "ns";
    public static $NSEW = "nsew";
    public static $NUMERIC = "numeric";
    public static $NW = "nw";
    public static $OUTSIDE = "outside";
    public static $PAGES = "pages";
    public static $PIESLICE = "pieslice";
    public static $PROJECTING = "projecting";
    public static $RADIOBUTTON = "radiobutton";
    public static $RAISED = "raised";
    public static $RIDGE = "ridge";
    public static $RIGHT = "right";
    public static $ROUND = "round";
    public static $S = "s";
    public static $SCROLL = "scroll";
    public static $SE = "se";
    public static $SEL = "sel";
    public static $SEL_FIRST = "sel.first";
    public static $SEL_LAST = "sel.last";
    public static $SEPARATOR = "separator";
    public static $SINGLE = "single";
    public static $SOLID = "solid";
    public static $SUNKEN = "sunken";
    public static $SW = "sw";
    public static $TOP = "top";
    public static $UNDERLINE = "underline";
    public static $UNITS = "units";
    public static $VERTICAL = "vertical";
    public static $W = "w";
    public static $WORD = "word";
    public static $X = "x";
    public static $Y = "y";
    public static $__cached__ = "/opt/anaconda3/lib/python3.11/tkinter/__pycache__/__init__.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/tkinter/__init__.py";
    public static $__name__ = "tkinter";
    public static $__package__ = "tkinter";
    public static $_default_root = null;
    public static $_support_default_root = true;

    public static $BaseWidget = null;
    public static $BitmapImage = null;
    public static $BooleanVar = null;
    public static $Button = null;
    public static $CallWrapper = null;
    public static $Canvas = null;
    public static $Checkbutton = null;
    public static $DoubleVar = null;
    public static $Entry = null;
    public static $Event = null;
    public static $EventType = null;
    public static $Frame = null;
    public static $Grid = null;
    public static $Image = null;
    public static $IntVar = null;
    public static $Label = null;
    public static $LabelFrame = null;
    public static $Listbox = null;
    public static $Menu = null;
    public static $Menubutton = null;
    public static $Message = null;
    public static $Misc = null;
    public static $OptionMenu = null;
    public static $Pack = null;
    public static $PanedWindow = null;
    public static $PhotoImage = null;
    public static $Place = null;
    public static $Radiobutton = null;
    public static $Scale = null;
    public static $Scrollbar = null;
    public static $Spinbox = null;
    public static $StringVar = null;
    public static $TclError = null;
    public static $Text = null;
    public static $Tk = null;
    public static $Toplevel = null;
    public static $Variable = null;
    public static $Widget = null;
    public static $Wm = null;
    public static $XView = null;
    public static $YView = null;
    public static $_VersionInfoType = null;
    public static $__path__ = null;
    public static $__spec__ = null;
    public static $_magic_re = null;
    public static $_setit = null;
    public static $_space_re = null;
    public static $_tkinter = null;
    public static $collections = null;
    public static $constants = null;
    public static $enum = null;
    public static $getdouble = null;
    public static $getint = null;
    public static $re = null;
    public static $sys = null;
    public static $types = null;

    public static function NoDefaultRoot()
    {
        return self::$__module->NoDefaultRoot();
    }
    public static function Tcl($screenName=null, $baseName=null, $className="Tk", $useTk=false)
    {
        return self::$__module->Tcl($screenName, $baseName, $className, $useTk);
    }
    public static function _cnfmerge($cnfs)
    {
        return self::$__module->_cnfmerge($cnfs);
    }
    public static function _destroy_temp_root($master)
    {
        return self::$__module->_destroy_temp_root($master);
    }
    public static function _exit($code=0)
    {
        return self::$__module->_exit($code);
    }
    public static function _flatten($item)
    {
        return self::$__module->_flatten($item);
    }
    public static function _get_default_root($what=null)
    {
        return self::$__module->_get_default_root($what);
    }
    public static function _get_temp_root()
    {
        return self::$__module->_get_temp_root();
    }
    public static function _join($value)
    {
        return self::$__module->_join($value);
    }
    public static function _parse_version($version)
    {
        return self::$__module->_parse_version($version);
    }
    public static function _splitdict($tk, $v, $cut_minus=true, $conv=null)
    {
        return self::$__module->_splitdict($tk, $v, $cut_minus, $conv);
    }
    public static function _stringify($value)
    {
        return self::$__module->_stringify($value);
    }
    public static function _test()
    {
        return self::$__module->_test();
    }
    public static function _tkerror($err)
    {
        return self::$__module->_tkerror($err);
    }
    public static function getboolean($s)
    {
        return self::$__module->getboolean($s);
    }
    public static function image_names()
    {
        return self::$__module->image_names();
    }
    public static function image_types()
    {
        return self::$__module->image_types();
    }
    public static function mainloop($n=0)
    {
        return self::$__module->mainloop($n);
    }
}

tkinter::__init();
