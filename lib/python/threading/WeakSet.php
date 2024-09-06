<?php
namespace python\threading;

/**
*/
class WeakSet
{
    private $_self;

    public function __construct($data = null)
    {
        $this->_self = \PyCore::import('threading')->WeakSet($data);
    }

    public function add($item)
    {
        return $this->_self->add($item);
    }

    public function clear()
    {
        return $this->_self->clear();
    }

    public function copy()
    {
        return $this->_self->copy();
    }

    public function difference($other)
    {
        return $this->_self->difference($other);
    }

    public function difference_update($other)
    {
        return $this->_self->difference_update($other);
    }

    public function discard($item)
    {
        return $this->_self->discard($item);
    }

    public function intersection($other)
    {
        return $this->_self->intersection($other);
    }

    public function intersection_update($other)
    {
        return $this->_self->intersection_update($other);
    }

    public function isdisjoint($other)
    {
        return $this->_self->isdisjoint($other);
    }

    public function issubset($other)
    {
        return $this->_self->issubset($other);
    }

    public function issuperset($other)
    {
        return $this->_self->issuperset($other);
    }

    public function pop()
    {
        return $this->_self->pop();
    }

    public function remove($item)
    {
        return $this->_self->remove($item);
    }

    public function symmetric_difference($other)
    {
        return $this->_self->symmetric_difference($other);
    }

    public function symmetric_difference_update($other)
    {
        return $this->_self->symmetric_difference_update($other);
    }

    public function union($other)
    {
        return $this->_self->union($other);
    }

    public function update($other)
    {
        return $this->_self->update($other);
    }

}
