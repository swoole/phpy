# Module Encapsulation
 `phpy` automatically generates encapsulated modules for all `PHP` extension functions and classes using reflection tools. The package name is `php` and can be used directly.
 
```python
from php import [ext-name]
```

to import constants, functions, and classes defined in the `PHP` extension.


## Naming Conventions
- Module names are all lowercase, for example, `PDO`, corresponds to the module `php.pdo`.
- Standard library functions are in the `php.std` module, for example, `php.std.file_get_contents()`.
- Core language functions are in the `php.core` module, for example, `php.core.get_included_files()`.
- When the function prefix matches the extension name, the extension name prefix can be omitted, for example, `php.curl.curl_init()` can be abbreviated as `php.curl.init()`.
- When a class name uses a namespace and matches the extension name, it will be converted to camel case, for example, `Swoole\Http\Server` becomes `php.swoole.HttpServer`.
- When a function name uses a namespace, it will be converted to snake case, for example, `MongoDB\BSON\fromJSON` becomes `php.mongodb.bson_fromjson`.
- If a function or method name conflicts with a Python keyword, an underscore prefix will be automatically added, for example, `gmp_import` becomes `php.gmp._import`.

## Object Instance

```python
from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
```

## Function Instance

```python
from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)
```