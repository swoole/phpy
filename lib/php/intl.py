import phpy

MAX_LOCALE_LEN = 156
ICU_VERSION = "60.3"
ICU_DATA_VERSION = "60.3"
ULOC_ACTUAL_LOCALE = 0
ULOC_VALID_LOCALE = 1
GRAPHEME_EXTR_COUNT = 0
GRAPHEME_EXTR_MAXBYTES = 1
GRAPHEME_EXTR_MAXCHARS = 2
U_USING_FALLBACK_WARNING = -128
U_ERROR_WARNING_START = -128
U_USING_DEFAULT_WARNING = -127
U_SAFECLONE_ALLOCATED_WARNING = -126
U_STATE_OLD_WARNING = -125
U_STRING_NOT_TERMINATED_WARNING = -124
U_SORT_KEY_TOO_SHORT_WARNING = -123
U_AMBIGUOUS_ALIAS_WARNING = -122
U_DIFFERENT_UCA_VERSION = -121
U_ERROR_WARNING_LIMIT = -119
U_ZERO_ERROR = 0
U_ILLEGAL_ARGUMENT_ERROR = 1
U_MISSING_RESOURCE_ERROR = 2
U_INVALID_FORMAT_ERROR = 3
U_FILE_ACCESS_ERROR = 4
U_INTERNAL_PROGRAM_ERROR = 5
U_MESSAGE_PARSE_ERROR = 6
U_MEMORY_ALLOCATION_ERROR = 7
U_INDEX_OUTOFBOUNDS_ERROR = 8
U_PARSE_ERROR = 9
U_INVALID_CHAR_FOUND = 10
U_TRUNCATED_CHAR_FOUND = 11
U_ILLEGAL_CHAR_FOUND = 12
U_INVALID_TABLE_FORMAT = 13
U_INVALID_TABLE_FILE = 14
U_BUFFER_OVERFLOW_ERROR = 15
U_UNSUPPORTED_ERROR = 16
U_RESOURCE_TYPE_MISMATCH = 17
U_ILLEGAL_ESCAPE_SEQUENCE = 18
U_UNSUPPORTED_ESCAPE_SEQUENCE = 19
U_NO_SPACE_AVAILABLE = 20
U_CE_NOT_FOUND_ERROR = 21
U_PRIMARY_TOO_LONG_ERROR = 22
U_STATE_TOO_OLD_ERROR = 23
U_TOO_MANY_ALIASES_ERROR = 24
U_ENUM_OUT_OF_SYNC_ERROR = 25
U_INVARIANT_CONVERSION_ERROR = 26
U_INVALID_STATE_ERROR = 27
U_COLLATOR_VERSION_MISMATCH = 28
U_USELESS_COLLATOR_ERROR = 29
U_NO_WRITE_PERMISSION = 30
U_STANDARD_ERROR_LIMIT = 31
U_BAD_VARIABLE_DEFINITION = 65536
U_PARSE_ERROR_START = 65536
U_MALFORMED_RULE = 65537
U_MALFORMED_SET = 65538
U_MALFORMED_SYMBOL_REFERENCE = 65539
U_MALFORMED_UNICODE_ESCAPE = 65540
U_MALFORMED_VARIABLE_DEFINITION = 65541
U_MALFORMED_VARIABLE_REFERENCE = 65542
U_MISMATCHED_SEGMENT_DELIMITERS = 65543
U_MISPLACED_ANCHOR_START = 65544
U_MISPLACED_CURSOR_OFFSET = 65545
U_MISPLACED_QUANTIFIER = 65546
U_MISSING_OPERATOR = 65547
U_MISSING_SEGMENT_CLOSE = 65548
U_MULTIPLE_ANTE_CONTEXTS = 65549
U_MULTIPLE_CURSORS = 65550
U_MULTIPLE_POST_CONTEXTS = 65551
U_TRAILING_BACKSLASH = 65552
U_UNDEFINED_SEGMENT_REFERENCE = 65553
U_UNDEFINED_VARIABLE = 65554
U_UNQUOTED_SPECIAL = 65555
U_UNTERMINATED_QUOTE = 65556
U_RULE_MASK_ERROR = 65557
U_MISPLACED_COMPOUND_FILTER = 65558
U_MULTIPLE_COMPOUND_FILTERS = 65559
U_INVALID_RBT_SYNTAX = 65560
U_INVALID_PROPERTY_PATTERN = 65561
U_MALFORMED_PRAGMA = 65562
U_UNCLOSED_SEGMENT = 65563
U_ILLEGAL_CHAR_IN_SEGMENT = 65564
U_VARIABLE_RANGE_EXHAUSTED = 65565
U_VARIABLE_RANGE_OVERLAP = 65566
U_ILLEGAL_CHARACTER = 65567
U_INTERNAL_TRANSLITERATOR_ERROR = 65568
U_INVALID_ID = 65569
U_INVALID_FUNCTION = 65570
U_PARSE_ERROR_LIMIT = 65571
U_UNEXPECTED_TOKEN = 65792
U_FMT_PARSE_ERROR_START = 65792
U_MULTIPLE_DECIMAL_SEPARATORS = 65793
U_MULTIPLE_DECIMAL_SEPERATORS = 65793
U_MULTIPLE_EXPONENTIAL_SYMBOLS = 65794
U_MALFORMED_EXPONENTIAL_PATTERN = 65795
U_MULTIPLE_PERCENT_SYMBOLS = 65796
U_MULTIPLE_PERMILL_SYMBOLS = 65797
U_MULTIPLE_PAD_SPECIFIERS = 65798
U_PATTERN_SYNTAX_ERROR = 65799
U_ILLEGAL_PAD_POSITION = 65800
U_UNMATCHED_BRACES = 65801
U_UNSUPPORTED_PROPERTY = 65802
U_UNSUPPORTED_ATTRIBUTE = 65803
U_FMT_PARSE_ERROR_LIMIT = 65810
U_BRK_INTERNAL_ERROR = 66048
U_BRK_ERROR_START = 66048
U_BRK_HEX_DIGITS_EXPECTED = 66049
U_BRK_SEMICOLON_EXPECTED = 66050
U_BRK_RULE_SYNTAX = 66051
U_BRK_UNCLOSED_SET = 66052
U_BRK_ASSIGN_ERROR = 66053
U_BRK_VARIABLE_REDFINITION = 66054
U_BRK_MISMATCHED_PAREN = 66055
U_BRK_NEW_LINE_IN_QUOTED_STRING = 66056
U_BRK_UNDEFINED_VARIABLE = 66057
U_BRK_INIT_ERROR = 66058
U_BRK_RULE_EMPTY_SET = 66059
U_BRK_UNRECOGNIZED_OPTION = 66060
U_BRK_MALFORMED_RULE_TAG = 66061
U_BRK_ERROR_LIMIT = 66062
U_REGEX_INTERNAL_ERROR = 66304
U_REGEX_ERROR_START = 66304
U_REGEX_RULE_SYNTAX = 66305
U_REGEX_INVALID_STATE = 66306
U_REGEX_BAD_ESCAPE_SEQUENCE = 66307
U_REGEX_PROPERTY_SYNTAX = 66308
U_REGEX_UNIMPLEMENTED = 66309
U_REGEX_MISMATCHED_PAREN = 66310
U_REGEX_NUMBER_TOO_BIG = 66311
U_REGEX_BAD_INTERVAL = 66312
U_REGEX_MAX_LT_MIN = 66313
U_REGEX_INVALID_BACK_REF = 66314
U_REGEX_INVALID_FLAG = 66315
U_REGEX_LOOK_BEHIND_LIMIT = 66316
U_REGEX_SET_CONTAINS_STRING = 66317
U_REGEX_ERROR_LIMIT = 66326
U_IDNA_PROHIBITED_ERROR = 66560
U_IDNA_ERROR_START = 66560
U_IDNA_UNASSIGNED_ERROR = 66561
U_IDNA_CHECK_BIDI_ERROR = 66562
U_IDNA_STD3_ASCII_RULES_ERROR = 66563
U_IDNA_ACE_PREFIX_ERROR = 66564
U_IDNA_VERIFICATION_ERROR = 66565
U_IDNA_LABEL_TOO_LONG_ERROR = 66566
U_IDNA_ZERO_LENGTH_LABEL_ERROR = 66567
U_IDNA_DOMAIN_NAME_TOO_LONG_ERROR = 66568
U_IDNA_ERROR_LIMIT = 66569
U_STRINGPREP_PROHIBITED_ERROR = 66560
U_STRINGPREP_UNASSIGNED_ERROR = 66561
U_STRINGPREP_CHECK_BIDI_ERROR = 66562
U_ERROR_LIMIT = 66818
IDNA_DEFAULT = 0
IDNA_ALLOW_UNASSIGNED = 1
IDNA_USE_STD3_RULES = 2
IDNA_CHECK_BIDI = 4
IDNA_CHECK_CONTEXTJ = 8
IDNA_NONTRANSITIONAL_TO_ASCII = 16
IDNA_NONTRANSITIONAL_TO_UNICODE = 32
IDNA_VARIANT_UTS46 = 1
IDNA_ERROR_EMPTY_LABEL = 1
IDNA_ERROR_LABEL_TOO_LONG = 2
IDNA_ERROR_DOMAIN_NAME_TOO_LONG = 4
IDNA_ERROR_LEADING_HYPHEN = 8
IDNA_ERROR_TRAILING_HYPHEN = 16
IDNA_ERROR_HYPHEN_3_4 = 32
IDNA_ERROR_LEADING_COMBINING_MARK = 64
IDNA_ERROR_DISALLOWED = 128
IDNA_ERROR_PUNYCODE = 256
IDNA_ERROR_LABEL_HAS_DOT = 512
IDNA_ERROR_INVALID_ACE_LABEL = 1024
IDNA_ERROR_BIDI = 2048
IDNA_ERROR_CONTEXTJ = 4096


def intlcal_create_instance(_timezone=None, _locale=None):
    return phpy.call('intlcal_create_instance', _timezone, _locale)


def intlcal_get_keyword_values_for_locale(_keyword, _locale, _only_common):
    return phpy.call('intlcal_get_keyword_values_for_locale', _keyword, _locale, _only_common)


def intlcal_get_now():
    return phpy.call('intlcal_get_now', )


def intlcal_get_available_locales():
    return phpy.call('intlcal_get_available_locales', )


def intlcal_get(_calendar, _field):
    return phpy.call('intlcal_get', _calendar, _field)


def intlcal_get_time(_calendar):
    return phpy.call('intlcal_get_time', _calendar)


def intlcal_set_time(_calendar, _timestamp):
    return phpy.call('intlcal_set_time', _calendar, _timestamp)


def intlcal_add(_calendar, _field, _value):
    return phpy.call('intlcal_add', _calendar, _field, _value)


def intlcal_set_time_zone(_calendar, _timezone):
    return phpy.call('intlcal_set_time_zone', _calendar, _timezone)


def intlcal_after(_calendar, _other):
    return phpy.call('intlcal_after', _calendar, _other)


def intlcal_before(_calendar, _other):
    return phpy.call('intlcal_before', _calendar, _other)


def intlcal_set(_calendar, _year, _month, _day_of_month=None, _hour=None, _minute=None, _second=None):
    return phpy.call('intlcal_set', _calendar, _year, _month, _day_of_month, _hour, _minute, _second)


def intlcal_roll(_calendar, _field, _value):
    return phpy.call('intlcal_roll', _calendar, _field, _value)


def intlcal_clear(_calendar, _field=None):
    return phpy.call('intlcal_clear', _calendar, _field)


def intlcal_field_difference(_calendar, _timestamp, _field):
    return phpy.call('intlcal_field_difference', _calendar, _timestamp, _field)


def intlcal_get_actual_maximum(_calendar, _field):
    return phpy.call('intlcal_get_actual_maximum', _calendar, _field)


def intlcal_get_actual_minimum(_calendar, _field):
    return phpy.call('intlcal_get_actual_minimum', _calendar, _field)


def intlcal_get_day_of_week_type(_calendar, _day_of_week):
    return phpy.call('intlcal_get_day_of_week_type', _calendar, _day_of_week)


def intlcal_get_first_day_of_week(_calendar):
    return phpy.call('intlcal_get_first_day_of_week', _calendar)


def intlcal_get_least_maximum(_calendar, _field):
    return phpy.call('intlcal_get_least_maximum', _calendar, _field)


def intlcal_get_greatest_minimum(_calendar, _field):
    return phpy.call('intlcal_get_greatest_minimum', _calendar, _field)


def intlcal_get_locale(_calendar, _type):
    return phpy.call('intlcal_get_locale', _calendar, _type)


def intlcal_get_maximum(_calendar, _field):
    return phpy.call('intlcal_get_maximum', _calendar, _field)


def intlcal_get_minimal_days_in_first_week(_calendar):
    return phpy.call('intlcal_get_minimal_days_in_first_week', _calendar)


def intlcal_set_minimal_days_in_first_week(_calendar, _days):
    return phpy.call('intlcal_set_minimal_days_in_first_week', _calendar, _days)


def intlcal_get_minimum(_calendar, _field):
    return phpy.call('intlcal_get_minimum', _calendar, _field)


def intlcal_get_time_zone(_calendar):
    return phpy.call('intlcal_get_time_zone', _calendar)


def intlcal_get_type(_calendar):
    return phpy.call('intlcal_get_type', _calendar)


def intlcal_get_weekend_transition(_calendar, _day_of_week):
    return phpy.call('intlcal_get_weekend_transition', _calendar, _day_of_week)


def intlcal_in_daylight_time(_calendar):
    return phpy.call('intlcal_in_daylight_time', _calendar)


def intlcal_is_lenient(_calendar):
    return phpy.call('intlcal_is_lenient', _calendar)


def intlcal_is_set(_calendar, _field):
    return phpy.call('intlcal_is_set', _calendar, _field)


def intlcal_is_equivalent_to(_calendar, _other):
    return phpy.call('intlcal_is_equivalent_to', _calendar, _other)


def intlcal_is_weekend(_calendar, _timestamp=None):
    return phpy.call('intlcal_is_weekend', _calendar, _timestamp)


def intlcal_set_first_day_of_week(_calendar, _day_of_week):
    return phpy.call('intlcal_set_first_day_of_week', _calendar, _day_of_week)


def intlcal_set_lenient(_calendar, _lenient):
    return phpy.call('intlcal_set_lenient', _calendar, _lenient)


def intlcal_get_repeated_wall_time_option(_calendar):
    return phpy.call('intlcal_get_repeated_wall_time_option', _calendar)


def intlcal_equals(_calendar, _other):
    return phpy.call('intlcal_equals', _calendar, _other)


def intlcal_get_skipped_wall_time_option(_calendar):
    return phpy.call('intlcal_get_skipped_wall_time_option', _calendar)


def intlcal_set_repeated_wall_time_option(_calendar, _option):
    return phpy.call('intlcal_set_repeated_wall_time_option', _calendar, _option)


def intlcal_set_skipped_wall_time_option(_calendar, _option):
    return phpy.call('intlcal_set_skipped_wall_time_option', _calendar, _option)


def intlcal_from_date_time(_datetime, _locale=None):
    return phpy.call('intlcal_from_date_time', _datetime, _locale)


def intlcal_to_date_time(_calendar):
    return phpy.call('intlcal_to_date_time', _calendar)


def intlcal_get_error_code(_calendar):
    return phpy.call('intlcal_get_error_code', _calendar)


def intlcal_get_error_message(_calendar):
    return phpy.call('intlcal_get_error_message', _calendar)


def intlgregcal_create_instance(_timezone_or_year=None, _locale_or_month=None, _day=None, _hour=None, _minute=None, _second=None):
    return phpy.call('intlgregcal_create_instance', _timezone_or_year, _locale_or_month, _day, _hour, _minute, _second)


def intlgregcal_set_gregorian_change(_calendar, _timestamp):
    return phpy.call('intlgregcal_set_gregorian_change', _calendar, _timestamp)


def intlgregcal_get_gregorian_change(_calendar):
    return phpy.call('intlgregcal_get_gregorian_change', _calendar)


def intlgregcal_is_leap_year(_calendar, _year):
    return phpy.call('intlgregcal_is_leap_year', _calendar, _year)


def collator_create(_locale):
    return phpy.call('collator_create', _locale)


def collator_compare(_object, _string1, _string2):
    return phpy.call('collator_compare', _object, _string1, _string2)


def collator_get_attribute(_object, _attribute):
    return phpy.call('collator_get_attribute', _object, _attribute)


def collator_set_attribute(_object, _attribute, _value):
    return phpy.call('collator_set_attribute', _object, _attribute, _value)


def collator_get_strength(_object):
    return phpy.call('collator_get_strength', _object)


def collator_set_strength(_object, _strength):
    return phpy.call('collator_set_strength', _object, _strength)


def collator_sort(_object, _array, _flags=0):
    return phpy.call('collator_sort', _object, _array, _flags)


def collator_sort_with_sort_keys(_object, _array):
    return phpy.call('collator_sort_with_sort_keys', _object, _array)


def collator_asort(_object, _array, _flags=0):
    return phpy.call('collator_asort', _object, _array, _flags)


def collator_get_locale(_object, _type):
    return phpy.call('collator_get_locale', _object, _type)


def collator_get_error_code(_object):
    return phpy.call('collator_get_error_code', _object)


def collator_get_error_message(_object):
    return phpy.call('collator_get_error_message', _object)


def collator_get_sort_key(_object, _string):
    return phpy.call('collator_get_sort_key', _object, _string)


def get_error_code():
    return phpy.call('intl_get_error_code', )


def get_error_message():
    return phpy.call('intl_get_error_message', )


def is_failure(_error_code):
    return phpy.call('intl_is_failure', _error_code)


def error_name(_error_code):
    return phpy.call('intl_error_name', _error_code)


def datefmt_create(_locale, _date_type=0, _time_type=0, _timezone=None, _calendar=None, _pattern=None):
    return phpy.call('datefmt_create', _locale, _date_type, _time_type, _timezone, _calendar, _pattern)


def datefmt_get_datetype(_formatter):
    return phpy.call('datefmt_get_datetype', _formatter)


def datefmt_get_timetype(_formatter):
    return phpy.call('datefmt_get_timetype', _formatter)


def datefmt_get_calendar(_formatter):
    return phpy.call('datefmt_get_calendar', _formatter)


def datefmt_set_calendar(_formatter, _calendar):
    return phpy.call('datefmt_set_calendar', _formatter, _calendar)


def datefmt_get_timezone_id(_formatter):
    return phpy.call('datefmt_get_timezone_id', _formatter)


def datefmt_get_calendar_object(_formatter):
    return phpy.call('datefmt_get_calendar_object', _formatter)


def datefmt_get_timezone(_formatter):
    return phpy.call('datefmt_get_timezone', _formatter)


def datefmt_set_timezone(_formatter, _timezone):
    return phpy.call('datefmt_set_timezone', _formatter, _timezone)


def datefmt_set_pattern(_formatter, _pattern):
    return phpy.call('datefmt_set_pattern', _formatter, _pattern)


def datefmt_get_pattern(_formatter):
    return phpy.call('datefmt_get_pattern', _formatter)


def datefmt_get_locale(_formatter, _type=0):
    return phpy.call('datefmt_get_locale', _formatter, _type)


def datefmt_set_lenient(_formatter, _lenient):
    return phpy.call('datefmt_set_lenient', _formatter, _lenient)


def datefmt_is_lenient(_formatter):
    return phpy.call('datefmt_is_lenient', _formatter)


def datefmt_format(_formatter, _datetime):
    return phpy.call('datefmt_format', _formatter, _datetime)


def datefmt_format_object(_datetime, _format=None, _locale=None):
    return phpy.call('datefmt_format_object', _datetime, _format, _locale)


def datefmt_parse(_formatter, _string, _offset=None):
    return phpy.call('datefmt_parse', _formatter, _string, _offset)


def datefmt_localtime(_formatter, _string, _offset=None):
    return phpy.call('datefmt_localtime', _formatter, _string, _offset)


def datefmt_get_error_code(_formatter):
    return phpy.call('datefmt_get_error_code', _formatter)


def datefmt_get_error_message(_formatter):
    return phpy.call('datefmt_get_error_message', _formatter)


def numfmt_create(_locale, _style, _pattern=None):
    return phpy.call('numfmt_create', _locale, _style, _pattern)


def numfmt_format(_formatter, _num, _type=0):
    return phpy.call('numfmt_format', _formatter, _num, _type)


def numfmt_parse(_formatter, _string, _type=3, _offset=None):
    return phpy.call('numfmt_parse', _formatter, _string, _type, _offset)


def numfmt_format_currency(_formatter, _amount, _currency):
    return phpy.call('numfmt_format_currency', _formatter, _amount, _currency)


def numfmt_parse_currency(_formatter, _string, _currency, _offset=None):
    return phpy.call('numfmt_parse_currency', _formatter, _string, _currency, _offset)


def numfmt_set_attribute(_formatter, _attribute, _value):
    return phpy.call('numfmt_set_attribute', _formatter, _attribute, _value)


def numfmt_get_attribute(_formatter, _attribute):
    return phpy.call('numfmt_get_attribute', _formatter, _attribute)


def numfmt_set_text_attribute(_formatter, _attribute, _value):
    return phpy.call('numfmt_set_text_attribute', _formatter, _attribute, _value)


def numfmt_get_text_attribute(_formatter, _attribute):
    return phpy.call('numfmt_get_text_attribute', _formatter, _attribute)


def numfmt_set_symbol(_formatter, _symbol, _value):
    return phpy.call('numfmt_set_symbol', _formatter, _symbol, _value)


def numfmt_get_symbol(_formatter, _symbol):
    return phpy.call('numfmt_get_symbol', _formatter, _symbol)


def numfmt_set_pattern(_formatter, _pattern):
    return phpy.call('numfmt_set_pattern', _formatter, _pattern)


def numfmt_get_pattern(_formatter):
    return phpy.call('numfmt_get_pattern', _formatter)


def numfmt_get_locale(_formatter, _type=0):
    return phpy.call('numfmt_get_locale', _formatter, _type)


def numfmt_get_error_code(_formatter):
    return phpy.call('numfmt_get_error_code', _formatter)


def numfmt_get_error_message(_formatter):
    return phpy.call('numfmt_get_error_message', _formatter)


def grapheme_strlen(_string):
    return phpy.call('grapheme_strlen', _string)


def grapheme_strpos(_haystack, _needle, _offset=0):
    return phpy.call('grapheme_strpos', _haystack, _needle, _offset)


def grapheme_stripos(_haystack, _needle, _offset=0):
    return phpy.call('grapheme_stripos', _haystack, _needle, _offset)


def grapheme_strrpos(_haystack, _needle, _offset=0):
    return phpy.call('grapheme_strrpos', _haystack, _needle, _offset)


def grapheme_strripos(_haystack, _needle, _offset=0):
    return phpy.call('grapheme_strripos', _haystack, _needle, _offset)


def grapheme_substr(_string, _offset, _length=None):
    return phpy.call('grapheme_substr', _string, _offset, _length)


def grapheme_strstr(_haystack, _needle, _before_needle=False):
    return phpy.call('grapheme_strstr', _haystack, _needle, _before_needle)


def grapheme_stristr(_haystack, _needle, _before_needle=False):
    return phpy.call('grapheme_stristr', _haystack, _needle, _before_needle)


def grapheme_extract(_haystack, _size, _type=0, _offset=0, _next=None):
    return phpy.call('grapheme_extract', _haystack, _size, _type, _offset, _next)


def idn_to_ascii(_domain, _flags=0, _variant=1, _idna_info=None):
    return phpy.call('idn_to_ascii', _domain, _flags, _variant, _idna_info)


def idn_to_utf8(_domain, _flags=0, _variant=1, _idna_info=None):
    return phpy.call('idn_to_utf8', _domain, _flags, _variant, _idna_info)


def locale_get_default():
    return phpy.call('locale_get_default', )


def locale_set_default(_locale):
    return phpy.call('locale_set_default', _locale)


def locale_get_primary_language(_locale):
    return phpy.call('locale_get_primary_language', _locale)


def locale_get_script(_locale):
    return phpy.call('locale_get_script', _locale)


def locale_get_region(_locale):
    return phpy.call('locale_get_region', _locale)


def locale_get_keywords(_locale):
    return phpy.call('locale_get_keywords', _locale)


def locale_get_display_script(_locale, _display_locale=None):
    return phpy.call('locale_get_display_script', _locale, _display_locale)


def locale_get_display_region(_locale, _display_locale=None):
    return phpy.call('locale_get_display_region', _locale, _display_locale)


def locale_get_display_name(_locale, _display_locale=None):
    return phpy.call('locale_get_display_name', _locale, _display_locale)


def locale_get_display_language(_locale, _display_locale=None):
    return phpy.call('locale_get_display_language', _locale, _display_locale)


def locale_get_display_variant(_locale, _display_locale=None):
    return phpy.call('locale_get_display_variant', _locale, _display_locale)


def locale_compose(_subtags):
    return phpy.call('locale_compose', _subtags)


def locale_parse(_locale):
    return phpy.call('locale_parse', _locale)


def locale_get_all_variants(_locale):
    return phpy.call('locale_get_all_variants', _locale)


def locale_filter_matches(_language_tag, _locale, _canonicalize=False):
    return phpy.call('locale_filter_matches', _language_tag, _locale, _canonicalize)


def locale_canonicalize(_locale):
    return phpy.call('locale_canonicalize', _locale)


def locale_lookup(_language_tag, _locale, _canonicalize=False, _default_locale=None):
    return phpy.call('locale_lookup', _language_tag, _locale, _canonicalize, _default_locale)


def locale_accept_from_http(_header):
    return phpy.call('locale_accept_from_http', _header)


def msgfmt_create(_locale, _pattern):
    return phpy.call('msgfmt_create', _locale, _pattern)


def msgfmt_format(_formatter, _values):
    return phpy.call('msgfmt_format', _formatter, _values)


def msgfmt_format_message(_locale, _pattern, _values):
    return phpy.call('msgfmt_format_message', _locale, _pattern, _values)


def msgfmt_parse(_formatter, _string):
    return phpy.call('msgfmt_parse', _formatter, _string)


def msgfmt_parse_message(_locale, _pattern, _message):
    return phpy.call('msgfmt_parse_message', _locale, _pattern, _message)


def msgfmt_set_pattern(_formatter, _pattern):
    return phpy.call('msgfmt_set_pattern', _formatter, _pattern)


def msgfmt_get_pattern(_formatter):
    return phpy.call('msgfmt_get_pattern', _formatter)


def msgfmt_get_locale(_formatter):
    return phpy.call('msgfmt_get_locale', _formatter)


def msgfmt_get_error_code(_formatter):
    return phpy.call('msgfmt_get_error_code', _formatter)


def msgfmt_get_error_message(_formatter):
    return phpy.call('msgfmt_get_error_message', _formatter)


def normalizer_normalize(_string, _form=16):
    return phpy.call('normalizer_normalize', _string, _form)


def normalizer_is_normalized(_string, _form=16):
    return phpy.call('normalizer_is_normalized', _string, _form)


def normalizer_get_raw_decomposition(_string, _form=16):
    return phpy.call('normalizer_get_raw_decomposition', _string, _form)


def resourcebundle_create(_locale, _bundle, _fallback=True):
    return phpy.call('resourcebundle_create', _locale, _bundle, _fallback)


def resourcebundle_get(_bundle, _index, _fallback=True):
    return phpy.call('resourcebundle_get', _bundle, _index, _fallback)


def resourcebundle_count(_bundle):
    return phpy.call('resourcebundle_count', _bundle)


def resourcebundle_locales(_bundle):
    return phpy.call('resourcebundle_locales', _bundle)


def resourcebundle_get_error_code(_bundle):
    return phpy.call('resourcebundle_get_error_code', _bundle)


def resourcebundle_get_error_message(_bundle):
    return phpy.call('resourcebundle_get_error_message', _bundle)


def intltz_count_equivalent_ids(_timezone_id):
    return phpy.call('intltz_count_equivalent_ids', _timezone_id)


def intltz_create_default():
    return phpy.call('intltz_create_default', )


def intltz_create_enumeration(_country_or_raw_offset=None):
    return phpy.call('intltz_create_enumeration', _country_or_raw_offset)


def intltz_create_time_zone(_timezone_id):
    return phpy.call('intltz_create_time_zone', _timezone_id)


def intltz_create_time_zone_id_enumeration(_type, _region=None, _raw_offset=None):
    return phpy.call('intltz_create_time_zone_id_enumeration', _type, _region, _raw_offset)


def intltz_from_date_time_zone(_timezone):
    return phpy.call('intltz_from_date_time_zone', _timezone)


def intltz_get_canonical_id(_timezone_id, _is_system_id=None):
    return phpy.call('intltz_get_canonical_id', _timezone_id, _is_system_id)


def intltz_get_display_name(_timezone, _dst=False, _style=2, _locale=None):
    return phpy.call('intltz_get_display_name', _timezone, _dst, _style, _locale)


def intltz_get_dst_savings(_timezone):
    return phpy.call('intltz_get_dst_savings', _timezone)


def intltz_get_equivalent_id(_timezone_id, _offset):
    return phpy.call('intltz_get_equivalent_id', _timezone_id, _offset)


def intltz_get_error_code(_timezone):
    return phpy.call('intltz_get_error_code', _timezone)


def intltz_get_error_message(_timezone):
    return phpy.call('intltz_get_error_message', _timezone)


def intltz_get_gmt():
    return phpy.call('intltz_get_gmt', )


def intltz_get_id(_timezone):
    return phpy.call('intltz_get_id', _timezone)


def intltz_get_offset(_timezone, _timestamp, _local, _raw_offset, _dst_offset):
    return phpy.call('intltz_get_offset', _timezone, _timestamp, _local, _raw_offset, _dst_offset)


def intltz_get_raw_offset(_timezone):
    return phpy.call('intltz_get_raw_offset', _timezone)


def intltz_get_region(_timezone_id):
    return phpy.call('intltz_get_region', _timezone_id)


def intltz_get_tz_data_version():
    return phpy.call('intltz_get_tz_data_version', )


def intltz_get_unknown():
    return phpy.call('intltz_get_unknown', )


def intltz_get_windows_id(_timezone_id):
    return phpy.call('intltz_get_windows_id', _timezone_id)


def intltz_get_id_for_windows_id(_timezone_id, _region=None):
    return phpy.call('intltz_get_id_for_windows_id', _timezone_id, _region)


def intltz_has_same_rules(_timezone, _other):
    return phpy.call('intltz_has_same_rules', _timezone, _other)


def intltz_to_date_time_zone(_timezone):
    return phpy.call('intltz_to_date_time_zone', _timezone)


def intltz_use_daylight_time(_timezone):
    return phpy.call('intltz_use_daylight_time', _timezone)


def transliterator_create(_id, _direction=0):
    return phpy.call('transliterator_create', _id, _direction)


def transliterator_create_from_rules(_rules, _direction=0):
    return phpy.call('transliterator_create_from_rules', _rules, _direction)


def transliterator_list_ids():
    return phpy.call('transliterator_list_ids', )


def transliterator_create_inverse(_transliterator):
    return phpy.call('transliterator_create_inverse', _transliterator)


def transliterator_transliterate(_transliterator, _string, _start=0, _end=-1):
    return phpy.call('transliterator_transliterate', _transliterator, _string, _start, _end)


def transliterator_get_error_code(_transliterator):
    return phpy.call('transliterator_get_error_code', _transliterator)


def transliterator_get_error_message(_transliterator):
    return phpy.call('transliterator_get_error_message', _transliterator)




class Collator():
    DEFAULT_VALUE = -1
    PRIMARY = 0
    SECONDARY = 1
    TERTIARY = 2
    DEFAULT_STRENGTH = 2
    QUATERNARY = 3
    IDENTICAL = 15
    OFF = 16
    ON = 17
    SHIFTED = 20
    NON_IGNORABLE = 21
    LOWER_FIRST = 24
    UPPER_FIRST = 25
    FRENCH_COLLATION = 0
    ALTERNATE_HANDLING = 1
    CASE_FIRST = 2
    CASE_LEVEL = 3
    NORMALIZATION_MODE = 4
    STRENGTH = 5
    HIRAGANA_QUATERNARY_MODE = 6
    NUMERIC_COLLATION = 7
    SORT_REGULAR = 0
    SORT_STRING = 1
    SORT_NUMERIC = 2

    def __init__(self, _locale):
        self.__this = phpy.Object(f'Collator', _locale)

    def create(_locale):
        return phpy.call(f"Collator::create", _locale)

    def compare(self, _string1, _string2):
        return self.__this.call(f"compare", _string1, _string2)

    def sort(self, _array, _flags=0):
        return self.__this.call(f"sort", _array, _flags)

    def sortWithSortKeys(self, _array):
        return self.__this.call(f"sortWithSortKeys", _array)

    def asort(self, _array, _flags=0):
        return self.__this.call(f"asort", _array, _flags)

    def getAttribute(self, _attribute):
        return self.__this.call(f"getAttribute", _attribute)

    def setAttribute(self, _attribute, _value):
        return self.__this.call(f"setAttribute", _attribute, _value)

    def getStrength(self):
        return self.__this.call(f"getStrength", )

    def setStrength(self, _strength):
        return self.__this.call(f"setStrength", _strength)

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getSortKey(self, _string):
        return self.__this.call(f"getSortKey", _string)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class NumberFormatter():
    PATTERN_DECIMAL = 0
    DECIMAL = 1
    CURRENCY = 2
    PERCENT = 3
    SCIENTIFIC = 4
    SPELLOUT = 5
    ORDINAL = 6
    DURATION = 7
    PATTERN_RULEBASED = 9
    IGNORE = 0
    CURRENCY_ACCOUNTING = 12
    DEFAULT_STYLE = 1
    ROUND_CEILING = 0
    ROUND_FLOOR = 1
    ROUND_DOWN = 2
    ROUND_UP = 3
    ROUND_HALFEVEN = 4
    ROUND_HALFDOWN = 5
    ROUND_HALFUP = 6
    PAD_BEFORE_PREFIX = 0
    PAD_AFTER_PREFIX = 1
    PAD_BEFORE_SUFFIX = 2
    PAD_AFTER_SUFFIX = 3
    PARSE_INT_ONLY = 0
    GROUPING_USED = 1
    DECIMAL_ALWAYS_SHOWN = 2
    MAX_INTEGER_DIGITS = 3
    MIN_INTEGER_DIGITS = 4
    INTEGER_DIGITS = 5
    MAX_FRACTION_DIGITS = 6
    MIN_FRACTION_DIGITS = 7
    FRACTION_DIGITS = 8
    MULTIPLIER = 9
    GROUPING_SIZE = 10
    ROUNDING_MODE = 11
    ROUNDING_INCREMENT = 12
    FORMAT_WIDTH = 13
    PADDING_POSITION = 14
    SECONDARY_GROUPING_SIZE = 15
    SIGNIFICANT_DIGITS_USED = 16
    MIN_SIGNIFICANT_DIGITS = 17
    MAX_SIGNIFICANT_DIGITS = 18
    LENIENT_PARSE = 19
    POSITIVE_PREFIX = 0
    POSITIVE_SUFFIX = 1
    NEGATIVE_PREFIX = 2
    NEGATIVE_SUFFIX = 3
    PADDING_CHARACTER = 4
    CURRENCY_CODE = 5
    DEFAULT_RULESET = 6
    PUBLIC_RULESETS = 7
    DECIMAL_SEPARATOR_SYMBOL = 0
    GROUPING_SEPARATOR_SYMBOL = 1
    PATTERN_SEPARATOR_SYMBOL = 2
    PERCENT_SYMBOL = 3
    ZERO_DIGIT_SYMBOL = 4
    DIGIT_SYMBOL = 5
    MINUS_SIGN_SYMBOL = 6
    PLUS_SIGN_SYMBOL = 7
    CURRENCY_SYMBOL = 8
    INTL_CURRENCY_SYMBOL = 9
    MONETARY_SEPARATOR_SYMBOL = 10
    EXPONENTIAL_SYMBOL = 11
    PERMILL_SYMBOL = 12
    PAD_ESCAPE_SYMBOL = 13
    INFINITY_SYMBOL = 14
    NAN_SYMBOL = 15
    SIGNIFICANT_DIGIT_SYMBOL = 16
    MONETARY_GROUPING_SEPARATOR_SYMBOL = 17
    TYPE_DEFAULT = 0
    TYPE_INT32 = 1
    TYPE_INT64 = 2
    TYPE_DOUBLE = 3
    TYPE_CURRENCY = 4

    def __init__(self, _locale, _style, _pattern=None):
        self.__this = phpy.Object(f'NumberFormatter', _locale, _style, _pattern)

    def create(_locale, _style, _pattern=None):
        return phpy.call(f"NumberFormatter::create", _locale, _style, _pattern)

    def format(self, _num, _type=0):
        return self.__this.call(f"format", _num, _type)

    def parse(self, _string, _type=3, _offset=None):
        return self.__this.call(f"parse", _string, _type, _offset)

    def formatCurrency(self, _amount, _currency):
        return self.__this.call(f"formatCurrency", _amount, _currency)

    def parseCurrency(self, _string, _currency, _offset=None):
        return self.__this.call(f"parseCurrency", _string, _currency, _offset)

    def setAttribute(self, _attribute, _value):
        return self.__this.call(f"setAttribute", _attribute, _value)

    def getAttribute(self, _attribute):
        return self.__this.call(f"getAttribute", _attribute)

    def setTextAttribute(self, _attribute, _value):
        return self.__this.call(f"setTextAttribute", _attribute, _value)

    def getTextAttribute(self, _attribute):
        return self.__this.call(f"getTextAttribute", _attribute)

    def setSymbol(self, _symbol, _value):
        return self.__this.call(f"setSymbol", _symbol, _value)

    def getSymbol(self, _symbol):
        return self.__this.call(f"getSymbol", _symbol)

    def setPattern(self, _pattern):
        return self.__this.call(f"setPattern", _pattern)

    def getPattern(self):
        return self.__this.call(f"getPattern", )

    def getLocale(self, _type=0):
        return self.__this.call(f"getLocale", _type)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Normalizer():
    FORM_D = 4
    NFD = 4
    FORM_KD = 8
    NFKD = 8
    FORM_C = 16
    NFC = 16
    FORM_KC = 32
    NFKC = 32
    FORM_KC_CF = 48
    NFKC_CF = 48

    def normalize(_string, _form=16):
        return phpy.call(f"Normalizer::normalize", _string, _form)

    def isNormalized(_string, _form=16):
        return phpy.call(f"Normalizer::isNormalized", _string, _form)

    def getRawDecomposition(_string, _form=16):
        return phpy.call(f"Normalizer::getRawDecomposition", _string, _form)

    def __init__(self):
        self.__this = phpy.Object(f'Normalizer')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Locale():
    ACTUAL_LOCALE = 0
    VALID_LOCALE = 1
    DEFAULT_LOCALE = None
    LANG_TAG = "language"
    EXTLANG_TAG = "extlang"
    SCRIPT_TAG = "script"
    REGION_TAG = "region"
    VARIANT_TAG = "variant"
    GRANDFATHERED_LANG_TAG = "grandfathered"
    PRIVATE_TAG = "private"

    def getDefault():
        return phpy.call(f"Locale::getDefault", )

    def setDefault(_locale):
        return phpy.call(f"Locale::setDefault", _locale)

    def getPrimaryLanguage(_locale):
        return phpy.call(f"Locale::getPrimaryLanguage", _locale)

    def getScript(_locale):
        return phpy.call(f"Locale::getScript", _locale)

    def getRegion(_locale):
        return phpy.call(f"Locale::getRegion", _locale)

    def getKeywords(_locale):
        return phpy.call(f"Locale::getKeywords", _locale)

    def getDisplayScript(_locale, _display_locale=None):
        return phpy.call(f"Locale::getDisplayScript", _locale, _display_locale)

    def getDisplayRegion(_locale, _display_locale=None):
        return phpy.call(f"Locale::getDisplayRegion", _locale, _display_locale)

    def getDisplayName(_locale, _display_locale=None):
        return phpy.call(f"Locale::getDisplayName", _locale, _display_locale)

    def getDisplayLanguage(_locale, _display_locale=None):
        return phpy.call(f"Locale::getDisplayLanguage", _locale, _display_locale)

    def getDisplayVariant(_locale, _display_locale=None):
        return phpy.call(f"Locale::getDisplayVariant", _locale, _display_locale)

    def composeLocale(_subtags):
        return phpy.call(f"Locale::composeLocale", _subtags)

    def parseLocale(_locale):
        return phpy.call(f"Locale::parseLocale", _locale)

    def getAllVariants(_locale):
        return phpy.call(f"Locale::getAllVariants", _locale)

    def filterMatches(_language_tag, _locale, _canonicalize=False):
        return phpy.call(f"Locale::filterMatches", _language_tag, _locale, _canonicalize)

    def lookup(_language_tag, _locale, _canonicalize=False, _default_locale=None):
        return phpy.call(f"Locale::lookup", _language_tag, _locale, _canonicalize, _default_locale)

    def canonicalize(_locale):
        return phpy.call(f"Locale::canonicalize", _locale)

    def acceptFromHttp(_header):
        return phpy.call(f"Locale::acceptFromHttp", _header)

    def __init__(self):
        self.__this = phpy.Object(f'Locale')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class MessageFormatter():

    def __init__(self, _locale, _pattern):
        self.__this = phpy.Object(f'MessageFormatter', _locale, _pattern)

    def create(_locale, _pattern):
        return phpy.call(f"MessageFormatter::create", _locale, _pattern)

    def format(self, _values):
        return self.__this.call(f"format", _values)

    def formatMessage(_locale, _pattern, _values):
        return phpy.call(f"MessageFormatter::formatMessage", _locale, _pattern, _values)

    def parse(self, _string):
        return self.__this.call(f"parse", _string)

    def parseMessage(_locale, _pattern, _message):
        return phpy.call(f"MessageFormatter::parseMessage", _locale, _pattern, _message)

    def setPattern(self, _pattern):
        return self.__this.call(f"setPattern", _pattern)

    def getPattern(self):
        return self.__this.call(f"getPattern", )

    def getLocale(self):
        return self.__this.call(f"getLocale", )

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlDateFormatter():
    FULL = 0
    LONG = 1
    MEDIUM = 2
    SHORT = 3
    NONE = -1
    RELATIVE_FULL = 128
    RELATIVE_LONG = 129
    RELATIVE_MEDIUM = 130
    RELATIVE_SHORT = 131
    GREGORIAN = 1
    TRADITIONAL = 0

    def __init__(self, _locale, _date_type=0, _time_type=0, _timezone=None, _calendar=None, _pattern=None):
        self.__this = phpy.Object(f'IntlDateFormatter', _locale, _date_type, _time_type, _timezone, _calendar, _pattern)

    def create(_locale, _date_type=0, _time_type=0, _timezone=None, _calendar=None, _pattern=None):
        return phpy.call(f"IntlDateFormatter::create", _locale, _date_type, _time_type, _timezone, _calendar, _pattern)

    def getDateType(self):
        return self.__this.call(f"getDateType", )

    def getTimeType(self):
        return self.__this.call(f"getTimeType", )

    def getCalendar(self):
        return self.__this.call(f"getCalendar", )

    def setCalendar(self, _calendar):
        return self.__this.call(f"setCalendar", _calendar)

    def getTimeZoneId(self):
        return self.__this.call(f"getTimeZoneId", )

    def getCalendarObject(self):
        return self.__this.call(f"getCalendarObject", )

    def getTimeZone(self):
        return self.__this.call(f"getTimeZone", )

    def setTimeZone(self, _timezone):
        return self.__this.call(f"setTimeZone", _timezone)

    def setPattern(self, _pattern):
        return self.__this.call(f"setPattern", _pattern)

    def getPattern(self):
        return self.__this.call(f"getPattern", )

    def getLocale(self, _type=0):
        return self.__this.call(f"getLocale", _type)

    def setLenient(self, _lenient):
        return self.__this.call(f"setLenient", _lenient)

    def isLenient(self):
        return self.__this.call(f"isLenient", )

    def format(self, _datetime):
        return self.__this.call(f"format", _datetime)

    def formatObject(_datetime, _format=None, _locale=None):
        return phpy.call(f"IntlDateFormatter::formatObject", _datetime, _format, _locale)

    def parse(self, _string, _offset=None):
        return self.__this.call(f"parse", _string, _offset)

    def localtime(self, _string, _offset=None):
        return self.__this.call(f"localtime", _string, _offset)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlDatePatternGenerator():

    def __init__(self, _locale=None):
        self.__this = phpy.Object(f'IntlDatePatternGenerator', _locale)

    def create(_locale=None):
        return phpy.call(f"IntlDatePatternGenerator::create", _locale)

    def getBestPattern(self, _skeleton):
        return self.__this.call(f"getBestPattern", _skeleton)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ResourceBundle():

    def __init__(self, _locale, _bundle, _fallback=True):
        self.__this = phpy.Object(f'ResourceBundle', _locale, _bundle, _fallback)

    def create(_locale, _bundle, _fallback=True):
        return phpy.call(f"ResourceBundle::create", _locale, _bundle, _fallback)

    def get(self, _index, _fallback=True):
        return self.__this.call(f"get", _index, _fallback)

    def count(self):
        return self.__this.call(f"count", )

    def getLocales(_bundle):
        return phpy.call(f"ResourceBundle::getLocales", _bundle)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Transliterator():
    FORWARD = 0
    REVERSE = 1

    def create(_id, _direction=0):
        return phpy.call(f"Transliterator::create", _id, _direction)

    def createFromRules(_rules, _direction=0):
        return phpy.call(f"Transliterator::createFromRules", _rules, _direction)

    def createInverse(self):
        return self.__this.call(f"createInverse", )

    def listIDs():
        return phpy.call(f"Transliterator::listIDs", )

    def transliterate(self, _string, _start=0, _end=-1):
        return self.__this.call(f"transliterate", _string, _start, _end)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def __init__(self):
        self.__this = phpy.Object(f'Transliterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlTimeZone():
    DISPLAY_SHORT = 1
    DISPLAY_LONG = 2
    DISPLAY_SHORT_GENERIC = 3
    DISPLAY_LONG_GENERIC = 4
    DISPLAY_SHORT_GMT = 5
    DISPLAY_LONG_GMT = 6
    DISPLAY_SHORT_COMMONLY_USED = 7
    DISPLAY_GENERIC_LOCATION = 8
    TYPE_ANY = 0
    TYPE_CANONICAL = 1
    TYPE_CANONICAL_LOCATION = 2

    def countEquivalentIDs(_timezone_id):
        return phpy.call(f"IntlTimeZone::countEquivalentIDs", _timezone_id)

    def createDefault():
        return phpy.call(f"IntlTimeZone::createDefault", )

    def createEnumeration(_country_or_raw_offset=None):
        return phpy.call(f"IntlTimeZone::createEnumeration", _country_or_raw_offset)

    def createTimeZone(_timezone_id):
        return phpy.call(f"IntlTimeZone::createTimeZone", _timezone_id)

    def createTimeZoneIDEnumeration(_type, _region=None, _raw_offset=None):
        return phpy.call(f"IntlTimeZone::createTimeZoneIDEnumeration", _type, _region, _raw_offset)

    def fromDateTimeZone(_timezone):
        return phpy.call(f"IntlTimeZone::fromDateTimeZone", _timezone)

    def getCanonicalID(_timezone_id, _is_system_id=None):
        return phpy.call(f"IntlTimeZone::getCanonicalID", _timezone_id, _is_system_id)

    def getDisplayName(self, _dst=False, _style=2, _locale=None):
        return self.__this.call(f"getDisplayName", _dst, _style, _locale)

    def getDSTSavings(self):
        return self.__this.call(f"getDSTSavings", )

    def getEquivalentID(_timezone_id, _offset):
        return phpy.call(f"IntlTimeZone::getEquivalentID", _timezone_id, _offset)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getGMT():
        return phpy.call(f"IntlTimeZone::getGMT", )

    def getID(self):
        return self.__this.call(f"getID", )

    def getOffset(self, _timestamp, _local, _raw_offset, _dst_offset):
        return self.__this.call(f"getOffset", _timestamp, _local, _raw_offset, _dst_offset)

    def getRawOffset(self):
        return self.__this.call(f"getRawOffset", )

    def getRegion(_timezone_id):
        return phpy.call(f"IntlTimeZone::getRegion", _timezone_id)

    def getTZDataVersion():
        return phpy.call(f"IntlTimeZone::getTZDataVersion", )

    def getUnknown():
        return phpy.call(f"IntlTimeZone::getUnknown", )

    def getWindowsID(_timezone_id):
        return phpy.call(f"IntlTimeZone::getWindowsID", _timezone_id)

    def getIDForWindowsID(_timezone_id, _region=None):
        return phpy.call(f"IntlTimeZone::getIDForWindowsID", _timezone_id, _region)

    def hasSameRules(self, _other):
        return self.__this.call(f"hasSameRules", _other)

    def toDateTimeZone(self):
        return self.__this.call(f"toDateTimeZone", )

    def useDaylightTime(self):
        return self.__this.call(f"useDaylightTime", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlTimeZone')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlCalendar():
    FIELD_ERA = 0
    FIELD_YEAR = 1
    FIELD_MONTH = 2
    FIELD_WEEK_OF_YEAR = 3
    FIELD_WEEK_OF_MONTH = 4
    FIELD_DATE = 5
    FIELD_DAY_OF_YEAR = 6
    FIELD_DAY_OF_WEEK = 7
    FIELD_DAY_OF_WEEK_IN_MONTH = 8
    FIELD_AM_PM = 9
    FIELD_HOUR = 10
    FIELD_HOUR_OF_DAY = 11
    FIELD_MINUTE = 12
    FIELD_SECOND = 13
    FIELD_MILLISECOND = 14
    FIELD_ZONE_OFFSET = 15
    FIELD_DST_OFFSET = 16
    FIELD_YEAR_WOY = 17
    FIELD_DOW_LOCAL = 18
    FIELD_EXTENDED_YEAR = 19
    FIELD_JULIAN_DAY = 20
    FIELD_MILLISECONDS_IN_DAY = 21
    FIELD_IS_LEAP_MONTH = 22
    FIELD_FIELD_COUNT = 23
    FIELD_DAY_OF_MONTH = 5
    DOW_SUNDAY = 1
    DOW_MONDAY = 2
    DOW_TUESDAY = 3
    DOW_WEDNESDAY = 4
    DOW_THURSDAY = 5
    DOW_FRIDAY = 6
    DOW_SATURDAY = 7
    DOW_TYPE_WEEKDAY = 0
    DOW_TYPE_WEEKEND = 1
    DOW_TYPE_WEEKEND_OFFSET = 2
    DOW_TYPE_WEEKEND_CEASE = 3
    WALLTIME_FIRST = 1
    WALLTIME_LAST = 0
    WALLTIME_NEXT_VALID = 2

    def createInstance(_timezone=None, _locale=None):
        return phpy.call(f"IntlCalendar::createInstance", _timezone, _locale)

    def equals(self, _other):
        return self.__this.call(f"equals", _other)

    def fieldDifference(self, _timestamp, _field):
        return self.__this.call(f"fieldDifference", _timestamp, _field)

    def add(self, _field, _value):
        return self.__this.call(f"add", _field, _value)

    def after(self, _other):
        return self.__this.call(f"after", _other)

    def before(self, _other):
        return self.__this.call(f"before", _other)

    def clear(self, _field=None):
        return self.__this.call(f"clear", _field)

    def fromDateTime(_datetime, _locale=None):
        return phpy.call(f"IntlCalendar::fromDateTime", _datetime, _locale)

    def get(self, _field):
        return self.__this.call(f"get", _field)

    def getActualMaximum(self, _field):
        return self.__this.call(f"getActualMaximum", _field)

    def getActualMinimum(self, _field):
        return self.__this.call(f"getActualMinimum", _field)

    def getAvailableLocales():
        return phpy.call(f"IntlCalendar::getAvailableLocales", )

    def getDayOfWeekType(self, _day_of_week):
        return self.__this.call(f"getDayOfWeekType", _day_of_week)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getFirstDayOfWeek(self):
        return self.__this.call(f"getFirstDayOfWeek", )

    def getGreatestMinimum(self, _field):
        return self.__this.call(f"getGreatestMinimum", _field)

    def getKeywordValuesForLocale(_keyword, _locale, _only_common):
        return phpy.call(f"IntlCalendar::getKeywordValuesForLocale", _keyword, _locale, _only_common)

    def getLeastMaximum(self, _field):
        return self.__this.call(f"getLeastMaximum", _field)

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getMaximum(self, _field):
        return self.__this.call(f"getMaximum", _field)

    def getMinimalDaysInFirstWeek(self):
        return self.__this.call(f"getMinimalDaysInFirstWeek", )

    def setMinimalDaysInFirstWeek(self, _days):
        return self.__this.call(f"setMinimalDaysInFirstWeek", _days)

    def getMinimum(self, _field):
        return self.__this.call(f"getMinimum", _field)

    def getNow():
        return phpy.call(f"IntlCalendar::getNow", )

    def getRepeatedWallTimeOption(self):
        return self.__this.call(f"getRepeatedWallTimeOption", )

    def getSkippedWallTimeOption(self):
        return self.__this.call(f"getSkippedWallTimeOption", )

    def getTime(self):
        return self.__this.call(f"getTime", )

    def getTimeZone(self):
        return self.__this.call(f"getTimeZone", )

    def getType(self):
        return self.__this.call(f"getType", )

    def getWeekendTransition(self, _day_of_week):
        return self.__this.call(f"getWeekendTransition", _day_of_week)

    def inDaylightTime(self):
        return self.__this.call(f"inDaylightTime", )

    def isEquivalentTo(self, _other):
        return self.__this.call(f"isEquivalentTo", _other)

    def isLenient(self):
        return self.__this.call(f"isLenient", )

    def isWeekend(self, _timestamp=None):
        return self.__this.call(f"isWeekend", _timestamp)

    def roll(self, _field, _value):
        return self.__this.call(f"roll", _field, _value)

    def isSet(self, _field):
        return self.__this.call(f"isSet", _field)

    def set(self, _year, _month, _day_of_month=None, _hour=None, _minute=None, _second=None):
        return self.__this.call(f"set", _year, _month, _day_of_month, _hour, _minute, _second)

    def setFirstDayOfWeek(self, _day_of_week):
        return self.__this.call(f"setFirstDayOfWeek", _day_of_week)

    def setLenient(self, _lenient):
        return self.__this.call(f"setLenient", _lenient)

    def setRepeatedWallTimeOption(self, _option):
        return self.__this.call(f"setRepeatedWallTimeOption", _option)

    def setSkippedWallTimeOption(self, _option):
        return self.__this.call(f"setSkippedWallTimeOption", _option)

    def setTime(self, _timestamp):
        return self.__this.call(f"setTime", _timestamp)

    def setTimeZone(self, _timezone):
        return self.__this.call(f"setTimeZone", _timezone)

    def toDateTime(self):
        return self.__this.call(f"toDateTime", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlCalendar')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlGregorianCalendar():
    FIELD_ERA = 0
    FIELD_YEAR = 1
    FIELD_MONTH = 2
    FIELD_WEEK_OF_YEAR = 3
    FIELD_WEEK_OF_MONTH = 4
    FIELD_DATE = 5
    FIELD_DAY_OF_YEAR = 6
    FIELD_DAY_OF_WEEK = 7
    FIELD_DAY_OF_WEEK_IN_MONTH = 8
    FIELD_AM_PM = 9
    FIELD_HOUR = 10
    FIELD_HOUR_OF_DAY = 11
    FIELD_MINUTE = 12
    FIELD_SECOND = 13
    FIELD_MILLISECOND = 14
    FIELD_ZONE_OFFSET = 15
    FIELD_DST_OFFSET = 16
    FIELD_YEAR_WOY = 17
    FIELD_DOW_LOCAL = 18
    FIELD_EXTENDED_YEAR = 19
    FIELD_JULIAN_DAY = 20
    FIELD_MILLISECONDS_IN_DAY = 21
    FIELD_IS_LEAP_MONTH = 22
    FIELD_FIELD_COUNT = 23
    FIELD_DAY_OF_MONTH = 5
    DOW_SUNDAY = 1
    DOW_MONDAY = 2
    DOW_TUESDAY = 3
    DOW_WEDNESDAY = 4
    DOW_THURSDAY = 5
    DOW_FRIDAY = 6
    DOW_SATURDAY = 7
    DOW_TYPE_WEEKDAY = 0
    DOW_TYPE_WEEKEND = 1
    DOW_TYPE_WEEKEND_OFFSET = 2
    DOW_TYPE_WEEKEND_CEASE = 3
    WALLTIME_FIRST = 1
    WALLTIME_LAST = 0
    WALLTIME_NEXT_VALID = 2

    def __init__(self, _timezone_or_year=None, _locale_or_month=None, _day=None, _hour=None, _minute=None, _second=None):
        self.__this = phpy.Object(f'IntlGregorianCalendar', _timezone_or_year, _locale_or_month, _day, _hour, _minute, _second)

    def setGregorianChange(self, _timestamp):
        return self.__this.call(f"setGregorianChange", _timestamp)

    def getGregorianChange(self):
        return self.__this.call(f"getGregorianChange", )

    def isLeapYear(self, _year):
        return self.__this.call(f"isLeapYear", _year)

    def createInstance(_timezone=None, _locale=None):
        return phpy.call(f"IntlGregorianCalendar::createInstance", _timezone, _locale)

    def equals(self, _other):
        return self.__this.call(f"equals", _other)

    def fieldDifference(self, _timestamp, _field):
        return self.__this.call(f"fieldDifference", _timestamp, _field)

    def add(self, _field, _value):
        return self.__this.call(f"add", _field, _value)

    def after(self, _other):
        return self.__this.call(f"after", _other)

    def before(self, _other):
        return self.__this.call(f"before", _other)

    def clear(self, _field=None):
        return self.__this.call(f"clear", _field)

    def fromDateTime(_datetime, _locale=None):
        return phpy.call(f"IntlGregorianCalendar::fromDateTime", _datetime, _locale)

    def get(self, _field):
        return self.__this.call(f"get", _field)

    def getActualMaximum(self, _field):
        return self.__this.call(f"getActualMaximum", _field)

    def getActualMinimum(self, _field):
        return self.__this.call(f"getActualMinimum", _field)

    def getAvailableLocales():
        return phpy.call(f"IntlGregorianCalendar::getAvailableLocales", )

    def getDayOfWeekType(self, _day_of_week):
        return self.__this.call(f"getDayOfWeekType", _day_of_week)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getFirstDayOfWeek(self):
        return self.__this.call(f"getFirstDayOfWeek", )

    def getGreatestMinimum(self, _field):
        return self.__this.call(f"getGreatestMinimum", _field)

    def getKeywordValuesForLocale(_keyword, _locale, _only_common):
        return phpy.call(f"IntlGregorianCalendar::getKeywordValuesForLocale", _keyword, _locale, _only_common)

    def getLeastMaximum(self, _field):
        return self.__this.call(f"getLeastMaximum", _field)

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getMaximum(self, _field):
        return self.__this.call(f"getMaximum", _field)

    def getMinimalDaysInFirstWeek(self):
        return self.__this.call(f"getMinimalDaysInFirstWeek", )

    def setMinimalDaysInFirstWeek(self, _days):
        return self.__this.call(f"setMinimalDaysInFirstWeek", _days)

    def getMinimum(self, _field):
        return self.__this.call(f"getMinimum", _field)

    def getNow():
        return phpy.call(f"IntlGregorianCalendar::getNow", )

    def getRepeatedWallTimeOption(self):
        return self.__this.call(f"getRepeatedWallTimeOption", )

    def getSkippedWallTimeOption(self):
        return self.__this.call(f"getSkippedWallTimeOption", )

    def getTime(self):
        return self.__this.call(f"getTime", )

    def getTimeZone(self):
        return self.__this.call(f"getTimeZone", )

    def getType(self):
        return self.__this.call(f"getType", )

    def getWeekendTransition(self, _day_of_week):
        return self.__this.call(f"getWeekendTransition", _day_of_week)

    def inDaylightTime(self):
        return self.__this.call(f"inDaylightTime", )

    def isEquivalentTo(self, _other):
        return self.__this.call(f"isEquivalentTo", _other)

    def isLenient(self):
        return self.__this.call(f"isLenient", )

    def isWeekend(self, _timestamp=None):
        return self.__this.call(f"isWeekend", _timestamp)

    def roll(self, _field, _value):
        return self.__this.call(f"roll", _field, _value)

    def isSet(self, _field):
        return self.__this.call(f"isSet", _field)

    def set(self, _year, _month, _day_of_month=None, _hour=None, _minute=None, _second=None):
        return self.__this.call(f"set", _year, _month, _day_of_month, _hour, _minute, _second)

    def setFirstDayOfWeek(self, _day_of_week):
        return self.__this.call(f"setFirstDayOfWeek", _day_of_week)

    def setLenient(self, _lenient):
        return self.__this.call(f"setLenient", _lenient)

    def setRepeatedWallTimeOption(self, _option):
        return self.__this.call(f"setRepeatedWallTimeOption", _option)

    def setSkippedWallTimeOption(self, _option):
        return self.__this.call(f"setSkippedWallTimeOption", _option)

    def setTime(self, _timestamp):
        return self.__this.call(f"setTime", _timestamp)

    def setTimeZone(self, _timezone):
        return self.__this.call(f"setTimeZone", _timezone)

    def toDateTime(self):
        return self.__this.call(f"toDateTime", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Spoofchecker():
    SINGLE_SCRIPT_CONFUSABLE = 1
    MIXED_SCRIPT_CONFUSABLE = 2
    WHOLE_SCRIPT_CONFUSABLE = 4
    ANY_CASE = 8
    SINGLE_SCRIPT = 16
    INVISIBLE = 32
    CHAR_LIMIT = 64
    ASCII = 268435456
    HIGHLY_RESTRICTIVE = 805306368
    MODERATELY_RESTRICTIVE = 1073741824
    MINIMALLY_RESTRICTIVE = 1342177280
    UNRESTRICTIVE = 1610612736
    SINGLE_SCRIPT_RESTRICTIVE = 536870912

    def __init__(self):
        self.__this = phpy.Object(f'Spoofchecker', )

    def isSuspicious(self, _string, _error_code=None):
        return self.__this.call(f"isSuspicious", _string, _error_code)

    def areConfusable(self, _string1, _string2, _error_code=None):
        return self.__this.call(f"areConfusable", _string1, _string2, _error_code)

    def setAllowedLocales(self, _locales):
        return self.__this.call(f"setAllowedLocales", _locales)

    def setChecks(self, _checks):
        return self.__this.call(f"setChecks", _checks)

    def setRestrictionLevel(self, _level):
        return self.__this.call(f"setRestrictionLevel", _level)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'IntlException', _message, _code, _previous)

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

class IntlIterator():

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlBreakIterator():
    DONE = -1
    WORD_NONE = 0
    WORD_NONE_LIMIT = 100
    WORD_NUMBER = 100
    WORD_NUMBER_LIMIT = 200
    WORD_LETTER = 200
    WORD_LETTER_LIMIT = 300
    WORD_KANA = 300
    WORD_KANA_LIMIT = 400
    WORD_IDEO = 400
    WORD_IDEO_LIMIT = 500
    LINE_SOFT = 0
    LINE_SOFT_LIMIT = 100
    LINE_HARD = 100
    LINE_HARD_LIMIT = 200
    SENTENCE_TERM = 0
    SENTENCE_TERM_LIMIT = 100
    SENTENCE_SEP = 100
    SENTENCE_SEP_LIMIT = 200

    def createCharacterInstance(_locale=None):
        return phpy.call(f"IntlBreakIterator::createCharacterInstance", _locale)

    def createCodePointInstance():
        return phpy.call(f"IntlBreakIterator::createCodePointInstance", )

    def createLineInstance(_locale=None):
        return phpy.call(f"IntlBreakIterator::createLineInstance", _locale)

    def createSentenceInstance(_locale=None):
        return phpy.call(f"IntlBreakIterator::createSentenceInstance", _locale)

    def createTitleInstance(_locale=None):
        return phpy.call(f"IntlBreakIterator::createTitleInstance", _locale)

    def createWordInstance(_locale=None):
        return phpy.call(f"IntlBreakIterator::createWordInstance", _locale)

    def current(self):
        return self.__this.call(f"current", )

    def first(self):
        return self.__this.call(f"first", )

    def following(self, _offset):
        return self.__this.call(f"following", _offset)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getPartsIterator(self, _type=0):
        return self.__this.call(f"getPartsIterator", _type)

    def getText(self):
        return self.__this.call(f"getText", )

    def isBoundary(self, _offset):
        return self.__this.call(f"isBoundary", _offset)

    def last(self):
        return self.__this.call(f"last", )

    def next(self, _offset=None):
        return self.__this.call(f"next", _offset)

    def preceding(self, _offset):
        return self.__this.call(f"preceding", _offset)

    def previous(self):
        return self.__this.call(f"previous", )

    def setText(self, _text):
        return self.__this.call(f"setText", _text)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlBreakIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlRuleBasedBreakIterator():
    DONE = -1
    WORD_NONE = 0
    WORD_NONE_LIMIT = 100
    WORD_NUMBER = 100
    WORD_NUMBER_LIMIT = 200
    WORD_LETTER = 200
    WORD_LETTER_LIMIT = 300
    WORD_KANA = 300
    WORD_KANA_LIMIT = 400
    WORD_IDEO = 400
    WORD_IDEO_LIMIT = 500
    LINE_SOFT = 0
    LINE_SOFT_LIMIT = 100
    LINE_HARD = 100
    LINE_HARD_LIMIT = 200
    SENTENCE_TERM = 0
    SENTENCE_TERM_LIMIT = 100
    SENTENCE_SEP = 100
    SENTENCE_SEP_LIMIT = 200

    def __init__(self, _rules, _compiled=False):
        self.__this = phpy.Object(f'IntlRuleBasedBreakIterator', _rules, _compiled)

    def getBinaryRules(self):
        return self.__this.call(f"getBinaryRules", )

    def getRules(self):
        return self.__this.call(f"getRules", )

    def getRuleStatus(self):
        return self.__this.call(f"getRuleStatus", )

    def getRuleStatusVec(self):
        return self.__this.call(f"getRuleStatusVec", )

    def createCharacterInstance(_locale=None):
        return phpy.call(f"IntlRuleBasedBreakIterator::createCharacterInstance", _locale)

    def createCodePointInstance():
        return phpy.call(f"IntlRuleBasedBreakIterator::createCodePointInstance", )

    def createLineInstance(_locale=None):
        return phpy.call(f"IntlRuleBasedBreakIterator::createLineInstance", _locale)

    def createSentenceInstance(_locale=None):
        return phpy.call(f"IntlRuleBasedBreakIterator::createSentenceInstance", _locale)

    def createTitleInstance(_locale=None):
        return phpy.call(f"IntlRuleBasedBreakIterator::createTitleInstance", _locale)

    def createWordInstance(_locale=None):
        return phpy.call(f"IntlRuleBasedBreakIterator::createWordInstance", _locale)

    def current(self):
        return self.__this.call(f"current", )

    def first(self):
        return self.__this.call(f"first", )

    def following(self, _offset):
        return self.__this.call(f"following", _offset)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getPartsIterator(self, _type=0):
        return self.__this.call(f"getPartsIterator", _type)

    def getText(self):
        return self.__this.call(f"getText", )

    def isBoundary(self, _offset):
        return self.__this.call(f"isBoundary", _offset)

    def last(self):
        return self.__this.call(f"last", )

    def next(self, _offset=None):
        return self.__this.call(f"next", _offset)

    def preceding(self, _offset):
        return self.__this.call(f"preceding", _offset)

    def previous(self):
        return self.__this.call(f"previous", )

    def setText(self, _text):
        return self.__this.call(f"setText", _text)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlCodePointBreakIterator():
    DONE = -1
    WORD_NONE = 0
    WORD_NONE_LIMIT = 100
    WORD_NUMBER = 100
    WORD_NUMBER_LIMIT = 200
    WORD_LETTER = 200
    WORD_LETTER_LIMIT = 300
    WORD_KANA = 300
    WORD_KANA_LIMIT = 400
    WORD_IDEO = 400
    WORD_IDEO_LIMIT = 500
    LINE_SOFT = 0
    LINE_SOFT_LIMIT = 100
    LINE_HARD = 100
    LINE_HARD_LIMIT = 200
    SENTENCE_TERM = 0
    SENTENCE_TERM_LIMIT = 100
    SENTENCE_SEP = 100
    SENTENCE_SEP_LIMIT = 200

    def getLastCodePoint(self):
        return self.__this.call(f"getLastCodePoint", )

    def createCharacterInstance(_locale=None):
        return phpy.call(f"IntlCodePointBreakIterator::createCharacterInstance", _locale)

    def createCodePointInstance():
        return phpy.call(f"IntlCodePointBreakIterator::createCodePointInstance", )

    def createLineInstance(_locale=None):
        return phpy.call(f"IntlCodePointBreakIterator::createLineInstance", _locale)

    def createSentenceInstance(_locale=None):
        return phpy.call(f"IntlCodePointBreakIterator::createSentenceInstance", _locale)

    def createTitleInstance(_locale=None):
        return phpy.call(f"IntlCodePointBreakIterator::createTitleInstance", _locale)

    def createWordInstance(_locale=None):
        return phpy.call(f"IntlCodePointBreakIterator::createWordInstance", _locale)

    def current(self):
        return self.__this.call(f"current", )

    def first(self):
        return self.__this.call(f"first", )

    def following(self, _offset):
        return self.__this.call(f"following", _offset)

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getLocale(self, _type):
        return self.__this.call(f"getLocale", _type)

    def getPartsIterator(self, _type=0):
        return self.__this.call(f"getPartsIterator", _type)

    def getText(self):
        return self.__this.call(f"getText", )

    def isBoundary(self, _offset):
        return self.__this.call(f"isBoundary", _offset)

    def last(self):
        return self.__this.call(f"last", )

    def next(self, _offset=None):
        return self.__this.call(f"next", _offset)

    def preceding(self, _offset):
        return self.__this.call(f"preceding", _offset)

    def previous(self):
        return self.__this.call(f"previous", )

    def setText(self, _text):
        return self.__this.call(f"setText", _text)

    def getIterator(self):
        return self.__this.call(f"getIterator", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlCodePointBreakIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlPartsIterator():
    KEY_SEQUENTIAL = 0
    KEY_LEFT = 1
    KEY_RIGHT = 2

    def getBreakIterator(self):
        return self.__this.call(f"getBreakIterator", )

    def getRuleStatus(self):
        return self.__this.call(f"getRuleStatus", )

    def current(self):
        return self.__this.call(f"current", )

    def key(self):
        return self.__this.call(f"key", )

    def next(self):
        return self.__this.call(f"next", )

    def rewind(self):
        return self.__this.call(f"rewind", )

    def valid(self):
        return self.__this.call(f"valid", )

    def __init__(self):
        self.__this = phpy.Object(f'IntlPartsIterator')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class UConverter():
    REASON_UNASSIGNED = 0
    REASON_ILLEGAL = 1
    REASON_IRREGULAR = 2
    REASON_RESET = 3
    REASON_CLOSE = 4
    REASON_CLONE = 5
    UNSUPPORTED_CONVERTER = -1
    SBCS = 0
    DBCS = 1
    MBCS = 2
    LATIN_1 = 3
    UTF8 = 4
    UTF16_BigEndian = 5
    UTF16_LittleEndian = 6
    UTF32_BigEndian = 7
    UTF32_LittleEndian = 8
    EBCDIC_STATEFUL = 9
    ISO_2022 = 10
    LMBCS_1 = 11
    LMBCS_2 = 12
    LMBCS_3 = 13
    LMBCS_4 = 14
    LMBCS_5 = 15
    LMBCS_6 = 16
    LMBCS_8 = 17
    LMBCS_11 = 18
    LMBCS_16 = 19
    LMBCS_17 = 20
    LMBCS_18 = 21
    LMBCS_19 = 22
    LMBCS_LAST = 22
    HZ = 23
    SCSU = 24
    ISCII = 25
    US_ASCII = 26
    UTF7 = 27
    BOCU1 = 28
    UTF16 = 29
    UTF32 = 30
    CESU8 = 31
    IMAP_MAILBOX = 32

    def __init__(self, _destination_encoding=None, _source_encoding=None):
        self.__this = phpy.Object(f'UConverter', _destination_encoding, _source_encoding)

    def convert(self, _str, _reverse=False):
        return self.__this.call(f"convert", _str, _reverse)

    def fromUCallback(self, _reason, _source, _code_point, _error):
        return self.__this.call(f"fromUCallback", _reason, _source, _code_point, _error)

    def getAliases(_name):
        return phpy.call(f"UConverter::getAliases", _name)

    def getAvailable():
        return phpy.call(f"UConverter::getAvailable", )

    def getDestinationEncoding(self):
        return self.__this.call(f"getDestinationEncoding", )

    def getDestinationType(self):
        return self.__this.call(f"getDestinationType", )

    def getErrorCode(self):
        return self.__this.call(f"getErrorCode", )

    def getErrorMessage(self):
        return self.__this.call(f"getErrorMessage", )

    def getSourceEncoding(self):
        return self.__this.call(f"getSourceEncoding", )

    def getSourceType(self):
        return self.__this.call(f"getSourceType", )

    def getStandards():
        return phpy.call(f"UConverter::getStandards", )

    def getSubstChars(self):
        return self.__this.call(f"getSubstChars", )

    def reasonText(_reason):
        return phpy.call(f"UConverter::reasonText", _reason)

    def setDestinationEncoding(self, _encoding):
        return self.__this.call(f"setDestinationEncoding", _encoding)

    def setSourceEncoding(self, _encoding):
        return self.__this.call(f"setSourceEncoding", _encoding)

    def setSubstChars(self, _chars):
        return self.__this.call(f"setSubstChars", _chars)

    def toUCallback(self, _reason, _source, _code_units, _error):
        return self.__this.call(f"toUCallback", _reason, _source, _code_units, _error)

    def transcode(_str, _to_encoding, _from_encoding, _options=None):
        return phpy.call(f"UConverter::transcode", _str, _to_encoding, _from_encoding, _options)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class IntlChar():
    UNICODE_VERSION = "10.0"
    CODEPOINT_MIN = 0
    CODEPOINT_MAX = 1114111
    NO_NUMERIC_VALUE = -123456789
    PROPERTY_ALPHABETIC = 0
    PROPERTY_BINARY_START = 0
    PROPERTY_ASCII_HEX_DIGIT = 1
    PROPERTY_BIDI_CONTROL = 2
    PROPERTY_BIDI_MIRRORED = 3
    PROPERTY_DASH = 4
    PROPERTY_DEFAULT_IGNORABLE_CODE_POINT = 5
    PROPERTY_DEPRECATED = 6
    PROPERTY_DIACRITIC = 7
    PROPERTY_EXTENDER = 8
    PROPERTY_FULL_COMPOSITION_EXCLUSION = 9
    PROPERTY_GRAPHEME_BASE = 10
    PROPERTY_GRAPHEME_EXTEND = 11
    PROPERTY_GRAPHEME_LINK = 12
    PROPERTY_HEX_DIGIT = 13
    PROPERTY_HYPHEN = 14
    PROPERTY_ID_CONTINUE = 15
    PROPERTY_ID_START = 16
    PROPERTY_IDEOGRAPHIC = 17
    PROPERTY_IDS_BINARY_OPERATOR = 18
    PROPERTY_IDS_TRINARY_OPERATOR = 19
    PROPERTY_JOIN_CONTROL = 20
    PROPERTY_LOGICAL_ORDER_EXCEPTION = 21
    PROPERTY_LOWERCASE = 22
    PROPERTY_MATH = 23
    PROPERTY_NONCHARACTER_CODE_POINT = 24
    PROPERTY_QUOTATION_MARK = 25
    PROPERTY_RADICAL = 26
    PROPERTY_SOFT_DOTTED = 27
    PROPERTY_TERMINAL_PUNCTUATION = 28
    PROPERTY_UNIFIED_IDEOGRAPH = 29
    PROPERTY_UPPERCASE = 30
    PROPERTY_WHITE_SPACE = 31
    PROPERTY_XID_CONTINUE = 32
    PROPERTY_XID_START = 33
    PROPERTY_CASE_SENSITIVE = 34
    PROPERTY_S_TERM = 35
    PROPERTY_VARIATION_SELECTOR = 36
    PROPERTY_NFD_INERT = 37
    PROPERTY_NFKD_INERT = 38
    PROPERTY_NFC_INERT = 39
    PROPERTY_NFKC_INERT = 40
    PROPERTY_SEGMENT_STARTER = 41
    PROPERTY_PATTERN_SYNTAX = 42
    PROPERTY_PATTERN_WHITE_SPACE = 43
    PROPERTY_POSIX_ALNUM = 44
    PROPERTY_POSIX_BLANK = 45
    PROPERTY_POSIX_GRAPH = 46
    PROPERTY_POSIX_PRINT = 47
    PROPERTY_POSIX_XDIGIT = 48
    PROPERTY_CASED = 49
    PROPERTY_CASE_IGNORABLE = 50
    PROPERTY_CHANGES_WHEN_LOWERCASED = 51
    PROPERTY_CHANGES_WHEN_UPPERCASED = 52
    PROPERTY_CHANGES_WHEN_TITLECASED = 53
    PROPERTY_CHANGES_WHEN_CASEFOLDED = 54
    PROPERTY_CHANGES_WHEN_CASEMAPPED = 55
    PROPERTY_CHANGES_WHEN_NFKC_CASEFOLDED = 56
    PROPERTY_BINARY_LIMIT = 64
    PROPERTY_BIDI_CLASS = 4096
    PROPERTY_INT_START = 4096
    PROPERTY_BLOCK = 4097
    PROPERTY_CANONICAL_COMBINING_CLASS = 4098
    PROPERTY_DECOMPOSITION_TYPE = 4099
    PROPERTY_EAST_ASIAN_WIDTH = 4100
    PROPERTY_GENERAL_CATEGORY = 4101
    PROPERTY_JOINING_GROUP = 4102
    PROPERTY_JOINING_TYPE = 4103
    PROPERTY_LINE_BREAK = 4104
    PROPERTY_NUMERIC_TYPE = 4105
    PROPERTY_SCRIPT = 4106
    PROPERTY_HANGUL_SYLLABLE_TYPE = 4107
    PROPERTY_NFD_QUICK_CHECK = 4108
    PROPERTY_NFKD_QUICK_CHECK = 4109
    PROPERTY_NFC_QUICK_CHECK = 4110
    PROPERTY_NFKC_QUICK_CHECK = 4111
    PROPERTY_LEAD_CANONICAL_COMBINING_CLASS = 4112
    PROPERTY_TRAIL_CANONICAL_COMBINING_CLASS = 4113
    PROPERTY_GRAPHEME_CLUSTER_BREAK = 4114
    PROPERTY_SENTENCE_BREAK = 4115
    PROPERTY_WORD_BREAK = 4116
    PROPERTY_BIDI_PAIRED_BRACKET_TYPE = 4117
    PROPERTY_INT_LIMIT = 4118
    PROPERTY_GENERAL_CATEGORY_MASK = 8192
    PROPERTY_MASK_START = 8192
    PROPERTY_MASK_LIMIT = 8193
    PROPERTY_NUMERIC_VALUE = 12288
    PROPERTY_DOUBLE_START = 12288
    PROPERTY_DOUBLE_LIMIT = 12289
    PROPERTY_AGE = 16384
    PROPERTY_STRING_START = 16384
    PROPERTY_BIDI_MIRRORING_GLYPH = 16385
    PROPERTY_CASE_FOLDING = 16386
    PROPERTY_ISO_COMMENT = 16387
    PROPERTY_LOWERCASE_MAPPING = 16388
    PROPERTY_NAME = 16389
    PROPERTY_SIMPLE_CASE_FOLDING = 16390
    PROPERTY_SIMPLE_LOWERCASE_MAPPING = 16391
    PROPERTY_SIMPLE_TITLECASE_MAPPING = 16392
    PROPERTY_SIMPLE_UPPERCASE_MAPPING = 16393
    PROPERTY_TITLECASE_MAPPING = 16394
    PROPERTY_UNICODE_1_NAME = 16395
    PROPERTY_UPPERCASE_MAPPING = 16396
    PROPERTY_BIDI_PAIRED_BRACKET = 16397
    PROPERTY_STRING_LIMIT = 16398
    PROPERTY_SCRIPT_EXTENSIONS = 28672
    PROPERTY_OTHER_PROPERTY_START = 28672
    PROPERTY_OTHER_PROPERTY_LIMIT = 28673
    PROPERTY_INVALID_CODE = -1
    CHAR_CATEGORY_UNASSIGNED = 0
    CHAR_CATEGORY_GENERAL_OTHER_TYPES = 0
    CHAR_CATEGORY_UPPERCASE_LETTER = 1
    CHAR_CATEGORY_LOWERCASE_LETTER = 2
    CHAR_CATEGORY_TITLECASE_LETTER = 3
    CHAR_CATEGORY_MODIFIER_LETTER = 4
    CHAR_CATEGORY_OTHER_LETTER = 5
    CHAR_CATEGORY_NON_SPACING_MARK = 6
    CHAR_CATEGORY_ENCLOSING_MARK = 7
    CHAR_CATEGORY_COMBINING_SPACING_MARK = 8
    CHAR_CATEGORY_DECIMAL_DIGIT_NUMBER = 9
    CHAR_CATEGORY_LETTER_NUMBER = 10
    CHAR_CATEGORY_OTHER_NUMBER = 11
    CHAR_CATEGORY_SPACE_SEPARATOR = 12
    CHAR_CATEGORY_LINE_SEPARATOR = 13
    CHAR_CATEGORY_PARAGRAPH_SEPARATOR = 14
    CHAR_CATEGORY_CONTROL_CHAR = 15
    CHAR_CATEGORY_FORMAT_CHAR = 16
    CHAR_CATEGORY_PRIVATE_USE_CHAR = 17
    CHAR_CATEGORY_SURROGATE = 18
    CHAR_CATEGORY_DASH_PUNCTUATION = 19
    CHAR_CATEGORY_START_PUNCTUATION = 20
    CHAR_CATEGORY_END_PUNCTUATION = 21
    CHAR_CATEGORY_CONNECTOR_PUNCTUATION = 22
    CHAR_CATEGORY_OTHER_PUNCTUATION = 23
    CHAR_CATEGORY_MATH_SYMBOL = 24
    CHAR_CATEGORY_CURRENCY_SYMBOL = 25
    CHAR_CATEGORY_MODIFIER_SYMBOL = 26
    CHAR_CATEGORY_OTHER_SYMBOL = 27
    CHAR_CATEGORY_INITIAL_PUNCTUATION = 28
    CHAR_CATEGORY_FINAL_PUNCTUATION = 29
    CHAR_CATEGORY_CHAR_CATEGORY_COUNT = 30
    CHAR_DIRECTION_LEFT_TO_RIGHT = 0
    CHAR_DIRECTION_RIGHT_TO_LEFT = 1
    CHAR_DIRECTION_EUROPEAN_NUMBER = 2
    CHAR_DIRECTION_EUROPEAN_NUMBER_SEPARATOR = 3
    CHAR_DIRECTION_EUROPEAN_NUMBER_TERMINATOR = 4
    CHAR_DIRECTION_ARABIC_NUMBER = 5
    CHAR_DIRECTION_COMMON_NUMBER_SEPARATOR = 6
    CHAR_DIRECTION_BLOCK_SEPARATOR = 7
    CHAR_DIRECTION_SEGMENT_SEPARATOR = 8
    CHAR_DIRECTION_WHITE_SPACE_NEUTRAL = 9
    CHAR_DIRECTION_OTHER_NEUTRAL = 10
    CHAR_DIRECTION_LEFT_TO_RIGHT_EMBEDDING = 11
    CHAR_DIRECTION_LEFT_TO_RIGHT_OVERRIDE = 12
    CHAR_DIRECTION_RIGHT_TO_LEFT_ARABIC = 13
    CHAR_DIRECTION_RIGHT_TO_LEFT_EMBEDDING = 14
    CHAR_DIRECTION_RIGHT_TO_LEFT_OVERRIDE = 15
    CHAR_DIRECTION_POP_DIRECTIONAL_FORMAT = 16
    CHAR_DIRECTION_DIR_NON_SPACING_MARK = 17
    CHAR_DIRECTION_BOUNDARY_NEUTRAL = 18
    CHAR_DIRECTION_FIRST_STRONG_ISOLATE = 19
    CHAR_DIRECTION_LEFT_TO_RIGHT_ISOLATE = 20
    CHAR_DIRECTION_RIGHT_TO_LEFT_ISOLATE = 21
    CHAR_DIRECTION_POP_DIRECTIONAL_ISOLATE = 22
    CHAR_DIRECTION_CHAR_DIRECTION_COUNT = 23
    BLOCK_CODE_NO_BLOCK = 0
    BLOCK_CODE_BASIC_LATIN = 1
    BLOCK_CODE_LATIN_1_SUPPLEMENT = 2
    BLOCK_CODE_LATIN_EXTENDED_A = 3
    BLOCK_CODE_LATIN_EXTENDED_B = 4
    BLOCK_CODE_IPA_EXTENSIONS = 5
    BLOCK_CODE_SPACING_MODIFIER_LETTERS = 6
    BLOCK_CODE_COMBINING_DIACRITICAL_MARKS = 7
    BLOCK_CODE_GREEK = 8
    BLOCK_CODE_CYRILLIC = 9
    BLOCK_CODE_ARMENIAN = 10
    BLOCK_CODE_HEBREW = 11
    BLOCK_CODE_ARABIC = 12
    BLOCK_CODE_SYRIAC = 13
    BLOCK_CODE_THAANA = 14
    BLOCK_CODE_DEVANAGARI = 15
    BLOCK_CODE_BENGALI = 16
    BLOCK_CODE_GURMUKHI = 17
    BLOCK_CODE_GUJARATI = 18
    BLOCK_CODE_ORIYA = 19
    BLOCK_CODE_TAMIL = 20
    BLOCK_CODE_TELUGU = 21
    BLOCK_CODE_KANNADA = 22
    BLOCK_CODE_MALAYALAM = 23
    BLOCK_CODE_SINHALA = 24
    BLOCK_CODE_THAI = 25
    BLOCK_CODE_LAO = 26
    BLOCK_CODE_TIBETAN = 27
    BLOCK_CODE_MYANMAR = 28
    BLOCK_CODE_GEORGIAN = 29
    BLOCK_CODE_HANGUL_JAMO = 30
    BLOCK_CODE_ETHIOPIC = 31
    BLOCK_CODE_CHEROKEE = 32
    BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS = 33
    BLOCK_CODE_OGHAM = 34
    BLOCK_CODE_RUNIC = 35
    BLOCK_CODE_KHMER = 36
    BLOCK_CODE_MONGOLIAN = 37
    BLOCK_CODE_LATIN_EXTENDED_ADDITIONAL = 38
    BLOCK_CODE_GREEK_EXTENDED = 39
    BLOCK_CODE_GENERAL_PUNCTUATION = 40
    BLOCK_CODE_SUPERSCRIPTS_AND_SUBSCRIPTS = 41
    BLOCK_CODE_CURRENCY_SYMBOLS = 42
    BLOCK_CODE_COMBINING_MARKS_FOR_SYMBOLS = 43
    BLOCK_CODE_LETTERLIKE_SYMBOLS = 44
    BLOCK_CODE_NUMBER_FORMS = 45
    BLOCK_CODE_ARROWS = 46
    BLOCK_CODE_MATHEMATICAL_OPERATORS = 47
    BLOCK_CODE_MISCELLANEOUS_TECHNICAL = 48
    BLOCK_CODE_CONTROL_PICTURES = 49
    BLOCK_CODE_OPTICAL_CHARACTER_RECOGNITION = 50
    BLOCK_CODE_ENCLOSED_ALPHANUMERICS = 51
    BLOCK_CODE_BOX_DRAWING = 52
    BLOCK_CODE_BLOCK_ELEMENTS = 53
    BLOCK_CODE_GEOMETRIC_SHAPES = 54
    BLOCK_CODE_MISCELLANEOUS_SYMBOLS = 55
    BLOCK_CODE_DINGBATS = 56
    BLOCK_CODE_BRAILLE_PATTERNS = 57
    BLOCK_CODE_CJK_RADICALS_SUPPLEMENT = 58
    BLOCK_CODE_KANGXI_RADICALS = 59
    BLOCK_CODE_IDEOGRAPHIC_DESCRIPTION_CHARACTERS = 60
    BLOCK_CODE_CJK_SYMBOLS_AND_PUNCTUATION = 61
    BLOCK_CODE_HIRAGANA = 62
    BLOCK_CODE_KATAKANA = 63
    BLOCK_CODE_BOPOMOFO = 64
    BLOCK_CODE_HANGUL_COMPATIBILITY_JAMO = 65
    BLOCK_CODE_KANBUN = 66
    BLOCK_CODE_BOPOMOFO_EXTENDED = 67
    BLOCK_CODE_ENCLOSED_CJK_LETTERS_AND_MONTHS = 68
    BLOCK_CODE_CJK_COMPATIBILITY = 69
    BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A = 70
    BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS = 71
    BLOCK_CODE_YI_SYLLABLES = 72
    BLOCK_CODE_YI_RADICALS = 73
    BLOCK_CODE_HANGUL_SYLLABLES = 74
    BLOCK_CODE_HIGH_SURROGATES = 75
    BLOCK_CODE_HIGH_PRIVATE_USE_SURROGATES = 76
    BLOCK_CODE_LOW_SURROGATES = 77
    BLOCK_CODE_PRIVATE_USE_AREA = 78
    BLOCK_CODE_PRIVATE_USE = 78
    BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS = 79
    BLOCK_CODE_ALPHABETIC_PRESENTATION_FORMS = 80
    BLOCK_CODE_ARABIC_PRESENTATION_FORMS_A = 81
    BLOCK_CODE_COMBINING_HALF_MARKS = 82
    BLOCK_CODE_CJK_COMPATIBILITY_FORMS = 83
    BLOCK_CODE_SMALL_FORM_VARIANTS = 84
    BLOCK_CODE_ARABIC_PRESENTATION_FORMS_B = 85
    BLOCK_CODE_SPECIALS = 86
    BLOCK_CODE_HALFWIDTH_AND_FULLWIDTH_FORMS = 87
    BLOCK_CODE_OLD_ITALIC = 88
    BLOCK_CODE_GOTHIC = 89
    BLOCK_CODE_DESERET = 90
    BLOCK_CODE_BYZANTINE_MUSICAL_SYMBOLS = 91
    BLOCK_CODE_MUSICAL_SYMBOLS = 92
    BLOCK_CODE_MATHEMATICAL_ALPHANUMERIC_SYMBOLS = 93
    BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B = 94
    BLOCK_CODE_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT = 95
    BLOCK_CODE_TAGS = 96
    BLOCK_CODE_CYRILLIC_SUPPLEMENT = 97
    BLOCK_CODE_CYRILLIC_SUPPLEMENTARY = 97
    BLOCK_CODE_TAGALOG = 98
    BLOCK_CODE_HANUNOO = 99
    BLOCK_CODE_BUHID = 100
    BLOCK_CODE_TAGBANWA = 101
    BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A = 102
    BLOCK_CODE_SUPPLEMENTAL_ARROWS_A = 103
    BLOCK_CODE_SUPPLEMENTAL_ARROWS_B = 104
    BLOCK_CODE_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B = 105
    BLOCK_CODE_SUPPLEMENTAL_MATHEMATICAL_OPERATORS = 106
    BLOCK_CODE_KATAKANA_PHONETIC_EXTENSIONS = 107
    BLOCK_CODE_VARIATION_SELECTORS = 108
    BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_A = 109
    BLOCK_CODE_SUPPLEMENTARY_PRIVATE_USE_AREA_B = 110
    BLOCK_CODE_LIMBU = 111
    BLOCK_CODE_TAI_LE = 112
    BLOCK_CODE_KHMER_SYMBOLS = 113
    BLOCK_CODE_PHONETIC_EXTENSIONS = 114
    BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_ARROWS = 115
    BLOCK_CODE_YIJING_HEXAGRAM_SYMBOLS = 116
    BLOCK_CODE_LINEAR_B_SYLLABARY = 117
    BLOCK_CODE_LINEAR_B_IDEOGRAMS = 118
    BLOCK_CODE_AEGEAN_NUMBERS = 119
    BLOCK_CODE_UGARITIC = 120
    BLOCK_CODE_SHAVIAN = 121
    BLOCK_CODE_OSMANYA = 122
    BLOCK_CODE_CYPRIOT_SYLLABARY = 123
    BLOCK_CODE_TAI_XUAN_JING_SYMBOLS = 124
    BLOCK_CODE_VARIATION_SELECTORS_SUPPLEMENT = 125
    BLOCK_CODE_ANCIENT_GREEK_MUSICAL_NOTATION = 126
    BLOCK_CODE_ANCIENT_GREEK_NUMBERS = 127
    BLOCK_CODE_ARABIC_SUPPLEMENT = 128
    BLOCK_CODE_BUGINESE = 129
    BLOCK_CODE_CJK_STROKES = 130
    BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT = 131
    BLOCK_CODE_COPTIC = 132
    BLOCK_CODE_ETHIOPIC_EXTENDED = 133
    BLOCK_CODE_ETHIOPIC_SUPPLEMENT = 134
    BLOCK_CODE_GEORGIAN_SUPPLEMENT = 135
    BLOCK_CODE_GLAGOLITIC = 136
    BLOCK_CODE_KHAROSHTHI = 137
    BLOCK_CODE_MODIFIER_TONE_LETTERS = 138
    BLOCK_CODE_NEW_TAI_LUE = 139
    BLOCK_CODE_OLD_PERSIAN = 140
    BLOCK_CODE_PHONETIC_EXTENSIONS_SUPPLEMENT = 141
    BLOCK_CODE_SUPPLEMENTAL_PUNCTUATION = 142
    BLOCK_CODE_SYLOTI_NAGRI = 143
    BLOCK_CODE_TIFINAGH = 144
    BLOCK_CODE_VERTICAL_FORMS = 145
    BLOCK_CODE_NKO = 146
    BLOCK_CODE_BALINESE = 147
    BLOCK_CODE_LATIN_EXTENDED_C = 148
    BLOCK_CODE_LATIN_EXTENDED_D = 149
    BLOCK_CODE_PHAGS_PA = 150
    BLOCK_CODE_PHOENICIAN = 151
    BLOCK_CODE_CUNEIFORM = 152
    BLOCK_CODE_CUNEIFORM_NUMBERS_AND_PUNCTUATION = 153
    BLOCK_CODE_COUNTING_ROD_NUMERALS = 154
    BLOCK_CODE_SUNDANESE = 155
    BLOCK_CODE_LEPCHA = 156
    BLOCK_CODE_OL_CHIKI = 157
    BLOCK_CODE_CYRILLIC_EXTENDED_A = 158
    BLOCK_CODE_VAI = 159
    BLOCK_CODE_CYRILLIC_EXTENDED_B = 160
    BLOCK_CODE_SAURASHTRA = 161
    BLOCK_CODE_KAYAH_LI = 162
    BLOCK_CODE_REJANG = 163
    BLOCK_CODE_CHAM = 164
    BLOCK_CODE_ANCIENT_SYMBOLS = 165
    BLOCK_CODE_PHAISTOS_DISC = 166
    BLOCK_CODE_LYCIAN = 167
    BLOCK_CODE_CARIAN = 168
    BLOCK_CODE_LYDIAN = 169
    BLOCK_CODE_MAHJONG_TILES = 170
    BLOCK_CODE_DOMINO_TILES = 171
    BLOCK_CODE_SAMARITAN = 172
    BLOCK_CODE_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED = 173
    BLOCK_CODE_TAI_THAM = 174
    BLOCK_CODE_VEDIC_EXTENSIONS = 175
    BLOCK_CODE_LISU = 176
    BLOCK_CODE_BAMUM = 177
    BLOCK_CODE_COMMON_INDIC_NUMBER_FORMS = 178
    BLOCK_CODE_DEVANAGARI_EXTENDED = 179
    BLOCK_CODE_HANGUL_JAMO_EXTENDED_A = 180
    BLOCK_CODE_JAVANESE = 181
    BLOCK_CODE_MYANMAR_EXTENDED_A = 182
    BLOCK_CODE_TAI_VIET = 183
    BLOCK_CODE_MEETEI_MAYEK = 184
    BLOCK_CODE_HANGUL_JAMO_EXTENDED_B = 185
    BLOCK_CODE_IMPERIAL_ARAMAIC = 186
    BLOCK_CODE_OLD_SOUTH_ARABIAN = 187
    BLOCK_CODE_AVESTAN = 188
    BLOCK_CODE_INSCRIPTIONAL_PARTHIAN = 189
    BLOCK_CODE_INSCRIPTIONAL_PAHLAVI = 190
    BLOCK_CODE_OLD_TURKIC = 191
    BLOCK_CODE_RUMI_NUMERAL_SYMBOLS = 192
    BLOCK_CODE_KAITHI = 193
    BLOCK_CODE_EGYPTIAN_HIEROGLYPHS = 194
    BLOCK_CODE_ENCLOSED_ALPHANUMERIC_SUPPLEMENT = 195
    BLOCK_CODE_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT = 196
    BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C = 197
    BLOCK_CODE_MANDAIC = 198
    BLOCK_CODE_BATAK = 199
    BLOCK_CODE_ETHIOPIC_EXTENDED_A = 200
    BLOCK_CODE_BRAHMI = 201
    BLOCK_CODE_BAMUM_SUPPLEMENT = 202
    BLOCK_CODE_KANA_SUPPLEMENT = 203
    BLOCK_CODE_PLAYING_CARDS = 204
    BLOCK_CODE_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS = 205
    BLOCK_CODE_EMOTICONS = 206
    BLOCK_CODE_TRANSPORT_AND_MAP_SYMBOLS = 207
    BLOCK_CODE_ALCHEMICAL_SYMBOLS = 208
    BLOCK_CODE_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D = 209
    BLOCK_CODE_ARABIC_EXTENDED_A = 210
    BLOCK_CODE_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS = 211
    BLOCK_CODE_CHAKMA = 212
    BLOCK_CODE_MEETEI_MAYEK_EXTENSIONS = 213
    BLOCK_CODE_MEROITIC_CURSIVE = 214
    BLOCK_CODE_MEROITIC_HIEROGLYPHS = 215
    BLOCK_CODE_MIAO = 216
    BLOCK_CODE_SHARADA = 217
    BLOCK_CODE_SORA_SOMPENG = 218
    BLOCK_CODE_SUNDANESE_SUPPLEMENT = 219
    BLOCK_CODE_TAKRI = 220
    BLOCK_CODE_BASSA_VAH = 221
    BLOCK_CODE_CAUCASIAN_ALBANIAN = 222
    BLOCK_CODE_COPTIC_EPACT_NUMBERS = 223
    BLOCK_CODE_COMBINING_DIACRITICAL_MARKS_EXTENDED = 224
    BLOCK_CODE_DUPLOYAN = 225
    BLOCK_CODE_ELBASAN = 226
    BLOCK_CODE_GEOMETRIC_SHAPES_EXTENDED = 227
    BLOCK_CODE_GRANTHA = 228
    BLOCK_CODE_KHOJKI = 229
    BLOCK_CODE_KHUDAWADI = 230
    BLOCK_CODE_LATIN_EXTENDED_E = 231
    BLOCK_CODE_LINEAR_A = 232
    BLOCK_CODE_MAHAJANI = 233
    BLOCK_CODE_MANICHAEAN = 234
    BLOCK_CODE_MENDE_KIKAKUI = 235
    BLOCK_CODE_MODI = 236
    BLOCK_CODE_MRO = 237
    BLOCK_CODE_MYANMAR_EXTENDED_B = 238
    BLOCK_CODE_NABATAEAN = 239
    BLOCK_CODE_OLD_NORTH_ARABIAN = 240
    BLOCK_CODE_OLD_PERMIC = 241
    BLOCK_CODE_ORNAMENTAL_DINGBATS = 242
    BLOCK_CODE_PAHAWH_HMONG = 243
    BLOCK_CODE_PALMYRENE = 244
    BLOCK_CODE_PAU_CIN_HAU = 245
    BLOCK_CODE_PSALTER_PAHLAVI = 246
    BLOCK_CODE_SHORTHAND_FORMAT_CONTROLS = 247
    BLOCK_CODE_SIDDHAM = 248
    BLOCK_CODE_SINHALA_ARCHAIC_NUMBERS = 249
    BLOCK_CODE_SUPPLEMENTAL_ARROWS_C = 250
    BLOCK_CODE_TIRHUTA = 251
    BLOCK_CODE_WARANG_CITI = 252
    BLOCK_CODE_COUNT = 281
    BLOCK_CODE_INVALID_CODE = -1
    BPT_NONE = 0
    BPT_OPEN = 1
    BPT_CLOSE = 2
    BPT_COUNT = 3
    EA_NEUTRAL = 0
    EA_AMBIGUOUS = 1
    EA_HALFWIDTH = 2
    EA_FULLWIDTH = 3
    EA_NARROW = 4
    EA_WIDE = 5
    EA_COUNT = 6
    UNICODE_CHAR_NAME = 0
    UNICODE_10_CHAR_NAME = 1
    EXTENDED_CHAR_NAME = 2
    CHAR_NAME_ALIAS = 3
    CHAR_NAME_CHOICE_COUNT = 4
    SHORT_PROPERTY_NAME = 0
    LONG_PROPERTY_NAME = 1
    PROPERTY_NAME_CHOICE_COUNT = 2
    DT_NONE = 0
    DT_CANONICAL = 1
    DT_COMPAT = 2
    DT_CIRCLE = 3
    DT_FINAL = 4
    DT_FONT = 5
    DT_FRACTION = 6
    DT_INITIAL = 7
    DT_ISOLATED = 8
    DT_MEDIAL = 9
    DT_NARROW = 10
    DT_NOBREAK = 11
    DT_SMALL = 12
    DT_SQUARE = 13
    DT_SUB = 14
    DT_SUPER = 15
    DT_VERTICAL = 16
    DT_WIDE = 17
    DT_COUNT = 18
    JT_NON_JOINING = 0
    JT_JOIN_CAUSING = 1
    JT_DUAL_JOINING = 2
    JT_LEFT_JOINING = 3
    JT_RIGHT_JOINING = 4
    JT_TRANSPARENT = 5
    JT_COUNT = 6
    JG_NO_JOINING_GROUP = 0
    JG_AIN = 1
    JG_ALAPH = 2
    JG_ALEF = 3
    JG_BEH = 4
    JG_BETH = 5
    JG_DAL = 6
    JG_DALATH_RISH = 7
    JG_E = 8
    JG_FEH = 9
    JG_FINAL_SEMKATH = 10
    JG_GAF = 11
    JG_GAMAL = 12
    JG_HAH = 13
    JG_TEH_MARBUTA_GOAL = 14
    JG_HAMZA_ON_HEH_GOAL = 14
    JG_HE = 15
    JG_HEH = 16
    JG_HEH_GOAL = 17
    JG_HETH = 18
    JG_KAF = 19
    JG_KAPH = 20
    JG_KNOTTED_HEH = 21
    JG_LAM = 22
    JG_LAMADH = 23
    JG_MEEM = 24
    JG_MIM = 25
    JG_NOON = 26
    JG_NUN = 27
    JG_PE = 28
    JG_QAF = 29
    JG_QAPH = 30
    JG_REH = 31
    JG_REVERSED_PE = 32
    JG_SAD = 33
    JG_SADHE = 34
    JG_SEEN = 35
    JG_SEMKATH = 36
    JG_SHIN = 37
    JG_SWASH_KAF = 38
    JG_SYRIAC_WAW = 39
    JG_TAH = 40
    JG_TAW = 41
    JG_TEH_MARBUTA = 42
    JG_TETH = 43
    JG_WAW = 44
    JG_YEH = 45
    JG_YEH_BARREE = 46
    JG_YEH_WITH_TAIL = 47
    JG_YUDH = 48
    JG_YUDH_HE = 49
    JG_ZAIN = 50
    JG_FE = 51
    JG_KHAPH = 52
    JG_ZHAIN = 53
    JG_BURUSHASKI_YEH_BARREE = 54
    JG_FARSI_YEH = 55
    JG_NYA = 56
    JG_ROHINGYA_YEH = 57
    JG_MANICHAEAN_ALEPH = 58
    JG_MANICHAEAN_AYIN = 59
    JG_MANICHAEAN_BETH = 60
    JG_MANICHAEAN_DALETH = 61
    JG_MANICHAEAN_DHAMEDH = 62
    JG_MANICHAEAN_FIVE = 63
    JG_MANICHAEAN_GIMEL = 64
    JG_MANICHAEAN_HETH = 65
    JG_MANICHAEAN_HUNDRED = 66
    JG_MANICHAEAN_KAPH = 67
    JG_MANICHAEAN_LAMEDH = 68
    JG_MANICHAEAN_MEM = 69
    JG_MANICHAEAN_NUN = 70
    JG_MANICHAEAN_ONE = 71
    JG_MANICHAEAN_PE = 72
    JG_MANICHAEAN_QOPH = 73
    JG_MANICHAEAN_RESH = 74
    JG_MANICHAEAN_SADHE = 75
    JG_MANICHAEAN_SAMEKH = 76
    JG_MANICHAEAN_TAW = 77
    JG_MANICHAEAN_TEN = 78
    JG_MANICHAEAN_TETH = 79
    JG_MANICHAEAN_THAMEDH = 80
    JG_MANICHAEAN_TWENTY = 81
    JG_MANICHAEAN_WAW = 82
    JG_MANICHAEAN_YODH = 83
    JG_MANICHAEAN_ZAYIN = 84
    JG_STRAIGHT_WAW = 85
    JG_COUNT = 100
    GCB_OTHER = 0
    GCB_CONTROL = 1
    GCB_CR = 2
    GCB_EXTEND = 3
    GCB_L = 4
    GCB_LF = 5
    GCB_LV = 6
    GCB_LVT = 7
    GCB_T = 8
    GCB_V = 9
    GCB_SPACING_MARK = 10
    GCB_PREPEND = 11
    GCB_REGIONAL_INDICATOR = 12
    GCB_COUNT = 18
    WB_OTHER = 0
    WB_ALETTER = 1
    WB_FORMAT = 2
    WB_KATAKANA = 3
    WB_MIDLETTER = 4
    WB_MIDNUM = 5
    WB_NUMERIC = 6
    WB_EXTENDNUMLET = 7
    WB_CR = 8
    WB_EXTEND = 9
    WB_LF = 10
    WB_MIDNUMLET = 11
    WB_NEWLINE = 12
    WB_REGIONAL_INDICATOR = 13
    WB_HEBREW_LETTER = 14
    WB_SINGLE_QUOTE = 15
    WB_DOUBLE_QUOTE = 16
    WB_COUNT = 22
    SB_OTHER = 0
    SB_ATERM = 1
    SB_CLOSE = 2
    SB_FORMAT = 3
    SB_LOWER = 4
    SB_NUMERIC = 5
    SB_OLETTER = 6
    SB_SEP = 7
    SB_SP = 8
    SB_STERM = 9
    SB_UPPER = 10
    SB_CR = 11
    SB_EXTEND = 12
    SB_LF = 13
    SB_SCONTINUE = 14
    SB_COUNT = 15
    LB_UNKNOWN = 0
    LB_AMBIGUOUS = 1
    LB_ALPHABETIC = 2
    LB_BREAK_BOTH = 3
    LB_BREAK_AFTER = 4
    LB_BREAK_BEFORE = 5
    LB_MANDATORY_BREAK = 6
    LB_CONTINGENT_BREAK = 7
    LB_CLOSE_PUNCTUATION = 8
    LB_COMBINING_MARK = 9
    LB_CARRIAGE_RETURN = 10
    LB_EXCLAMATION = 11
    LB_GLUE = 12
    LB_HYPHEN = 13
    LB_IDEOGRAPHIC = 14
    LB_INSEPARABLE = 15
    LB_INSEPERABLE = 15
    LB_INFIX_NUMERIC = 16
    LB_LINE_FEED = 17
    LB_NONSTARTER = 18
    LB_NUMERIC = 19
    LB_OPEN_PUNCTUATION = 20
    LB_POSTFIX_NUMERIC = 21
    LB_PREFIX_NUMERIC = 22
    LB_QUOTATION = 23
    LB_COMPLEX_CONTEXT = 24
    LB_SURROGATE = 25
    LB_SPACE = 26
    LB_BREAK_SYMBOLS = 27
    LB_ZWSPACE = 28
    LB_NEXT_LINE = 29
    LB_WORD_JOINER = 30
    LB_H2 = 31
    LB_H3 = 32
    LB_JL = 33
    LB_JT = 34
    LB_JV = 35
    LB_CLOSE_PARENTHESIS = 36
    LB_CONDITIONAL_JAPANESE_STARTER = 37
    LB_HEBREW_LETTER = 38
    LB_REGIONAL_INDICATOR = 39
    LB_COUNT = 43
    NT_NONE = 0
    NT_DECIMAL = 1
    NT_DIGIT = 2
    NT_NUMERIC = 3
    NT_COUNT = 4
    HST_NOT_APPLICABLE = 0
    HST_LEADING_JAMO = 1
    HST_VOWEL_JAMO = 2
    HST_TRAILING_JAMO = 3
    HST_LV_SYLLABLE = 4
    HST_LVT_SYLLABLE = 5
    HST_COUNT = 6
    FOLD_CASE_DEFAULT = 0
    FOLD_CASE_EXCLUDE_SPECIAL_I = 1

    def hasBinaryProperty(_codepoint, _property):
        return phpy.call(f"IntlChar::hasBinaryProperty", _codepoint, _property)

    def charAge(_codepoint):
        return phpy.call(f"IntlChar::charAge", _codepoint)

    def charDigitValue(_codepoint):
        return phpy.call(f"IntlChar::charDigitValue", _codepoint)

    def charDirection(_codepoint):
        return phpy.call(f"IntlChar::charDirection", _codepoint)

    def charFromName(_name, _type=0):
        return phpy.call(f"IntlChar::charFromName", _name, _type)

    def charMirror(_codepoint):
        return phpy.call(f"IntlChar::charMirror", _codepoint)

    def charName(_codepoint, _type=0):
        return phpy.call(f"IntlChar::charName", _codepoint, _type)

    def charType(_codepoint):
        return phpy.call(f"IntlChar::charType", _codepoint)

    def chr(_codepoint):
        return phpy.call(f"IntlChar::chr", _codepoint)

    def digit(_codepoint, _base=10):
        return phpy.call(f"IntlChar::digit", _codepoint, _base)

    def enumCharNames(_start, _end, _callback, _type=0):
        return phpy.call(f"IntlChar::enumCharNames", _start, _end, _callback, _type)

    def enumCharTypes(_callback):
        return phpy.call(f"IntlChar::enumCharTypes", _callback)

    def foldCase(_codepoint, _options=0):
        return phpy.call(f"IntlChar::foldCase", _codepoint, _options)

    def forDigit(_digit, _base=10):
        return phpy.call(f"IntlChar::forDigit", _digit, _base)

    def getBidiPairedBracket(_codepoint):
        return phpy.call(f"IntlChar::getBidiPairedBracket", _codepoint)

    def getBlockCode(_codepoint):
        return phpy.call(f"IntlChar::getBlockCode", _codepoint)

    def getCombiningClass(_codepoint):
        return phpy.call(f"IntlChar::getCombiningClass", _codepoint)

    def getFC_NFKC_Closure(_codepoint):
        return phpy.call(f"IntlChar::getFC_NFKC_Closure", _codepoint)

    def getIntPropertyMaxValue(_property):
        return phpy.call(f"IntlChar::getIntPropertyMaxValue", _property)

    def getIntPropertyMinValue(_property):
        return phpy.call(f"IntlChar::getIntPropertyMinValue", _property)

    def getIntPropertyValue(_codepoint, _property):
        return phpy.call(f"IntlChar::getIntPropertyValue", _codepoint, _property)

    def getNumericValue(_codepoint):
        return phpy.call(f"IntlChar::getNumericValue", _codepoint)

    def getPropertyEnum(_alias):
        return phpy.call(f"IntlChar::getPropertyEnum", _alias)

    def getPropertyName(_property, _type=1):
        return phpy.call(f"IntlChar::getPropertyName", _property, _type)

    def getPropertyValueEnum(_property, _name):
        return phpy.call(f"IntlChar::getPropertyValueEnum", _property, _name)

    def getPropertyValueName(_property, _value, _type=1):
        return phpy.call(f"IntlChar::getPropertyValueName", _property, _value, _type)

    def getUnicodeVersion():
        return phpy.call(f"IntlChar::getUnicodeVersion", )

    def isalnum(_codepoint):
        return phpy.call(f"IntlChar::isalnum", _codepoint)

    def isalpha(_codepoint):
        return phpy.call(f"IntlChar::isalpha", _codepoint)

    def isbase(_codepoint):
        return phpy.call(f"IntlChar::isbase", _codepoint)

    def isblank(_codepoint):
        return phpy.call(f"IntlChar::isblank", _codepoint)

    def iscntrl(_codepoint):
        return phpy.call(f"IntlChar::iscntrl", _codepoint)

    def isdefined(_codepoint):
        return phpy.call(f"IntlChar::isdefined", _codepoint)

    def isdigit(_codepoint):
        return phpy.call(f"IntlChar::isdigit", _codepoint)

    def isgraph(_codepoint):
        return phpy.call(f"IntlChar::isgraph", _codepoint)

    def isIDIgnorable(_codepoint):
        return phpy.call(f"IntlChar::isIDIgnorable", _codepoint)

    def isIDPart(_codepoint):
        return phpy.call(f"IntlChar::isIDPart", _codepoint)

    def isIDStart(_codepoint):
        return phpy.call(f"IntlChar::isIDStart", _codepoint)

    def isISOControl(_codepoint):
        return phpy.call(f"IntlChar::isISOControl", _codepoint)

    def isJavaIDPart(_codepoint):
        return phpy.call(f"IntlChar::isJavaIDPart", _codepoint)

    def isJavaIDStart(_codepoint):
        return phpy.call(f"IntlChar::isJavaIDStart", _codepoint)

    def isJavaSpaceChar(_codepoint):
        return phpy.call(f"IntlChar::isJavaSpaceChar", _codepoint)

    def islower(_codepoint):
        return phpy.call(f"IntlChar::islower", _codepoint)

    def isMirrored(_codepoint):
        return phpy.call(f"IntlChar::isMirrored", _codepoint)

    def isprint(_codepoint):
        return phpy.call(f"IntlChar::isprint", _codepoint)

    def ispunct(_codepoint):
        return phpy.call(f"IntlChar::ispunct", _codepoint)

    def isspace(_codepoint):
        return phpy.call(f"IntlChar::isspace", _codepoint)

    def istitle(_codepoint):
        return phpy.call(f"IntlChar::istitle", _codepoint)

    def isUAlphabetic(_codepoint):
        return phpy.call(f"IntlChar::isUAlphabetic", _codepoint)

    def isULowercase(_codepoint):
        return phpy.call(f"IntlChar::isULowercase", _codepoint)

    def isupper(_codepoint):
        return phpy.call(f"IntlChar::isupper", _codepoint)

    def isUUppercase(_codepoint):
        return phpy.call(f"IntlChar::isUUppercase", _codepoint)

    def isUWhiteSpace(_codepoint):
        return phpy.call(f"IntlChar::isUWhiteSpace", _codepoint)

    def isWhitespace(_codepoint):
        return phpy.call(f"IntlChar::isWhitespace", _codepoint)

    def isxdigit(_codepoint):
        return phpy.call(f"IntlChar::isxdigit", _codepoint)

    def ord(_character):
        return phpy.call(f"IntlChar::ord", _character)

    def tolower(_codepoint):
        return phpy.call(f"IntlChar::tolower", _codepoint)

    def totitle(_codepoint):
        return phpy.call(f"IntlChar::totitle", _codepoint)

    def toupper(_codepoint):
        return phpy.call(f"IntlChar::toupper", _codepoint)

    def __init__(self):
        self.__this = phpy.Object(f'IntlChar')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

