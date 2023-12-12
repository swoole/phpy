import phpy

HMAC = 1


def hash(_algo, _data, _binary=False, _options=[]):
    return phpy.call('hash', _algo, _data, _binary, _options)


def file(_algo, _filename, _binary=False, _options=[]):
    return phpy.call('hash_file', _algo, _filename, _binary, _options)


def hmac(_algo, _data, _key, _binary=False):
    return phpy.call('hash_hmac', _algo, _data, _key, _binary)


def hmac_file(_algo, _filename, _key, _binary=False):
    return phpy.call('hash_hmac_file', _algo, _filename, _key, _binary)


def init(_algo, _flags=0, _key="", _options=[]):
    return phpy.call('hash_init', _algo, _flags, _key, _options)


def update(_context, _data):
    return phpy.call('hash_update', _context, _data)


def update_stream(_context, _stream, _length=-1):
    return phpy.call('hash_update_stream', _context, _stream, _length)


def update_file(_context, _filename, _stream_context=None):
    return phpy.call('hash_update_file', _context, _filename, _stream_context)


def final(_context, _binary=False):
    return phpy.call('hash_final', _context, _binary)


def copy(_context):
    return phpy.call('hash_copy', _context)


def algos():
    return phpy.call('hash_algos', )


def hmac_algos():
    return phpy.call('hash_hmac_algos', )


def pbkdf2(_algo, _password, _salt, _iterations, _length=0, _binary=False):
    return phpy.call('hash_pbkdf2', _algo, _password, _salt, _iterations, _length, _binary)


def equals(_known_string, _user_string):
    return phpy.call('hash_equals', _known_string, _user_string)


def hkdf(_algo, _key, _length=0, _info="", _salt=""):
    return phpy.call('hash_hkdf', _algo, _key, _length, _info, _salt)




def HashContext():

    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)


