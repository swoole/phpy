import phpy

PHP_SESSION_DISABLED = 0
PHP_SESSION_NONE = 1
PHP_SESSION_ACTIVE = 2


def name(_name=None):
    return phpy.call('session_name', _name)


def module_name(_module=None):
    return phpy.call('session_module_name', _module)


def save_path(_path=None):
    return phpy.call('session_save_path', _path)


def id(_id=None):
    return phpy.call('session_id', _id)


def create_id(_prefix=""):
    return phpy.call('session_create_id', _prefix)


def regenerate_id(_delete_old_session=False):
    return phpy.call('session_regenerate_id', _delete_old_session)


def decode(_data):
    return phpy.call('session_decode', _data)


def encode():
    return phpy.call('session_encode', )


def destroy():
    return phpy.call('session_destroy', )


def unset():
    return phpy.call('session_unset', )


def gc():
    return phpy.call('session_gc', )


def get_cookie_params():
    return phpy.call('session_get_cookie_params', )


def write_close():
    return phpy.call('session_write_close', )


def abort():
    return phpy.call('session_abort', )


def reset():
    return phpy.call('session_reset', )


def status():
    return phpy.call('session_status', )


def register_shutdown():
    return phpy.call('session_register_shutdown', )


def commit():
    return phpy.call('session_commit', )


def set_save_handler(_open, _close=None, _read=None, _write=None, _destroy=None, _gc=None, _create_sid=None, _validate_sid=None, _update_timestamp=None):
    return phpy.call('session_set_save_handler', _open, _close, _read, _write, _destroy, _gc, _create_sid, _validate_sid, _update_timestamp)


def cache_limiter(_value=None):
    return phpy.call('session_cache_limiter', _value)


def cache_expire(_value=None):
    return phpy.call('session_cache_expire', _value)


def set_cookie_params(_lifetime_or_options, _path=None, _domain=None, _secure=None, _httponly=None):
    return phpy.call('session_set_cookie_params', _lifetime_or_options, _path, _domain, _secure, _httponly)


def start(_options=[]):
    return phpy.call('session_start', _options)




class SessionHandlerInterface():

    def open(self, _path, _name):
        return self.__this.call(f"open", _path, _name)

    def close(self):
        return self.__this.call(f"close", )

    def read(self, _id):
        return self.__this.call(f"read", _id)

    def write(self, _id, _data):
        return self.__this.call(f"write", _id, _data)

    def destroy(self, _id):
        return self.__this.call(f"destroy", _id)

    def gc(self, _max_lifetime):
        return self.__this.call(f"gc", _max_lifetime)

    def __init__(self):
        self.__this = phpy.Object(f'SessionHandlerInterface')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class SessionIdInterface():

    def create_sid(self):
        return self.__this.call(f"create_sid", )

    def __init__(self):
        self.__this = phpy.Object(f'SessionIdInterface')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class SessionUpdateTimestampHandlerInterface():

    def validateId(self, _id):
        return self.__this.call(f"validateId", _id)

    def updateTimestamp(self, _id, _data):
        return self.__this.call(f"updateTimestamp", _id, _data)

    def __init__(self):
        self.__this = phpy.Object(f'SessionUpdateTimestampHandlerInterface')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class SessionHandler():

    def open(self, _path, _name):
        return self.__this.call(f"open", _path, _name)

    def close(self):
        return self.__this.call(f"close", )

    def read(self, _id):
        return self.__this.call(f"read", _id)

    def write(self, _id, _data):
        return self.__this.call(f"write", _id, _data)

    def destroy(self, _id):
        return self.__this.call(f"destroy", _id)

    def gc(self, _max_lifetime):
        return self.__this.call(f"gc", _max_lifetime)

    def create_sid(self):
        return self.__this.call(f"create_sid", )

    def __init__(self):
        self.__this = phpy.Object(f'SessionHandler')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

