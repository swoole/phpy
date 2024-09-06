<?php
namespace python\calendar;

/**
*/
class _localized_day
{
    private $_self;

    public function __construct($format)
    {
        $this->_self = \PyCore::import('calendar')->_localized_day($format);
    }

}
