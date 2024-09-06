<?php
namespace python\calendar;

/**
* @property $firstweekday
*/
class LocaleTextCalendar
{
    private $_self;

    public function __construct($firstweekday = 0, $locale = null)
    {
        $this->_self = \PyCore::import('calendar')->LocaleTextCalendar($firstweekday, $locale);
    }

    public function formatday($day, $weekday, $width)
    {
        return $this->_self->formatday($day, $weekday, $width);
    }

    public function formatmonth($theyear, $themonth, $w = 0, $l = 0)
    {
        return $this->_self->formatmonth($theyear, $themonth, $w, $l);
    }

    public function formatmonthname($theyear, $themonth, $width, $withyear = true)
    {
        return $this->_self->formatmonthname($theyear, $themonth, $width, $withyear);
    }

    public function formatweek($theweek, $width)
    {
        return $this->_self->formatweek($theweek, $width);
    }

    public function formatweekday($day, $width)
    {
        return $this->_self->formatweekday($day, $width);
    }

    public function formatweekheader($width)
    {
        return $this->_self->formatweekheader($width);
    }

    public function formatyear($theyear, $w = 2, $l = 1, $c = 6, $m = 3)
    {
        return $this->_self->formatyear($theyear, $w, $l, $c, $m);
    }

    public function getfirstweekday()
    {
        return $this->_self->getfirstweekday();
    }

    public function itermonthdates($year, $month)
    {
        return $this->_self->itermonthdates($year, $month);
    }

    public function itermonthdays($year, $month)
    {
        return $this->_self->itermonthdays($year, $month);
    }

    public function itermonthdays2($year, $month)
    {
        return $this->_self->itermonthdays2($year, $month);
    }

    public function itermonthdays3($year, $month)
    {
        return $this->_self->itermonthdays3($year, $month);
    }

    public function itermonthdays4($year, $month)
    {
        return $this->_self->itermonthdays4($year, $month);
    }

    public function iterweekdays()
    {
        return $this->_self->iterweekdays();
    }

    public function monthdatescalendar($year, $month)
    {
        return $this->_self->monthdatescalendar($year, $month);
    }

    public function monthdays2calendar($year, $month)
    {
        return $this->_self->monthdays2calendar($year, $month);
    }

    public function monthdayscalendar($year, $month)
    {
        return $this->_self->monthdayscalendar($year, $month);
    }

    public function prmonth($theyear, $themonth, $w = 0, $l = 0)
    {
        return $this->_self->prmonth($theyear, $themonth, $w, $l);
    }

    public function prweek($theweek, $width)
    {
        return $this->_self->prweek($theweek, $width);
    }

    public function pryear($theyear, $w = 0, $l = 0, $c = 6, $m = 3)
    {
        return $this->_self->pryear($theyear, $w, $l, $c, $m);
    }

    public function setfirstweekday($firstweekday)
    {
        return $this->_self->setfirstweekday($firstweekday);
    }

    public function yeardatescalendar($year, $width = 3)
    {
        return $this->_self->yeardatescalendar($year, $width);
    }

    public function yeardays2calendar($year, $width = 3)
    {
        return $this->_self->yeardays2calendar($year, $width);
    }

    public function yeardayscalendar($year, $width = 3)
    {
        return $this->_self->yeardayscalendar($year, $width);
    }

}
