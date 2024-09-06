<?php
namespace python\torch;

/**
*/
class _TritonLibrary
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->_TritonLibrary();
    }

}
