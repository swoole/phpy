<?php
namespace python\calendar;

/**
* @property $firstweekday
*/
class LocaleHTMLCalendar
{
    private $_self;

    public function __construct($firstweekday = 0, $locale = null)
    {
        $this->_self = \PyCore::import('calendar')->LocaleHTMLCalendar($firstweekday, $locale);
    }

    public function formatday($day, $weekday)
    {
        return $this->_self->formatday($day, $weekday);
    }

    public function formatmonth($theyear, $themonth, $withyear = true)
    {
        return $this->_self->formatmonth($theyear, $themonth, $withyear);
    }

    public function formatmonthname($theyear, $themonth, $withyear = true)
    {
        return $this->_self->formatmonthname($theyear, $themonth, $withyear);
    }

    public function formatweek($theweek)
    {
        return $this->_self->formatweek($theweek);
    }

    public function formatweekday($day)
    {
        return $this->_self->formatweekday($day);
    }

    public function formatweekheader()
    {
        return $this->_self->formatweekheader();
    }

    public function formatyear($theyear, $width = 3)
    {
        return $this->_self->formatyear($theyear, $width);
    }

    public function formatyearpage($theyear, $width = 3, $css = "calendar.css", $encoding = null)
    {
        return $this->_self->formatyearpage($theyear, $width, $css, $encoding);
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
