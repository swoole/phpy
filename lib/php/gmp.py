import phpy

ROUND_ZERO = 0
ROUND_PLUSINF = 1
ROUND_MINUSINF = 2
VERSION = "6.2.1"
MSW_FIRST = 1
LSW_FIRST = 2
LITTLE_ENDIAN = 4
BIG_ENDIAN = 8
NATIVE_ENDIAN = 16


def init(_num, _base=0):
    return phpy.call('gmp_init', _num, _base)


def _import(_data, _word_size=1, _flags=17):
    return phpy.call('gmp_import', _data, _word_size, _flags)


def export(_num, _word_size=1, _flags=17):
    return phpy.call('gmp_export', _num, _word_size, _flags)


def intval(_num):
    return phpy.call('gmp_intval', _num)


def strval(_num, _base=10):
    return phpy.call('gmp_strval', _num, _base)


def add(_num1, _num2):
    return phpy.call('gmp_add', _num1, _num2)


def sub(_num1, _num2):
    return phpy.call('gmp_sub', _num1, _num2)


def mul(_num1, _num2):
    return phpy.call('gmp_mul', _num1, _num2)


def div_qr(_num1, _num2, _rounding_mode=0):
    return phpy.call('gmp_div_qr', _num1, _num2, _rounding_mode)


def div_q(_num1, _num2, _rounding_mode=0):
    return phpy.call('gmp_div_q', _num1, _num2, _rounding_mode)


def div_r(_num1, _num2, _rounding_mode=0):
    return phpy.call('gmp_div_r', _num1, _num2, _rounding_mode)


def div(_num1, _num2, _rounding_mode=0):
    return phpy.call('gmp_div', _num1, _num2, _rounding_mode)


def mod(_num1, _num2):
    return phpy.call('gmp_mod', _num1, _num2)


def divexact(_num1, _num2):
    return phpy.call('gmp_divexact', _num1, _num2)


def neg(_num):
    return phpy.call('gmp_neg', _num)


def abs(_num):
    return phpy.call('gmp_abs', _num)


def fact(_num):
    return phpy.call('gmp_fact', _num)


def sqrt(_num):
    return phpy.call('gmp_sqrt', _num)


def sqrtrem(_num):
    return phpy.call('gmp_sqrtrem', _num)


def root(_num, _nth):
    return phpy.call('gmp_root', _num, _nth)


def rootrem(_num, _nth):
    return phpy.call('gmp_rootrem', _num, _nth)


def pow(_num, _exponent):
    return phpy.call('gmp_pow', _num, _exponent)


def powm(_num, _exponent, _modulus):
    return phpy.call('gmp_powm', _num, _exponent, _modulus)


def perfect_square(_num):
    return phpy.call('gmp_perfect_square', _num)


def perfect_power(_num):
    return phpy.call('gmp_perfect_power', _num)


def prob_prime(_num, _repetitions=10):
    return phpy.call('gmp_prob_prime', _num, _repetitions)


def gcd(_num1, _num2):
    return phpy.call('gmp_gcd', _num1, _num2)


def gcdext(_num1, _num2):
    return phpy.call('gmp_gcdext', _num1, _num2)


def lcm(_num1, _num2):
    return phpy.call('gmp_lcm', _num1, _num2)


def invert(_num1, _num2):
    return phpy.call('gmp_invert', _num1, _num2)


def jacobi(_num1, _num2):
    return phpy.call('gmp_jacobi', _num1, _num2)


def legendre(_num1, _num2):
    return phpy.call('gmp_legendre', _num1, _num2)


def kronecker(_num1, _num2):
    return phpy.call('gmp_kronecker', _num1, _num2)


def cmp(_num1, _num2):
    return phpy.call('gmp_cmp', _num1, _num2)


def sign(_num):
    return phpy.call('gmp_sign', _num)


def random_seed(_seed):
    return phpy.call('gmp_random_seed', _seed)


def random_bits(_bits):
    return phpy.call('gmp_random_bits', _bits)


def random_range(_min, _max):
    return phpy.call('gmp_random_range', _min, _max)


def _and(_num1, _num2):
    return phpy.call('gmp_and', _num1, _num2)


def _or(_num1, _num2):
    return phpy.call('gmp_or', _num1, _num2)


def com(_num):
    return phpy.call('gmp_com', _num)


def xor(_num1, _num2):
    return phpy.call('gmp_xor', _num1, _num2)


def setbit(_num, _index, _value=True):
    return phpy.call('gmp_setbit', _num, _index, _value)


def clrbit(_num, _index):
    return phpy.call('gmp_clrbit', _num, _index)


def testbit(_num, _index):
    return phpy.call('gmp_testbit', _num, _index)


def scan0(_num1, _start):
    return phpy.call('gmp_scan0', _num1, _start)


def scan1(_num1, _start):
    return phpy.call('gmp_scan1', _num1, _start)


def popcount(_num):
    return phpy.call('gmp_popcount', _num)


def hamdist(_num1, _num2):
    return phpy.call('gmp_hamdist', _num1, _num2)


def nextprime(_num):
    return phpy.call('gmp_nextprime', _num)


def binomial(_n, _k):
    return phpy.call('gmp_binomial', _n, _k)




class GMP():


    def __serialize(self):
        return self.__this.call(f"__serialize", )

    def __unserialize(self, _data):
        return self.__this.call(f"__unserialize", _data)

    def __init__(self):
        self.__this = phpy.Object(f'GMP')


