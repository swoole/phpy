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
class os
{
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
    public $MFD_ALLOW_SEALING = 2;
    public $MFD_CLOEXEC = 1;
    public $MFD_HUGETLB = 4;
    public $MFD_HUGE_16GB = -2013265920;
    public $MFD_HUGE_16MB = 1610612736;
    public $MFD_HUGE_1GB = 2013265920;
    public $MFD_HUGE_1MB = 1342177280;
    public $MFD_HUGE_256MB = 1879048192;
    public $MFD_HUGE_2GB = 2080374784;
    public $MFD_HUGE_2MB = 1409286144;
    public $MFD_HUGE_32MB = 1677721600;
    public $MFD_HUGE_512KB = 1275068416;
    public $MFD_HUGE_512MB = 1946157056;
    public $MFD_HUGE_64KB = 1073741824;
    public $MFD_HUGE_8MB = 1543503872;
    public $MFD_HUGE_MASK = 63;
    public $MFD_HUGE_SHIFT = 26;
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
    public $P_PIDFD = 3;
    public $P_WAIT = 0;
    public $RTLD_DEEPBIND = 8;
    public $RTLD_GLOBAL = 256;
    public $RTLD_LAZY = 1;
    public $RTLD_LOCAL = 0;
    public $RTLD_NODELETE = 4096;
    public $RTLD_NOLOAD = 4;
    public $RTLD_NOW = 2;
    public $RWF_APPEND = 16;
    public $RWF_DSYNC = 2;
    public $RWF_HIPRI = 1;
    public $RWF_NOWAIT = 8;
    public $RWF_SYNC = 4;
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

    public $Mapping = null;
    public $MutableMapping = null;
    public $PathLike = null;
    public $_Environ = null;
    public $abc = null;
    public $confstr_names = null;
    public $environ = null;
    public $environb = null;
    public $path = null;
    public $pathconf_names = null;
    public $st = null;
    public $supports_dir_fd = null;
    public $supports_effective_ids = null;
    public $supports_fd = null;
    public $supports_follow_symlinks = null;
    public $sys = null;
    public $sysconf_names = null;

    /**
    * @return mixed
    */
    public function WCOREDUMP($status)
    {
    }

    /**
    * @return mixed
    */
    public function WEXITSTATUS($status)
    {
    }

    /**
    * @return mixed
    */
    public function WIFCONTINUED($status)
    {
    }

    /**
    * @return mixed
    */
    public function WIFEXITED($status)
    {
    }

    /**
    * @return mixed
    */
    public function WIFSIGNALED($status)
    {
    }

    /**
    * @return mixed
    */
    public function WIFSTOPPED($status)
    {
    }

    /**
    * @return mixed
    */
    public function WSTOPSIG($status)
    {
    }

    /**
    * @return mixed
    */
    public function WTERMSIG($status)
    {
    }

    /**
    * @return mixed
    */
    public function _check_methods($C)
    {
    }

    /**
    * @return mixed
    */
    public function _execvpe($file, $args, $env = null)
    {
    }

    /**
    * @return mixed
    */
    public function _exists($name)
    {
    }

    /**
    * @return mixed
    */
    public function _exit($status)
    {
    }

    /**
    * @return mixed
    */
    public function _fspath($path)
    {
    }

    /**
    * @return mixed
    */
    public function _fwalk($topfd, $toppath, $isbytes, $topdown, $onerror, $follow_symlinks)
    {
    }

    /**
    * @return mixed
    */
    public function _get_exports_list($module)
    {
    }

    /**
    * @return mixed
    */
    public function _spawnvef($mode, $file, $args, $env, $func)
    {
    }

    /**
    * @return mixed
    */
    public function _walk($top, $topdown, $onerror, $followlinks)
    {
    }

    /**
    * @return mixed
    */
    public function abort()
    {
    }

    /**
    * @return mixed
    */
    public function access($path, $mode)
    {
    }

    /**
    * @return mixed
    */
    public function chdir($path)
    {
    }

    /**
    * @return mixed
    */
    public function chmod($path, $mode)
    {
    }

    /**
    * @return mixed
    */
    public function chown($path, $uid, $gid)
    {
    }

    /**
    * @return mixed
    */
    public function chroot($path)
    {
    }

    /**
    * @return mixed
    */
    public function close($fd)
    {
    }

    /**
    * @return mixed
    */
    public function closerange($fd_low, $fd_high)
    {
    }

    /**
    * @return mixed
    */
    public function confstr($name)
    {
    }

    /**
    * @return mixed
    */
    public function copy_file_range($src, $dst, $count, $offset_src = null, $offset_dst = null)
    {
    }

    /**
    * @return mixed
    */
    public function cpu_count()
    {
    }

    /**
    * @return mixed
    */
    public function ctermid()
    {
    }

    /**
    * @return mixed
    */
    public function device_encoding($fd)
    {
    }

    /**
    * @return mixed
    */
    public function dup($fd)
    {
    }

    /**
    * @return mixed
    */
    public function dup2($fd, $fd2, $inheritable = true)
    {
    }

    /**
    * @return mixed
    */
    public function eventfd($initval, $flags = 524288)
    {
    }

    /**
    * @return mixed
    */
    public function eventfd_read($fd)
    {
    }

    /**
    * @return mixed
    */
    public function eventfd_write($fd, $value)
    {
    }

    /**
    * @return mixed
    */
    public function execl($file)
    {
    }

    /**
    * @return mixed
    */
    public function execle($file)
    {
    }

    /**
    * @return mixed
    */
    public function execlp($file)
    {
    }

    /**
    * @return mixed
    */
    public function execlpe($file)
    {
    }

    /**
    * @return mixed
    */
    public function execv($path, $argv)
    {
    }

    /**
    * @return mixed
    */
    public function execve($path, $argv, $env)
    {
    }

    /**
    * @return mixed
    */
    public function execvp($file, $args)
    {
    }

    /**
    * @return mixed
    */
    public function execvpe($file, $args, $env)
    {
    }

    /**
    * @return mixed
    */
    public function fchdir($fd)
    {
    }

    /**
    * @return mixed
    */
    public function fchmod($fd, $mode)
    {
    }

    /**
    * @return mixed
    */
    public function fchown($fd, $uid, $gid)
    {
    }

    /**
    * @return mixed
    */
    public function fdatasync($fd)
    {
    }

    /**
    * @return mixed
    */
    public function fdopen($fd, $mode = "r", $buffering = -1, $encoding = null)
    {
    }

    /**
    * @return mixed
    */
    public function fork()
    {
    }

    /**
    * @return mixed
    */
    public function forkpty()
    {
    }

    /**
    * @return mixed
    */
    public function fpathconf($fd, $name)
    {
    }

    /**
    * @return mixed
    */
    public function fsdecode($filename)
    {
    }

    /**
    * @return mixed
    */
    public function fsencode($filename)
    {
    }

    /**
    * @return mixed
    */
    public function fspath($path)
    {
    }

    /**
    * @return mixed
    */
    public function fstat($fd)
    {
    }

    /**
    * @return mixed
    */
    public function fstatvfs($fd)
    {
    }

    /**
    * @return mixed
    */
    public function fsync($fd)
    {
    }

    /**
    * @return mixed
    */
    public function ftruncate($fd, $length)
    {
    }

    /**
    * @return mixed
    */
    public function fwalk($top = ".", $topdown = true, $onerror = null)
    {
    }

    /**
    * @return mixed
    */
    public function get_blocking($fd)
    {
    }

    /**
    * @return mixed
    */
    public function get_exec_path($env = null)
    {
    }

    /**
    * @return mixed
    */
    public function get_inheritable($fd)
    {
    }

    /**
    * @return mixed
    */
    public function getcwd()
    {
    }

    /**
    * @return mixed
    */
    public function getcwdb()
    {
    }

    /**
    * @return mixed
    */
    public function getegid()
    {
    }

    /**
    * @return mixed
    */
    public function getenv($key, $default = null)
    {
    }

    /**
    * @return mixed
    */
    public function getenvb($key, $default = null)
    {
    }

    /**
    * @return mixed
    */
    public function geteuid()
    {
    }

    /**
    * @return mixed
    */
    public function getgid()
    {
    }

    /**
    * @return mixed
    */
    public function getgrouplist($user, $group)
    {
    }

    /**
    * @return mixed
    */
    public function getgroups()
    {
    }

    /**
    * @return mixed
    */
    public function getloadavg()
    {
    }

    /**
    * @return mixed
    */
    public function getlogin()
    {
    }

    /**
    * @return mixed
    */
    public function getpgid($pid)
    {
    }

    /**
    * @return mixed
    */
    public function getpgrp()
    {
    }

    /**
    * @return mixed
    */
    public function getpid()
    {
    }

    /**
    * @return mixed
    */
    public function getppid()
    {
    }

    /**
    * @return mixed
    */
    public function getpriority($which, $who)
    {
    }

    /**
    * @return mixed
    */
    public function getrandom($size, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function getresgid()
    {
    }

    /**
    * @return mixed
    */
    public function getresuid()
    {
    }

    /**
    * @return mixed
    */
    public function getsid($pid)
    {
    }

    /**
    * @return mixed
    */
    public function getuid()
    {
    }

    /**
    * @return mixed
    */
    public function getxattr($path, $attribute)
    {
    }

    /**
    * @return mixed
    */
    public function initgroups($username, $gid)
    {
    }

    /**
    * @return mixed
    */
    public function isatty($fd)
    {
    }

    /**
    * @return mixed
    */
    public function kill($pid, $signal)
    {
    }

    /**
    * @return mixed
    */
    public function killpg($pgid, $signal)
    {
    }

    /**
    * @return mixed
    */
    public function lchown($path, $uid, $gid)
    {
    }

    /**
    * @return mixed
    */
    public function link($src, $dst)
    {
    }

    /**
    * @return mixed
    */
    public function listdir($path = null)
    {
    }

    /**
    * @return mixed
    */
    public function listxattr($path = null)
    {
    }

    /**
    * @return mixed
    */
    public function lockf($fd, $command, $length)
    {
    }

    /**
    * @return mixed
    */
    public function lseek($fd, $position, $how)
    {
    }

    /**
    * @return mixed
    */
    public function lstat($path)
    {
    }

    /**
    * @return mixed
    */
    public function major($device)
    {
    }

    /**
    * @return mixed
    */
    public function makedev($major, $minor)
    {
    }

    /**
    * @return mixed
    */
    public function makedirs($name, $mode = 511, $exist_ok = false)
    {
    }

    /**
    * @return mixed
    */
    public function memfd_create($name, $flags = 1)
    {
    }

    /**
    * @return mixed
    */
    public function minor($device)
    {
    }

    /**
    * @return mixed
    */
    public function mkdir($path, $mode = 511)
    {
    }

    /**
    * @return mixed
    */
    public function mkfifo($path, $mode = 438)
    {
    }

    /**
    * @return mixed
    */
    public function mknod($path, $mode = 384, $device = 0)
    {
    }

    /**
    * @return mixed
    */
    public function nice($increment)
    {
    }

    /**
    * @return mixed
    */
    public function open($path, $flags, $mode = 511)
    {
    }

    /**
    * @return mixed
    */
    public function openpty()
    {
    }

    /**
    * @return mixed
    */
    public function pathconf($path, $name)
    {
    }

    /**
    * @return mixed
    */
    public function pidfd_open($pid, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function pipe()
    {
    }

    /**
    * @return mixed
    */
    public function pipe2($flags)
    {
    }

    /**
    * @return mixed
    */
    public function popen($cmd, $mode = "r", $buffering = -1)
    {
    }

    /**
    * @return mixed
    */
    public function posix_fadvise($fd, $offset, $length, $advice)
    {
    }

    /**
    * @return mixed
    */
    public function posix_fallocate($fd, $offset, $length)
    {
    }

    /**
    * @return mixed
    */
    public function pread($fd, $length, $offset)
    {
    }

    /**
    * @return mixed
    */
    public function preadv($fd, $buffers, $offset, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function putenv($name, $value)
    {
    }

    /**
    * @return mixed
    */
    public function pwrite($fd, $buffer, $offset)
    {
    }

    /**
    * @return mixed
    */
    public function pwritev($fd, $buffers, $offset, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function read($fd, $length)
    {
    }

    /**
    * @return mixed
    */
    public function readlink($path)
    {
    }

    /**
    * @return mixed
    */
    public function readv($fd, $buffers)
    {
    }

    /**
    * @return mixed
    */
    public function remove($path)
    {
    }

    /**
    * @return mixed
    */
    public function removedirs($name)
    {
    }

    /**
    * @return mixed
    */
    public function removexattr($path, $attribute)
    {
    }

    /**
    * @return mixed
    */
    public function rename($src, $dst)
    {
    }

    /**
    * @return mixed
    */
    public function renames($old, $new)
    {
    }

    /**
    * @return mixed
    */
    public function replace($src, $dst)
    {
    }

    /**
    * @return mixed
    */
    public function rmdir($path)
    {
    }

    /**
    * @return mixed
    */
    public function scandir($path = null)
    {
    }

    /**
    * @return mixed
    */
    public function sched_get_priority_max($policy)
    {
    }

    /**
    * @return mixed
    */
    public function sched_get_priority_min($policy)
    {
    }

    /**
    * @return mixed
    */
    public function sched_getaffinity($pid)
    {
    }

    /**
    * @return mixed
    */
    public function sched_getparam($pid)
    {
    }

    /**
    * @return mixed
    */
    public function sched_getscheduler($pid)
    {
    }

    /**
    * @return mixed
    */
    public function sched_rr_get_interval($pid)
    {
    }

    /**
    * @return mixed
    */
    public function sched_setaffinity($pid, $mask)
    {
    }

    /**
    * @return mixed
    */
    public function sched_setparam($pid, $param)
    {
    }

    /**
    * @return mixed
    */
    public function sched_setscheduler($pid, $policy, $param)
    {
    }

    /**
    * @return mixed
    */
    public function sched_yield()
    {
    }

    /**
    * @return mixed
    */
    public function sendfile($out_fd, $in_fd, $offset, $count)
    {
    }

    /**
    * @return mixed
    */
    public function set_blocking($fd, $blocking)
    {
    }

    /**
    * @return mixed
    */
    public function set_inheritable($fd, $inheritable)
    {
    }

    /**
    * @return mixed
    */
    public function setegid($egid)
    {
    }

    /**
    * @return mixed
    */
    public function seteuid($euid)
    {
    }

    /**
    * @return mixed
    */
    public function setgid($gid)
    {
    }

    /**
    * @return mixed
    */
    public function setgroups($groups)
    {
    }

    /**
    * @return mixed
    */
    public function setpgid($pid, $pgrp)
    {
    }

    /**
    * @return mixed
    */
    public function setpgrp()
    {
    }

    /**
    * @return mixed
    */
    public function setpriority($which, $who, $priority)
    {
    }

    /**
    * @return mixed
    */
    public function setregid($rgid, $egid)
    {
    }

    /**
    * @return mixed
    */
    public function setresgid($rgid, $egid, $sgid)
    {
    }

    /**
    * @return mixed
    */
    public function setresuid($ruid, $euid, $suid)
    {
    }

    /**
    * @return mixed
    */
    public function setreuid($ruid, $euid)
    {
    }

    /**
    * @return mixed
    */
    public function setsid()
    {
    }

    /**
    * @return mixed
    */
    public function setuid($uid)
    {
    }

    /**
    * @return mixed
    */
    public function setxattr($path, $attribute, $value, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function spawnl($mode, $file)
    {
    }

    /**
    * @return mixed
    */
    public function spawnle($mode, $file)
    {
    }

    /**
    * @return mixed
    */
    public function spawnlp($mode, $file)
    {
    }

    /**
    * @return mixed
    */
    public function spawnlpe($mode, $file)
    {
    }

    /**
    * @return mixed
    */
    public function spawnv($mode, $file, $args)
    {
    }

    /**
    * @return mixed
    */
    public function spawnve($mode, $file, $args, $env)
    {
    }

    /**
    * @return mixed
    */
    public function spawnvp($mode, $file, $args)
    {
    }

    /**
    * @return mixed
    */
    public function spawnvpe($mode, $file, $args, $env)
    {
    }

    /**
    * @return mixed
    */
    public function splice($src, $dst, $count, $offset_src = null, $offset_dst = null, $flags = 0)
    {
    }

    /**
    * @return mixed
    */
    public function stat($path)
    {
    }

    /**
    * @return mixed
    */
    public function statvfs($path)
    {
    }

    /**
    * @return mixed
    */
    public function strerror($code)
    {
    }

    /**
    * @return mixed
    */
    public function symlink($src, $dst, $target_is_directory = false)
    {
    }

    /**
    * @return mixed
    */
    public function sync()
    {
    }

    /**
    * @return mixed
    */
    public function sysconf($name)
    {
    }

    /**
    * @return mixed
    */
    public function system($command)
    {
    }

    /**
    * @return mixed
    */
    public function tcgetpgrp($fd)
    {
    }

    /**
    * @return mixed
    */
    public function tcsetpgrp($fd, $pgid)
    {
    }

    /**
    * @return mixed
    */
    public function times()
    {
    }

    /**
    * @return mixed
    */
    public function truncate($path, $length)
    {
    }

    /**
    * @return mixed
    */
    public function ttyname($fd)
    {
    }

    /**
    * @return mixed
    */
    public function umask($mask)
    {
    }

    /**
    * @return mixed
    */
    public function uname()
    {
    }

    /**
    * @return mixed
    */
    public function unlink($path)
    {
    }

    /**
    * @return mixed
    */
    public function unsetenv($name)
    {
    }

    /**
    * @return mixed
    */
    public function urandom($size)
    {
    }

    /**
    * @return mixed
    */
    public function wait()
    {
    }

    /**
    * @return mixed
    */
    public function wait3($options)
    {
    }

    /**
    * @return mixed
    */
    public function wait4($pid, $options)
    {
    }

    /**
    * @return mixed
    */
    public function waitid($idtype, $id, $options)
    {
    }

    /**
    * @return mixed
    */
    public function waitpid($pid, $options)
    {
    }

    /**
    * @return mixed
    */
    public function waitstatus_to_exitcode($status)
    {
    }

    /**
    * @return mixed
    */
    public function walk($top, $topdown = true, $onerror = null, $followlinks = false)
    {
    }

    /**
    * @return mixed
    */
    public function write($fd, $data)
    {
    }

    /**
    * @return mixed
    */
    public function writev($fd, $buffers)
    {
    }

}
