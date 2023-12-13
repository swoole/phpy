import phpy

MB_CASE_UPPER = 0
MB_CASE_LOWER = 1
MB_CASE_TITLE = 2
MB_CASE_FOLD = 3
MB_CASE_UPPER_SIMPLE = 4
MB_CASE_LOWER_SIMPLE = 5
MB_CASE_TITLE_SIMPLE = 6
MB_CASE_FOLD_SIMPLE = 7
MB_ONIGURUMA_VERSION = "6.9.7"


def mb_language(_language=None):
    return phpy.call('mb_language', _language)


def mb_internal_encoding(_encoding=None):
    return phpy.call('mb_internal_encoding', _encoding)


def mb_http_input(_type=None):
    return phpy.call('mb_http_input', _type)


def mb_http_output(_encoding=None):
    return phpy.call('mb_http_output', _encoding)


def mb_detect_order(_encoding=None):
    return phpy.call('mb_detect_order', _encoding)


def mb_substitute_character(_substitute_character=None):
    return phpy.call('mb_substitute_character', _substitute_character)


def mb_preferred_mime_name(_encoding):
    return phpy.call('mb_preferred_mime_name', _encoding)


def mb_parse_str(_string, _result):
    return phpy.call('mb_parse_str', _string, _result)


def mb_output_handler(_string, _status):
    return phpy.call('mb_output_handler', _string, _status)


def mb_str_split(_string, _length=1, _encoding=None):
    return phpy.call('mb_str_split', _string, _length, _encoding)


def mb_strlen(_string, _encoding=None):
    return phpy.call('mb_strlen', _string, _encoding)


def mb_strpos(_haystack, _needle, _offset=0, _encoding=None):
    return phpy.call('mb_strpos', _haystack, _needle, _offset, _encoding)


def mb_strrpos(_haystack, _needle, _offset=0, _encoding=None):
    return phpy.call('mb_strrpos', _haystack, _needle, _offset, _encoding)


def mb_stripos(_haystack, _needle, _offset=0, _encoding=None):
    return phpy.call('mb_stripos', _haystack, _needle, _offset, _encoding)


def mb_strripos(_haystack, _needle, _offset=0, _encoding=None):
    return phpy.call('mb_strripos', _haystack, _needle, _offset, _encoding)


def mb_strstr(_haystack, _needle, _before_needle=False, _encoding=None):
    return phpy.call('mb_strstr', _haystack, _needle, _before_needle, _encoding)


def mb_strrchr(_haystack, _needle, _before_needle=False, _encoding=None):
    return phpy.call('mb_strrchr', _haystack, _needle, _before_needle, _encoding)


def mb_stristr(_haystack, _needle, _before_needle=False, _encoding=None):
    return phpy.call('mb_stristr', _haystack, _needle, _before_needle, _encoding)


def mb_strrichr(_haystack, _needle, _before_needle=False, _encoding=None):
    return phpy.call('mb_strrichr', _haystack, _needle, _before_needle, _encoding)


def mb_substr_count(_haystack, _needle, _encoding=None):
    return phpy.call('mb_substr_count', _haystack, _needle, _encoding)


def mb_substr(_string, _start, _length=None, _encoding=None):
    return phpy.call('mb_substr', _string, _start, _length, _encoding)


def mb_strcut(_string, _start, _length=None, _encoding=None):
    return phpy.call('mb_strcut', _string, _start, _length, _encoding)


def mb_strwidth(_string, _encoding=None):
    return phpy.call('mb_strwidth', _string, _encoding)


def mb_strimwidth(_string, _start, _width, _trim_marker="", _encoding=None):
    return phpy.call('mb_strimwidth', _string, _start, _width, _trim_marker, _encoding)


def mb_convert_encoding(_string, _to_encoding, _from_encoding=None):
    return phpy.call('mb_convert_encoding', _string, _to_encoding, _from_encoding)


def mb_convert_case(_string, _mode, _encoding=None):
    return phpy.call('mb_convert_case', _string, _mode, _encoding)


def mb_strtoupper(_string, _encoding=None):
    return phpy.call('mb_strtoupper', _string, _encoding)


def mb_strtolower(_string, _encoding=None):
    return phpy.call('mb_strtolower', _string, _encoding)


def mb_detect_encoding(_string, _encodings=None, _strict=False):
    return phpy.call('mb_detect_encoding', _string, _encodings, _strict)


def mb_list_encodings():
    return phpy.call('mb_list_encodings', )


def mb_encoding_aliases(_encoding):
    return phpy.call('mb_encoding_aliases', _encoding)


def mb_encode_mimeheader(_string, _charset=None, _transfer_encoding=None, _newline="\r\n", _indent=0):
    return phpy.call('mb_encode_mimeheader', _string, _charset, _transfer_encoding, _newline, _indent)


def mb_decode_mimeheader(_string):
    return phpy.call('mb_decode_mimeheader', _string)


def mb_convert_kana(_string, _mode="KV", _encoding=None):
    return phpy.call('mb_convert_kana', _string, _mode, _encoding)


def mb_convert_variables(_to_encoding, _from_encoding, _var, _vars=None):
    return phpy.call('mb_convert_variables', _to_encoding, _from_encoding, _var, _vars)


def mb_encode_numericentity(_string, _map, _encoding=None, _hex=False):
    return phpy.call('mb_encode_numericentity', _string, _map, _encoding, _hex)


def mb_decode_numericentity(_string, _map, _encoding=None):
    return phpy.call('mb_decode_numericentity', _string, _map, _encoding)


def mb_send_mail(_to, _subject, _message, _additional_headers=[], _additional_params=None):
    return phpy.call('mb_send_mail', _to, _subject, _message, _additional_headers, _additional_params)


def mb_get_info(_type="all"):
    return phpy.call('mb_get_info', _type)


def mb_check_encoding(_value=None, _encoding=None):
    return phpy.call('mb_check_encoding', _value, _encoding)


def mb_scrub(_string, _encoding=None):
    return phpy.call('mb_scrub', _string, _encoding)


def mb_ord(_string, _encoding=None):
    return phpy.call('mb_ord', _string, _encoding)


def mb_chr(_codepoint, _encoding=None):
    return phpy.call('mb_chr', _codepoint, _encoding)


def mb_regex_encoding(_encoding=None):
    return phpy.call('mb_regex_encoding', _encoding)


def mb_ereg(_pattern, _string, _matches=None):
    return phpy.call('mb_ereg', _pattern, _string, _matches)


def mb_eregi(_pattern, _string, _matches=None):
    return phpy.call('mb_eregi', _pattern, _string, _matches)


def mb_ereg_replace(_pattern, _replacement, _string, _options=None):
    return phpy.call('mb_ereg_replace', _pattern, _replacement, _string, _options)


def mb_eregi_replace(_pattern, _replacement, _string, _options=None):
    return phpy.call('mb_eregi_replace', _pattern, _replacement, _string, _options)


def mb_ereg_replace_callback(_pattern, _callback, _string, _options=None):
    return phpy.call('mb_ereg_replace_callback', _pattern, _callback, _string, _options)


def mb_split(_pattern, _string, _limit=-1):
    return phpy.call('mb_split', _pattern, _string, _limit)


def mb_ereg_match(_pattern, _string, _options=None):
    return phpy.call('mb_ereg_match', _pattern, _string, _options)


def mb_ereg_search(_pattern=None, _options=None):
    return phpy.call('mb_ereg_search', _pattern, _options)


def mb_ereg_search_pos(_pattern=None, _options=None):
    return phpy.call('mb_ereg_search_pos', _pattern, _options)


def mb_ereg_search_regs(_pattern=None, _options=None):
    return phpy.call('mb_ereg_search_regs', _pattern, _options)


def mb_ereg_search_init(_string, _pattern=None, _options=None):
    return phpy.call('mb_ereg_search_init', _string, _pattern, _options)


def mb_ereg_search_getregs():
    return phpy.call('mb_ereg_search_getregs', )


def mb_ereg_search_getpos():
    return phpy.call('mb_ereg_search_getpos', )


def mb_ereg_search_setpos(_offset):
    return phpy.call('mb_ereg_search_setpos', _offset)


def mb_regex_set_options(_options=None):
    return phpy.call('mb_regex_set_options', _options)




