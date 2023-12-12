import phpy



def bzopen(_file, _mode):
    return phpy.call('bzopen', _file, _mode)


def bzread(_bz, _length=1024):
    return phpy.call('bzread', _bz, _length)


def bzwrite(_bz, _data, _length=None):
    return phpy.call('bzwrite', _bz, _data, _length)


def bzflush(_bz):
    return phpy.call('bzflush', _bz)


def bzclose(_bz):
    return phpy.call('bzclose', _bz)


def bzerrno(_bz):
    return phpy.call('bzerrno', _bz)


def bzerrstr(_bz):
    return phpy.call('bzerrstr', _bz)


def bzerror(_bz):
    return phpy.call('bzerror', _bz)


def bzcompress(_data, _block_size=4, _work_factor=0):
    return phpy.call('bzcompress', _data, _block_size, _work_factor)


def bzdecompress(_data, _use_less_memory=False):
    return phpy.call('bzdecompress', _data, _use_less_memory)




