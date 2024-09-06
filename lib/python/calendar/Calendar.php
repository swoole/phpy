<?php
namespace python\calendar;

/**
* @property $firstweekday
*/
class Calendar
{
    private $_self;

    public function __construct($firstweekday = 0)
    {
        $this->_self = \PyCore::import('calendar')->Calendar($firstweekday);
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
