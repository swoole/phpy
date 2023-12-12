import phpy

ANY_SCALAR_STYLE = 0
PLAIN_SCALAR_STYLE = 1
SINGLE_QUOTED_SCALAR_STYLE = 2
DOUBLE_QUOTED_SCALAR_STYLE = 3
LITERAL_SCALAR_STYLE = 4
FOLDED_SCALAR_STYLE = 5
NULL_TAG = "tag:yaml.org,2002:null"
BOOL_TAG = "tag:yaml.org,2002:bool"
STR_TAG = "tag:yaml.org,2002:str"
INT_TAG = "tag:yaml.org,2002:int"
FLOAT_TAG = "tag:yaml.org,2002:float"
TIMESTAMP_TAG = "tag:yaml.org,2002:timestamp"
SEQ_TAG = "tag:yaml.org,2002:seq"
MAP_TAG = "tag:yaml.org,2002:map"
PHP_TAG = "!php/object"
MERGE_TAG = "tag:yaml.org,2002:merge"
BINARY_TAG = "tag:yaml.org,2002:binary"
ANY_ENCODING = 0
UTF8_ENCODING = 1
UTF16LE_ENCODING = 2
UTF16BE_ENCODING = 3
ANY_BREAK = 0
CR_BREAK = 1
LN_BREAK = 2
CRLN_BREAK = 3


def parse(_input, _pos=None, _ndocs=None, _callbacks=None):
    return phpy.call('yaml_parse', _input, _pos, _ndocs, _callbacks)


def parse_file(_filename, _pos=None, _ndocs=None, _callbacks=None):
    return phpy.call('yaml_parse_file', _filename, _pos, _ndocs, _callbacks)


def parse_url(_url, _pos=None, _ndocs=None, _callbacks=None):
    return phpy.call('yaml_parse_url', _url, _pos, _ndocs, _callbacks)


def emit(_data, _encoding=None, _linebreak=None, _callbacks=None):
    return phpy.call('yaml_emit', _data, _encoding, _linebreak, _callbacks)


def emit_file(_filename, _data, _encoding=None, _linebreak=None, _callbacks=None):
    return phpy.call('yaml_emit_file', _filename, _data, _encoding, _linebreak, _callbacks)




