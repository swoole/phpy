<?php
namespace python\tkinter;

/**
*/
class Tk
{
    private $_self;

    public function __construct($screenName = null, $baseName = null, $className = "Tk", $useTk = true, $sync = false, $use = null)
    {
        $this->_self = \PyCore::import('tkinter')->Tk($screenName, $baseName, $className, $useTk, $sync, $use);
    }

    public function after($ms, $func = null)
    {
        return $this->_self->after($ms, $func);
    }

    public function after_cancel($id)
    {
        return $this->_self->after_cancel($id);
    }

    public function after_idle($func)
    {
        return $this->_self->after_idle($func);
    }

    public function anchor($anchor = null)
    {
        return $this->_self->anchor($anchor);
    }

    public function aspect($minNumer = null, $minDenom = null, $maxNumer = null, $maxDenom = null)
    {
        return $this->_self->aspect($minNumer, $minDenom, $maxNumer, $maxDenom);
    }

    public function attributes()
    {
        return $this->_self->attributes();
    }

    public function bbox($column = null, $row = null, $col2 = null, $row2 = null)
    {
        return $this->_self->bbox($column, $row, $col2, $row2);
    }

    public function bell($displayof = 0)
    {
        return $this->_self->bell($displayof);
    }

    public function bind($sequence = null, $func = null, $add = null)
    {
        return $this->_self->bind($sequence, $func, $add);
    }

    public function bind_all($sequence = null, $func = null, $add = null)
    {
        return $this->_self->bind_all($sequence, $func, $add);
    }

    public function bind_class($className, $sequence = null, $func = null, $add = null)
    {
        return $this->_self->bind_class($className, $sequence, $func, $add);
    }

    public function bindtags($tagList = null)
    {
        return $this->_self->bindtags($tagList);
    }

    public function cget($key)
    {
        return $this->_self->cget($key);
    }

    public function client($name = null)
    {
        return $this->_self->client($name);
    }

    public function clipboard_append($string)
    {
        return $this->_self->clipboard_append($string);
    }

    public function clipboard_clear()
    {
        return $this->_self->clipboard_clear();
    }

    public function clipboard_get()
    {
        return $this->_self->clipboard_get();
    }

    public function colormapwindows()
    {
        return $this->_self->colormapwindows();
    }

    public function columnconfigure($index, $cnf = [])
    {
        return $this->_self->columnconfigure($index, $cnf);
    }

    public function command($value = null)
    {
        return $this->_self->command($value);
    }

    public function config($cnf = null)
    {
        return $this->_self->config($cnf);
    }

    public function configure($cnf = null)
    {
        return $this->_self->configure($cnf);
    }

    public function deiconify()
    {
        return $this->_self->deiconify();
    }

    public function deletecommand($name)
    {
        return $this->_self->deletecommand($name);
    }

    public function destroy()
    {
        return $this->_self->destroy();
    }

    public function event_add($virtual)
    {
        return $this->_self->event_add($virtual);
    }

    public function event_delete($virtual)
    {
        return $this->_self->event_delete($virtual);
    }

    public function event_generate($sequence)
    {
        return $this->_self->event_generate($sequence);
    }

    public function event_info($virtual = null)
    {
        return $this->_self->event_info($virtual);
    }

    public function focus()
    {
        return $this->_self->focus();
    }

    public function focus_displayof()
    {
        return $this->_self->focus_displayof();
    }

    public function focus_force()
    {
        return $this->_self->focus_force();
    }

    public function focus_get()
    {
        return $this->_self->focus_get();
    }

    public function focus_lastfor()
    {
        return $this->_self->focus_lastfor();
    }

    public function focus_set()
    {
        return $this->_self->focus_set();
    }

    public function focusmodel($model = null)
    {
        return $this->_self->focusmodel($model);
    }

    public function forget($window)
    {
        return $this->_self->forget($window);
    }

    public function frame()
    {
        return $this->_self->frame();
    }

    public function geometry($newGeometry = null)
    {
        return $this->_self->geometry($newGeometry);
    }

    public function getboolean($s)
    {
        return $this->_self->getboolean($s);
    }

    public function getdouble($s)
    {
        return $this->_self->getdouble($s);
    }

    public function getint($s)
    {
        return $this->_self->getint($s);
    }

    public function getvar($name = "PY_VAR")
    {
        return $this->_self->getvar($name);
    }

    public function grab_current()
    {
        return $this->_self->grab_current();
    }

    public function grab_release()
    {
        return $this->_self->grab_release();
    }

    public function grab_set()
    {
        return $this->_self->grab_set();
    }

    public function grab_set_global()
    {
        return $this->_self->grab_set_global();
    }

    public function grab_status()
    {
        return $this->_self->grab_status();
    }

    public function grid($baseWidth = null, $baseHeight = null, $widthInc = null, $heightInc = null)
    {
        return $this->_self->grid($baseWidth, $baseHeight, $widthInc, $heightInc);
    }

    public function grid_anchor($anchor = null)
    {
        return $this->_self->grid_anchor($anchor);
    }

    public function grid_bbox($column = null, $row = null, $col2 = null, $row2 = null)
    {
        return $this->_self->grid_bbox($column, $row, $col2, $row2);
    }

    public function grid_columnconfigure($index, $cnf = [])
    {
        return $this->_self->grid_columnconfigure($index, $cnf);
    }

    public function grid_location($x, $y)
    {
        return $this->_self->grid_location($x, $y);
    }

    public function grid_propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->grid_propagate($flag);
    }

    public function grid_rowconfigure($index, $cnf = [])
    {
        return $this->_self->grid_rowconfigure($index, $cnf);
    }

    public function grid_size()
    {
        return $this->_self->grid_size();
    }

    public function grid_slaves($row = null, $column = null)
    {
        return $this->_self->grid_slaves($row, $column);
    }

    public function group($pathName = null)
    {
        return $this->_self->group($pathName);
    }

    public function iconbitmap($bitmap = null, $default = null)
    {
        return $this->_self->iconbitmap($bitmap, $default);
    }

    public function iconify()
    {
        return $this->_self->iconify();
    }

    public function iconmask($bitmap = null)
    {
        return $this->_self->iconmask($bitmap);
    }

    public function iconname($newName = null)
    {
        return $this->_self->iconname($newName);
    }

    public function iconphoto($default = false)
    {
        return $this->_self->iconphoto($default);
    }

    public function iconposition($x = null, $y = null)
    {
        return $this->_self->iconposition($x, $y);
    }

    public function iconwindow($pathName = null)
    {
        return $this->_self->iconwindow($pathName);
    }

    public function image_names()
    {
        return $this->_self->image_names();
    }

    public function image_types()
    {
        return $this->_self->image_types();
    }

    public function keys()
    {
        return $this->_self->keys();
    }

    public function lift($aboveThis = null)
    {
        return $this->_self->lift($aboveThis);
    }

    public function loadtk()
    {
        return $this->_self->loadtk();
    }

    public function lower($belowThis = null)
    {
        return $this->_self->lower($belowThis);
    }

    public function mainloop($n = 0)
    {
        return $this->_self->mainloop($n);
    }

    public function manage($widget)
    {
        return $this->_self->manage($widget);
    }

    public function maxsize($width = null, $height = null)
    {
        return $this->_self->maxsize($width, $height);
    }

    public function minsize($width = null, $height = null)
    {
        return $this->_self->minsize($width, $height);
    }

    public function nametowidget($name)
    {
        return $this->_self->nametowidget($name);
    }

    public function option_add($pattern, $value, $priority = null)
    {
        return $this->_self->option_add($pattern, $value, $priority);
    }

    public function option_clear()
    {
        return $this->_self->option_clear();
    }

    public function option_get($name, $className)
    {
        return $this->_self->option_get($name, $className);
    }

    public function option_readfile($fileName, $priority = null)
    {
        return $this->_self->option_readfile($fileName, $priority);
    }

    public function overrideredirect($boolean = null)
    {
        return $this->_self->overrideredirect($boolean);
    }

    public function pack_propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->pack_propagate($flag);
    }

    public function pack_slaves()
    {
        return $this->_self->pack_slaves();
    }

    public function place_slaves()
    {
        return $this->_self->place_slaves();
    }

    public function positionfrom($who = null)
    {
        return $this->_self->positionfrom($who);
    }

    public function propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->propagate($flag);
    }

    public function protocol($name = null, $func = null)
    {
        return $this->_self->protocol($name, $func);
    }

    public function quit()
    {
        return $this->_self->quit();
    }

    public function readprofile($baseName, $className)
    {
        return $this->_self->readprofile($baseName, $className);
    }

    public function register($func, $subst = null, $needcleanup = 1)
    {
        return $this->_self->register($func, $subst, $needcleanup);
    }

    public function report_callback_exception($exc, $val, $tb)
    {
        return $this->_self->report_callback_exception($exc, $val, $tb);
    }

    public function resizable($width = null, $height = null)
    {
        return $this->_self->resizable($width, $height);
    }

    public function rowconfigure($index, $cnf = [])
    {
        return $this->_self->rowconfigure($index, $cnf);
    }

    public function selection_clear()
    {
        return $this->_self->selection_clear();
    }

    public function selection_get()
    {
        return $this->_self->selection_get();
    }

    public function selection_handle($command)
    {
        return $this->_self->selection_handle($command);
    }

    public function selection_own()
    {
        return $this->_self->selection_own();
    }

    public function selection_own_get()
    {
        return $this->_self->selection_own_get();
    }

    public function send($interp, $cmd)
    {
        return $this->_self->send($interp, $cmd);
    }

    public function setvar($name = "PY_VAR", $value = "1")
    {
        return $this->_self->setvar($name, $value);
    }

    public function size()
    {
        return $this->_self->size();
    }

    public function sizefrom($who = null)
    {
        return $this->_self->sizefrom($who);
    }

    public function slaves()
    {
        return $this->_self->slaves();
    }

    public function state($newstate = null)
    {
        return $this->_self->state($newstate);
    }

    public function title($string = null)
    {
        return $this->_self->title($string);
    }

    public function tk_bisque()
    {
        return $this->_self->tk_bisque();
    }

    public function tk_focusFollowsMouse()
    {
        return $this->_self->tk_focusFollowsMouse();
    }

    public function tk_focusNext()
    {
        return $this->_self->tk_focusNext();
    }

    public function tk_focusPrev()
    {
        return $this->_self->tk_focusPrev();
    }

    public function tk_setPalette()
    {
        return $this->_self->tk_setPalette();
    }

    public function tk_strictMotif($boolean = null)
    {
        return $this->_self->tk_strictMotif($boolean);
    }

    public function tkraise($aboveThis = null)
    {
        return $this->_self->tkraise($aboveThis);
    }

    public function transient($master = null)
    {
        return $this->_self->transient($master);
    }

    public function unbind($sequence, $funcid = null)
    {
        return $this->_self->unbind($sequence, $funcid);
    }

    public function unbind_all($sequence)
    {
        return $this->_self->unbind_all($sequence);
    }

    public function unbind_class($className, $sequence)
    {
        return $this->_self->unbind_class($className, $sequence);
    }

    public function update()
    {
        return $this->_self->update();
    }

    public function update_idletasks()
    {
        return $this->_self->update_idletasks();
    }

    public function wait_variable($name = "PY_VAR")
    {
        return $this->_self->wait_variable($name);
    }

    public function wait_visibility($window = null)
    {
        return $this->_self->wait_visibility($window);
    }

    public function wait_window($window = null)
    {
        return $this->_self->wait_window($window);
    }

    public function waitvar($name = "PY_VAR")
    {
        return $this->_self->waitvar($name);
    }

    public function winfo_atom($name, $displayof = 0)
    {
        return $this->_self->winfo_atom($name, $displayof);
    }

    public function winfo_atomname($id, $displayof = 0)
    {
        return $this->_self->winfo_atomname($id, $displayof);
    }

    public function winfo_cells()
    {
        return $this->_self->winfo_cells();
    }

    public function winfo_children()
    {
        return $this->_self->winfo_children();
    }

    public function winfo_class()
    {
        return $this->_self->winfo_class();
    }

    public function winfo_colormapfull()
    {
        return $this->_self->winfo_colormapfull();
    }

    public function winfo_containing($rootX, $rootY, $displayof = 0)
    {
        return $this->_self->winfo_containing($rootX, $rootY, $displayof);
    }

    public function winfo_depth()
    {
        return $this->_self->winfo_depth();
    }

    public function winfo_exists()
    {
        return $this->_self->winfo_exists();
    }

    public function winfo_fpixels($number)
    {
        return $this->_self->winfo_fpixels($number);
    }

    public function winfo_geometry()
    {
        return $this->_self->winfo_geometry();
    }

    public function winfo_height()
    {
        return $this->_self->winfo_height();
    }

    public function winfo_id()
    {
        return $this->_self->winfo_id();
    }

    public function winfo_interps($displayof = 0)
    {
        return $this->_self->winfo_interps($displayof);
    }

    public function winfo_ismapped()
    {
        return $this->_self->winfo_ismapped();
    }

    public function winfo_manager()
    {
        return $this->_self->winfo_manager();
    }

    public function winfo_name()
    {
        return $this->_self->winfo_name();
    }

    public function winfo_parent()
    {
        return $this->_self->winfo_parent();
    }

    public function winfo_pathname($id, $displayof = 0)
    {
        return $this->_self->winfo_pathname($id, $displayof);
    }

    public function winfo_pixels($number)
    {
        return $this->_self->winfo_pixels($number);
    }

    public function winfo_pointerx()
    {
        return $this->_self->winfo_pointerx();
    }

    public function winfo_pointerxy()
    {
        return $this->_self->winfo_pointerxy();
    }

    public function winfo_pointery()
    {
        return $this->_self->winfo_pointery();
    }

    public function winfo_reqheight()
    {
        return $this->_self->winfo_reqheight();
    }

    public function winfo_reqwidth()
    {
        return $this->_self->winfo_reqwidth();
    }

    public function winfo_rgb($color)
    {
        return $this->_self->winfo_rgb($color);
    }

    public function winfo_rootx()
    {
        return $this->_self->winfo_rootx();
    }

    public function winfo_rooty()
    {
        return $this->_self->winfo_rooty();
    }

    public function winfo_screen()
    {
        return $this->_self->winfo_screen();
    }

    public function winfo_screencells()
    {
        return $this->_self->winfo_screencells();
    }

    public function winfo_screendepth()
    {
        return $this->_self->winfo_screendepth();
    }

    public function winfo_screenheight()
    {
        return $this->_self->winfo_screenheight();
    }

    public function winfo_screenmmheight()
    {
        return $this->_self->winfo_screenmmheight();
    }

    public function winfo_screenmmwidth()
    {
        return $this->_self->winfo_screenmmwidth();
    }

    public function winfo_screenvisual()
    {
        return $this->_self->winfo_screenvisual();
    }

    public function winfo_screenwidth()
    {
        return $this->_self->winfo_screenwidth();
    }

    public function winfo_server()
    {
        return $this->_self->winfo_server();
    }

    public function winfo_toplevel()
    {
        return $this->_self->winfo_toplevel();
    }

    public function winfo_viewable()
    {
        return $this->_self->winfo_viewable();
    }

    public function winfo_visual()
    {
        return $this->_self->winfo_visual();
    }

    public function winfo_visualid()
    {
        return $this->_self->winfo_visualid();
    }

    public function winfo_visualsavailable($includeids = false)
    {
        return $this->_self->winfo_visualsavailable($includeids);
    }

    public function winfo_vrootheight()
    {
        return $this->_self->winfo_vrootheight();
    }

    public function winfo_vrootwidth()
    {
        return $this->_self->winfo_vrootwidth();
    }

    public function winfo_vrootx()
    {
        return $this->_self->winfo_vrootx();
    }

    public function winfo_vrooty()
    {
        return $this->_self->winfo_vrooty();
    }

    public function winfo_width()
    {
        return $this->_self->winfo_width();
    }

    public function winfo_x()
    {
        return $this->_self->winfo_x();
    }

    public function winfo_y()
    {
        return $this->_self->winfo_y();
    }

    public function withdraw()
    {
        return $this->_self->withdraw();
    }

    public function wm_aspect($minNumer = null, $minDenom = null, $maxNumer = null, $maxDenom = null)
    {
        return $this->_self->wm_aspect($minNumer, $minDenom, $maxNumer, $maxDenom);
    }

    public function wm_attributes()
    {
        return $this->_self->wm_attributes();
    }

    public function wm_client($name = null)
    {
        return $this->_self->wm_client($name);
    }

    public function wm_colormapwindows()
    {
        return $this->_self->wm_colormapwindows();
    }

    public function wm_command($value = null)
    {
        return $this->_self->wm_command($value);
    }

    public function wm_deiconify()
    {
        return $this->_self->wm_deiconify();
    }

    public function wm_focusmodel($model = null)
    {
        return $this->_self->wm_focusmodel($model);
    }

    public function wm_forget($window)
    {
        return $this->_self->wm_forget($window);
    }

    public function wm_frame()
    {
        return $this->_self->wm_frame();
    }

    public function wm_geometry($newGeometry = null)
    {
        return $this->_self->wm_geometry($newGeometry);
    }

    public function wm_grid($baseWidth = null, $baseHeight = null, $widthInc = null, $heightInc = null)
    {
        return $this->_self->wm_grid($baseWidth, $baseHeight, $widthInc, $heightInc);
    }

    public function wm_group($pathName = null)
    {
        return $this->_self->wm_group($pathName);
    }

    public function wm_iconbitmap($bitmap = null, $default = null)
    {
        return $this->_self->wm_iconbitmap($bitmap, $default);
    }

    public function wm_iconify()
    {
        return $this->_self->wm_iconify();
    }

    public function wm_iconmask($bitmap = null)
    {
        return $this->_self->wm_iconmask($bitmap);
    }

    public function wm_iconname($newName = null)
    {
        return $this->_self->wm_iconname($newName);
    }

    public function wm_iconphoto($default = false)
    {
        return $this->_self->wm_iconphoto($default);
    }

    public function wm_iconposition($x = null, $y = null)
    {
        return $this->_self->wm_iconposition($x, $y);
    }

    public function wm_iconwindow($pathName = null)
    {
        return $this->_self->wm_iconwindow($pathName);
    }

    public function wm_manage($widget)
    {
        return $this->_self->wm_manage($widget);
    }

    public function wm_maxsize($width = null, $height = null)
    {
        return $this->_self->wm_maxsize($width, $height);
    }

    public function wm_minsize($width = null, $height = null)
    {
        return $this->_self->wm_minsize($width, $height);
    }

    public function wm_overrideredirect($boolean = null)
    {
        return $this->_self->wm_overrideredirect($boolean);
    }

    public function wm_positionfrom($who = null)
    {
        return $this->_self->wm_positionfrom($who);
    }

    public function wm_protocol($name = null, $func = null)
    {
        return $this->_self->wm_protocol($name, $func);
    }

    public function wm_resizable($width = null, $height = null)
    {
        return $this->_self->wm_resizable($width, $height);
    }

    public function wm_sizefrom($who = null)
    {
        return $this->_self->wm_sizefrom($who);
    }

    public function wm_state($newstate = null)
    {
        return $this->_self->wm_state($newstate);
    }

    public function wm_title($string = null)
    {
        return $this->_self->wm_title($string);
    }

    public function wm_transient($master = null)
    {
        return $this->_self->wm_transient($master);
    }

    public function wm_withdraw()
    {
        return $this->_self->wm_withdraw();
    }

}
