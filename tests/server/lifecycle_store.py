"""Process-global storage used by the PHP server lifecycle test."""

import gc


retained = []
retained_array = None
internal_class = None
user_class = None


def retain(*values):
    global retained
    retained = list(values)
    return [type(value).__name__ for value in retained]


def release():
    global retained
    count = len(retained)
    retained = []
    gc.collect()
    return count


def create_request_array():
    global retained_array
    # The Python object survives in this process-global module, while the
    # underlying Zend array belongs to the current PHP request.
    import phpy
    retained_array = phpy.Array({"key": "request value"})
    return retained_array.get("key")


def read_expired_array():
    global retained_array
    value = retained_array.get("key")
    retained_array = None
    gc.collect()
    return value


def retain_classes():
    global internal_class, user_class
    import phpy
    internal_class = phpy.Class("stdClass")
    user_class = phpy.Class("RequestScopedClass")
    return [type(internal_class).__name__, type(user_class).__name__]


def inspect_classes():
    internal_object = internal_class.new()
    try:
        user_class.new()
    except RuntimeError as error:
        user_error = str(error)
    else:
        user_error = None
    return {
        "internal_object": type(internal_object).__name__,
        "user_error": user_error,
    }
