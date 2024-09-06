<?php
namespace python\calendar;

/**
*/
class IllegalWeekdayError
{
    private $_self;

    public function __construct($weekday)
    {
        $this->_self = \PyCore::import('calendar')->IllegalWeekdayError($weekday);
    }

}
