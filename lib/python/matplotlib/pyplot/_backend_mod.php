<?php
namespace python\matplotlib\pyplot;

/**
*/
class _backend_mod
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('matplotlib.pyplot')->_backend_mod();
    }

    public function export()
    {
        return $this->_self->export();
    }

}
