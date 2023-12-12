import phpy

VERSION = 20910
DOTTED_VERSION = "2.9.10"
LOADED_VERSION = "20910"
NOENT = 2
DTDLOAD = 4
DTDATTR = 8
DTDVALID = 16
NOERROR = 32
NOWARNING = 64
NOBLANKS = 256
XINCLUDE = 1024
NSCLEAN = 8192
NOCDATA = 16384
NONET = 2048
PEDANTIC = 128
COMPACT = 65536
NOXMLDECL = 2
PARSEHUGE = 524288
BIGLINES = 4194304
NOEMPTYTAG = 4
SCHEMA_CREATE = 1
HTML_NOIMPLIED = 8192
HTML_NODEFDTD = 4
ERR_NONE = 0
ERR_WARNING = 1
ERR_ERROR = 2
ERR_FATAL = 3


def set_streams_context(_context):
    return phpy.call('libxml_set_streams_context', _context)


def use_internal_errors(_use_errors=None):
    return phpy.call('libxml_use_internal_errors', _use_errors)


def get_last_error():
    return phpy.call('libxml_get_last_error', )


def get_errors():
    return phpy.call('libxml_get_errors', )


def clear_errors():
    return phpy.call('libxml_clear_errors', )


def disable_entity_loader(_disable=True):
    return phpy.call('libxml_disable_entity_loader', _disable)


def set_external_entity_loader(_resolver_function):
    return phpy.call('libxml_set_external_entity_loader', _resolver_function)




