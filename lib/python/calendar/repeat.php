<?php
namespace python\calendar;

/**
*/
class repeat
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('calendar')->repeat();
    }

}
