import phpy

ERROR_NONE = 0
ERROR_NO_MEMORY = 1
ERROR_SYNTAX = 2
ERROR_NO_ELEMENTS = 3
ERROR_INVALID_TOKEN = 4
ERROR_UNCLOSED_TOKEN = 5
ERROR_PARTIAL_CHAR = 6
ERROR_TAG_MISMATCH = 7
ERROR_DUPLICATE_ATTRIBUTE = 8
ERROR_JUNK_AFTER_DOC_ELEMENT = 9
ERROR_PARAM_ENTITY_REF = 10
ERROR_UNDEFINED_ENTITY = 11
ERROR_RECURSIVE_ENTITY_REF = 12
ERROR_ASYNC_ENTITY = 13
ERROR_BAD_CHAR_REF = 14
ERROR_BINARY_ENTITY_REF = 15
ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF = 16
ERROR_MISPLACED_XML_PI = 17
ERROR_UNKNOWN_ENCODING = 18
ERROR_INCORRECT_ENCODING = 19
ERROR_UNCLOSED_CDATA_SECTION = 20
ERROR_EXTERNAL_ENTITY_HANDLING = 21
OPTION_CASE_FOLDING = 1
OPTION_TARGET_ENCODING = 2
OPTION_SKIP_TAGSTART = 3
OPTION_SKIP_WHITE = 4
SAX_IMPL = "libxml"


def parser_create(_encoding=None):
    return phpy.call('xml_parser_create', _encoding)


def parser_create_ns(_encoding=None, _separator=":"):
    return phpy.call('xml_parser_create_ns', _encoding, _separator)


def set_object(_parser, _object):
    return phpy.call('xml_set_object', _parser, _object)


def set_element_handler(_parser, _start_handler, _end_handler):
    return phpy.call('xml_set_element_handler', _parser, _start_handler, _end_handler)


def set_character_data_handler(_parser, _handler):
    return phpy.call('xml_set_character_data_handler', _parser, _handler)


def set_processing_instruction_handler(_parser, _handler):
    return phpy.call('xml_set_processing_instruction_handler', _parser, _handler)


def set_default_handler(_parser, _handler):
    return phpy.call('xml_set_default_handler', _parser, _handler)


def set_unparsed_entity_decl_handler(_parser, _handler):
    return phpy.call('xml_set_unparsed_entity_decl_handler', _parser, _handler)


def set_notation_decl_handler(_parser, _handler):
    return phpy.call('xml_set_notation_decl_handler', _parser, _handler)


def set_external_entity_ref_handler(_parser, _handler):
    return phpy.call('xml_set_external_entity_ref_handler', _parser, _handler)


def set_start_namespace_decl_handler(_parser, _handler):
    return phpy.call('xml_set_start_namespace_decl_handler', _parser, _handler)


def set_end_namespace_decl_handler(_parser, _handler):
    return phpy.call('xml_set_end_namespace_decl_handler', _parser, _handler)


def parse(_parser, _data, _is_final=False):
    return phpy.call('xml_parse', _parser, _data, _is_final)


def parse_into_struct(_parser, _data, _values, _index=None):
    return phpy.call('xml_parse_into_struct', _parser, _data, _values, _index)


def get_error_code(_parser):
    return phpy.call('xml_get_error_code', _parser)


def error_string(_error_code):
    return phpy.call('xml_error_string', _error_code)


def get_current_line_number(_parser):
    return phpy.call('xml_get_current_line_number', _parser)


def get_current_column_number(_parser):
    return phpy.call('xml_get_current_column_number', _parser)


def get_current_byte_index(_parser):
    return phpy.call('xml_get_current_byte_index', _parser)


def parser_free(_parser):
    return phpy.call('xml_parser_free', _parser)


def parser_set_option(_parser, _option, _value):
    return phpy.call('xml_parser_set_option', _parser, _option, _value)


def parser_get_option(_parser, _option):
    return phpy.call('xml_parser_get_option', _parser, _option)




