import phpy





class PharException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'PharException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Phar():
    CURRENT_MODE_MASK = 240
    CURRENT_AS_PATHNAME = 32
    CURRENT_AS_FILEINFO = 0
    CURRENT_AS_SELF = 16
    KEY_MODE_MASK = 3840
    KEY_AS_PATHNAME = 0
    FOLLOW_SYMLINKS = 16384
    KEY_AS_FILENAME = 256
    NEW_CURRENT_AND_KEY = 256
    OTHER_MODE_MASK = 28672
    SKIP_DOTS = 4096
    UNIX_PATHS = 8192
    BZ2 = 8192
    GZ = 4096
    NONE = 0
    PHAR = 1
    TAR = 2
    ZIP = 3
    COMPRESSED = 61440
    PHP = 0
    PHPS = 1
    MD5 = 1
    OPENSSL = 16
    OPENSSL_SHA256 = 17
    OPENSSL_SHA512 = 18
    SHA1 = 2
    SHA256 = 3
    SHA512 = 4

    def __init__(self, _filename, _flags=12288, _alias=None):
        self.__this = phpy.Object(f'Phar', _filename, _flags, _alias)

    def addEmptyDir(self, _directory):
        return self.__this.call(f"addEmptyDir", _directory)

    def addFile(self, _filename, _local_name=None):
        return self.__this.call(f"addFile", _filename, _local_name)

    def addFromString(self, _local_name, _contents):
        return self.__this.call(f"addFromString", _local_name, _contents)

    def buildFromDirectory(self, _directory, _pattern=""):
        return self.__this.call(f"buildFromDirectory", _directory, _pattern)

    def buildFromIterator(self, _iterator, _base_directory=None):
        return self.__this.call(f"buildFromIterator", _iterator, _base_directory)

    def compressFiles(self, _compression):
        return self.__this.call(f"compressFiles", _compression)

    def decompressFiles(self):
        return self.__this.call(f"decompressFiles", )

    def compress(self, _compression, _extension=None):
        return self.__this.call(f"compress", _compression, _extension)

    def decompress(self, _extension=None):
        return self.__this.call(f"decompress", _extension)

    def convertToExecutable(self, _format=None, _compression=None, _extension=None):
        return self.__this.call(f"convertToExecutable", _format, _compression, _extension)

    def convertToData(self, _format=None, _compression=None, _extension=None):
        return self.__this.call(f"convertToData", _format, _compression, _extension)

    def copy(self, _from, _to):
        return self.__this.call(f"copy", _from, _to)

    def count(self, _mode=0):
        return self.__this.call(f"count", _mode)

    def delete(self, _local_name):
        return self.__this.call(f"delete", _local_name)

    def delMetadata(self):
        return self.__this.call(f"delMetadata", )

    def extractTo(self, _directory, _files=None, _overwrite=False):
        return self.__this.call(f"extractTo", _directory, _files, _overwrite)

    def getAlias(self):
        return self.__this.call(f"getAlias", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getMetadata(self, _unserialize_options=[]):
        return self.__this.call(f"getMetadata", _unserialize_options)

    def getModified(self):
        return self.__this.call(f"getModified", )

    def getSignature(self):
        return self.__this.call(f"getSignature", )

    def getStub(self):
        return self.__this.call(f"getStub", )

    def getVersion(self):
        return self.__this.call(f"getVersion", )

    def hasMetadata(self):
        return self.__this.call(f"hasMetadata", )

    def isBuffering(self):
        return self.__this.call(f"isBuffering", )

    def isCompressed(self):
        return self.__this.call(f"isCompressed", )

    def isFileFormat(self, _format):
        return self.__this.call(f"isFileFormat", _format)

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def offsetExists(self, _local_name):
        return self.__this.call(f"offsetExists", _local_name)

    def offsetGet(self, _local_name):
        return self.__this.call(f"offsetGet", _local_name)

    def offsetSet(self, _local_name, _value):
        return self.__this.call(f"offsetSet", _local_name, _value)

    def offsetUnset(self, _local_name):
        return self.__this.call(f"offsetUnset", _local_name)

    def setAlias(self, _alias):
        return self.__this.call(f"setAlias", _alias)

    def setDefaultStub(self, _index=None, _web_index=None):
        return self.__this.call(f"setDefaultStub", _index, _web_index)

    def setMetadata(self, _metadata):
        return self.__this.call(f"setMetadata", _metadata)

    def setSignatureAlgorithm(self, _algo, _private_key=None):
        return self.__this.call(f"setSignatureAlgorithm", _algo, _private_key)

    def setStub(self, _stub, _length=None):
        return self.__this.call(f"setStub", _stub, _length)

    def startBuffering(self):
        return self.__this.call(f"startBuffering", )

    def stopBuffering(self):
        return self.__this.call(f"stopBuffering", )

    def apiVersion():
        return phpy.call(f"Phar::apiVersion", )

    def canCompress(_compression=0):
        return phpy.call(f"Phar::canCompress", _compression)

    def canWrite():
        return phpy.call(f"Phar::canWrite", )

    def createDefaultStub(_index=None, _web_index=None):
        return phpy.call(f"Phar::createDefaultStub", _index, _web_index)

    def getSupportedCompression():
        return phpy.call(f"Phar::getSupportedCompression", )

    def getSupportedSignatures():
        return phpy.call(f"Phar::getSupportedSignatures", )

    def interceptFileFuncs():
        return phpy.call(f"Phar::interceptFileFuncs", )

    def isValidPharFilename(_filename, _executable=True):
        return phpy.call(f"Phar::isValidPharFilename", _filename, _executable)

    def loadPhar(_filename, _alias=None):
        return phpy.call(f"Phar::loadPhar", _filename, _alias)

    def mapPhar(_alias=None, _offset=0):
        return phpy.call(f"Phar::mapPhar", _alias, _offset)

    def running(_return_phar=True):
        return phpy.call(f"Phar::running", _return_phar)

    def mount(_phar_path, _external_path):
        return phpy.call(f"Phar::mount", _phar_path, _external_path)

    def mungServer(_variables):
        return phpy.call(f"Phar::mungServer", _variables)

    def unlinkArchive(_filename):
        return phpy.call(f"Phar::unlinkArchive", _filename)

    def webPhar(_alias=None, _index=None, _file_not_found_script=None, _mime_types=[], _rewrite=None):
        return phpy.call(f"Phar::webPhar", _alias, _index, _file_not_found_script, _mime_types, _rewrite)

    def hasChildren(self, _allow_links=False):
        return self.__this.call(f"hasChildren", _allow_links)

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def getSubPath(self):
        return self.__this.call(f"getSubPath", )

    def getSubPathname(self):
        return self.__this.call(f"getSubPathname", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class PharData():
    CURRENT_MODE_MASK = 240
    CURRENT_AS_PATHNAME = 32
    CURRENT_AS_FILEINFO = 0
    CURRENT_AS_SELF = 16
    KEY_MODE_MASK = 3840
    KEY_AS_PATHNAME = 0
    FOLLOW_SYMLINKS = 16384
    KEY_AS_FILENAME = 256
    NEW_CURRENT_AND_KEY = 256
    OTHER_MODE_MASK = 28672
    SKIP_DOTS = 4096
    UNIX_PATHS = 8192

    def __init__(self, _filename, _flags=12288, _alias=None, _format=0):
        self.__this = phpy.Object(f'PharData', _filename, _flags, _alias, _format)

    def addEmptyDir(self, _directory):
        return self.__this.call(f"addEmptyDir", _directory)

    def addFile(self, _filename, _local_name=None):
        return self.__this.call(f"addFile", _filename, _local_name)

    def addFromString(self, _local_name, _contents):
        return self.__this.call(f"addFromString", _local_name, _contents)

    def buildFromDirectory(self, _directory, _pattern=""):
        return self.__this.call(f"buildFromDirectory", _directory, _pattern)

    def buildFromIterator(self, _iterator, _base_directory=None):
        return self.__this.call(f"buildFromIterator", _iterator, _base_directory)

    def compressFiles(self, _compression):
        return self.__this.call(f"compressFiles", _compression)

    def decompressFiles(self):
        return self.__this.call(f"decompressFiles", )

    def compress(self, _compression, _extension=None):
        return self.__this.call(f"compress", _compression, _extension)

    def decompress(self, _extension=None):
        return self.__this.call(f"decompress", _extension)

    def convertToExecutable(self, _format=None, _compression=None, _extension=None):
        return self.__this.call(f"convertToExecutable", _format, _compression, _extension)

    def convertToData(self, _format=None, _compression=None, _extension=None):
        return self.__this.call(f"convertToData", _format, _compression, _extension)

    def copy(self, _from, _to):
        return self.__this.call(f"copy", _from, _to)

    def count(self, _mode=0):
        return self.__this.call(f"count", _mode)

    def delete(self, _local_name):
        return self.__this.call(f"delete", _local_name)

    def delMetadata(self):
        return self.__this.call(f"delMetadata", )

    def extractTo(self, _directory, _files=None, _overwrite=False):
        return self.__this.call(f"extractTo", _directory, _files, _overwrite)

    def getAlias(self):
        return self.__this.call(f"getAlias", )

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getMetadata(self, _unserialize_options=[]):
        return self.__this.call(f"getMetadata", _unserialize_options)

    def getModified(self):
        return self.__this.call(f"getModified", )

    def getSignature(self):
        return self.__this.call(f"getSignature", )

    def getStub(self):
        return self.__this.call(f"getStub", )

    def getVersion(self):
        return self.__this.call(f"getVersion", )

    def hasMetadata(self):
        return self.__this.call(f"hasMetadata", )

    def isBuffering(self):
        return self.__this.call(f"isBuffering", )

    def isCompressed(self):
        return self.__this.call(f"isCompressed", )

    def isFileFormat(self, _format):
        return self.__this.call(f"isFileFormat", _format)

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def offsetExists(self, _local_name):
        return self.__this.call(f"offsetExists", _local_name)

    def offsetGet(self, _local_name):
        return self.__this.call(f"offsetGet", _local_name)

    def offsetSet(self, _local_name, _value):
        return self.__this.call(f"offsetSet", _local_name, _value)

    def offsetUnset(self, _local_name):
        return self.__this.call(f"offsetUnset", _local_name)

    def setAlias(self, _alias):
        return self.__this.call(f"setAlias", _alias)

    def setDefaultStub(self, _index=None, _web_index=None):
        return self.__this.call(f"setDefaultStub", _index, _web_index)

    def setMetadata(self, _metadata):
        return self.__this.call(f"setMetadata", _metadata)

    def setSignatureAlgorithm(self, _algo, _private_key=None):
        return self.__this.call(f"setSignatureAlgorithm", _algo, _private_key)

    def setStub(self, _stub, _length=None):
        return self.__this.call(f"setStub", _stub, _length)

    def startBuffering(self):
        return self.__this.call(f"startBuffering", )

    def stopBuffering(self):
        return self.__this.call(f"stopBuffering", )

    def apiVersion():
        return phpy.call(f"PharData::apiVersion", )

    def canCompress(_compression=0):
        return phpy.call(f"PharData::canCompress", _compression)

    def canWrite():
        return phpy.call(f"PharData::canWrite", )

    def createDefaultStub(_index=None, _web_index=None):
        return phpy.call(f"PharData::createDefaultStub", _index, _web_index)

    def getSupportedCompression():
        return phpy.call(f"PharData::getSupportedCompression", )

    def getSupportedSignatures():
        return phpy.call(f"PharData::getSupportedSignatures", )

    def interceptFileFuncs():
        return phpy.call(f"PharData::interceptFileFuncs", )

    def isValidPharFilename(_filename, _executable=True):
        return phpy.call(f"PharData::isValidPharFilename", _filename, _executable)

    def loadPhar(_filename, _alias=None):
        return phpy.call(f"PharData::loadPhar", _filename, _alias)

    def mapPhar(_alias=None, _offset=0):
        return phpy.call(f"PharData::mapPhar", _alias, _offset)

    def running(_return_phar=True):
        return phpy.call(f"PharData::running", _return_phar)

    def mount(_phar_path, _external_path):
        return phpy.call(f"PharData::mount", _phar_path, _external_path)

    def mungServer(_variables):
        return phpy.call(f"PharData::mungServer", _variables)

    def unlinkArchive(_filename):
        return phpy.call(f"PharData::unlinkArchive", _filename)

    def webPhar(_alias=None, _index=None, _file_not_found_script=None, _mime_types=[], _rewrite=None):
        return phpy.call(f"PharData::webPhar", _alias, _index, _file_not_found_script, _mime_types, _rewrite)

    def hasChildren(self, _allow_links=False):
        return self.__this.call(f"hasChildren", _allow_links)

    def getChildren(self):
        return self.__this.call(f"getChildren", )

    def getSubPath(self):
        return self.__this.call(f"getSubPath", )

    def getSubPathname(self):
        return self.__this.call(f"getSubPathname", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def key(self):
        return self.__this.call(f"key", )

    def current(self):
        return self.__this.call(f"current", )

    def getFlags(self):
        return self.__this.call(f"getFlags", )

    def setFlags(self, _flags):
        return self.__this.call(f"setFlags", _flags)

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def isDot(self):
        return self.__this.call(f"isDot", )

    def valid(self):
        return self.__this.call(f"valid", )

    def next(self):
        return self.__this.call(f"next", )

    def seek(self, _offset):
        return self.__this.call(f"seek", _offset)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class PharFileInfo():

    def __init__(self, _filename):
        self.__this = phpy.Object(f'PharFileInfo', _filename)

    def chmod(self, _perms):
        return self.__this.call(f"chmod", _perms)

    def compress(self, _compression):
        return self.__this.call(f"compress", _compression)

    def decompress(self):
        return self.__this.call(f"decompress", )

    def delMetadata(self):
        return self.__this.call(f"delMetadata", )

    def getCompressedSize(self):
        return self.__this.call(f"getCompressedSize", )

    def getCRC32(self):
        return self.__this.call(f"getCRC32", )

    def getContent(self):
        return self.__this.call(f"getContent", )

    def getMetadata(self, _unserialize_options=[]):
        return self.__this.call(f"getMetadata", _unserialize_options)

    def getPharFlags(self):
        return self.__this.call(f"getPharFlags", )

    def hasMetadata(self):
        return self.__this.call(f"hasMetadata", )

    def isCompressed(self, _compression=None):
        return self.__this.call(f"isCompressed", _compression)

    def isCRCChecked(self):
        return self.__this.call(f"isCRCChecked", )

    def setMetadata(self, _metadata):
        return self.__this.call(f"setMetadata", _metadata)

    def getPath(self):
        return self.__this.call(f"getPath", )

    def getFilename(self):
        return self.__this.call(f"getFilename", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getBasename(self, _suffix=""):
        return self.__this.call(f"getBasename", _suffix)

    def getPathname(self):
        return self.__this.call(f"getPathname", )

    def getPerms(self):
        return self.__this.call(f"getPerms", )

    def getInode(self):
        return self.__this.call(f"getInode", )

    def getSize(self):
        return self.__this.call(f"getSize", )

    def getOwner(self):
        return self.__this.call(f"getOwner", )

    def getGroup(self):
        return self.__this.call(f"getGroup", )

    def getATime(self):
        return self.__this.call(f"getATime", )

    def getMTime(self):
        return self.__this.call(f"getMTime", )

    def getCTime(self):
        return self.__this.call(f"getCTime", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isWritable(self):
        return self.__this.call(f"isWritable", )

    def isReadable(self):
        return self.__this.call(f"isReadable", )

    def isExecutable(self):
        return self.__this.call(f"isExecutable", )

    def isFile(self):
        return self.__this.call(f"isFile", )

    def isDir(self):
        return self.__this.call(f"isDir", )

    def isLink(self):
        return self.__this.call(f"isLink", )

    def getLinkTarget(self):
        return self.__this.call(f"getLinkTarget", )

    def getRealPath(self):
        return self.__this.call(f"getRealPath", )

    def getFileInfo(self, _class=None):
        return self.__this.call(f"getFileInfo", _class)

    def getPathInfo(self, _class=None):
        return self.__this.call(f"getPathInfo", _class)

    def openFile(self, _mode="r", _use_include_path=False, _context=None):
        return self.__this.call(f"openFile", _mode, _use_include_path, _context)

    def setFileClass(self, _class="SplFileObject"):
        return self.__this.call(f"setFileClass", _class)

    def setInfoClass(self, _class="SplFileInfo"):
        return self.__this.call(f"setInfoClass", _class)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __debugInfo(self):
        return self.__this.call(f"__debugInfo", )

    def _bad_state_ex(self):
        return self.__this.call(f"_bad_state_ex", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

