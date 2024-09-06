<?php
namespace python\calendar;

/**
*/
class error
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('calendar')->error();
    }

}
