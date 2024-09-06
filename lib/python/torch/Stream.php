<?php
namespace python\torch;

/**
*/
class Stream
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->Stream();
    }

}
