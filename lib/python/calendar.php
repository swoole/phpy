<?php
namespace python;

use \PyModule;
use \PyCore;

/**
Calendar printing functions

Note when comparing these calendars to the ones printed by cal(1): By
default, these calendars have Monday as the first day of the week, and
Sunday as the last (the European convention). Use setfirstweekday() to
set the first day of the week (0=Monday, 6=Sunday).*/
class calendar{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('calendar');
            self::$Calendar = self::$__module->Calendar;
            self::$HTMLCalendar = self::$__module->HTMLCalendar;
            self::$IllegalMonthError = self::$__module->IllegalMonthError;
            self::$IllegalWeekdayError = self::$__module->IllegalWeekdayError;
            self::$LocaleHTMLCalendar = self::$__module->LocaleHTMLCalendar;
            self::$LocaleTextCalendar = self::$__module->LocaleTextCalendar;
            self::$TextCalendar = self::$__module->TextCalendar;
            self::$__spec__ = self::$__module->__spec__;
            self::$_locale = self::$__module->_locale;
            self::$_localized_day = self::$__module->_localized_day;
            self::$_localized_month = self::$__module->_localized_month;
            self::$c = self::$__module->c;
            self::$calendar = self::$__module->calendar;
            self::$datetime = self::$__module->datetime;
            self::$day_abbr = self::$__module->day_abbr;
            self::$day_name = self::$__module->day_name;
            self::$different_locale = self::$__module->different_locale;
            self::$error = self::$__module->error;
            self::$firstweekday = self::$__module->firstweekday;
            self::$mdays = self::$__module->mdays;
            self::$month = self::$__module->month;
            self::$month_abbr = self::$__module->month_abbr;
            self::$month_name = self::$__module->month_name;
            self::$monthcalendar = self::$__module->monthcalendar;
            self::$prcal = self::$__module->prcal;
            self::$prmonth = self::$__module->prmonth;
            self::$prweek = self::$__module->prweek;
            self::$repeat = self::$__module->repeat;
            self::$sys = self::$__module->sys;
            self::$week = self::$__module->week;
            self::$weekheader = self::$__module->weekheader;
        }
    }

    public const EPOCH = 1970;
    public const FRIDAY = 4;
    public const February = 2;
    public const January = 1;
    public const MONDAY = 0;
    public const SATURDAY = 5;
    public const SUNDAY = 6;
    public const THURSDAY = 3;
    public const TUESDAY = 1;
    public const WEDNESDAY = 2;
    public const _EPOCH_ORD = 719163;
    public const _colwidth = 20;
    public const _spacing = 6;

    public static $__cached__ = "/opt/anaconda3/lib/python3.11/__pycache__/calendar.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/calendar.py";
    public static $__name__ = "calendar";
    public static $__package__ = "";

    public static $Calendar = null;
    public static $HTMLCalendar = null;
    public static $IllegalMonthError = null;
    public static $IllegalWeekdayError = null;
    public static $LocaleHTMLCalendar = null;
    public static $LocaleTextCalendar = null;
    public static $TextCalendar = null;
    public static $__spec__ = null;
    public static $_locale = null;
    public static $_localized_day = null;
    public static $_localized_month = null;
    public static $c = null;
    public static $calendar = null;
    public static $datetime = null;
    public static $day_abbr = null;
    public static $day_name = null;
    public static $different_locale = null;
    public static $error = null;
    public static $firstweekday = null;
    public static $mdays = null;
    public static $month = null;
    public static $month_abbr = null;
    public static $month_name = null;
    public static $monthcalendar = null;
    public static $prcal = null;
    public static $prmonth = null;
    public static $prweek = null;
    public static $repeat = null;
    public static $sys = null;
    public static $week = null;
    public static $weekheader = null;

    public static function _get_default_locale()
    {
        return self::$__module->_get_default_locale();
    }
    public static function _monthlen($year, $month)
    {
        return self::$__module->_monthlen($year, $month);
    }
    public static function _nextmonth($year, $month)
    {
        return self::$__module->_nextmonth($year, $month);
    }
    public static function _prevmonth($year, $month)
    {
        return self::$__module->_prevmonth($year, $month);
    }
    public static function format($cols, $colwidth=20, $spacing=6)
    {
        return self::$__module->format($cols, $colwidth, $spacing);
    }
    public static function formatstring($cols, $colwidth=20, $spacing=6)
    {
        return self::$__module->formatstring($cols, $colwidth, $spacing);
    }
    public static function isleap($year)
    {
        return self::$__module->isleap($year);
    }
    public static function leapdays($y1, $y2)
    {
        return self::$__module->leapdays($y1, $y2);
    }
    public static function main($args)
    {
        return self::$__module->main($args);
    }
    public static function monthrange($year, $month)
    {
        return self::$__module->monthrange($year, $month);
    }
    public static function setfirstweekday($firstweekday)
    {
        return self::$__module->setfirstweekday($firstweekday);
    }
    public static function timegm($tuple)
    {
        return self::$__module->timegm($tuple);
    }
    public static function weekday($year, $month, $day)
    {
        return self::$__module->weekday($year, $month, $day);
    }
}

calendar::__init();
