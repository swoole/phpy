<?php

/**
 * @generate-function-entries
 */

class PyError extends Exception
{
    public ?PyObject $value = null;
    public ?PyObject $type = null;
    public ?PyObject $error = null;
    public ?PyObject $traceback = null;
}
