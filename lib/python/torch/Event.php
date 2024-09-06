<?php
namespace python\torch;

/**
*/
class Event
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->Event();
    }

}
