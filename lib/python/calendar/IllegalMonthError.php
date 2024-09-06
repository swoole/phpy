<?php
namespace python\calendar;

/**
*/
class IllegalMonthError
{
    private $_self;

    public function __construct($month)
    {
        $this->_self = \PyCore::import('calendar')->IllegalMonthError($month);
    }

}
