<?php
namespace python\subprocess;

/**
* @property $universal_newlines
*/
class Popen
{
    private $_self;

    public function __construct($args, $bufsize = -1, $executable = null, $stdin = null, $stdout = null, $stderr = null, $preexec_fn = null, $close_fds = true, $shell = false, $cwd = null, $env = null, $universal_newlines = null, $startupinfo = null, $creationflags = 0, $restore_signals = true, $start_new_session = false, $pass_fds = [])
    {
        $this->_self = \PyCore::import('subprocess')->Popen($args, $bufsize, $executable, $stdin, $stdout, $stderr, $preexec_fn, $close_fds, $shell, $cwd, $env, $universal_newlines, $startupinfo, $creationflags, $restore_signals, $start_new_session, $pass_fds);
    }

    public function communicate($input = null, $timeout = null)
    {
        return $this->_self->communicate($input, $timeout);
    }

    public function kill()
    {
        return $this->_self->kill();
    }

    public function poll()
    {
        return $this->_self->poll();
    }

    public function send_signal($sig)
    {
        return $this->_self->send_signal($sig);
    }

    public function terminate()
    {
        return $this->_self->terminate();
    }

    public function wait($timeout = null)
    {
        return $this->_self->wait($timeout);
    }

}
