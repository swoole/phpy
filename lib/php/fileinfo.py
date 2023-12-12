import phpy

NONE = 0
SYMLINK = 2
MIME = 1040
MIME_TYPE = 16
MIME_ENCODING = 1024
DEVICES = 8
CONTINUE = 32
PRESERVE_ATIME = 128
RAW = 256
EXTENSION = 16777216


def finfo_open(_flags=0, _magic_database=None):
    return phpy.call('finfo_open', _flags, _magic_database)


def finfo_close(_finfo):
    return phpy.call('finfo_close', _finfo)


def finfo_set_flags(_finfo, _flags):
    return phpy.call('finfo_set_flags', _finfo, _flags)


def finfo_file(_finfo, _filename, _flags=0, _context=None):
    return phpy.call('finfo_file', _finfo, _filename, _flags, _context)


def finfo_buffer(_finfo, _string, _flags=0, _context=None):
    return phpy.call('finfo_buffer', _finfo, _string, _flags, _context)


def mime_content_type(_filename):
    return phpy.call('mime_content_type', _filename)




def finfo():

    def __init__(self, _flags=0, _magic_database=None):
        self.__this = phpy.Object(f'finfo', _flags, _magic_database)

    def file(self, _filename, _flags=0, _context=None):
        return self.__this.call(f"file", _filename, _flags, _context)

    def buffer(self, _string, _flags=0, _context=None):
        return self.__this.call(f"buffer", _string, _flags, _context)

    def set_flags(self, _flags):
        return self.__this.call(f"set_flags", _flags)


