<?php
namespace python\pickle;

/**
*/
class _Unpickler
{
    private $_self;

    public function __construct($file)
    {
        $this->_self = \PyCore::import('pickle')->_Unpickler($file);
    }

    public function find_class($module, $name)
    {
        return $this->_self->find_class($module, $name);
    }

    public function get_extension($code)
    {
        return $this->_self->get_extension($code);
    }

    public function load()
    {
        return $this->_self->load();
    }

    public function load_additems()
    {
        return $this->_self->load_additems();
    }

    public function load_append()
    {
        return $this->_self->load_append();
    }

    public function load_appends()
    {
        return $this->_self->load_appends();
    }

    public function load_binbytes()
    {
        return $this->_self->load_binbytes();
    }

    public function load_binbytes8()
    {
        return $this->_self->load_binbytes8();
    }

    public function load_binfloat()
    {
        return $this->_self->load_binfloat();
    }

    public function load_binget()
    {
        return $this->_self->load_binget();
    }

    public function load_binint()
    {
        return $this->_self->load_binint();
    }

    public function load_binint1()
    {
        return $this->_self->load_binint1();
    }

    public function load_binint2()
    {
        return $this->_self->load_binint2();
    }

    public function load_binpersid()
    {
        return $this->_self->load_binpersid();
    }

    public function load_binput()
    {
        return $this->_self->load_binput();
    }

    public function load_binstring()
    {
        return $this->_self->load_binstring();
    }

    public function load_binunicode()
    {
        return $this->_self->load_binunicode();
    }

    public function load_binunicode8()
    {
        return $this->_self->load_binunicode8();
    }

    public function load_build()
    {
        return $this->_self->load_build();
    }

    public function load_bytearray8()
    {
        return $this->_self->load_bytearray8();
    }

    public function load_dict()
    {
        return $this->_self->load_dict();
    }

    public function load_dup()
    {
        return $this->_self->load_dup();
    }

    public function load_empty_dictionary()
    {
        return $this->_self->load_empty_dictionary();
    }

    public function load_empty_list()
    {
        return $this->_self->load_empty_list();
    }

    public function load_empty_set()
    {
        return $this->_self->load_empty_set();
    }

    public function load_empty_tuple()
    {
        return $this->_self->load_empty_tuple();
    }

    public function load_ext1()
    {
        return $this->_self->load_ext1();
    }

    public function load_ext2()
    {
        return $this->_self->load_ext2();
    }

    public function load_ext4()
    {
        return $this->_self->load_ext4();
    }

    public function load_false()
    {
        return $this->_self->load_false();
    }

    public function load_float()
    {
        return $this->_self->load_float();
    }

    public function load_frame()
    {
        return $this->_self->load_frame();
    }

    public function load_frozenset()
    {
        return $this->_self->load_frozenset();
    }

    public function load_get()
    {
        return $this->_self->load_get();
    }

    public function load_global()
    {
        return $this->_self->load_global();
    }

    public function load_inst()
    {
        return $this->_self->load_inst();
    }

    public function load_int()
    {
        return $this->_self->load_int();
    }

    public function load_list()
    {
        return $this->_self->load_list();
    }

    public function load_long()
    {
        return $this->_self->load_long();
    }

    public function load_long1()
    {
        return $this->_self->load_long1();
    }

    public function load_long4()
    {
        return $this->_self->load_long4();
    }

    public function load_long_binget()
    {
        return $this->_self->load_long_binget();
    }

    public function load_long_binput()
    {
        return $this->_self->load_long_binput();
    }

    public function load_mark()
    {
        return $this->_self->load_mark();
    }

    public function load_memoize()
    {
        return $this->_self->load_memoize();
    }

    public function load_newobj()
    {
        return $this->_self->load_newobj();
    }

    public function load_newobj_ex()
    {
        return $this->_self->load_newobj_ex();
    }

    public function load_next_buffer()
    {
        return $this->_self->load_next_buffer();
    }

    public function load_none()
    {
        return $this->_self->load_none();
    }

    public function load_obj()
    {
        return $this->_self->load_obj();
    }

    public function load_persid()
    {
        return $this->_self->load_persid();
    }

    public function load_pop()
    {
        return $this->_self->load_pop();
    }

    public function load_pop_mark()
    {
        return $this->_self->load_pop_mark();
    }

    public function load_proto()
    {
        return $this->_self->load_proto();
    }

    public function load_put()
    {
        return $this->_self->load_put();
    }

    public function load_readonly_buffer()
    {
        return $this->_self->load_readonly_buffer();
    }

    public function load_reduce()
    {
        return $this->_self->load_reduce();
    }

    public function load_setitem()
    {
        return $this->_self->load_setitem();
    }

    public function load_setitems()
    {
        return $this->_self->load_setitems();
    }

    public function load_short_binbytes()
    {
        return $this->_self->load_short_binbytes();
    }

    public function load_short_binstring()
    {
        return $this->_self->load_short_binstring();
    }

    public function load_short_binunicode()
    {
        return $this->_self->load_short_binunicode();
    }

    public function load_stack_global()
    {
        return $this->_self->load_stack_global();
    }

    public function load_stop()
    {
        return $this->_self->load_stop();
    }

    public function load_string()
    {
        return $this->_self->load_string();
    }

    public function load_true()
    {
        return $this->_self->load_true();
    }

    public function load_tuple()
    {
        return $this->_self->load_tuple();
    }

    public function load_tuple1()
    {
        return $this->_self->load_tuple1();
    }

    public function load_tuple2()
    {
        return $this->_self->load_tuple2();
    }

    public function load_tuple3()
    {
        return $this->_self->load_tuple3();
    }

    public function load_unicode()
    {
        return $this->_self->load_unicode();
    }

    public function persistent_load($pid)
    {
        return $this->_self->persistent_load($pid);
    }

    public function pop_mark()
    {
        return $this->_self->pop_mark();
    }

}
