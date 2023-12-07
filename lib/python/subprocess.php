<?php
namespace python;

use \PyModule;
use \PyCore;

/**
Subprocesses with accessible I/O streams

This module allows you to spawn processes, connect to their
input/output/error pipes, and obtain their return codes.

For a complete description of this module see the Python documentation.

Main API
========
run(...): Runs a command, waits for it to complete, then returns a
          CompletedProcess instance.
Popen(...): A class for flexibly executing a command in a new process

Constants
---------
DEVNULL: Special value that indicates that os.devnull should be used
PIPE:    Special value that indicates a pipe should be created
STDOUT:  Special value that indicates that stderr should go to stdout


Older API
=========
call(...): Runs a command, waits for it to complete, then returns
    the return code.
check_call(...): Same as call() but raises CalledProcessError()
    if return code is not 0
check_output(...): Same as check_call() but returns the contents of
    stdout instead of a return code
getoutput(...): Runs a command in the shell, waits for it to complete,
    then returns the output
getstatusoutput(...): Runs a command in the shell, waits for it to complete,
    then returns a (exitcode, output) tuple
*/
class subprocess{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('subprocess');
            self::$CalledProcessError = self::$__module->CalledProcessError;
            self::$CompletedProcess = self::$__module->CompletedProcess;
            self::$Popen = self::$__module->Popen;
            self::$SubprocessError = self::$__module->SubprocessError;
            self::$TimeoutExpired = self::$__module->TimeoutExpired;
            self::$_PopenSelector = self::$__module->_PopenSelector;
            self::$__spec__ = self::$__module->__spec__;
            self::$_active = self::$__module->_active;
            self::$builtins = self::$__module->builtins;
            self::$contextlib = self::$__module->contextlib;
            self::$errno = self::$__module->errno;
            self::$fcntl = self::$__module->fcntl;
            self::$io = self::$__module->io;
            self::$locale = self::$__module->locale;
            self::$os = self::$__module->os;
            self::$select = self::$__module->select;
            self::$selectors = self::$__module->selectors;
            self::$signal = self::$__module->signal;
            self::$sys = self::$__module->sys;
            self::$threading = self::$__module->threading;
            self::$time = self::$__module->time;
            self::$types = self::$__module->types;
            self::$warnings = self::$__module->warnings;
        }
    }

    public const DEVNULL = -3;
    public const PIPE = -1;
    public const STDOUT = -2;
    public const _PIPE_BUF = 4096;
    public const _WNOHANG = 1;

    public static $_USE_POSIX_SPAWN = true;
    public static $_USE_VFORK = true;
    public static $__cached__ = "/opt/anaconda3/lib/python3.11/__pycache__/subprocess.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/subprocess.py";
    public static $__name__ = "subprocess";
    public static $__package__ = "";
    public static $_can_fork_exec = true;
    public static $_mswindows = false;

    public static $CalledProcessError = null;
    public static $CompletedProcess = null;
    public static $Popen = null;
    public static $SubprocessError = null;
    public static $TimeoutExpired = null;
    public static $_PopenSelector = null;
    public static $__spec__ = null;
    public static $_active = null;
    public static $builtins = null;
    public static $contextlib = null;
    public static $errno = null;
    public static $fcntl = null;
    public static $io = null;
    public static $locale = null;
    public static $os = null;
    public static $select = null;
    public static $selectors = null;
    public static $signal = null;
    public static $sys = null;
    public static $threading = null;
    public static $time = null;
    public static $types = null;
    public static $warnings = null;

    public static function _WIFSTOPPED($status)
    {
        return self::$__module->_WIFSTOPPED($status);
    }
    public static function _WSTOPSIG($status)
    {
        return self::$__module->_WSTOPSIG($status);
    }
    public static function _args_from_interpreter_flags()
    {
        return self::$__module->_args_from_interpreter_flags();
    }
    public static function _cleanup()
    {
        return self::$__module->_cleanup();
    }
    public static function _optim_args_from_interpreter_flags()
    {
        return self::$__module->_optim_args_from_interpreter_flags();
    }
    public static function _text_encoding()
    {
        return self::$__module->_text_encoding();
    }
    public static function _use_posix_spawn()
    {
        return self::$__module->_use_posix_spawn();
    }
    public static function _waitpid($pid, $options)
    {
        return self::$__module->_waitpid($pid, $options);
    }
    public static function _waitstatus_to_exitcode($status)
    {
        return self::$__module->_waitstatus_to_exitcode($status);
    }
    public static function call()
    {
        return self::$__module->call();
    }
    public static function check_call()
    {
        return self::$__module->check_call();
    }
    public static function check_output()
    {
        return self::$__module->check_output();
    }
    public static function getoutput($cmd)
    {
        return self::$__module->getoutput($cmd);
    }
    public static function getstatusoutput($cmd)
    {
        return self::$__module->getstatusoutput($cmd);
    }
    public static function list2cmdline($seq)
    {
        return self::$__module->list2cmdline($seq);
    }
    public static function run()
    {
        return self::$__module->run();
    }
}

subprocess::__init();
