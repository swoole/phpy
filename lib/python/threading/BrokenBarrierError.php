<?php
namespace python\threading;

/**
*/
class BrokenBarrierError
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('threading')->BrokenBarrierError();
    }

}
