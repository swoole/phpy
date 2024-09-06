<?php
namespace python\uuid;

/**
*/
class bytes_
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('uuid')->bytes_();
    }

}
