<?php
namespace python\ast;

/**
*/
class NodeVisitor
{
    private $_self;

    public function __construct()
    {
        $this->_self = \PyCore::import('ast')->NodeVisitor();
    }

    public function generic_visit($node)
    {
        return $this->_self->generic_visit($node);
    }

    public function visit($node)
    {
        return $this->_self->visit($node);
    }

    public function visit_Constant($node)
    {
        return $this->_self->visit_Constant($node);
    }

}
