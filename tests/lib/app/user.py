from enum import Enum


def test():
    print("app.user.main.test()")


storage = {}


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class User:
    def __init__(self, name):
        self._name = name

    def echo(self):
        print(self._name)

    def getName(self):
        return self._name

    def kwargs(self, a, b, name='default_name', value='default_value', date='default_date'):
        print(a, b)
        print(name, value, date)

    def __getattr__(self, item):
        print(item)
        return "call __getattr__\n"


class KwargsCtor:
    args: dict

    def __init__(self, a, b, name='default_name', value='default_value', date='default_date'):
        self.args = {
            'a': a,
            'b': b,
            'name': name,
            'value': value,
            'date': date
        }


def test_callback(cb):
    return cb(__name__)


def lazy_square(limit):
    for x in range(1, limit + 1):
        yield x, x ** 2


def get_type(d, k):
    return repr(d[k])
