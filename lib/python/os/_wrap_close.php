<?php
namespace python\os;

/**
*/
class _wrap_close
{
    private $_self;

    public function __construct($stream, $proc)
    {
        $this->_self = \PyCore::import('os')->_wrap_close($stream, $proc);
    }

    public function close()
    {
        return $this->_self->close();
    }

}
