<?php
namespace python\calendar;

/**
*/
class different_locale
{
    private $_self;

    public function __construct($locale)
    {
        $this->_self = \PyCore::import('calendar')->different_locale($locale);
    }

}
