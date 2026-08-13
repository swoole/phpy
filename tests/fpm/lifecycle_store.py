"""Process-global storage used by the PHP-FPM request lifecycle test."""

import gc


retained = []
retained_array = None


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
