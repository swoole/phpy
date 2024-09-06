<?php
namespace python\torch;

/**
*/
class qscheme
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('torch')->qscheme();
    }

}
