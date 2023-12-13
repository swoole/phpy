import phpy



def alnum(_text):
    return phpy.call('ctype_alnum', _text)


def alpha(_text):
    return phpy.call('ctype_alpha', _text)


def cntrl(_text):
    return phpy.call('ctype_cntrl', _text)


def digit(_text):
    return phpy.call('ctype_digit', _text)


def lower(_text):
    return phpy.call('ctype_lower', _text)


def graph(_text):
    return phpy.call('ctype_graph', _text)


def print(_text):
    return phpy.call('ctype_print', _text)


def punct(_text):
    return phpy.call('ctype_punct', _text)


def space(_text):
    return phpy.call('ctype_space', _text)


def upper(_text):
    return phpy.call('ctype_upper', _text)


def xdigit(_text):
    return phpy.call('ctype_xdigit', _text)




