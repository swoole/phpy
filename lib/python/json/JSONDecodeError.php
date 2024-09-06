<?php
namespace python\json;

/**
*/
class JSONDecodeError
{
    private $_self;

    public function __construct($msg, $doc, $pos)
    {
        $this->_self = \PyCore::import('json')->JSONDecodeError($msg, $doc, $pos);
    }

}
