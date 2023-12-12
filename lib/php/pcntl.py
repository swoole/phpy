import phpy

WNOHANG = 1
WUNTRACED = 2
SIG_IGN = 1
SIG_DFL = 0
SIG_ERR = -1
SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGABRT = 6
SIGIOT = 6
SIGBUS = 7
SIGFPE = 8
SIGKILL = 9
SIGUSR1 = 10
SIGSEGV = 11
SIGUSR2 = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGSTKFLT = 16
SIGCHLD = 17
SIGCONT = 18
SIGSTOP = 19
SIGTSTP = 20
SIGTTIN = 21
SIGTTOU = 22
SIGURG = 23
SIGXCPU = 24
SIGXFSZ = 25
SIGVTALRM = 26
SIGPROF = 27
SIGWINCH = 28
SIGPOLL = 29
SIGIO = 29
SIGPWR = 30
SIGSYS = 31
SIGBABY = 31
SIGRTMIN = 35
SIGRTMAX = 64
PRIO_PGRP = 1
PRIO_USER = 2
PRIO_PROCESS = 0
SIG_BLOCK = 0
SIG_UNBLOCK = 1
SIG_SETMASK = 2
SI_USER = 0
SI_KERNEL = 128
SI_QUEUE = -1
SI_TIMER = -2
SI_MESGQ = -3
SI_ASYNCIO = -4
SI_SIGIO = -5
SI_TKILL = -6
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
TRAP_BRKPT = 1
TRAP_TRACE = 2
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 7
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
CLONE_NEWNS = 131072
CLONE_NEWIPC = 134217728
CLONE_NEWUTS = 67108864
CLONE_NEWNET = 1073741824
CLONE_NEWPID = 536870912
CLONE_NEWUSER = 268435456
CLONE_NEWCGROUP = 33554432
EINTR = 4
ECHILD = 10
EINVAL = 22
EAGAIN = 11
ESRCH = 3
EACCES = 13
EPERM = 1
ENOMEM = 12
E2BIG = 7
EFAULT = 14
EIO = 5
EISDIR = 21
ELIBBAD = 80
ELOOP = 40
EMFILE = 24
ENAMETOOLONG = 36
ENFILE = 23
ENOENT = 2
ENOEXEC = 8
ENOTDIR = 20
ETXTBSY = 26
ENOSPC = 28
EUSERS = 87


def fork():
    return phpy.call('pcntl_fork', )


def waitpid(_process_id, _status, _flags=0, _resource_usage=[]):
    return phpy.call('pcntl_waitpid', _process_id, _status, _flags, _resource_usage)


def wait(_status, _flags=0, _resource_usage=[]):
    return phpy.call('pcntl_wait', _status, _flags, _resource_usage)


def signal(_signal, _handler, _restart_syscalls=True):
    return phpy.call('pcntl_signal', _signal, _handler, _restart_syscalls)


def signal_get_handler(_signal):
    return phpy.call('pcntl_signal_get_handler', _signal)


def signal_dispatch():
    return phpy.call('pcntl_signal_dispatch', )


def sigprocmask(_mode, _signals, _old_signals=None):
    return phpy.call('pcntl_sigprocmask', _mode, _signals, _old_signals)


def sigwaitinfo(_signals, _info=[]):
    return phpy.call('pcntl_sigwaitinfo', _signals, _info)


def sigtimedwait(_signals, _info=[], _seconds=0, _nanoseconds=0):
    return phpy.call('pcntl_sigtimedwait', _signals, _info, _seconds, _nanoseconds)


def wifexited(_status):
    return phpy.call('pcntl_wifexited', _status)


def wifstopped(_status):
    return phpy.call('pcntl_wifstopped', _status)


def wifsignaled(_status):
    return phpy.call('pcntl_wifsignaled', _status)


def wexitstatus(_status):
    return phpy.call('pcntl_wexitstatus', _status)


def wtermsig(_status):
    return phpy.call('pcntl_wtermsig', _status)


def wstopsig(_status):
    return phpy.call('pcntl_wstopsig', _status)


def exec(_path, _args=[], _env_vars=[]):
    return phpy.call('pcntl_exec', _path, _args, _env_vars)


def alarm(_seconds):
    return phpy.call('pcntl_alarm', _seconds)


def get_last_error():
    return phpy.call('pcntl_get_last_error', )


def errno():
    return phpy.call('pcntl_errno', )


def getpriority(_process_id=None, _mode=0):
    return phpy.call('pcntl_getpriority', _process_id, _mode)


def setpriority(_priority, _process_id=None, _mode=0):
    return phpy.call('pcntl_setpriority', _priority, _process_id, _mode)


def strerror(_error_code):
    return phpy.call('pcntl_strerror', _error_code)


def async_signals(_enable=None):
    return phpy.call('pcntl_async_signals', _enable)


def unshare(_flags):
    return phpy.call('pcntl_unshare', _flags)




