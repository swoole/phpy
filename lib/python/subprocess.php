<?php
namespace python;

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
    /**
    * @return subprocess 
    */
    public static function import()
    {
        return \PyCore::import('subprocess');
    }
    public $DEVNULL = -3;
    public $PIPE = -1;
    public $STDOUT = -2;
    public $_PIPE_BUF = 4096;
    public $_WNOHANG = 1;

    public $_USE_POSIX_SPAWN = true;
    public $_USE_VFORK = true;
    public $__name__ = "subprocess";
    public $__package__ = "";
    public $_can_fork_exec = true;
    public $_mswindows = false;

    public $CalledProcessError = null;
    public $CompletedProcess = null;
    public $Popen = null;
    public $SubprocessError = null;
    public $TimeoutExpired = null;
    public $_PopenSelector = null;
    public $_active = null;
    public $builtins = null;
    public $contextlib = null;
    public $errno = null;
    public $fcntl = null;
    public $io = null;
    public $locale = null;
    public $os = null;
    public $select = null;
    public $selectors = null;
    public $signal = null;
    public $sys = null;
    public $threading = null;
    public $time = null;
    public $types = null;
    public $warnings = null;

    public function _WIFSTOPPED($status)
    {
    }

    public function _WSTOPSIG($status)
    {
    }

    public function _args_from_interpreter_flags()
    {
    }

    public function _cleanup()
    {
    }

    public function _optim_args_from_interpreter_flags()
    {
    }

    public function _text_encoding()
    {
    }

    public function _use_posix_spawn()
    {
    }

    public function _waitpid($pid, $options)
    {
    }

    public function _waitstatus_to_exitcode($status)
    {
    }

    public function call()
    {
    }

    public function check_call()
    {
    }

    public function check_output()
    {
    }

    public function getoutput($cmd)
    {
    }

    public function getstatusoutput($cmd)
    {
    }

    public function list2cmdline($seq)
    {
    }

    public function run()
    {
    }

}
