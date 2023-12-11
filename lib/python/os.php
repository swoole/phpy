<?php
namespace python;

/**
OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).
*/
class os{
    /**
    * @return os 
    */
    public static function import()
    {
        return \PyCore::import('os');
    }
    public $CLD_CONTINUED = 6;
    public $CLD_DUMPED = 3;
    public $CLD_EXITED = 1;
    public $CLD_KILLED = 2;
    public $CLD_STOPPED = 5;
    public $CLD_TRAPPED = 4;
    public $EFD_CLOEXEC = 524288;
    public $EFD_NONBLOCK = 2048;
    public $EFD_SEMAPHORE = 1;
    public $EX_CANTCREAT = 73;
    public $EX_CONFIG = 78;
    public $EX_DATAERR = 65;
    public $EX_IOERR = 74;
    public $EX_NOHOST = 68;
    public $EX_NOINPUT = 66;
    public $EX_NOPERM = 77;
    public $EX_NOUSER = 67;
    public $EX_OK = 0;
    public $EX_OSERR = 71;
    public $EX_OSFILE = 72;
    public $EX_PROTOCOL = 76;
    public $EX_SOFTWARE = 70;
    public $EX_TEMPFAIL = 75;
    public $EX_UNAVAILABLE = 69;
    public $EX_USAGE = 64;
    public $F_LOCK = 1;
    public $F_OK = 0;
    public $F_TEST = 3;
    public $F_TLOCK = 2;
    public $F_ULOCK = 0;
    public $GRND_NONBLOCK = 1;
    public $GRND_RANDOM = 2;
    public $NGROUPS_MAX = 65536;
    public $O_ACCMODE = 3;
    public $O_APPEND = 1024;
    public $O_ASYNC = 8192;
    public $O_CLOEXEC = 524288;
    public $O_CREAT = 64;
    public $O_DIRECT = 16384;
    public $O_DIRECTORY = 65536;
    public $O_DSYNC = 4096;
    public $O_EXCL = 128;
    public $O_FSYNC = 1052672;
    public $O_LARGEFILE = 0;
    public $O_NDELAY = 2048;
    public $O_NOATIME = 262144;
    public $O_NOCTTY = 256;
    public $O_NOFOLLOW = 131072;
    public $O_NONBLOCK = 2048;
    public $O_PATH = 2097152;
    public $O_RDONLY = 0;
    public $O_RDWR = 2;
    public $O_RSYNC = 1052672;
    public $O_SYNC = 1052672;
    public $O_TMPFILE = 4259840;
    public $O_TRUNC = 512;
    public $O_WRONLY = 1;
    public $POSIX_FADV_DONTNEED = 4;
    public $POSIX_FADV_NOREUSE = 5;
    public $POSIX_FADV_NORMAL = 0;
    public $POSIX_FADV_RANDOM = 1;
    public $POSIX_FADV_SEQUENTIAL = 2;
    public $POSIX_FADV_WILLNEED = 3;
    public $POSIX_SPAWN_CLOSE = 1;
    public $POSIX_SPAWN_DUP2 = 2;
    public $POSIX_SPAWN_OPEN = 0;
    public $PRIO_PGRP = 1;
    public $PRIO_PROCESS = 0;
    public $PRIO_USER = 2;
    public $P_ALL = 0;
    public $P_NOWAIT = 1;
    public $P_NOWAITO = 1;
    public $P_PGID = 2;
    public $P_PID = 1;
    public $P_WAIT = 0;
    public $RTLD_DEEPBIND = 8;
    public $RTLD_GLOBAL = 256;
    public $RTLD_LAZY = 1;
    public $RTLD_LOCAL = 0;
    public $RTLD_NODELETE = 4096;
    public $RTLD_NOLOAD = 4;
    public $RTLD_NOW = 2;
    public $R_OK = 4;
    public $SCHED_BATCH = 3;
    public $SCHED_FIFO = 1;
    public $SCHED_IDLE = 5;
    public $SCHED_OTHER = 0;
    public $SCHED_RESET_ON_FORK = 1073741824;
    public $SCHED_RR = 2;
    public $SEEK_CUR = 1;
    public $SEEK_DATA = 3;
    public $SEEK_END = 2;
    public $SEEK_HOLE = 4;
    public $SEEK_SET = 0;
    public $SPLICE_F_MORE = 4;
    public $SPLICE_F_MOVE = 1;
    public $SPLICE_F_NONBLOCK = 2;
    public $ST_APPEND = 256;
    public $ST_MANDLOCK = 64;
    public $ST_NOATIME = 1024;
    public $ST_NODEV = 4;
    public $ST_NODIRATIME = 2048;
    public $ST_NOEXEC = 8;
    public $ST_NOSUID = 2;
    public $ST_RDONLY = 1;
    public $ST_RELATIME = 4096;
    public $ST_SYNCHRONOUS = 16;
    public $ST_WRITE = 128;
    public $TMP_MAX = 238328;
    public $WCONTINUED = 8;
    public $WEXITED = 4;
    public $WNOHANG = 1;
    public $WNOWAIT = 16777216;
    public $WSTOPPED = 2;
    public $WUNTRACED = 2;
    public $W_OK = 2;
    public $XATTR_CREATE = 1;
    public $XATTR_REPLACE = 2;
    public $XATTR_SIZE_MAX = 65536;
    public $X_OK = 1;

    public $__name__ = "os";
    public $__package__ = "";
    public $altsep = null;
    public $curdir = ".";
    public $defpath = "/bin:/usr/bin";
    public $devnull = "/dev/null";
    public $extsep = ".";
    public $linesep = "\n";
    public $name = "posix";
    public $pardir = "..";
    public $pathsep = ":";
    public $sep = "/";
    public $supports_bytes_environ = true;

    public $DirEntry = null;
    public $GenericAlias = null;
    public $Mapping = null;
    public $MutableMapping = null;
    public $PathLike = null;
    public $_Environ = null;
    public $_wrap_close = null;
    public $abc = null;
    public $confstr_names = null;
    public $environ = null;
    public $environb = null;
    public $error = null;
    public $path = null;
    public $pathconf_names = null;
    public $sched_param = null;
    public $st = null;
    public $stat_result = null;
    public $statvfs_result = null;
    public $supports_dir_fd = null;
    public $supports_effective_ids = null;
    public $supports_fd = null;
    public $supports_follow_symlinks = null;
    public $sys = null;
    public $sysconf_names = null;
    public $terminal_size = null;
    public $times_result = null;
    public $uname_result = null;
    public $waitid_result = null;

    public function WCOREDUMP($status)
    {
    }

    public function WEXITSTATUS($status)
    {
    }

    public function WIFCONTINUED($status)
    {
    }

    public function WIFEXITED($status)
    {
    }

    public function WIFSIGNALED($status)
    {
    }

    public function WIFSTOPPED($status)
    {
    }

    public function WSTOPSIG($status)
    {
    }

    public function WTERMSIG($status)
    {
    }

    public function _check_methods($C)
    {
    }

    public function _execvpe($file, $args, $env = null)
    {
    }

    public function _exists($name)
    {
    }

    public function _exit($status)
    {
    }

    public function _fspath($path)
    {
    }

    public function _fwalk($topfd, $toppath, $isbytes, $topdown, $onerror, $follow_symlinks)
    {
    }

    public function _get_exports_list($module)
    {
    }

    public function _spawnvef($mode, $file, $args, $env, $func)
    {
    }

    public function _walk($top, $topdown, $onerror, $followlinks)
    {
    }

    public function abort()
    {
    }

    public function access($path, $mode)
    {
    }

    public function chdir($path)
    {
    }

    public function chmod($path, $mode)
    {
    }

    public function chown($path, $uid, $gid)
    {
    }

    public function chroot($path)
    {
    }

    public function close($fd)
    {
    }

    public function closerange($fd_low, $fd_high)
    {
    }

    public function confstr($name)
    {
    }

    public function cpu_count()
    {
    }

    public function ctermid()
    {
    }

    public function device_encoding($fd)
    {
    }

    public function dup($fd)
    {
    }

    public function dup2($fd, $fd2, $inheritable = true)
    {
    }

    public function eventfd($initval, $flags = 524288)
    {
    }

    public function eventfd_read($fd)
    {
    }

    public function eventfd_write($fd, $value)
    {
    }

    public function execl($file)
    {
    }

    public function execle($file)
    {
    }

    public function execlp($file)
    {
    }

    public function execlpe($file)
    {
    }

    public function execv($path, $argv)
    {
    }

    public function execve($path, $argv, $env)
    {
    }

    public function execvp($file, $args)
    {
    }

    public function execvpe($file, $args, $env)
    {
    }

    public function fchdir($fd)
    {
    }

    public function fchmod($fd, $mode)
    {
    }

    public function fchown($fd, $uid, $gid)
    {
    }

    public function fdatasync($fd)
    {
    }

    public function fdopen($fd, $mode = "r", $buffering = -1, $encoding = null)
    {
    }

    public function fork()
    {
    }

    public function forkpty()
    {
    }

    public function fpathconf($fd, $name)
    {
    }

    public function fsdecode($filename)
    {
    }

    public function fsencode($filename)
    {
    }

    public function fspath($path)
    {
    }

    public function fstat($fd)
    {
    }

    public function fstatvfs($fd)
    {
    }

    public function fsync($fd)
    {
    }

    public function ftruncate($fd, $length)
    {
    }

    public function fwalk($top = ".", $topdown = true, $onerror = null)
    {
    }

    public function get_blocking($fd)
    {
    }

    public function get_exec_path($env = null)
    {
    }

    public function get_inheritable($fd)
    {
    }

    public function getcwd()
    {
    }

    public function getcwdb()
    {
    }

    public function getegid()
    {
    }

    public function getenv($key, $default = null)
    {
    }

    public function getenvb($key, $default = null)
    {
    }

    public function geteuid()
    {
    }

    public function getgid()
    {
    }

    public function getgrouplist($user, $group)
    {
    }

    public function getgroups()
    {
    }

    public function getloadavg()
    {
    }

    public function getlogin()
    {
    }

    public function getpgid($pid)
    {
    }

    public function getpgrp()
    {
    }

    public function getpid()
    {
    }

    public function getppid()
    {
    }

    public function getpriority($which, $who)
    {
    }

    public function getrandom($size, $flags = 0)
    {
    }

    public function getresgid()
    {
    }

    public function getresuid()
    {
    }

    public function getsid($pid)
    {
    }

    public function getuid()
    {
    }

    public function getxattr($path, $attribute)
    {
    }

    public function initgroups($username, $gid)
    {
    }

    public function isatty($fd)
    {
    }

    public function kill($pid, $signal)
    {
    }

    public function killpg($pgid, $signal)
    {
    }

    public function lchown($path, $uid, $gid)
    {
    }

    public function link($src, $dst)
    {
    }

    public function listdir($path = null)
    {
    }

    public function listxattr($path = null)
    {
    }

    public function lockf($fd, $command, $length)
    {
    }

    public function login_tty($fd)
    {
    }

    public function lseek($fd, $position, $whence)
    {
    }

    public function lstat($path)
    {
    }

    public function major($device)
    {
    }

    public function makedev($major, $minor)
    {
    }

    public function makedirs($name, $mode = 511, $exist_ok = false)
    {
    }

    public function minor($device)
    {
    }

    public function mkdir($path, $mode = 511)
    {
    }

    public function mkfifo($path, $mode = 438)
    {
    }

    public function mknod($path, $mode = 384, $device = 0)
    {
    }

    public function nice($increment)
    {
    }

    public function open($path, $flags, $mode = 511)
    {
    }

    public function openpty()
    {
    }

    public function pathconf($path, $name)
    {
    }

    public function pipe()
    {
    }

    public function pipe2($flags)
    {
    }

    public function popen($cmd, $mode = "r", $buffering = -1)
    {
    }

    public function posix_fadvise($fd, $offset, $length, $advice)
    {
    }

    public function posix_fallocate($fd, $offset, $length)
    {
    }

    public function pread($fd, $length, $offset)
    {
    }

    public function preadv($fd, $buffers, $offset, $flags = 0)
    {
    }

    public function putenv($name, $value)
    {
    }

    public function pwrite($fd, $buffer, $offset)
    {
    }

    public function pwritev($fd, $buffers, $offset, $flags = 0)
    {
    }

    public function read($fd, $length)
    {
    }

    public function readlink($path)
    {
    }

    public function readv($fd, $buffers)
    {
    }

    public function remove($path)
    {
    }

    public function removedirs($name)
    {
    }

    public function removexattr($path, $attribute)
    {
    }

    public function rename($src, $dst)
    {
    }

    public function renames($old, $new)
    {
    }

    public function replace($src, $dst)
    {
    }

    public function rmdir($path)
    {
    }

    public function scandir($path = null)
    {
    }

    public function sched_get_priority_max($policy)
    {
    }

    public function sched_get_priority_min($policy)
    {
    }

    public function sched_getaffinity($pid)
    {
    }

    public function sched_getparam($pid)
    {
    }

    public function sched_getscheduler($pid)
    {
    }

    public function sched_rr_get_interval($pid)
    {
    }

    public function sched_setaffinity($pid, $mask)
    {
    }

    public function sched_setparam($pid, $param)
    {
    }

    public function sched_setscheduler($pid, $policy, $param)
    {
    }

    public function sched_yield()
    {
    }

    public function sendfile($out_fd, $in_fd, $offset, $count)
    {
    }

    public function set_blocking($fd, $blocking)
    {
    }

    public function set_inheritable($fd, $inheritable)
    {
    }

    public function setegid($egid)
    {
    }

    public function seteuid($euid)
    {
    }

    public function setgid($gid)
    {
    }

    public function setgroups($groups)
    {
    }

    public function setpgid($pid, $pgrp)
    {
    }

    public function setpgrp()
    {
    }

    public function setpriority($which, $who, $priority)
    {
    }

    public function setregid($rgid, $egid)
    {
    }

    public function setresgid($rgid, $egid, $sgid)
    {
    }

    public function setresuid($ruid, $euid, $suid)
    {
    }

    public function setreuid($ruid, $euid)
    {
    }

    public function setsid()
    {
    }

    public function setuid($uid)
    {
    }

    public function setxattr($path, $attribute, $value, $flags = 0)
    {
    }

    public function spawnl($mode, $file)
    {
    }

    public function spawnle($mode, $file)
    {
    }

    public function spawnlp($mode, $file)
    {
    }

    public function spawnlpe($mode, $file)
    {
    }

    public function spawnv($mode, $file, $args)
    {
    }

    public function spawnve($mode, $file, $args, $env)
    {
    }

    public function spawnvp($mode, $file, $args)
    {
    }

    public function spawnvpe($mode, $file, $args, $env)
    {
    }

    public function splice($src, $dst, $count, $offset_src = null, $offset_dst = null, $flags = 0)
    {
    }

    public function stat($path)
    {
    }

    public function statvfs($path)
    {
    }

    public function strerror($code)
    {
    }

    public function symlink($src, $dst, $target_is_directory = false)
    {
    }

    public function sync()
    {
    }

    public function sysconf($name)
    {
    }

    public function system($command)
    {
    }

    public function tcgetpgrp($fd)
    {
    }

    public function tcsetpgrp($fd, $pgid)
    {
    }

    public function times()
    {
    }

    public function truncate($path, $length)
    {
    }

    public function ttyname($fd)
    {
    }

    public function umask($mask)
    {
    }

    public function uname()
    {
    }

    public function unlink($path)
    {
    }

    public function unsetenv($name)
    {
    }

    public function urandom($size)
    {
    }

    public function wait()
    {
    }

    public function wait3($options)
    {
    }

    public function wait4($pid, $options)
    {
    }

    public function waitid($idtype, $id, $options)
    {
    }

    public function waitpid($pid, $options)
    {
    }

    public function waitstatus_to_exitcode($status)
    {
    }

    public function walk($top, $topdown = true, $onerror = null, $followlinks = false)
    {
    }

    public function write($fd, $data)
    {
    }

    public function writev($fd, $buffers)
    {
    }

}
