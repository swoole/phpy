<?php
namespace python\pickle;

/**
*/
class _Pickler
{
    private $_self;

    public function __construct($file, $protocol = null)
    {
        $this->_self = \PyCore::import('pickle')->_Pickler($file, $protocol);
    }

    public function clear_memo()
    {
        return $this->_self->clear_memo();
    }

    public function dump($obj)
    {
        return $this->_self->dump($obj);
    }

    public function get($i)
    {
        return $this->_self->get($i);
    }

    public function memoize($obj)
    {
        return $this->_self->memoize($obj);
    }

    public function persistent_id($obj)
    {
        return $this->_self->persistent_id($obj);
    }

    public function put($idx)
    {
        return $this->_self->put($idx);
    }

    public function save($obj, $save_persistent_id = true)
    {
        return $this->_self->save($obj, $save_persistent_id);
    }

    public function save_bool($obj)
    {
        return $this->_self->save_bool($obj);
    }

    public function save_bytearray($obj)
    {
        return $this->_self->save_bytearray($obj);
    }

    public function save_bytes($obj)
    {
        return $this->_self->save_bytes($obj);
    }

    public function save_dict($obj)
    {
        return $this->_self->save_dict($obj);
    }

    public function save_float($obj)
    {
        return $this->_self->save_float($obj);
    }

    public function save_frozenset($obj)
    {
        return $this->_self->save_frozenset($obj);
    }

    public function save_global($obj, $name = null)
    {
        return $this->_self->save_global($obj, $name);
    }

    public function save_list($obj)
    {
        return $this->_self->save_list($obj);
    }

    public function save_long($obj)
    {
        return $this->_self->save_long($obj);
    }

    public function save_none($obj)
    {
        return $this->_self->save_none($obj);
    }

    public function save_pers($pid)
    {
        return $this->_self->save_pers($pid);
    }

    public function save_picklebuffer($obj)
    {
        return $this->_self->save_picklebuffer($obj);
    }

    public function save_reduce($func, $args, $state = null, $listitems = null, $dictitems = null, $state_setter = null)
    {
        return $this->_self->save_reduce($func, $args, $state, $listitems, $dictitems, $state_setter);
    }

    public function save_set($obj)
    {
        return $this->_self->save_set($obj);
    }

    public function save_str($obj)
    {
        return $this->_self->save_str($obj);
    }

    public function save_tuple($obj)
    {
        return $this->_self->save_tuple($obj);
    }

    public function save_type($obj)
    {
        return $this->_self->save_type($obj);
    }

}
