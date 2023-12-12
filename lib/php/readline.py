import phpy

LIB = "readline"


def readline(_prompt=None):
    return phpy.call('readline', _prompt)


def info(_var_name=None, _value=None):
    return phpy.call('readline_info', _var_name, _value)


def add_history(_prompt):
    return phpy.call('readline_add_history', _prompt)


def clear_history():
    return phpy.call('readline_clear_history', )


def list_history():
    return phpy.call('readline_list_history', )


def read_history(_filename=None):
    return phpy.call('readline_read_history', _filename)


def write_history(_filename=None):
    return phpy.call('readline_write_history', _filename)


def completion_function(_callback):
    return phpy.call('readline_completion_function', _callback)


def callback_handler_install(_prompt, _callback):
    return phpy.call('readline_callback_handler_install', _prompt, _callback)


def callback_read_char():
    return phpy.call('readline_callback_read_char', )


def callback_handler_remove():
    return phpy.call('readline_callback_handler_remove', )


def redisplay():
    return phpy.call('readline_redisplay', )


def on_new_line():
    return phpy.call('readline_on_new_line', )




