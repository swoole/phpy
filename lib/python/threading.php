<?php
namespace python;

/**
Thread module emulating a subset of Java's threading model.*/
class threading{
    /**
    * @return threading 
    */
    public static function import()
    {
        return \PyCore::import('threading');
    }
    public $TIMEOUT_MAX = 9223372036;

    public $_HAVE_THREAD_NATIVE_ID = true;
    public $_SHUTTING_DOWN = false;
    public $__name__ = "threading";
    public $__package__ = "";
    public $_profile_hook = null;
    public $_trace_hook = null;

    public $_active = null;
    public $_active_limbo_lock = null;
    public $_counter = null;
    public $_dangling = null;
    public $_limbo = null;
    public $_main_thread = null;
    public $_os = null;
    public $_shutdown_locks = null;
    public $_shutdown_locks_lock = null;
    public $_sys = null;
    public $_threading_atexits = null;
    public $functools = null;

    public function RLock()
    {
    }

    public function _after_fork()
    {
    }

    public function _enumerate()
    {
    }

    public function _maintain_shutdown_locks()
    {
    }

    public function _make_invoke_excepthook()
    {
    }

    public function _newname($name_template)
    {
    }

    public function _register_atexit($func)
    {
    }

    public function _shutdown()
    {
    }

    public function activeCount()
    {
    }

    public function active_count()
    {
    }

    public function currentThread()
    {
    }

    public function current_thread()
    {
    }

    public function enumerate()
    {
    }

    public function getprofile()
    {
    }

    public function gettrace()
    {
    }

    public function main_thread()
    {
    }

    public function setprofile($func)
    {
    }

    public function settrace($func)
    {
    }

}
