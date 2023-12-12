import phpy

AF_UNIX = 1
AF_INET = 2
AF_INET6 = 10
SOCK_STREAM = 1
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_SEQPACKET = 5
SOCK_RDM = 4
MSG_OOB = 1
MSG_WAITALL = 256
MSG_CTRUNC = 8
MSG_TRUNC = 32
MSG_PEEK = 2
MSG_DONTROUTE = 4
MSG_EOR = 128
MSG_EOF = 512
MSG_CONFIRM = 2048
MSG_ERRQUEUE = 8192
MSG_NOSIGNAL = 16384
MSG_DONTWAIT = 64
MSG_MORE = 32768
MSG_WAITFORONE = 65536
MSG_CMSG_CLOEXEC = 1073741824
SO_DEBUG = 1
SO_REUSEADDR = 2
SO_REUSEPORT = 15
SO_KEEPALIVE = 9
SO_DONTROUTE = 5
SO_LINGER = 13
SO_BROADCAST = 6
SO_OOBINLINE = 10
SO_SNDBUF = 7
SO_RCVBUF = 8
SO_SNDLOWAT = 19
SO_RCVLOWAT = 18
SO_SNDTIMEO = 21
SO_RCVTIMEO = 20
SO_TYPE = 3
SO_ERROR = 4
SO_BINDTODEVICE = 25
SOL_SOCKET = 1
SOMAXCONN = 128
SO_MARK = 36
TCP_NODELAY = 1
TCP_DEFER_ACCEPT = 9
PHP_NORMAL_READ = 1
PHP_BINARY_READ = 2
MCAST_JOIN_GROUP = 42
MCAST_LEAVE_GROUP = 45
MCAST_BLOCK_SOURCE = 43
MCAST_UNBLOCK_SOURCE = 44
MCAST_JOIN_SOURCE_GROUP = 46
MCAST_LEAVE_SOURCE_GROUP = 47
IP_MULTICAST_IF = 32
IP_MULTICAST_TTL = 33
IP_MULTICAST_LOOP = 34
IPV6_MULTICAST_IF = 17
IPV6_MULTICAST_HOPS = 18
IPV6_MULTICAST_LOOP = 19
IPV6_V6ONLY = 26
SOCKET_EPERM = 1
SOCKET_ENOENT = 2
SOCKET_EINTR = 4
SOCKET_EIO = 5
SOCKET_ENXIO = 6
SOCKET_E2BIG = 7
SOCKET_EBADF = 9
SOCKET_EAGAIN = 11
SOCKET_ENOMEM = 12
SOCKET_EACCES = 13
SOCKET_EFAULT = 14
SOCKET_ENOTBLK = 15
SOCKET_EBUSY = 16
SOCKET_EEXIST = 17
SOCKET_EXDEV = 18
SOCKET_ENODEV = 19
SOCKET_ENOTDIR = 20
SOCKET_EISDIR = 21
SOCKET_EINVAL = 22
SOCKET_ENFILE = 23
SOCKET_EMFILE = 24
SOCKET_ENOTTY = 25
SOCKET_ENOSPC = 28
SOCKET_ESPIPE = 29
SOCKET_EROFS = 30
SOCKET_EMLINK = 31
SOCKET_EPIPE = 32
SOCKET_ENAMETOOLONG = 36
SOCKET_ENOLCK = 37
SOCKET_ENOSYS = 38
SOCKET_ENOTEMPTY = 39
SOCKET_ELOOP = 40
SOCKET_EWOULDBLOCK = 11
SOCKET_ENOMSG = 42
SOCKET_EIDRM = 43
SOCKET_ECHRNG = 44
SOCKET_EL2NSYNC = 45
SOCKET_EL3HLT = 46
SOCKET_EL3RST = 47
SOCKET_ELNRNG = 48
SOCKET_EUNATCH = 49
SOCKET_ENOCSI = 50
SOCKET_EL2HLT = 51
SOCKET_EBADE = 52
SOCKET_EBADR = 53
SOCKET_EXFULL = 54
SOCKET_ENOANO = 55
SOCKET_EBADRQC = 56
SOCKET_EBADSLT = 57
SOCKET_ENOSTR = 60
SOCKET_ENODATA = 61
SOCKET_ETIME = 62
SOCKET_ENOSR = 63
SOCKET_ENONET = 64
SOCKET_EREMOTE = 66
SOCKET_ENOLINK = 67
SOCKET_EADV = 68
SOCKET_ESRMNT = 69
SOCKET_ECOMM = 70
SOCKET_EPROTO = 71
SOCKET_EMULTIHOP = 72
SOCKET_EBADMSG = 74
SOCKET_ENOTUNIQ = 76
SOCKET_EBADFD = 77
SOCKET_EREMCHG = 78
SOCKET_ERESTART = 85
SOCKET_ESTRPIPE = 86
SOCKET_EUSERS = 87
SOCKET_ENOTSOCK = 88
SOCKET_EDESTADDRREQ = 89
SOCKET_EMSGSIZE = 90
SOCKET_EPROTOTYPE = 91
SOCKET_ENOPROTOOPT = 92
SOCKET_EPROTONOSUPPORT = 93
SOCKET_ESOCKTNOSUPPORT = 94
SOCKET_EOPNOTSUPP = 95
SOCKET_EPFNOSUPPORT = 96
SOCKET_EAFNOSUPPORT = 97
SOCKET_EADDRINUSE = 98
SOCKET_EADDRNOTAVAIL = 99
SOCKET_ENETDOWN = 100
SOCKET_ENETUNREACH = 101
SOCKET_ENETRESET = 102
SOCKET_ECONNABORTED = 103
SOCKET_ECONNRESET = 104
SOCKET_ENOBUFS = 105
SOCKET_EISCONN = 106
SOCKET_ENOTCONN = 107
SOCKET_ESHUTDOWN = 108
SOCKET_ETOOMANYREFS = 109
SOCKET_ETIMEDOUT = 110
SOCKET_ECONNREFUSED = 111
SOCKET_EHOSTDOWN = 112
SOCKET_EHOSTUNREACH = 113
SOCKET_EALREADY = 114
SOCKET_EINPROGRESS = 115
SOCKET_EISNAM = 120
SOCKET_EREMOTEIO = 121
SOCKET_EDQUOT = 122
SOCKET_ENOMEDIUM = 123
SOCKET_EMEDIUMTYPE = 124
IPPROTO_IP = 0
IPPROTO_IPV6 = 41
SOL_TCP = 6
SOL_UDP = 17
IPV6_UNICAST_HOPS = 16
AI_PASSIVE = 1
AI_CANONNAME = 2
AI_NUMERICHOST = 4
AI_V4MAPPED = 8
AI_ALL = 16
AI_ADDRCONFIG = 32
AI_NUMERICSERV = 1024
IPV6_RECVPKTINFO = 49
IPV6_PKTINFO = 50
IPV6_RECVHOPLIMIT = 51
IPV6_HOPLIMIT = 52
IPV6_RECVTCLASS = 66
IPV6_TCLASS = 67
SCM_RIGHTS = 1
SCM_CREDENTIALS = 2
SO_PASSCRED = 16


def socket_select(_read, _write, _except, _seconds, _microseconds=0):
    return phpy.call('socket_select', _read, _write, _except, _seconds, _microseconds)


def socket_create_listen(_port, _backlog=128):
    return phpy.call('socket_create_listen', _port, _backlog)


def socket_accept(_socket):
    return phpy.call('socket_accept', _socket)


def socket_set_nonblock(_socket):
    return phpy.call('socket_set_nonblock', _socket)


def socket_set_block(_socket):
    return phpy.call('socket_set_block', _socket)


def socket_listen(_socket, _backlog=0):
    return phpy.call('socket_listen', _socket, _backlog)


def socket_close(_socket):
    return phpy.call('socket_close', _socket)


def socket_write(_socket, _data, _length=None):
    return phpy.call('socket_write', _socket, _data, _length)


def socket_read(_socket, _length, _mode=2):
    return phpy.call('socket_read', _socket, _length, _mode)


def socket_getsockname(_socket, _address, _port=None):
    return phpy.call('socket_getsockname', _socket, _address, _port)


def socket_getpeername(_socket, _address, _port=None):
    return phpy.call('socket_getpeername', _socket, _address, _port)


def socket_create(_domain, _type, _protocol):
    return phpy.call('socket_create', _domain, _type, _protocol)


def socket_connect(_socket, _address, _port=None):
    return phpy.call('socket_connect', _socket, _address, _port)


def socket_strerror(_error_code):
    return phpy.call('socket_strerror', _error_code)


def socket_bind(_socket, _address, _port=0):
    return phpy.call('socket_bind', _socket, _address, _port)


def socket_recv(_socket, _data, _length, _flags):
    return phpy.call('socket_recv', _socket, _data, _length, _flags)


def socket_send(_socket, _data, _length, _flags):
    return phpy.call('socket_send', _socket, _data, _length, _flags)


def socket_recvfrom(_socket, _data, _length, _flags, _address, _port=None):
    return phpy.call('socket_recvfrom', _socket, _data, _length, _flags, _address, _port)


def socket_sendto(_socket, _data, _length, _flags, _address, _port=None):
    return phpy.call('socket_sendto', _socket, _data, _length, _flags, _address, _port)


def socket_get_option(_socket, _level, _option):
    return phpy.call('socket_get_option', _socket, _level, _option)


def socket_getopt(_socket, _level, _option):
    return phpy.call('socket_getopt', _socket, _level, _option)


def socket_set_option(_socket, _level, _option, _value):
    return phpy.call('socket_set_option', _socket, _level, _option, _value)


def socket_setopt(_socket, _level, _option, _value):
    return phpy.call('socket_setopt', _socket, _level, _option, _value)


def socket_create_pair(_domain, _type, _protocol, _pair):
    return phpy.call('socket_create_pair', _domain, _type, _protocol, _pair)


def socket_shutdown(_socket, _mode=2):
    return phpy.call('socket_shutdown', _socket, _mode)


def socket_last_error(_socket=None):
    return phpy.call('socket_last_error', _socket)


def socket_clear_error(_socket=None):
    return phpy.call('socket_clear_error', _socket)


def socket_import_stream(_stream):
    return phpy.call('socket_import_stream', _stream)


def socket_export_stream(_socket):
    return phpy.call('socket_export_stream', _socket)


def socket_sendmsg(_socket, _message, _flags=0):
    return phpy.call('socket_sendmsg', _socket, _message, _flags)


def socket_recvmsg(_socket, _message, _flags=0):
    return phpy.call('socket_recvmsg', _socket, _message, _flags)


def socket_cmsg_space(_level, _type, _num=0):
    return phpy.call('socket_cmsg_space', _level, _type, _num)


def socket_addrinfo_lookup(_host, _service=None, _hints=[]):
    return phpy.call('socket_addrinfo_lookup', _host, _service, _hints)


def socket_addrinfo_connect(_address):
    return phpy.call('socket_addrinfo_connect', _address)


def socket_addrinfo_bind(_address):
    return phpy.call('socket_addrinfo_bind', _address)


def socket_addrinfo_explain(_address):
    return phpy.call('socket_addrinfo_explain', _address)




class Socket():

    def __init__(self):
        self.__this = phpy.Object(f'Socket')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class AddressInfo():

    def __init__(self):
        self.__this = phpy.Object(f'AddressInfo')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

