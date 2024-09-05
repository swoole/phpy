def wrap(fn):
    return lambda *args, **kwargs: fn(*args, **kwargs)
