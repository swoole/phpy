<?php
namespace python\matplotlib\pyplot;

/**
*/
class _IonContext
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->_IonContext();
    }

}
