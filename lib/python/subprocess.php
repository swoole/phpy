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
class subprocess
{
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

    public $_USE_POSIX_SPAWN = true;
    public $_USE_VFORK = true;
    public $__name__ = "subprocess";
    public $__package__ = "";
    public $_mswindows = false;

    public $_PopenSelector = null;
    public $_active = null;
    public $_posixsubprocess = null;
    public $builtins = null;
    public $contextlib = null;
    public $errno = null;
    public $fcntl = null;
    public $io = null;
    public $os = null;
    public $select = null;
    public $selectors = null;
    public $signal = null;
    public $sys = null;
    public $threading = null;
    public $time = null;
    public $types = null;
    public $warnings = null;

    /**
    * @return mixed
    */
    public function _args_from_interpreter_flags()
    {
    }

    /**
    * @return mixed
    */
    public function _cleanup()
    {
    }

    /**
    * @return mixed
    */
    public function _optim_args_from_interpreter_flags()
    {
    }

    /**
    * @return mixed
    */
    public function _use_posix_spawn()
    {
    }

    /**
    * @return mixed
    */
    public function call()
    {
    }

    /**
    * @return mixed
    */
    public function check_call()
    {
    }

    /**
    * @return mixed
    */
    public function check_output()
    {
    }

    /**
    * @return mixed
    */
    public function getoutput($cmd)
    {
    }

    /**
    * @return mixed
    */
    public function getstatusoutput($cmd)
    {
    }

    /**
    * @return mixed
    */
    public function list2cmdline($seq)
    {
    }

    /**
    * @return mixed
    */
    public function run()
    {
    }

}
