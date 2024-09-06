<?php
namespace python\tkinter;

/**
*/
class Text
{
    private $_self;

    public function __construct($master = null, $cnf = [])
    {
        $this->_self = \PyCore::import('tkinter')->Text($master, $cnf);
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

    public function bbox($index)
    {
        return $this->_self->bbox($index);
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

    public function columnconfigure($index, $cnf = [])
    {
        return $this->_self->columnconfigure($index, $cnf);
    }

    public function compare($index1, $op, $index2)
    {
        return $this->_self->compare($index1, $op, $index2);
    }

    public function config($cnf = null)
    {
        return $this->_self->config($cnf);
    }

    public function configure($cnf = null)
    {
        return $this->_self->configure($cnf);
    }

    public function count($index1, $index2)
    {
        return $this->_self->count($index1, $index2);
    }

    public function debug($boolean = null)
    {
        return $this->_self->debug($boolean);
    }

    public function delete($index1, $index2 = null)
    {
        return $this->_self->delete($index1, $index2);
    }

    public function deletecommand($name)
    {
        return $this->_self->deletecommand($name);
    }

    public function destroy()
    {
        return $this->_self->destroy();
    }

    public function dlineinfo($index)
    {
        return $this->_self->dlineinfo($index);
    }

    public function dump($index1, $index2 = null, $command = null)
    {
        return $this->_self->dump($index1, $index2, $command);
    }

    public function edit()
    {
        return $this->_self->edit();
    }

    public function edit_modified($arg = null)
    {
        return $this->_self->edit_modified($arg);
    }

    public function edit_redo()
    {
        return $this->_self->edit_redo();
    }

    public function edit_reset()
    {
        return $this->_self->edit_reset();
    }

    public function edit_separator()
    {
        return $this->_self->edit_separator();
    }

    public function edit_undo()
    {
        return $this->_self->edit_undo();
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

    public function forget()
    {
        return $this->_self->forget();
    }

    public function get($index1, $index2 = null)
    {
        return $this->_self->get($index1, $index2);
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

    public function grid($cnf = [])
    {
        return $this->_self->grid($cnf);
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

    public function grid_configure($cnf = [])
    {
        return $this->_self->grid_configure($cnf);
    }

    public function grid_forget()
    {
        return $this->_self->grid_forget();
    }

    public function grid_info()
    {
        return $this->_self->grid_info();
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

    public function grid_remove()
    {
        return $this->_self->grid_remove();
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

    public function image_cget($index, $option)
    {
        return $this->_self->image_cget($index, $option);
    }

    public function image_configure($index, $cnf = null)
    {
        return $this->_self->image_configure($index, $cnf);
    }

    public function image_create($index, $cnf = [])
    {
        return $this->_self->image_create($index, $cnf);
    }

    public function image_names()
    {
        return $this->_self->image_names();
    }

    public function image_types()
    {
        return $this->_self->image_types();
    }

    public function index($index)
    {
        return $this->_self->index($index);
    }

    public function info()
    {
        return $this->_self->info();
    }

    public function insert($index, $chars)
    {
        return $this->_self->insert($index, $chars);
    }

    public function keys()
    {
        return $this->_self->keys();
    }

    public function lift($aboveThis = null)
    {
        return $this->_self->lift($aboveThis);
    }

    public function location($x, $y)
    {
        return $this->_self->location($x, $y);
    }

    public function lower($belowThis = null)
    {
        return $this->_self->lower($belowThis);
    }

    public function mainloop($n = 0)
    {
        return $this->_self->mainloop($n);
    }

    public function mark_gravity($markName, $direction = null)
    {
        return $this->_self->mark_gravity($markName, $direction);
    }

    public function mark_names()
    {
        return $this->_self->mark_names();
    }

    public function mark_next($index)
    {
        return $this->_self->mark_next($index);
    }

    public function mark_previous($index)
    {
        return $this->_self->mark_previous($index);
    }

    public function mark_set($markName, $index)
    {
        return $this->_self->mark_set($markName, $index);
    }

    public function mark_unset()
    {
        return $this->_self->mark_unset();
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

    public function pack($cnf = [])
    {
        return $this->_self->pack($cnf);
    }

    public function pack_configure($cnf = [])
    {
        return $this->_self->pack_configure($cnf);
    }

    public function pack_forget()
    {
        return $this->_self->pack_forget();
    }

    public function pack_info()
    {
        return $this->_self->pack_info();
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

    public function peer_create($newPathName, $cnf = [])
    {
        return $this->_self->peer_create($newPathName, $cnf);
    }

    public function peer_names()
    {
        return $this->_self->peer_names();
    }

    public function place($cnf = [])
    {
        return $this->_self->place($cnf);
    }

    public function place_configure($cnf = [])
    {
        return $this->_self->place_configure($cnf);
    }

    public function place_forget()
    {
        return $this->_self->place_forget();
    }

    public function place_info()
    {
        return $this->_self->place_info();
    }

    public function place_slaves()
    {
        return $this->_self->place_slaves();
    }

    public function propagate($flag = array (
  0 => '_noarg_',
))
    {
        return $this->_self->propagate($flag);
    }

    public function quit()
    {
        return $this->_self->quit();
    }

    public function register($func, $subst = null, $needcleanup = 1)
    {
        return $this->_self->register($func, $subst, $needcleanup);
    }

    public function replace($index1, $index2, $chars)
    {
        return $this->_self->replace($index1, $index2, $chars);
    }

    public function rowconfigure($index, $cnf = [])
    {
        return $this->_self->rowconfigure($index, $cnf);
    }

    public function scan_dragto($x, $y)
    {
        return $this->_self->scan_dragto($x, $y);
    }

    public function scan_mark($x, $y)
    {
        return $this->_self->scan_mark($x, $y);
    }

    public function search($pattern, $index, $stopindex = null, $forwards = null, $backwards = null, $exact = null, $regexp = null, $nocase = null, $count = null, $elide = null)
    {
        return $this->_self->search($pattern, $index, $stopindex, $forwards, $backwards, $exact, $regexp, $nocase, $count, $elide);
    }

    public function see($index)
    {
        return $this->_self->see($index);
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

    public function slaves()
    {
        return $this->_self->slaves();
    }

    public function tag_add($tagName, $index1)
    {
        return $this->_self->tag_add($tagName, $index1);
    }

    public function tag_bind($tagName, $sequence, $func, $add = null)
    {
        return $this->_self->tag_bind($tagName, $sequence, $func, $add);
    }

    public function tag_cget($tagName, $option)
    {
        return $this->_self->tag_cget($tagName, $option);
    }

    public function tag_config($tagName, $cnf = null)
    {
        return $this->_self->tag_config($tagName, $cnf);
    }

    public function tag_configure($tagName, $cnf = null)
    {
        return $this->_self->tag_configure($tagName, $cnf);
    }

    public function tag_delete()
    {
        return $this->_self->tag_delete();
    }

    public function tag_lower($tagName, $belowThis = null)
    {
        return $this->_self->tag_lower($tagName, $belowThis);
    }

    public function tag_names($index = null)
    {
        return $this->_self->tag_names($index);
    }

    public function tag_nextrange($tagName, $index1, $index2 = null)
    {
        return $this->_self->tag_nextrange($tagName, $index1, $index2);
    }

    public function tag_prevrange($tagName, $index1, $index2 = null)
    {
        return $this->_self->tag_prevrange($tagName, $index1, $index2);
    }

    public function tag_raise($tagName, $aboveThis = null)
    {
        return $this->_self->tag_raise($tagName, $aboveThis);
    }

    public function tag_ranges($tagName)
    {
        return $this->_self->tag_ranges($tagName);
    }

    public function tag_remove($tagName, $index1, $index2 = null)
    {
        return $this->_self->tag_remove($tagName, $index1, $index2);
    }

    public function tag_unbind($tagName, $sequence, $funcid = null)
    {
        return $this->_self->tag_unbind($tagName, $sequence, $funcid);
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

    public function window_cget($index, $option)
    {
        return $this->_self->window_cget($index, $option);
    }

    public function window_config($index, $cnf = null)
    {
        return $this->_self->window_config($index, $cnf);
    }

    public function window_configure($index, $cnf = null)
    {
        return $this->_self->window_configure($index, $cnf);
    }

    public function window_create($index, $cnf = [])
    {
        return $this->_self->window_create($index, $cnf);
    }

    public function window_names()
    {
        return $this->_self->window_names();
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

    public function xview()
    {
        return $this->_self->xview();
    }

    public function xview_moveto($fraction)
    {
        return $this->_self->xview_moveto($fraction);
    }

    public function xview_scroll($number, $what)
    {
        return $this->_self->xview_scroll($number, $what);
    }

    public function yview()
    {
        return $this->_self->yview();
    }

    public function yview_moveto($fraction)
    {
        return $this->_self->yview_moveto($fraction);
    }

    public function yview_pickplace()
    {
        return $this->_self->yview_pickplace();
    }

    public function yview_scroll($number, $what)
    {
        return $this->_self->yview_scroll($number, $what);
    }

}
