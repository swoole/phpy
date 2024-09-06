<?php
namespace python;

/**
Thread module emulating a subset of Java's threading model.*/
class threading
{
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

    /**
    * @return mixed
    */
    public function RLock()
    {
    }

    /**
    * @return mixed
    */
    public function _after_fork()
    {
    }

    /**
    * @return mixed
    */
    public function _enumerate()
    {
    }

    /**
    * @return mixed
    */
    public function _maintain_shutdown_locks()
    {
    }

    /**
    * @return mixed
    */
    public function _make_invoke_excepthook()
    {
    }

    /**
    * @return mixed
    */
    public function _newname($name_template)
    {
    }

    /**
    * @return mixed
    */
    public function _register_atexit($func)
    {
    }

    /**
    * @return mixed
    */
    public function _shutdown()
    {
    }

    /**
    * @return mixed
    */
    public function activeCount()
    {
    }

    /**
    * @return mixed
    */
    public function active_count()
    {
    }

    /**
    * @return mixed
    */
    public function currentThread()
    {
    }

    /**
    * @return mixed
    */
    public function current_thread()
    {
    }

    /**
    * @return mixed
    */
    public function enumerate()
    {
    }

    /**
    * @return mixed
    */
    public function getprofile()
    {
    }

    /**
    * @return mixed
    */
    public function gettrace()
    {
    }

    /**
    * @return mixed
    */
    public function main_thread()
    {
    }

    /**
    * @return mixed
    */
    public function setprofile($func)
    {
    }

    /**
    * @return mixed
    */
    public function settrace($func)
    {
    }

}
