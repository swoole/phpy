<?php
namespace python\json;

/**
*/
class JSONEncoder
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('json')->JSONEncoder();
    }

    public function default($o)
    {
        return $this->_self->default($o);
    }

    public function encode($o)
    {
        return $this->_self->encode($o);
    }

    public function iterencode($o, $_one_shot = false)
    {
        return $this->_self->iterencode($o, $_one_shot);
    }

}
