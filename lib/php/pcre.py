import phpy

PREG_PATTERN_ORDER = 1
PREG_SET_ORDER = 2
PREG_OFFSET_CAPTURE = 256
PREG_UNMATCHED_AS_NULL = 512
PREG_SPLIT_NO_EMPTY = 1
PREG_SPLIT_DELIM_CAPTURE = 2
PREG_SPLIT_OFFSET_CAPTURE = 4
PREG_GREP_INVERT = 1
PREG_NO_ERROR = 0
PREG_INTERNAL_ERROR = 1
PREG_BACKTRACK_LIMIT_ERROR = 2
PREG_RECURSION_LIMIT_ERROR = 3
PREG_BAD_UTF8_ERROR = 4
PREG_BAD_UTF8_OFFSET_ERROR = 5
PREG_JIT_STACKLIMIT_ERROR = 6
VERSION = "10.39 2021-10-29"
VERSION_MAJOR = 10
VERSION_MINOR = 39
JIT_SUPPORT = True


def preg_match(_pattern, _subject, _matches=None, _flags=0, _offset=0):
    return phpy.call('preg_match', _pattern, _subject, _matches, _flags, _offset)


def preg_match_all(_pattern, _subject, _matches=None, _flags=0, _offset=0):
    return phpy.call('preg_match_all', _pattern, _subject, _matches, _flags, _offset)


def preg_replace(_pattern, _replacement, _subject, _limit=-1, _count=None):
    return phpy.call('preg_replace', _pattern, _replacement, _subject, _limit, _count)


def preg_filter(_pattern, _replacement, _subject, _limit=-1, _count=None):
    return phpy.call('preg_filter', _pattern, _replacement, _subject, _limit, _count)


def preg_replace_callback(_pattern, _callback, _subject, _limit=-1, _count=None, _flags=0):
    return phpy.call('preg_replace_callback', _pattern, _callback, _subject, _limit, _count, _flags)


def preg_replace_callback_array(_pattern, _subject, _limit=-1, _count=None, _flags=0):
    return phpy.call('preg_replace_callback_array', _pattern, _subject, _limit, _count, _flags)


def preg_split(_pattern, _subject, _limit=-1, _flags=0):
    return phpy.call('preg_split', _pattern, _subject, _limit, _flags)


def preg_quote(_str, _delimiter=None):
    return phpy.call('preg_quote', _str, _delimiter)


def preg_grep(_pattern, _array, _flags=0):
    return phpy.call('preg_grep', _pattern, _array, _flags)


def preg_last_error():
    return phpy.call('preg_last_error', )


def preg_last_error_msg():
    return phpy.call('preg_last_error_msg', )




