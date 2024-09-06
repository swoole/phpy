<?php
namespace python\uuid;

/**
*/
class int_
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('uuid')->int_();
    }

}
