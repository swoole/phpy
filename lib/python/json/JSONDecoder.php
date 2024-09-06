<?php
namespace python\json;

/**
*/
class JSONDecoder
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('json')->JSONDecoder();
    }

    public function decode($s, $_w = null)
    {
        return $this->_self->decode($s, $_w);
    }

    public function raw_decode($s, $idx = 0)
    {
        return $this->_self->raw_decode($s, $idx);
    }

}
