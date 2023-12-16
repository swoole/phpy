import phpy

ATOM = "Y-m-d\\TH:i:sP"
COOKIE = "l, d-M-Y H:i:s T"
ISO8601 = "Y-m-d\\TH:i:sO"
RFC822 = "D, d M y H:i:s O"
RFC850 = "l, d-M-y H:i:s T"
RFC1036 = "D, d M y H:i:s O"
RFC1123 = "D, d M Y H:i:s O"
RFC7231 = "D, d M Y H:i:s \\G\\M\\T"
RFC2822 = "D, d M Y H:i:s O"
RFC3339 = "Y-m-d\\TH:i:sP"
RFC3339_EXTENDED = "Y-m-d\\TH:i:s.vP"
RSS = "D, d M Y H:i:s O"
W3C = "Y-m-d\\TH:i:sP"
SUNFUNCS_RET_TIMESTAMP = 0
SUNFUNCS_RET_STRING = 1
SUNFUNCS_RET_DOUBLE = 2


def strtotime(_datetime, _base_timestamp=None):
    return phpy.call('strtotime', _datetime, _base_timestamp)


def date(_format, _timestamp=None):
    return phpy.call('date', _format, _timestamp)


def idate(_format, _timestamp=None):
    return phpy.call('idate', _format, _timestamp)


def gmdate(_format, _timestamp=None):
    return phpy.call('gmdate', _format, _timestamp)


def mktime(_hour, _minute=None, _second=None, _month=None, _day=None, _year=None):
    return phpy.call('mktime', _hour, _minute, _second, _month, _day, _year)


def gmmktime(_hour, _minute=None, _second=None, _month=None, _day=None, _year=None):
    return phpy.call('gmmktime', _hour, _minute, _second, _month, _day, _year)


def checkdate(_month, _day, _year):
    return phpy.call('checkdate', _month, _day, _year)


def strftime(_format, _timestamp=None):
    return phpy.call('strftime', _format, _timestamp)


def gmstrftime(_format, _timestamp=None):
    return phpy.call('gmstrftime', _format, _timestamp)


def time():
    return phpy.call('time', )


def localtime(_timestamp=None, _associative=False):
    return phpy.call('localtime', _timestamp, _associative)


def getdate(_timestamp=None):
    return phpy.call('getdate', _timestamp)


def create(_datetime="now", _timezone=None):
    return phpy.call('date_create', _datetime, _timezone)


def create_immutable(_datetime="now", _timezone=None):
    return phpy.call('date_create_immutable', _datetime, _timezone)


def create_from_format(_format, _datetime, _timezone=None):
    return phpy.call('date_create_from_format', _format, _datetime, _timezone)


def create_immutable_from_format(_format, _datetime, _timezone=None):
    return phpy.call('date_create_immutable_from_format', _format, _datetime, _timezone)


def parse(_datetime):
    return phpy.call('date_parse', _datetime)


def parse_from_format(_format, _datetime):
    return phpy.call('date_parse_from_format', _format, _datetime)


def get_last_errors():
    return phpy.call('date_get_last_errors', )


def format(_object, _format):
    return phpy.call('date_format', _object, _format)


def modify(_object, _modifier):
    return phpy.call('date_modify', _object, _modifier)


def add(_object, _interval):
    return phpy.call('date_add', _object, _interval)


def sub(_object, _interval):
    return phpy.call('date_sub', _object, _interval)


def timezone_get(_object):
    return phpy.call('date_timezone_get', _object)


def timezone_set(_object, _timezone):
    return phpy.call('date_timezone_set', _object, _timezone)


def offset_get(_object):
    return phpy.call('date_offset_get', _object)


def diff(_base_object, _target_object, _absolute=False):
    return phpy.call('date_diff', _base_object, _target_object, _absolute)


def time_set(_object, _hour, _minute, _second=0, _microsecond=0):
    return phpy.call('date_time_set', _object, _hour, _minute, _second, _microsecond)


def date_set(_object, _year, _month, _day):
    return phpy.call('date_date_set', _object, _year, _month, _day)


def isodate_set(_object, _year, _week, _day_of_week=1):
    return phpy.call('date_isodate_set', _object, _year, _week, _day_of_week)


def timestamp_set(_object, _timestamp):
    return phpy.call('date_timestamp_set', _object, _timestamp)


def timestamp_get(_object):
    return phpy.call('date_timestamp_get', _object)


def timezone_open(_timezone):
    return phpy.call('timezone_open', _timezone)


def timezone_name_get(_object):
    return phpy.call('timezone_name_get', _object)


def timezone_name_from_abbr(_abbr, _utc_offset=-1, _is_d_s_t=-1):
    return phpy.call('timezone_name_from_abbr', _abbr, _utc_offset, _is_d_s_t)


def timezone_offset_get(_object, _datetime):
    return phpy.call('timezone_offset_get', _object, _datetime)


def timezone_transitions_get(_object, _timestamp_begin=-9223372036854775808, _timestamp_end=9223372036854775807):
    return phpy.call('timezone_transitions_get', _object, _timestamp_begin, _timestamp_end)


def timezone_location_get(_object):
    return phpy.call('timezone_location_get', _object)


def timezone_identifiers_list(_timezone_group=2047, _country_code=None):
    return phpy.call('timezone_identifiers_list', _timezone_group, _country_code)


def timezone_abbreviations_list():
    return phpy.call('timezone_abbreviations_list', )


def timezone_version_get():
    return phpy.call('timezone_version_get', )


def interval_create_from_date_string(_datetime):
    return phpy.call('date_interval_create_from_date_string', _datetime)


def interval_format(_object, _format):
    return phpy.call('date_interval_format', _object, _format)


def default_timezone_set(_timezone_id):
    return phpy.call('date_default_timezone_set', _timezone_id)


def default_timezone_get():
    return phpy.call('date_default_timezone_get', )


def sunrise(_timestamp, _return_format=1, _latitude=None, _longitude=None, _zenith=None, _utc_offset=None):
    return phpy.call('date_sunrise', _timestamp, _return_format, _latitude, _longitude, _zenith, _utc_offset)


def sunset(_timestamp, _return_format=1, _latitude=None, _longitude=None, _zenith=None, _utc_offset=None):
    return phpy.call('date_sunset', _timestamp, _return_format, _latitude, _longitude, _zenith, _utc_offset)


def sun_info(_timestamp, _latitude, _longitude):
    return phpy.call('date_sun_info', _timestamp, _latitude, _longitude)




class DateTimeInterface():
    ATOM = "Y-m-d\\TH:i:sP"
    COOKIE = "l, d-M-Y H:i:s T"
    ISO8601 = "Y-m-d\\TH:i:sO"
    RFC822 = "D, d M y H:i:s O"
    RFC850 = "l, d-M-y H:i:s T"
    RFC1036 = "D, d M y H:i:s O"
    RFC1123 = "D, d M Y H:i:s O"
    RFC7231 = "D, d M Y H:i:s \\G\\M\\T"
    RFC2822 = "D, d M Y H:i:s O"
    RFC3339 = "Y-m-d\\TH:i:sP"
    RFC3339_EXTENDED = "Y-m-d\\TH:i:s.vP"
    RSS = "D, d M Y H:i:s O"
    W3C = "Y-m-d\\TH:i:sP"

    def format(self, _format):
        return self.__this.call(f"format", _format)

    def getTimezone(self):
        return self.__this.call(f"getTimezone", )

    def getOffset(self):
        return self.__this.call(f"getOffset", )

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def diff(self, _target_object, _absolute=False):
        return self.__this.call(f"diff", _target_object, _absolute)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __init__(self):
        self.__this = phpy.Object(f'DateTimeInterface')

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class DateTime():
    ATOM = "Y-m-d\\TH:i:sP"
    COOKIE = "l, d-M-Y H:i:s T"
    ISO8601 = "Y-m-d\\TH:i:sO"
    RFC822 = "D, d M y H:i:s O"
    RFC850 = "l, d-M-y H:i:s T"
    RFC1036 = "D, d M y H:i:s O"
    RFC1123 = "D, d M Y H:i:s O"
    RFC7231 = "D, d M Y H:i:s \\G\\M\\T"
    RFC2822 = "D, d M Y H:i:s O"
    RFC3339 = "Y-m-d\\TH:i:sP"
    RFC3339_EXTENDED = "Y-m-d\\TH:i:s.vP"
    RSS = "D, d M Y H:i:s O"
    W3C = "Y-m-d\\TH:i:sP"

    def __init__(self, _datetime="now", _timezone=None):
        self.__this = phpy.Object(f'DateTime', _datetime, _timezone)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __set_state(_array):
        return phpy.call(f"DateTime::__set_state", _array)

    def createFromImmutable(_object):
        return phpy.call(f"DateTime::createFromImmutable", _object)

    def createFromInterface(_object):
        return phpy.call(f"DateTime::createFromInterface", _object)

    def createFromFormat(_format, _datetime, _timezone=None):
        return phpy.call(f"DateTime::createFromFormat", _format, _datetime, _timezone)

    def getLastErrors():
        return phpy.call(f"DateTime::getLastErrors", )

    def format(self, _format):
        return self.__this.call(f"format", _format)

    def modify(self, _modifier):
        return self.__this.call(f"modify", _modifier)

    def add(self, _interval):
        return self.__this.call(f"add", _interval)

    def sub(self, _interval):
        return self.__this.call(f"sub", _interval)

    def getTimezone(self):
        return self.__this.call(f"getTimezone", )

    def setTimezone(self, _timezone):
        return self.__this.call(f"setTimezone", _timezone)

    def getOffset(self):
        return self.__this.call(f"getOffset", )

    def setTime(self, _hour, _minute, _second=0, _microsecond=0):
        return self.__this.call(f"setTime", _hour, _minute, _second, _microsecond)

    def setDate(self, _year, _month, _day):
        return self.__this.call(f"setDate", _year, _month, _day)

    def setISODate(self, _year, _week, _day_of_week=1):
        return self.__this.call(f"setISODate", _year, _week, _day_of_week)

    def setTimestamp(self, _timestamp):
        return self.__this.call(f"setTimestamp", _timestamp)

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def diff(self, _target_object, _absolute=False):
        return self.__this.call(f"diff", _target_object, _absolute)

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class DateTimeImmutable():
    ATOM = "Y-m-d\\TH:i:sP"
    COOKIE = "l, d-M-Y H:i:s T"
    ISO8601 = "Y-m-d\\TH:i:sO"
    RFC822 = "D, d M y H:i:s O"
    RFC850 = "l, d-M-y H:i:s T"
    RFC1036 = "D, d M y H:i:s O"
    RFC1123 = "D, d M Y H:i:s O"
    RFC7231 = "D, d M Y H:i:s \\G\\M\\T"
    RFC2822 = "D, d M Y H:i:s O"
    RFC3339 = "Y-m-d\\TH:i:sP"
    RFC3339_EXTENDED = "Y-m-d\\TH:i:s.vP"
    RSS = "D, d M Y H:i:s O"
    W3C = "Y-m-d\\TH:i:sP"

    def __init__(self, _datetime="now", _timezone=None):
        self.__this = phpy.Object(f'DateTimeImmutable', _datetime, _timezone)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __set_state(_array):
        return phpy.call(f"DateTimeImmutable::__set_state", _array)

    def createFromFormat(_format, _datetime, _timezone=None):
        return phpy.call(f"DateTimeImmutable::createFromFormat", _format, _datetime, _timezone)

    def getLastErrors():
        return phpy.call(f"DateTimeImmutable::getLastErrors", )

    def format(self, _format):
        return self.__this.call(f"format", _format)

    def getTimezone(self):
        return self.__this.call(f"getTimezone", )

    def getOffset(self):
        return self.__this.call(f"getOffset", )

    def getTimestamp(self):
        return self.__this.call(f"getTimestamp", )

    def diff(self, _target_object, _absolute=False):
        return self.__this.call(f"diff", _target_object, _absolute)

    def modify(self, _modifier):
        return self.__this.call(f"modify", _modifier)

    def add(self, _interval):
        return self.__this.call(f"add", _interval)

    def sub(self, _interval):
        return self.__this.call(f"sub", _interval)

    def setTimezone(self, _timezone):
        return self.__this.call(f"setTimezone", _timezone)

    def setTime(self, _hour, _minute, _second=0, _microsecond=0):
        return self.__this.call(f"setTime", _hour, _minute, _second, _microsecond)

    def setDate(self, _year, _month, _day):
        return self.__this.call(f"setDate", _year, _month, _day)

    def setISODate(self, _year, _week, _day_of_week=1):
        return self.__this.call(f"setISODate", _year, _week, _day_of_week)

    def setTimestamp(self, _timestamp):
        return self.__this.call(f"setTimestamp", _timestamp)

    def createFromMutable(_object):
        return phpy.call(f"DateTimeImmutable::createFromMutable", _object)

    def createFromInterface(_object):
        return phpy.call(f"DateTimeImmutable::createFromInterface", _object)

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class DateTimeZone():
    AFRICA = 1
    AMERICA = 2
    ANTARCTICA = 4
    ARCTIC = 8
    ASIA = 16
    ATLANTIC = 32
    AUSTRALIA = 64
    EUROPE = 128
    INDIAN = 256
    PACIFIC = 512
    UTC = 1024
    ALL = 2047
    ALL_WITH_BC = 4095
    PER_COUNTRY = 4096

    def __init__(self, _timezone):
        self.__this = phpy.Object(f'DateTimeZone', _timezone)

    def getName(self):
        return self.__this.call(f"getName", )

    def getOffset(self, _datetime):
        return self.__this.call(f"getOffset", _datetime)

    def getTransitions(self, _timestamp_begin=-9223372036854775808, _timestamp_end=9223372036854775807):
        return self.__this.call(f"getTransitions", _timestamp_begin, _timestamp_end)

    def getLocation(self):
        return self.__this.call(f"getLocation", )

    def listAbbreviations():
        return phpy.call(f"DateTimeZone::listAbbreviations", )

    def listIdentifiers(_timezone_group=2047, _country_code=None):
        return phpy.call(f"DateTimeZone::listIdentifiers", _timezone_group, _country_code)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __set_state(_array):
        return phpy.call(f"DateTimeZone::__set_state", _array)

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class DateInterval():

    def __init__(self, _duration):
        self.__this = phpy.Object(f'DateInterval', _duration)

    def createFromDateString(_datetime):
        return phpy.call(f"DateInterval::createFromDateString", _datetime)

    def format(self, _format):
        return self.__this.call(f"format", _format)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __set_state(_array):
        return phpy.call(f"DateInterval::__set_state", _array)

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

class DatePeriod():
    EXCLUDE_START_DATE = 1

    def __init__(self, _start, _interval=None, _end=None, _options=None):
        self.__this = phpy.Object(f'DatePeriod', _start, _interval, _end, _options)

    def getStartDate(self):
        return self.__this.call(f"getStartDate", )

    def getEndDate(self):
        return self.__this.call(f"getEndDate", )

    def getDateInterval(self):
        return self.__this.call(f"getDateInterval", )

    def getRecurrences(self):
        return self.__this.call(f"getRecurrences", )

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def __set_state(_array):
        return phpy.call(f"DatePeriod::__set_state", _array)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

