<?php
namespace python;

use \PyModule;
use \PyCore;

/**
Thread module emulating a subset of Java's threading model.*/
class threading{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('threading');
            self::$Barrier = self::$__module->Barrier;
            self::$BoundedSemaphore = self::$__module->BoundedSemaphore;
            self::$BrokenBarrierError = self::$__module->BrokenBarrierError;
            self::$Condition = self::$__module->Condition;
            self::$Event = self::$__module->Event;
            self::$ExceptHookArgs = self::$__module->ExceptHookArgs;
            self::$Semaphore = self::$__module->Semaphore;
            self::$Thread = self::$__module->Thread;
            self::$ThreadError = self::$__module->ThreadError;
            self::$Timer = self::$__module->Timer;
            self::$WeakSet = self::$__module->WeakSet;
            self::$_CRLock = self::$__module->_CRLock;
            self::$_DummyThread = self::$__module->_DummyThread;
            self::$_MainThread = self::$__module->_MainThread;
            self::$_PyRLock = self::$__module->_PyRLock;
            self::$_RLock = self::$__module->_RLock;
            self::$_active = self::$__module->_active;
            self::$_active_limbo_lock = self::$__module->_active_limbo_lock;
            self::$_count = self::$__module->_count;
            self::$_counter = self::$__module->_counter;
            self::$_dangling = self::$__module->_dangling;
            self::$_deque = self::$__module->_deque;
            self::$_islice = self::$__module->_islice;
            self::$_limbo = self::$__module->_limbo;
            self::$_main_thread = self::$__module->_main_thread;
            self::$_os = self::$__module->_os;
            self::$_shutdown_locks = self::$__module->_shutdown_locks;
            self::$_shutdown_locks_lock = self::$__module->_shutdown_locks_lock;
            self::$_sys = self::$__module->_sys;
            self::$_threading_atexits = self::$__module->_threading_atexits;
            self::$functools = self::$__module->functools;
            self::$local = self::$__module->local;
        }
    }

    public const TIMEOUT_MAX = 9223372036;

    public static $_HAVE_THREAD_NATIVE_ID = true;
    public static $_SHUTTING_DOWN = false;
    public static $__name__ = "threading";
    public static $__package__ = "";
    public static $_profile_hook = null;
    public static $_trace_hook = null;

    public static $Barrier = null;
    public static $BoundedSemaphore = null;
    public static $BrokenBarrierError = null;
    public static $Condition = null;
    public static $Event = null;
    public static $ExceptHookArgs = null;
    public static $Semaphore = null;
    public static $Thread = null;
    public static $ThreadError = null;
    public static $Timer = null;
    public static $WeakSet = null;
    public static $_CRLock = null;
    public static $_DummyThread = null;
    public static $_MainThread = null;
    public static $_PyRLock = null;
    public static $_RLock = null;
    public static $_active = null;
    public static $_active_limbo_lock = null;
    public static $_count = null;
    public static $_counter = null;
    public static $_dangling = null;
    public static $_deque = null;
    public static $_islice = null;
    public static $_limbo = null;
    public static $_main_thread = null;
    public static $_os = null;
    public static $_shutdown_locks = null;
    public static $_shutdown_locks_lock = null;
    public static $_sys = null;
    public static $_threading_atexits = null;
    public static $functools = null;
    public static $local = null;

    public static function RLock()
    {
        return self::$__module->RLock();
    }
    public static function _after_fork()
    {
        return self::$__module->_after_fork();
    }
    public static function _enumerate()
    {
        return self::$__module->_enumerate();
    }
    public static function _maintain_shutdown_locks()
    {
        return self::$__module->_maintain_shutdown_locks();
    }
    public static function _make_invoke_excepthook()
    {
        return self::$__module->_make_invoke_excepthook();
    }
    public static function _newname($name_template)
    {
        return self::$__module->_newname($name_template);
    }
    public static function _register_atexit($func)
    {
        return self::$__module->_register_atexit($func);
    }
    public static function _shutdown()
    {
        return self::$__module->_shutdown();
    }
    public static function activeCount()
    {
        return self::$__module->activeCount();
    }
    public static function active_count()
    {
        return self::$__module->active_count();
    }
    public static function currentThread()
    {
        return self::$__module->currentThread();
    }
    public static function current_thread()
    {
        return self::$__module->current_thread();
    }
    public static function enumerate()
    {
        return self::$__module->enumerate();
    }
    public static function getprofile()
    {
        return self::$__module->getprofile();
    }
    public static function gettrace()
    {
        return self::$__module->gettrace();
    }
    public static function main_thread()
    {
        return self::$__module->main_thread();
    }
    public static function setprofile($func)
    {
        return self::$__module->setprofile($func);
    }
    public static function settrace($func)
    {
        return self::$__module->settrace($func);
    }
}

threading::__init();
