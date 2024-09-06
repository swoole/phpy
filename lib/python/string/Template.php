<?php
namespace python\string;

/**
*/
class Template
{
    private $_self;

    public function __construct($template)
    {
        $this->_self = \PyCore::import('string')->Template($template);
    }

    public function safe_substitute($mapping = [])
    {
        return $this->_self->safe_substitute($mapping);
    }

    public function substitute($mapping = [])
    {
        return $this->_self->substitute($mapping);
    }

}
