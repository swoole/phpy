<?php
namespace python;

/**
Calendar printing functions

Note when comparing these calendars to the ones printed by cal(1): By
default, these calendars have Monday as the first day of the week, and
Sunday as the last (the European convention). Use setfirstweekday() to
set the first day of the week (0=Monday, 6=Sunday).*/
class calendar{
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

    public $Calendar = null;
    public $HTMLCalendar = null;
    public $IllegalMonthError = null;
    public $IllegalWeekdayError = null;
    public $LocaleHTMLCalendar = null;
    public $LocaleTextCalendar = null;
    public $TextCalendar = null;
    public $_locale = null;
    public $_localized_day = null;
    public $_localized_month = null;
    public $c = null;
    public $calendar = null;
    public $datetime = null;
    public $day_abbr = null;
    public $day_name = null;
    public $different_locale = null;
    public $error = null;
    public $firstweekday = null;
    public $mdays = null;
    public $month = null;
    public $month_abbr = null;
    public $month_name = null;
    public $monthcalendar = null;
    public $prcal = null;
    public $prmonth = null;
    public $prweek = null;
    public $repeat = null;
    public $sys = null;
    public $week = null;
    public $weekheader = null;

    public function _get_default_locale()
    {
    }

    public function _monthlen($year, $month)
    {
    }

    public function _nextmonth($year, $month)
    {
    }

    public function _prevmonth($year, $month)
    {
    }

    public function format($cols, $colwidth = 20, $spacing = 6)
    {
    }

    public function formatstring($cols, $colwidth = 20, $spacing = 6)
    {
    }

    public function isleap($year)
    {
    }

    public function leapdays($y1, $y2)
    {
    }

    public function main($args)
    {
    }

    public function monthrange($year, $month)
    {
    }

    public function setfirstweekday($firstweekday)
    {
    }

    public function timegm($tuple)
    {
    }

    public function weekday($year, $month, $day)
    {
    }

}
