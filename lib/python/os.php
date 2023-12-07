<?php
namespace python;

use \PyModule;
use \PyCore;

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
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('os');
            self::$DirEntry = self::$__module->DirEntry;
            self::$GenericAlias = self::$__module->GenericAlias;
            self::$Mapping = self::$__module->Mapping;
            self::$MutableMapping = self::$__module->MutableMapping;
            self::$PathLike = self::$__module->PathLike;
            self::$_Environ = self::$__module->_Environ;
            self::$_wrap_close = self::$__module->_wrap_close;
            self::$abc = self::$__module->abc;
            self::$confstr_names = self::$__module->confstr_names;
            self::$environ = self::$__module->environ;
            self::$environb = self::$__module->environb;
            self::$error = self::$__module->error;
            self::$path = self::$__module->path;
            self::$pathconf_names = self::$__module->pathconf_names;
            self::$sched_param = self::$__module->sched_param;
            self::$st = self::$__module->st;
            self::$stat_result = self::$__module->stat_result;
            self::$statvfs_result = self::$__module->statvfs_result;
            self::$supports_dir_fd = self::$__module->supports_dir_fd;
            self::$supports_effective_ids = self::$__module->supports_effective_ids;
            self::$supports_fd = self::$__module->supports_fd;
            self::$supports_follow_symlinks = self::$__module->supports_follow_symlinks;
            self::$sys = self::$__module->sys;
            self::$sysconf_names = self::$__module->sysconf_names;
            self::$terminal_size = self::$__module->terminal_size;
            self::$times_result = self::$__module->times_result;
            self::$uname_result = self::$__module->uname_result;
            self::$waitid_result = self::$__module->waitid_result;
        }
    }

    public const CLD_CONTINUED = 6;
    public const CLD_DUMPED = 3;
    public const CLD_EXITED = 1;
    public const CLD_KILLED = 2;
    public const CLD_STOPPED = 5;
    public const CLD_TRAPPED = 4;
    public const EFD_CLOEXEC = 524288;
    public const EFD_NONBLOCK = 2048;
    public const EFD_SEMAPHORE = 1;
    public const EX_CANTCREAT = 73;
    public const EX_CONFIG = 78;
    public const EX_DATAERR = 65;
    public const EX_IOERR = 74;
    public const EX_NOHOST = 68;
    public const EX_NOINPUT = 66;
    public const EX_NOPERM = 77;
    public const EX_NOUSER = 67;
    public const EX_OK = 0;
    public const EX_OSERR = 71;
    public const EX_OSFILE = 72;
    public const EX_PROTOCOL = 76;
    public const EX_SOFTWARE = 70;
    public const EX_TEMPFAIL = 75;
    public const EX_UNAVAILABLE = 69;
    public const EX_USAGE = 64;
    public const F_LOCK = 1;
    public const F_OK = 0;
    public const F_TEST = 3;
    public const F_TLOCK = 2;
    public const F_ULOCK = 0;
    public const GRND_NONBLOCK = 1;
    public const GRND_RANDOM = 2;
    public const NGROUPS_MAX = 65536;
    public const O_ACCMODE = 3;
    public const O_APPEND = 1024;
    public const O_ASYNC = 8192;
    public const O_CLOEXEC = 524288;
    public const O_CREAT = 64;
    public const O_DIRECT = 16384;
    public const O_DIRECTORY = 65536;
    public const O_DSYNC = 4096;
    public const O_EXCL = 128;
    public const O_FSYNC = 1052672;
    public const O_LARGEFILE = 0;
    public const O_NDELAY = 2048;
    public const O_NOATIME = 262144;
    public const O_NOCTTY = 256;
    public const O_NOFOLLOW = 131072;
    public const O_NONBLOCK = 2048;
    public const O_PATH = 2097152;
    public const O_RDONLY = 0;
    public const O_RDWR = 2;
    public const O_RSYNC = 1052672;
    public const O_SYNC = 1052672;
    public const O_TMPFILE = 4259840;
    public const O_TRUNC = 512;
    public const O_WRONLY = 1;
    public const POSIX_FADV_DONTNEED = 4;
    public const POSIX_FADV_NOREUSE = 5;
    public const POSIX_FADV_NORMAL = 0;
    public const POSIX_FADV_RANDOM = 1;
    public const POSIX_FADV_SEQUENTIAL = 2;
    public const POSIX_FADV_WILLNEED = 3;
    public const POSIX_SPAWN_CLOSE = 1;
    public const POSIX_SPAWN_DUP2 = 2;
    public const POSIX_SPAWN_OPEN = 0;
    public const PRIO_PGRP = 1;
    public const PRIO_PROCESS = 0;
    public const PRIO_USER = 2;
    public const P_ALL = 0;
    public const P_NOWAIT = 1;
    public const P_NOWAITO = 1;
    public const P_PGID = 2;
    public const P_PID = 1;
    public const P_WAIT = 0;
    public const RTLD_DEEPBIND = 8;
    public const RTLD_GLOBAL = 256;
    public const RTLD_LAZY = 1;
    public const RTLD_LOCAL = 0;
    public const RTLD_NODELETE = 4096;
    public const RTLD_NOLOAD = 4;
    public const RTLD_NOW = 2;
    public const R_OK = 4;
    public const SCHED_BATCH = 3;
    public const SCHED_FIFO = 1;
    public const SCHED_IDLE = 5;
    public const SCHED_OTHER = 0;
    public const SCHED_RESET_ON_FORK = 1073741824;
    public const SCHED_RR = 2;
    public const SEEK_CUR = 1;
    public const SEEK_DATA = 3;
    public const SEEK_END = 2;
    public const SEEK_HOLE = 4;
    public const SEEK_SET = 0;
    public const SPLICE_F_MORE = 4;
    public const SPLICE_F_MOVE = 1;
    public const SPLICE_F_NONBLOCK = 2;
    public const ST_APPEND = 256;
    public const ST_MANDLOCK = 64;
    public const ST_NOATIME = 1024;
    public const ST_NODEV = 4;
    public const ST_NODIRATIME = 2048;
    public const ST_NOEXEC = 8;
    public const ST_NOSUID = 2;
    public const ST_RDONLY = 1;
    public const ST_RELATIME = 4096;
    public const ST_SYNCHRONOUS = 16;
    public const ST_WRITE = 128;
    public const TMP_MAX = 238328;
    public const WCONTINUED = 8;
    public const WEXITED = 4;
    public const WNOHANG = 1;
    public const WNOWAIT = 16777216;
    public const WSTOPPED = 2;
    public const WUNTRACED = 2;
    public const W_OK = 2;
    public const XATTR_CREATE = 1;
    public const XATTR_REPLACE = 2;
    public const XATTR_SIZE_MAX = 65536;
    public const X_OK = 1;

    public static $__name__ = "os";
    public static $__package__ = "";
    public static $altsep = null;
    public static $curdir = ".";
    public static $defpath = "/bin:/usr/bin";
    public static $devnull = "/dev/null";
    public static $extsep = ".";
    public static $linesep = "\n";
    public static $name = "posix";
    public static $pardir = "..";
    public static $pathsep = ":";
    public static $sep = "/";
    public static $supports_bytes_environ = true;

    public static $DirEntry = null;
    public static $GenericAlias = null;
    public static $Mapping = null;
    public static $MutableMapping = null;
    public static $PathLike = null;
    public static $_Environ = null;
    public static $_wrap_close = null;
    public static $abc = null;
    public static $confstr_names = null;
    public static $environ = null;
    public static $environb = null;
    public static $error = null;
    public static $path = null;
    public static $pathconf_names = null;
    public static $sched_param = null;
    public static $st = null;
    public static $stat_result = null;
    public static $statvfs_result = null;
    public static $supports_dir_fd = null;
    public static $supports_effective_ids = null;
    public static $supports_fd = null;
    public static $supports_follow_symlinks = null;
    public static $sys = null;
    public static $sysconf_names = null;
    public static $terminal_size = null;
    public static $times_result = null;
    public static $uname_result = null;
    public static $waitid_result = null;

    public static function WCOREDUMP($status)
    {
        return self::$__module->WCOREDUMP($status);
    }
    public static function WEXITSTATUS($status)
    {
        return self::$__module->WEXITSTATUS($status);
    }
    public static function WIFCONTINUED($status)
    {
        return self::$__module->WIFCONTINUED($status);
    }
    public static function WIFEXITED($status)
    {
        return self::$__module->WIFEXITED($status);
    }
    public static function WIFSIGNALED($status)
    {
        return self::$__module->WIFSIGNALED($status);
    }
    public static function WIFSTOPPED($status)
    {
        return self::$__module->WIFSTOPPED($status);
    }
    public static function WSTOPSIG($status)
    {
        return self::$__module->WSTOPSIG($status);
    }
    public static function WTERMSIG($status)
    {
        return self::$__module->WTERMSIG($status);
    }
    public static function _check_methods($C)
    {
        return self::$__module->_check_methods($C);
    }
    public static function _execvpe($file, $args, $env=null)
    {
        return self::$__module->_execvpe($file, $args, $env);
    }
    public static function _exists($name)
    {
        return self::$__module->_exists($name);
    }
    public static function _exit($status)
    {
        return self::$__module->_exit($status);
    }
    public static function _fspath($path)
    {
        return self::$__module->_fspath($path);
    }
    public static function _fwalk($topfd, $toppath, $isbytes, $topdown, $onerror, $follow_symlinks)
    {
        return self::$__module->_fwalk($topfd, $toppath, $isbytes, $topdown, $onerror, $follow_symlinks);
    }
    public static function _get_exports_list($module)
    {
        return self::$__module->_get_exports_list($module);
    }
    public static function _spawnvef($mode, $file, $args, $env, $func)
    {
        return self::$__module->_spawnvef($mode, $file, $args, $env, $func);
    }
    public static function _walk($top, $topdown, $onerror, $followlinks)
    {
        return self::$__module->_walk($top, $topdown, $onerror, $followlinks);
    }
    public static function abort()
    {
        return self::$__module->abort();
    }
    public static function access($path, $mode)
    {
        return self::$__module->access($path, $mode);
    }
    public static function chdir($path)
    {
        return self::$__module->chdir($path);
    }
    public static function chmod($path, $mode)
    {
        return self::$__module->chmod($path, $mode);
    }
    public static function chown($path, $uid, $gid)
    {
        return self::$__module->chown($path, $uid, $gid);
    }
    public static function chroot($path)
    {
        return self::$__module->chroot($path);
    }
    public static function close($fd)
    {
        return self::$__module->close($fd);
    }
    public static function closerange($fd_low, $fd_high)
    {
        return self::$__module->closerange($fd_low, $fd_high);
    }
    public static function confstr($name)
    {
        return self::$__module->confstr($name);
    }
    public static function cpu_count()
    {
        return self::$__module->cpu_count();
    }
    public static function ctermid()
    {
        return self::$__module->ctermid();
    }
    public static function device_encoding($fd)
    {
        return self::$__module->device_encoding($fd);
    }
    public static function dup($fd)
    {
        return self::$__module->dup($fd);
    }
    public static function dup2($fd, $fd2, $inheritable=true)
    {
        return self::$__module->dup2($fd, $fd2, $inheritable);
    }
    public static function eventfd($initval, $flags=524288)
    {
        return self::$__module->eventfd($initval, $flags);
    }
    public static function eventfd_read($fd)
    {
        return self::$__module->eventfd_read($fd);
    }
    public static function eventfd_write($fd, $value)
    {
        return self::$__module->eventfd_write($fd, $value);
    }
    public static function execl($file)
    {
        return self::$__module->execl($file);
    }
    public static function execle($file)
    {
        return self::$__module->execle($file);
    }
    public static function execlp($file)
    {
        return self::$__module->execlp($file);
    }
    public static function execlpe($file)
    {
        return self::$__module->execlpe($file);
    }
    public static function execv($path, $argv)
    {
        return self::$__module->execv($path, $argv);
    }
    public static function execve($path, $argv, $env)
    {
        return self::$__module->execve($path, $argv, $env);
    }
    public static function execvp($file, $args)
    {
        return self::$__module->execvp($file, $args);
    }
    public static function execvpe($file, $args, $env)
    {
        return self::$__module->execvpe($file, $args, $env);
    }
    public static function fchdir($fd)
    {
        return self::$__module->fchdir($fd);
    }
    public static function fchmod($fd, $mode)
    {
        return self::$__module->fchmod($fd, $mode);
    }
    public static function fchown($fd, $uid, $gid)
    {
        return self::$__module->fchown($fd, $uid, $gid);
    }
    public static function fdatasync($fd)
    {
        return self::$__module->fdatasync($fd);
    }
    public static function fdopen($fd, $mode="r", $buffering=-1, $encoding=null)
    {
        return self::$__module->fdopen($fd, $mode, $buffering, $encoding);
    }
    public static function fork()
    {
        return self::$__module->fork();
    }
    public static function forkpty()
    {
        return self::$__module->forkpty();
    }
    public static function fpathconf($fd, $name)
    {
        return self::$__module->fpathconf($fd, $name);
    }
    public static function fsdecode($filename)
    {
        return self::$__module->fsdecode($filename);
    }
    public static function fsencode($filename)
    {
        return self::$__module->fsencode($filename);
    }
    public static function fspath($path)
    {
        return self::$__module->fspath($path);
    }
    public static function fstat($fd)
    {
        return self::$__module->fstat($fd);
    }
    public static function fstatvfs($fd)
    {
        return self::$__module->fstatvfs($fd);
    }
    public static function fsync($fd)
    {
        return self::$__module->fsync($fd);
    }
    public static function ftruncate($fd, $length)
    {
        return self::$__module->ftruncate($fd, $length);
    }
    public static function fwalk($top=".", $topdown=true, $onerror=null)
    {
        return self::$__module->fwalk($top, $topdown, $onerror);
    }
    public static function get_blocking($fd)
    {
        return self::$__module->get_blocking($fd);
    }
    public static function get_exec_path($env=null)
    {
        return self::$__module->get_exec_path($env);
    }
    public static function get_inheritable($fd)
    {
        return self::$__module->get_inheritable($fd);
    }
    public static function getcwd()
    {
        return self::$__module->getcwd();
    }
    public static function getcwdb()
    {
        return self::$__module->getcwdb();
    }
    public static function getegid()
    {
        return self::$__module->getegid();
    }
    public static function getenv($key, $default=null)
    {
        return self::$__module->getenv($key, $default);
    }
    public static function getenvb($key, $default=null)
    {
        return self::$__module->getenvb($key, $default);
    }
    public static function geteuid()
    {
        return self::$__module->geteuid();
    }
    public static function getgid()
    {
        return self::$__module->getgid();
    }
    public static function getgrouplist($user, $group)
    {
        return self::$__module->getgrouplist($user, $group);
    }
    public static function getgroups()
    {
        return self::$__module->getgroups();
    }
    public static function getloadavg()
    {
        return self::$__module->getloadavg();
    }
    public static function getlogin()
    {
        return self::$__module->getlogin();
    }
    public static function getpgid($pid)
    {
        return self::$__module->getpgid($pid);
    }
    public static function getpgrp()
    {
        return self::$__module->getpgrp();
    }
    public static function getpid()
    {
        return self::$__module->getpid();
    }
    public static function getppid()
    {
        return self::$__module->getppid();
    }
    public static function getpriority($which, $who)
    {
        return self::$__module->getpriority($which, $who);
    }
    public static function getrandom($size, $flags=0)
    {
        return self::$__module->getrandom($size, $flags);
    }
    public static function getresgid()
    {
        return self::$__module->getresgid();
    }
    public static function getresuid()
    {
        return self::$__module->getresuid();
    }
    public static function getsid($pid)
    {
        return self::$__module->getsid($pid);
    }
    public static function getuid()
    {
        return self::$__module->getuid();
    }
    public static function getxattr($path, $attribute)
    {
        return self::$__module->getxattr($path, $attribute);
    }
    public static function initgroups($username, $gid)
    {
        return self::$__module->initgroups($username, $gid);
    }
    public static function isatty($fd)
    {
        return self::$__module->isatty($fd);
    }
    public static function kill($pid, $signal)
    {
        return self::$__module->kill($pid, $signal);
    }
    public static function killpg($pgid, $signal)
    {
        return self::$__module->killpg($pgid, $signal);
    }
    public static function lchown($path, $uid, $gid)
    {
        return self::$__module->lchown($path, $uid, $gid);
    }
    public static function link($src, $dst)
    {
        return self::$__module->link($src, $dst);
    }
    public static function listdir($path=null)
    {
        return self::$__module->listdir($path);
    }
    public static function listxattr($path=null)
    {
        return self::$__module->listxattr($path);
    }
    public static function lockf($fd, $command, $length)
    {
        return self::$__module->lockf($fd, $command, $length);
    }
    public static function login_tty($fd)
    {
        return self::$__module->login_tty($fd);
    }
    public static function lseek($fd, $position, $whence)
    {
        return self::$__module->lseek($fd, $position, $whence);
    }
    public static function lstat($path)
    {
        return self::$__module->lstat($path);
    }
    public static function major($device)
    {
        return self::$__module->major($device);
    }
    public static function makedev($major, $minor)
    {
        return self::$__module->makedev($major, $minor);
    }
    public static function makedirs($name, $mode=511, $exist_ok=false)
    {
        return self::$__module->makedirs($name, $mode, $exist_ok);
    }
    public static function minor($device)
    {
        return self::$__module->minor($device);
    }
    public static function mkdir($path, $mode=511)
    {
        return self::$__module->mkdir($path, $mode);
    }
    public static function mkfifo($path, $mode=438)
    {
        return self::$__module->mkfifo($path, $mode);
    }
    public static function mknod($path, $mode=384, $device=0)
    {
        return self::$__module->mknod($path, $mode, $device);
    }
    public static function nice($increment)
    {
        return self::$__module->nice($increment);
    }
    public static function open($path, $flags, $mode=511)
    {
        return self::$__module->open($path, $flags, $mode);
    }
    public static function openpty()
    {
        return self::$__module->openpty();
    }
    public static function pathconf($path, $name)
    {
        return self::$__module->pathconf($path, $name);
    }
    public static function pipe()
    {
        return self::$__module->pipe();
    }
    public static function pipe2($flags)
    {
        return self::$__module->pipe2($flags);
    }
    public static function popen($cmd, $mode="r", $buffering=-1)
    {
        return self::$__module->popen($cmd, $mode, $buffering);
    }
    public static function posix_fadvise($fd, $offset, $length, $advice)
    {
        return self::$__module->posix_fadvise($fd, $offset, $length, $advice);
    }
    public static function posix_fallocate($fd, $offset, $length)
    {
        return self::$__module->posix_fallocate($fd, $offset, $length);
    }
    public static function pread($fd, $length, $offset)
    {
        return self::$__module->pread($fd, $length, $offset);
    }
    public static function preadv($fd, $buffers, $offset, $flags=0)
    {
        return self::$__module->preadv($fd, $buffers, $offset, $flags);
    }
    public static function putenv($name, $value)
    {
        return self::$__module->putenv($name, $value);
    }
    public static function pwrite($fd, $buffer, $offset)
    {
        return self::$__module->pwrite($fd, $buffer, $offset);
    }
    public static function pwritev($fd, $buffers, $offset, $flags=0)
    {
        return self::$__module->pwritev($fd, $buffers, $offset, $flags);
    }
    public static function read($fd, $length)
    {
        return self::$__module->read($fd, $length);
    }
    public static function readlink($path)
    {
        return self::$__module->readlink($path);
    }
    public static function readv($fd, $buffers)
    {
        return self::$__module->readv($fd, $buffers);
    }
    public static function remove($path)
    {
        return self::$__module->remove($path);
    }
    public static function removedirs($name)
    {
        return self::$__module->removedirs($name);
    }
    public static function removexattr($path, $attribute)
    {
        return self::$__module->removexattr($path, $attribute);
    }
    public static function rename($src, $dst)
    {
        return self::$__module->rename($src, $dst);
    }
    public static function renames($old, $new)
    {
        return self::$__module->renames($old, $new);
    }
    public static function replace($src, $dst)
    {
        return self::$__module->replace($src, $dst);
    }
    public static function rmdir($path)
    {
        return self::$__module->rmdir($path);
    }
    public static function scandir($path=null)
    {
        return self::$__module->scandir($path);
    }
    public static function sched_get_priority_max($policy)
    {
        return self::$__module->sched_get_priority_max($policy);
    }
    public static function sched_get_priority_min($policy)
    {
        return self::$__module->sched_get_priority_min($policy);
    }
    public static function sched_getaffinity($pid)
    {
        return self::$__module->sched_getaffinity($pid);
    }
    public static function sched_getparam($pid)
    {
        return self::$__module->sched_getparam($pid);
    }
    public static function sched_getscheduler($pid)
    {
        return self::$__module->sched_getscheduler($pid);
    }
    public static function sched_rr_get_interval($pid)
    {
        return self::$__module->sched_rr_get_interval($pid);
    }
    public static function sched_setaffinity($pid, $mask)
    {
        return self::$__module->sched_setaffinity($pid, $mask);
    }
    public static function sched_setparam($pid, $param)
    {
        return self::$__module->sched_setparam($pid, $param);
    }
    public static function sched_setscheduler($pid, $policy, $param)
    {
        return self::$__module->sched_setscheduler($pid, $policy, $param);
    }
    public static function sched_yield()
    {
        return self::$__module->sched_yield();
    }
    public static function sendfile($out_fd, $in_fd, $offset, $count)
    {
        return self::$__module->sendfile($out_fd, $in_fd, $offset, $count);
    }
    public static function set_blocking($fd, $blocking)
    {
        return self::$__module->set_blocking($fd, $blocking);
    }
    public static function set_inheritable($fd, $inheritable)
    {
        return self::$__module->set_inheritable($fd, $inheritable);
    }
    public static function setegid($egid)
    {
        return self::$__module->setegid($egid);
    }
    public static function seteuid($euid)
    {
        return self::$__module->seteuid($euid);
    }
    public static function setgid($gid)
    {
        return self::$__module->setgid($gid);
    }
    public static function setgroups($groups)
    {
        return self::$__module->setgroups($groups);
    }
    public static function setpgid($pid, $pgrp)
    {
        return self::$__module->setpgid($pid, $pgrp);
    }
    public static function setpgrp()
    {
        return self::$__module->setpgrp();
    }
    public static function setpriority($which, $who, $priority)
    {
        return self::$__module->setpriority($which, $who, $priority);
    }
    public static function setregid($rgid, $egid)
    {
        return self::$__module->setregid($rgid, $egid);
    }
    public static function setresgid($rgid, $egid, $sgid)
    {
        return self::$__module->setresgid($rgid, $egid, $sgid);
    }
    public static function setresuid($ruid, $euid, $suid)
    {
        return self::$__module->setresuid($ruid, $euid, $suid);
    }
    public static function setreuid($ruid, $euid)
    {
        return self::$__module->setreuid($ruid, $euid);
    }
    public static function setsid()
    {
        return self::$__module->setsid();
    }
    public static function setuid($uid)
    {
        return self::$__module->setuid($uid);
    }
    public static function setxattr($path, $attribute, $value, $flags=0)
    {
        return self::$__module->setxattr($path, $attribute, $value, $flags);
    }
    public static function spawnl($mode, $file)
    {
        return self::$__module->spawnl($mode, $file);
    }
    public static function spawnle($mode, $file)
    {
        return self::$__module->spawnle($mode, $file);
    }
    public static function spawnlp($mode, $file)
    {
        return self::$__module->spawnlp($mode, $file);
    }
    public static function spawnlpe($mode, $file)
    {
        return self::$__module->spawnlpe($mode, $file);
    }
    public static function spawnv($mode, $file, $args)
    {
        return self::$__module->spawnv($mode, $file, $args);
    }
    public static function spawnve($mode, $file, $args, $env)
    {
        return self::$__module->spawnve($mode, $file, $args, $env);
    }
    public static function spawnvp($mode, $file, $args)
    {
        return self::$__module->spawnvp($mode, $file, $args);
    }
    public static function spawnvpe($mode, $file, $args, $env)
    {
        return self::$__module->spawnvpe($mode, $file, $args, $env);
    }
    public static function splice($src, $dst, $count, $offset_src=null, $offset_dst=null, $flags=0)
    {
        return self::$__module->splice($src, $dst, $count, $offset_src, $offset_dst, $flags);
    }
    public static function stat($path)
    {
        return self::$__module->stat($path);
    }
    public static function statvfs($path)
    {
        return self::$__module->statvfs($path);
    }
    public static function strerror($code)
    {
        return self::$__module->strerror($code);
    }
    public static function symlink($src, $dst, $target_is_directory=false)
    {
        return self::$__module->symlink($src, $dst, $target_is_directory);
    }
    public static function sync()
    {
        return self::$__module->sync();
    }
    public static function sysconf($name)
    {
        return self::$__module->sysconf($name);
    }
    public static function system($command)
    {
        return self::$__module->system($command);
    }
    public static function tcgetpgrp($fd)
    {
        return self::$__module->tcgetpgrp($fd);
    }
    public static function tcsetpgrp($fd, $pgid)
    {
        return self::$__module->tcsetpgrp($fd, $pgid);
    }
    public static function times()
    {
        return self::$__module->times();
    }
    public static function truncate($path, $length)
    {
        return self::$__module->truncate($path, $length);
    }
    public static function ttyname($fd)
    {
        return self::$__module->ttyname($fd);
    }
    public static function umask($mask)
    {
        return self::$__module->umask($mask);
    }
    public static function uname()
    {
        return self::$__module->uname();
    }
    public static function unlink($path)
    {
        return self::$__module->unlink($path);
    }
    public static function unsetenv($name)
    {
        return self::$__module->unsetenv($name);
    }
    public static function urandom($size)
    {
        return self::$__module->urandom($size);
    }
    public static function wait()
    {
        return self::$__module->wait();
    }
    public static function wait3($options)
    {
        return self::$__module->wait3($options);
    }
    public static function wait4($pid, $options)
    {
        return self::$__module->wait4($pid, $options);
    }
    public static function waitid($idtype, $id, $options)
    {
        return self::$__module->waitid($idtype, $id, $options);
    }
    public static function waitpid($pid, $options)
    {
        return self::$__module->waitpid($pid, $options);
    }
    public static function waitstatus_to_exitcode($status)
    {
        return self::$__module->waitstatus_to_exitcode($status);
    }
    public static function walk($top, $topdown=true, $onerror=null, $followlinks=false)
    {
        return self::$__module->walk($top, $topdown, $onerror, $followlinks);
    }
    public static function write($fd, $data)
    {
        return self::$__module->write($fd, $data);
    }
    public static function writev($fd, $buffers)
    {
        return self::$__module->writev($fd, $buffers);
    }
}

os::__init();
