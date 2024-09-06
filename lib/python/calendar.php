<?php
namespace python;

/**
Calendar printing functions

Note when comparing these calendars to the ones printed by cal(1): By
default, these calendars have Monday as the first day of the week, and
Sunday as the last (the European convention). Use setfirstweekday() to
set the first day of the week (0=Monday, 6=Sunday).*/
class calendar
{
    /**
    * @return calendar
    */
    public static function import()
    {
        return \PyCore::import('calendar');
    }

    public $EPOCH = 1970;
    public $FRIDAY = 4;
    public $February = 2;
    public $January = 1;
    public $MONDAY = 0;
    public $SATURDAY = 5;
    public $SUNDAY = 6;
    public $THURSDAY = 3;
    public $TUESDAY = 1;
    public $WEDNESDAY = 2;
    public $_EPOCH_ORD = 719163;
    public $_colwidth = 20;
    public $_spacing = 6;

    public $__name__ = "calendar";
    public $__package__ = "";

    public $_locale = null;
    public $c = null;
    public $calendar = null;
    public $datetime = null;
    public $day_abbr = null;
    public $day_name = null;
    public $firstweekday = null;
    public $mdays = null;
    public $month = null;
    public $month_abbr = null;
    public $month_name = null;
    public $monthcalendar = null;
    public $prcal = null;
    public $prmonth = null;
    public $prweek = null;
    public $sys = null;
    public $week = null;
    public $weekheader = null;

    /**
    * @return mixed
    */
    public function _monthlen($year, $month)
    {
    }

    /**
    * @return mixed
    */
    public function _nextmonth($year, $month)
    {
    }

    /**
    * @return mixed
    */
    public function _prevmonth($year, $month)
    {
    }

    /**
    * @return mixed
    */
    public function format($cols, $colwidth = 20, $spacing = 6)
    {
    }

    /**
    * @return mixed
    */
    public function formatstring($cols, $colwidth = 20, $spacing = 6)
    {
    }

    /**
    * @return mixed
    */
    public function isleap($year)
    {
    }

    /**
    * @return mixed
    */
    public function leapdays($y1, $y2)
    {
    }

    /**
    * @return mixed
    */
    public function main($args)
    {
    }

    /**
    * @return mixed
    */
    public function monthrange($year, $month)
    {
    }

    /**
    * @return mixed
    */
    public function setfirstweekday($firstweekday)
    {
    }

    /**
    * @return mixed
    */
    public function timegm($tuple)
    {
    }

    /**
    * @return mixed
    */
    public function weekday($year, $month, $day)
    {
    }

}
