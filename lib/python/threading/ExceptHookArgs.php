<?php
namespace python\threading;

/**
*/
class ExceptHookArgs
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->ExceptHookArgs();
    }

}
