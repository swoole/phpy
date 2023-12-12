import phpy



def open(_filename):
    return phpy.call('zip_open', _filename)


def close(_zip):
    return phpy.call('zip_close', _zip)


def read(_zip):
    return phpy.call('zip_read', _zip)


def entry_open(_zip_dp, _zip_entry, _mode="rb"):
    return phpy.call('zip_entry_open', _zip_dp, _zip_entry, _mode)


def entry_close(_zip_entry):
    return phpy.call('zip_entry_close', _zip_entry)


def entry_read(_zip_entry, _len=1024):
    return phpy.call('zip_entry_read', _zip_entry, _len)


def entry_name(_zip_entry):
    return phpy.call('zip_entry_name', _zip_entry)


def entry_compressedsize(_zip_entry):
    return phpy.call('zip_entry_compressedsize', _zip_entry)


def entry_filesize(_zip_entry):
    return phpy.call('zip_entry_filesize', _zip_entry)


def entry_compressionmethod(_zip_entry):
    return phpy.call('zip_entry_compressionmethod', _zip_entry)




class ZipArchive():
    CREATE = 1
    EXCL = 2
    CHECKCONS = 4
    OVERWRITE = 8
    RDONLY = 16
    FL_NOCASE = 1
    FL_NODIR = 2
    FL_COMPRESSED = 4
    FL_UNCHANGED = 8
    FL_RECOMPRESS = 16
    FL_ENCRYPTED = 32
    FL_OVERWRITE = 8192
    FL_LOCAL = 256
    FL_CENTRAL = 512
    FL_ENC_GUESS = 0
    FL_ENC_RAW = 64
    FL_ENC_STRICT = 128
    FL_ENC_UTF_8 = 2048
    FL_ENC_CP437 = 4096
    CM_DEFAULT = -1
    CM_STORE = 0
    CM_SHRINK = 1
    CM_REDUCE_1 = 2
    CM_REDUCE_2 = 3
    CM_REDUCE_3 = 4
    CM_REDUCE_4 = 5
    CM_IMPLODE = 6
    CM_DEFLATE = 8
    CM_DEFLATE64 = 9
    CM_PKWARE_IMPLODE = 10
    CM_BZIP2 = 12
    CM_LZMA = 14
    CM_LZMA2 = 33
    CM_ZSTD = 93
    CM_XZ = 95
    CM_TERSE = 18
    CM_LZ77 = 19
    CM_WAVPACK = 97
    CM_PPMD = 98
    ER_OK = 0
    ER_MULTIDISK = 1
    ER_RENAME = 2
    ER_CLOSE = 3
    ER_SEEK = 4
    ER_READ = 5
    ER_WRITE = 6
    ER_CRC = 7
    ER_ZIPCLOSED = 8
    ER_NOENT = 9
    ER_EXISTS = 10
    ER_OPEN = 11
    ER_TMPOPEN = 12
    ER_ZLIB = 13
    ER_MEMORY = 14
    ER_CHANGED = 15
    ER_COMPNOTSUPP = 16
    ER_EOF = 17
    ER_INVAL = 18
    ER_NOZIP = 19
    ER_INTERNAL = 20
    ER_INCONS = 21
    ER_REMOVE = 22
    ER_DELETED = 23
    ER_ENCRNOTSUPP = 24
    ER_RDONLY = 25
    ER_NOPASSWD = 26
    ER_WRONGPASSWD = 27
    ER_OPNOTSUPP = 28
    ER_INUSE = 29
    ER_TELL = 30
    ER_COMPRESSED_DATA = 31
    ER_CANCELLED = 32
    OPSYS_DOS = 0
    OPSYS_AMIGA = 1
    OPSYS_OPENVMS = 2
    OPSYS_UNIX = 3
    OPSYS_VM_CMS = 4
    OPSYS_ATARI_ST = 5
    OPSYS_OS_2 = 6
    OPSYS_MACINTOSH = 7
    OPSYS_Z_SYSTEM = 8
    OPSYS_CPM = 9
    OPSYS_WINDOWS_NTFS = 10
    OPSYS_MVS = 11
    OPSYS_VSE = 12
    OPSYS_ACORN_RISC = 13
    OPSYS_VFAT = 14
    OPSYS_ALTERNATE_MVS = 15
    OPSYS_BEOS = 16
    OPSYS_TANDEM = 17
    OPSYS_OS_400 = 18
    OPSYS_OS_X = 19
    OPSYS_DEFAULT = 3
    EM_NONE = 0
    EM_TRAD_PKWARE = 1
    EM_AES_128 = 257
    EM_AES_192 = 258
    EM_AES_256 = 259
    EM_UNKNOWN = 65535
    LIBZIP_VERSION = "1.9.2"

    def open(self, _filename, _flags=0):
        return self.__this.call(f"open", _filename, _flags)

    def setPassword(self, _password):
        return self.__this.call(f"setPassword", _password)

    def close(self):
        return self.__this.call(f"close", )

    def count(self):
        return self.__this.call(f"count", )

    def getStatusString(self):
        return self.__this.call(f"getStatusString", )

    def addEmptyDir(self, _dirname, _flags=0):
        return self.__this.call(f"addEmptyDir", _dirname, _flags)

    def addFromString(self, _name, _content, _flags=8192):
        return self.__this.call(f"addFromString", _name, _content, _flags)

    def addFile(self, _filepath, _entryname="", _start=0, _length=0, _flags=8192):
        return self.__this.call(f"addFile", _filepath, _entryname, _start, _length, _flags)

    def replaceFile(self, _filepath, _index, _start=0, _length=0, _flags=0):
        return self.__this.call(f"replaceFile", _filepath, _index, _start, _length, _flags)

    def addGlob(self, _pattern, _flags=0, _options=[]):
        return self.__this.call(f"addGlob", _pattern, _flags, _options)

    def addPattern(self, _pattern, _path=".", _options=[]):
        return self.__this.call(f"addPattern", _pattern, _path, _options)

    def renameIndex(self, _index, _new_name):
        return self.__this.call(f"renameIndex", _index, _new_name)

    def renameName(self, _name, _new_name):
        return self.__this.call(f"renameName", _name, _new_name)

    def setArchiveComment(self, _comment):
        return self.__this.call(f"setArchiveComment", _comment)

    def getArchiveComment(self, _flags=0):
        return self.__this.call(f"getArchiveComment", _flags)

    def setCommentIndex(self, _index, _comment):
        return self.__this.call(f"setCommentIndex", _index, _comment)

    def setCommentName(self, _name, _comment):
        return self.__this.call(f"setCommentName", _name, _comment)

    def setMtimeIndex(self, _index, _timestamp, _flags=0):
        return self.__this.call(f"setMtimeIndex", _index, _timestamp, _flags)

    def setMtimeName(self, _name, _timestamp, _flags=0):
        return self.__this.call(f"setMtimeName", _name, _timestamp, _flags)

    def getCommentIndex(self, _index, _flags=0):
        return self.__this.call(f"getCommentIndex", _index, _flags)

    def getCommentName(self, _name, _flags=0):
        return self.__this.call(f"getCommentName", _name, _flags)

    def deleteIndex(self, _index):
        return self.__this.call(f"deleteIndex", _index)

    def deleteName(self, _name):
        return self.__this.call(f"deleteName", _name)

    def statName(self, _name, _flags=0):
        return self.__this.call(f"statName", _name, _flags)

    def statIndex(self, _index, _flags=0):
        return self.__this.call(f"statIndex", _index, _flags)

    def locateName(self, _name, _flags=0):
        return self.__this.call(f"locateName", _name, _flags)

    def getNameIndex(self, _index, _flags=0):
        return self.__this.call(f"getNameIndex", _index, _flags)

    def unchangeArchive(self):
        return self.__this.call(f"unchangeArchive", )

    def unchangeAll(self):
        return self.__this.call(f"unchangeAll", )

    def unchangeIndex(self, _index):
        return self.__this.call(f"unchangeIndex", _index)

    def unchangeName(self, _name):
        return self.__this.call(f"unchangeName", _name)

    def extractTo(self, _pathto, _files=None):
        return self.__this.call(f"extractTo", _pathto, _files)

    def getFromName(self, _name, _len=0, _flags=0):
        return self.__this.call(f"getFromName", _name, _len, _flags)

    def getFromIndex(self, _index, _len=0, _flags=0):
        return self.__this.call(f"getFromIndex", _index, _len, _flags)

    def getStream(self, _name):
        return self.__this.call(f"getStream", _name)

    def setExternalAttributesName(self, _name, _opsys, _attr, _flags=0):
        return self.__this.call(f"setExternalAttributesName", _name, _opsys, _attr, _flags)

    def setExternalAttributesIndex(self, _index, _opsys, _attr, _flags=0):
        return self.__this.call(f"setExternalAttributesIndex", _index, _opsys, _attr, _flags)

    def getExternalAttributesName(self, _name, _opsys, _attr, _flags=0):
        return self.__this.call(f"getExternalAttributesName", _name, _opsys, _attr, _flags)

    def getExternalAttributesIndex(self, _index, _opsys, _attr, _flags=0):
        return self.__this.call(f"getExternalAttributesIndex", _index, _opsys, _attr, _flags)

    def setCompressionName(self, _name, _method, _compflags=0):
        return self.__this.call(f"setCompressionName", _name, _method, _compflags)

    def setCompressionIndex(self, _index, _method, _compflags=0):
        return self.__this.call(f"setCompressionIndex", _index, _method, _compflags)

    def setEncryptionName(self, _name, _method, _password=None):
        return self.__this.call(f"setEncryptionName", _name, _method, _password)

    def setEncryptionIndex(self, _index, _method, _password=None):
        return self.__this.call(f"setEncryptionIndex", _index, _method, _password)

    def registerProgressCallback(self, _rate, _callback):
        return self.__this.call(f"registerProgressCallback", _rate, _callback)

    def registerCancelCallback(self, _callback):
        return self.__this.call(f"registerCancelCallback", _callback)

    def isCompressionMethodSupported(_method, _enc=True):
        return phpy.call(f"ZipArchive::isCompressionMethodSupported", _method, _enc)

    def isEncryptionMethodSupported(_method, _enc=True):
        return phpy.call(f"ZipArchive::isEncryptionMethodSupported", _method, _enc)

    def __init__(self):
        self.__this = phpy.Object(f'ZipArchive')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

