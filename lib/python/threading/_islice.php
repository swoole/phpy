<?php
namespace python\threading;

/**
*/
class _islice
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->_islice();
    }

}
