<?php
namespace python\matplotlib\pyplot;

/**
* @property $button_pick_id
* @property $callbacks
* @property $device_pixel_ratio
* @property $scroll_pick_id
*/
class FigureCanvasBase
{
    private $_self;

    public function __construct($figure = null)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->FigureCanvasBase($figure);
    }

    public function blit($bbox = null)
    {
        return $this->_self->blit($bbox);
    }

    public function button_press_event($x, $y, $button, $dblclick = false, $guiEvent = null)
    {
        return $this->_self->button_press_event($x, $y, $button, $dblclick, $guiEvent);
    }

    public function button_release_event($x, $y, $button, $guiEvent = null)
    {
        return $this->_self->button_release_event($x, $y, $button, $guiEvent);
    }

    public function close_event($guiEvent = null)
    {
        return $this->_self->close_event($guiEvent);
    }

    public function draw()
    {
        return $this->_self->draw();
    }

    public function draw_event($renderer)
    {
        return $this->_self->draw_event($renderer);
    }

    public function draw_idle()
    {
        return $this->_self->draw_idle();
    }

    public function enter_notify_event($guiEvent = null, $xy = null)
    {
        return $this->_self->enter_notify_event($guiEvent, $xy);
    }

    public function flush_events()
    {
        return $this->_self->flush_events();
    }

    public function get_default_filename()
    {
        return $this->_self->get_default_filename();
    }

    public function get_width_height()
    {
        return $this->_self->get_width_height();
    }

    public function get_window_title()
    {
        return $this->_self->get_window_title();
    }

    public function grab_mouse($ax)
    {
        return $this->_self->grab_mouse($ax);
    }

    public function inaxes($xy)
    {
        return $this->_self->inaxes($xy);
    }

    public function is_saving()
    {
        return $this->_self->is_saving();
    }

    public function key_press_event($key, $guiEvent = null)
    {
        return $this->_self->key_press_event($key, $guiEvent);
    }

    public function key_release_event($key, $guiEvent = null)
    {
        return $this->_self->key_release_event($key, $guiEvent);
    }

    public function leave_notify_event($guiEvent = null)
    {
        return $this->_self->leave_notify_event($guiEvent);
    }

    public function motion_notify_event($x, $y, $guiEvent = null)
    {
        return $this->_self->motion_notify_event($x, $y, $guiEvent);
    }

    public function mpl_connect($s, $func)
    {
        return $this->_self->mpl_connect($s, $func);
    }

    public function mpl_disconnect($cid)
    {
        return $this->_self->mpl_disconnect($cid);
    }

    public function new_timer($interval = null, $callbacks = null)
    {
        return $this->_self->new_timer($interval, $callbacks);
    }

    public function pick($mouseevent)
    {
        return $this->_self->pick($mouseevent);
    }

    public function pick_event($mouseevent, $artist)
    {
        return $this->_self->pick_event($mouseevent, $artist);
    }

    public function print_figure($filename, $dpi = null, $facecolor = null, $edgecolor = null, $orientation = "portrait", $format = null)
    {
        return $this->_self->print_figure($filename, $dpi, $facecolor, $edgecolor, $orientation, $format);
    }

    public function release_mouse($ax)
    {
        return $this->_self->release_mouse($ax);
    }

    public function resize($w, $h)
    {
        return $this->_self->resize($w, $h);
    }

    public function resize_event()
    {
        return $this->_self->resize_event();
    }

    public function scroll_event($x, $y, $step, $guiEvent = null)
    {
        return $this->_self->scroll_event($x, $y, $step, $guiEvent);
    }

    public function set_cursor($cursor)
    {
        return $this->_self->set_cursor($cursor);
    }

    public function set_window_title()
    {
        return $this->_self->set_window_title();
    }

    public function start_event_loop($timeout = 0)
    {
        return $this->_self->start_event_loop($timeout);
    }

    public function stop_event_loop()
    {
        return $this->_self->stop_event_loop();
    }

    public function switch_backends($FigureCanvasClass)
    {
        return $this->_self->switch_backends($FigureCanvasClass);
    }

}
