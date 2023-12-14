# 封装模块
 `phpy` 使用反射工具自动将所有 `PHP` 扩展函数和类生成了封装模块，包名称为 `php` 可以直接使用
 
```python
from php import [ext-name]
```

来导入 `PHP` 扩展中定义的常量、函数、类。


## 命名规则
- 模块名称全部使用小写，例如 `PDO` ，对应的模块为 `php.pdo`
- 标准库函数在 `php.std` 模块中，例如 `php.std.file_get_contents()`
- 语言核心函数在 `php.core` 模块中，例如 `php.core.get_included_files()`
- 函数前缀与扩展名称一致时，则省略扩展名称前缀，例如 `php.curl.curl_init()` 应简写为 `php.curl.init()`
- 类名使用命名空间并且与扩展名称一致时，将转为驼峰类名，例如 `Swoole\Http\Server` 为 `php.swoole.HttpServer`
- 函数名称使用了命名空间，将转为蛇形函数名，例如 `MongoDB\BSON\fromJSON` 为 `php.mongodb.bson_fromjson`
- 函数或方法名称是 `Python` 关键词，将自动添加下划线前缀，例如 `gmp_import` 为 `php.gmp._import`

## 对象实例

```python
from php import redis

db = redis.Redis()
db.connect("127.0.0.1", 6379, -1)
db.set("key", "swoole")
print(db.get("key"))
```

## 函数实例

```python
from php import std
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = std.stream_socket_client('tcp://127.0.0.1:9999', errno, errstr, 30)
```
