import phpy



def bcadd(_num1, _num2, _scale=None):
    return phpy.call('bcadd', _num1, _num2, _scale)


def bcsub(_num1, _num2, _scale=None):
    return phpy.call('bcsub', _num1, _num2, _scale)


def bcmul(_num1, _num2, _scale=None):
    return phpy.call('bcmul', _num1, _num2, _scale)


def bcdiv(_num1, _num2, _scale=None):
    return phpy.call('bcdiv', _num1, _num2, _scale)


def bcmod(_num1, _num2, _scale=None):
    return phpy.call('bcmod', _num1, _num2, _scale)


def bcpowmod(_num, _exponent, _modulus, _scale=None):
    return phpy.call('bcpowmod', _num, _exponent, _modulus, _scale)


def bcpow(_num, _exponent, _scale=None):
    return phpy.call('bcpow', _num, _exponent, _scale)


def bcsqrt(_num, _scale=None):
    return phpy.call('bcsqrt', _num, _scale)


def bccomp(_num1, _num2, _scale=None):
    return phpy.call('bccomp', _num1, _num2, _scale)


def bcscale(_scale=None):
    return phpy.call('bcscale', _scale)




