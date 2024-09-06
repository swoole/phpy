<?php
namespace python\string;

/**
*/
class Formatter
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('string')->Formatter();
    }

    public function check_unused_args($used_args, $args, $kwargs)
    {
        return $this->_self->check_unused_args($used_args, $args, $kwargs);
    }

    public function convert_field($value, $conversion)
    {
        return $this->_self->convert_field($value, $conversion);
    }

    public function format($format_string)
    {
        return $this->_self->format($format_string);
    }

    public function format_field($value, $format_spec)
    {
        return $this->_self->format_field($value, $format_spec);
    }

    public function get_field($field_name, $args, $kwargs)
    {
        return $this->_self->get_field($field_name, $args, $kwargs);
    }

    public function get_value($key, $args, $kwargs)
    {
        return $this->_self->get_value($key, $args, $kwargs);
    }

    public function parse($format_string)
    {
        return $this->_self->parse($format_string);
    }

    public function vformat($format_string, $args, $kwargs)
    {
        return $this->_self->vformat($format_string, $args, $kwargs);
    }

}
