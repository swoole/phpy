import phpy

FORCE_GZIP = 31
FORCE_DEFLATE = 15
ENCODING_RAW = -15
ENCODING_GZIP = 31
ENCODING_DEFLATE = 15
NO_FLUSH = 0
PARTIAL_FLUSH = 1
SYNC_FLUSH = 2
FULL_FLUSH = 3
BLOCK = 5
FINISH = 4
FILTERED = 1
HUFFMAN_ONLY = 2
RLE = 3
FIXED = 4
DEFAULT_STRATEGY = 0
VERSION = "1.2.11"
VERNUM = 4784
OK = 0
STREAM_END = 1
NEED_DICT = 2
ERRNO = -1
STREAM_ERROR = -2
DATA_ERROR = -3
MEM_ERROR = -4
BUF_ERROR = -5
VERSION_ERROR = -6


def ob_gzhandler(_data, _flags):
    return phpy.call('ob_gzhandler', _data, _flags)


def get_coding_type():
    return phpy.call('zlib_get_coding_type', )


def gzfile(_filename, _use_include_path=0):
    return phpy.call('gzfile', _filename, _use_include_path)


def gzopen(_filename, _mode, _use_include_path=0):
    return phpy.call('gzopen', _filename, _mode, _use_include_path)


def readgzfile(_filename, _use_include_path=0):
    return phpy.call('readgzfile', _filename, _use_include_path)


def encode(_data, _encoding, _level=-1):
    return phpy.call('zlib_encode', _data, _encoding, _level)


def decode(_data, _max_length=0):
    return phpy.call('zlib_decode', _data, _max_length)


def gzdeflate(_data, _level=-1, _encoding=-15):
    return phpy.call('gzdeflate', _data, _level, _encoding)


def gzencode(_data, _level=-1, _encoding=31):
    return phpy.call('gzencode', _data, _level, _encoding)


def gzcompress(_data, _level=-1, _encoding=15):
    return phpy.call('gzcompress', _data, _level, _encoding)


def gzinflate(_data, _max_length=0):
    return phpy.call('gzinflate', _data, _max_length)


def gzdecode(_data, _max_length=0):
    return phpy.call('gzdecode', _data, _max_length)


def gzuncompress(_data, _max_length=0):
    return phpy.call('gzuncompress', _data, _max_length)


def gzwrite(_stream, _data, _length=None):
    return phpy.call('gzwrite', _stream, _data, _length)


def gzputs(_stream, _data, _length=None):
    return phpy.call('gzputs', _stream, _data, _length)


def gzrewind(_stream):
    return phpy.call('gzrewind', _stream)


def gzclose(_stream):
    return phpy.call('gzclose', _stream)


def gzeof(_stream):
    return phpy.call('gzeof', _stream)


def gzgetc(_stream):
    return phpy.call('gzgetc', _stream)


def gzpassthru(_stream):
    return phpy.call('gzpassthru', _stream)


def gzseek(_stream, _offset, _whence=0):
    return phpy.call('gzseek', _stream, _offset, _whence)


def gztell(_stream):
    return phpy.call('gztell', _stream)


def gzread(_stream, _length):
    return phpy.call('gzread', _stream, _length)


def gzgets(_stream, _length=None):
    return phpy.call('gzgets', _stream, _length)


def deflate_init(_encoding, _options=[]):
    return phpy.call('deflate_init', _encoding, _options)


def deflate_add(_context, _data, _flush_mode=2):
    return phpy.call('deflate_add', _context, _data, _flush_mode)


def inflate_init(_encoding, _options=[]):
    return phpy.call('inflate_init', _encoding, _options)


def inflate_add(_context, _data, _flush_mode=2):
    return phpy.call('inflate_add', _context, _data, _flush_mode)


def inflate_get_status(_context):
    return phpy.call('inflate_get_status', _context)


def inflate_get_read_len(_context):
    return phpy.call('inflate_get_read_len', _context)




class InflateContext():

    def __init__(self):
        self.__this = phpy.Object(f'InflateContext')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class DeflateContext():

    def __init__(self):
        self.__this = phpy.Object(f'DeflateContext')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

