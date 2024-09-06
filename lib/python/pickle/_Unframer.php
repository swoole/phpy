<?php
namespace python\pickle;

/**
*/
class _Unframer
{
    private $_self;

    public function __construct($file_read, $file_readline, $file_tell = null)
    {
        $this->_self = \PyCore::import('pickle')->_Unframer($file_read, $file_readline, $file_tell);
    }

    public function load_frame($frame_size)
    {
        return $this->_self->load_frame($frame_size);
    }

    public function read($n)
    {
        return $this->_self->read($n);
    }

    public function readinto($buf)
    {
        return $this->_self->readinto($buf);
    }

    public function readline()
    {
        return $this->_self->readline();
    }

}
