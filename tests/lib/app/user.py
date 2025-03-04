from enum import Enum


def test():
    print("app.user.main.test()")


storage = {}


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class KvReadonly:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.d = {
            self.v1: 123456,
            self.v2: "hello",
        }

    def __getitem__(self, key):
        return self.d.get(key)

    def exists(self, key):
        return key in self.d


class Kv(KvReadonly):
    def __setitem__(self, key, value):
        self.d[key] = value


class KvCount(KvReadonly):
    def __len__(self):
        return len(self.d)


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


def test_redis(redis):
    redis.set('name', 'hello phpy')
    return redis.get('name')


def test_str_concat(a, b):
    return a + b


def test_raise(fn):
    try:
        fn()
    except StopIteration as e:
        return 'StopIteration'
    except TypeError as e:
        return [1, 2, 3, 4]
    except Exception as e:
        return str(e)
