<?php
namespace python\pickle;

/**
*/
class _Framer
{
    private $_self;

    public function __construct($file_write)
    {
        $this->_self = \PyCore::import('pickle')->_Framer($file_write);
    }

    public function commit_frame($force = false)
    {
        return $this->_self->commit_frame($force);
    }

    public function end_framing()
    {
        return $this->_self->end_framing();
    }

    public function start_framing()
    {
        return $this->_self->start_framing();
    }

    public function write($data)
    {
        return $this->_self->write($data);
    }

    public function write_large_bytes($header, $payload)
    {
        return $this->_self->write_large_bytes($header, $payload);
    }

}
