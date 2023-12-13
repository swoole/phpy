from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)

print(errno.get())
print(errstr.get())
print(rs)
