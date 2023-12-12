import phpy

F_OK = 0
X_OK = 1
W_OK = 2
R_OK = 4
S_IFREG = 32768
S_IFCHR = 8192
S_IFBLK = 24576
S_IFIFO = 4096
S_IFSOCK = 49152
RLIMIT_AS = 9
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_LOCKS = 10
RLIMIT_MEMLOCK = 8
RLIMIT_MSGQUEUE = 12
RLIMIT_NICE = 13
RLIMIT_NOFILE = 7
RLIMIT_NPROC = 6
RLIMIT_RSS = 5
RLIMIT_RTPRIO = 14
RLIMIT_RTTIME = 15
RLIMIT_SIGPENDING = 11
RLIMIT_STACK = 3
RLIMIT_INFINITY = -1


def kill(_process_id, _signal):
    return phpy.call('posix_kill', _process_id, _signal)


def getpid():
    return phpy.call('posix_getpid', )


def getppid():
    return phpy.call('posix_getppid', )


def getuid():
    return phpy.call('posix_getuid', )


def setuid(_user_id):
    return phpy.call('posix_setuid', _user_id)


def geteuid():
    return phpy.call('posix_geteuid', )


def seteuid(_user_id):
    return phpy.call('posix_seteuid', _user_id)


def getgid():
    return phpy.call('posix_getgid', )


def setgid(_group_id):
    return phpy.call('posix_setgid', _group_id)


def getegid():
    return phpy.call('posix_getegid', )


def setegid(_group_id):
    return phpy.call('posix_setegid', _group_id)


def getgroups():
    return phpy.call('posix_getgroups', )


def getlogin():
    return phpy.call('posix_getlogin', )


def getpgrp():
    return phpy.call('posix_getpgrp', )


def setsid():
    return phpy.call('posix_setsid', )


def setpgid(_process_id, _process_group_id):
    return phpy.call('posix_setpgid', _process_id, _process_group_id)


def getpgid(_process_id):
    return phpy.call('posix_getpgid', _process_id)


def getsid(_process_id):
    return phpy.call('posix_getsid', _process_id)


def uname():
    return phpy.call('posix_uname', )


def times():
    return phpy.call('posix_times', )


def ctermid():
    return phpy.call('posix_ctermid', )


def ttyname(_file_descriptor):
    return phpy.call('posix_ttyname', _file_descriptor)


def isatty(_file_descriptor):
    return phpy.call('posix_isatty', _file_descriptor)


def getcwd():
    return phpy.call('posix_getcwd', )


def mkfifo(_filename, _permissions):
    return phpy.call('posix_mkfifo', _filename, _permissions)


def mknod(_filename, _flags, _major=0, _minor=0):
    return phpy.call('posix_mknod', _filename, _flags, _major, _minor)


def access(_filename, _flags=0):
    return phpy.call('posix_access', _filename, _flags)


def getgrnam(_name):
    return phpy.call('posix_getgrnam', _name)


def getgrgid(_group_id):
    return phpy.call('posix_getgrgid', _group_id)


def getpwnam(_username):
    return phpy.call('posix_getpwnam', _username)


def getpwuid(_user_id):
    return phpy.call('posix_getpwuid', _user_id)


def getrlimit():
    return phpy.call('posix_getrlimit', )


def setrlimit(_resource, _soft_limit, _hard_limit):
    return phpy.call('posix_setrlimit', _resource, _soft_limit, _hard_limit)


def get_last_error():
    return phpy.call('posix_get_last_error', )


def errno():
    return phpy.call('posix_errno', )


def strerror(_error_code):
    return phpy.call('posix_strerror', _error_code)


def initgroups(_username, _group_id):
    return phpy.call('posix_initgroups', _username, _group_id)




