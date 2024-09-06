<?php
namespace python\tkinter;

/**
*/
class Wm
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('tkinter')->Wm();
    }

    public function aspect($minNumer = null, $minDenom = null, $maxNumer = null, $maxDenom = null)
    {
        return $this->_self->aspect($minNumer, $minDenom, $maxNumer, $maxDenom);
    }

    public function attributes()
    {
        return $this->_self->attributes();
    }

    public function client($name = null)
    {
        return $this->_self->client($name);
    }

    public function colormapwindows()
    {
        return $this->_self->colormapwindows();
    }

    public function command($value = null)
    {
        return $this->_self->command($value);
    }

    public function deiconify()
    {
        return $this->_self->deiconify();
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

    public function grid($baseWidth = null, $baseHeight = null, $widthInc = null, $heightInc = null)
    {
        return $this->_self->grid($baseWidth, $baseHeight, $widthInc, $heightInc);
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

    public function overrideredirect($boolean = null)
    {
        return $this->_self->overrideredirect($boolean);
    }

    public function positionfrom($who = null)
    {
        return $this->_self->positionfrom($who);
    }

    public function protocol($name = null, $func = null)
    {
        return $this->_self->protocol($name, $func);
    }

    public function resizable($width = null, $height = null)
    {
        return $this->_self->resizable($width, $height);
    }

    public function sizefrom($who = null)
    {
        return $this->_self->sizefrom($who);
    }

    public function state($newstate = null)
    {
        return $this->_self->state($newstate);
    }

    public function title($string = null)
    {
        return $this->_self->title($string);
    }

    public function transient($master = null)
    {
        return $this->_self->transient($master);
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
