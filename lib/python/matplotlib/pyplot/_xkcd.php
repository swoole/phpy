<?php
namespace python\matplotlib\pyplot;

/**
*/
class _xkcd
{
    private $_self;

    public function __construct($scale, $length, $randomness)
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->_xkcd($scale, $length, $randomness);
    }

}
