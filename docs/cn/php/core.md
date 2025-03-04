# 核心

所有 `Python` 的内置函数均作为 `PyCore` 类的静态方法，内置方法的使用参考 `Python` 文档。

## 导入包
```php
$os = PyCore::import('os');
```

成功后返回一个 `PyModule` 对象。可以导入 `Python` 内置的包，也可以导入其他第三方的包，或者用户自定义的包。

只能加载模块，不支持 `Python` 的 `from module import class` 语法，可用下面的语法代替。

```php
$module = PyCore::import($moduleName);
$class = $m->$className;
```

`Python` 底层会缓存已加载过的模块，当第二次加载时会自动返回缓存中的模块，不会重复加载。因此在 `PHP-FPM/Apache` 
等短生命周期环境下也可使用，不会有性能问题。

## 加载路径
可使用 `PyCore::import('sys')->path->append()` 将一些目录加入到加载路径列表中。
例如：`/workspace/app/user.py` 自定义的包，可以通过下面的步骤实现加载：

1. `PyCore::import('sys')->path->append('/workspace')` 将 `/workspace` 添加到 `sys.path` 中
2. `PyCore::import('app.user')` 将自动搜索 `sys.path` 找到对应的 `app/user.py` 包并载入

## 内置方法
- `PyCore::import($module)` 导入模块
- `PyCore::str()` 将对象转为字符串
- `PyCore::repr()` 
- `PyCore::type()` 获取对象的类型
- `PyCore::locals()` 获取当前空间内容的所有局部变量
- `PyCore::globals()` 获取所有全局变量
- `PyCore::hash()` 获取 Hash 值
- `PyCore::hasattr()` 检测对象是否存在某个属性
- `PyCore::id()` 获取对象的内部编号
- `PyCore::len()` 获取长度
- `PyCore::dir()` 获取对象所有的属性、方法
- `PyCore::int()` 构造一个整数
- `PyCore::float()` 构造一个浮点数
- `PyCore::fn()` 构造一个可调用函数
- `PyCore::eval()` 执行 `Python` 代码
- `PyCore::dict()` 构造一个字典对象
- `PyCore::set()` 构造一个集合对象
- `PyCore::range()` 构造一个范围序列
- `PyCore::scalar($pyobj)` 将 `PyObject` 对象转为 `PHP` 的标量类型，例如 `PyStr` 将转为 `PHP 字符串`，`Dict/Tuple/Set/List` 将转为 `Array`
- `PyCore::fileno($fp)` 获取 `PHP Stream` 资源的文件描述符，请注意仅支持 `tcp/udp/unix` 类型的资源

> `PyCore` 实现了 `__callStatic()` 魔术方法，对于 `PyCore` 静态方法调用会自动调用 `Python` 的 `builtins` 模块对应的方法 ，
> 可参考 [Built-in Functions](https://docs.python.org/3/library/functions.html) 了解更多内置方法的使用

## 动态链接库问题
导入库是发生动态链接库错误，原因可能是 `LD` 路径错误导致，可设置环境变量指定 `Python C 模块` 动态库路径。

> 可使用 `:` 分割设置多个路径

```shell
# 仅使用 anaconda3 base 环境
export LD_LIBRARY_PATH=/opt/anaconda3/lib
# 使用了特别的环境，名称为 cef
export LD_LIBRARY_PATH=/opt/anaconda3/envs/cef/lib:/opt/anaconda3/lib
php plot.php
```

这种方式仅对当前的 `bash` 会话有效，不会影响全局。不要直接修改 `/etc/ld.so.conf.d/*.conf` 增加 `/opt/anaconda3/lib`，这可能会导致
`libc` 库冲突，可能会影响操作系统其他程序的正常运行。

## 大小写敏感
`Python` 中所有函数、方法、变量、属性等均命名全部为大小写敏感，调用时必须使用与`Python`大小写完全一致的名称。

例如：

```python
def TestUser():
    pass
```

在 `PHP` 代码中必须使用 `$module->TestUser()` ，其他的方式如 `$module->testUser()` 、`$module->testuser()` 均是错误的写法。

## 环境变量
在 `phpy` 中 `Python` 的 `os.environ` 未被自动初始化，因此 `environ` 是一个空字典，需要遍历 `$_ENV` 将环境变量注入 `Python` 环境。

```php
$os = PyCore::import('os');
foreach($_ENV as $k => $v) {
    $os->environ->__setitem__($k, $v);
}
```

## undefined symbol:ffi_type_uint32, version LIBFFI_BASE_7.0
动态连接库路径存在冲突问题，可以尝试使用下面的方法解决。
若依然有问题，建议使用系统自带的 `Python` 环境代替 `conda` 创建的环境。

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
```

## Import 失败
大部分情况下，`from a import b` 是等价于 `PyCore::import('a')->b` ，
但有些特殊的库无法通过以上方法正确加载，可替换为以下方法：

```php
# 无法加载
$b = PyCore::import('a')->b;
# 替换为以下代码
$b = PyCore::import('a.b');
```

## 内置类型
某些情况下，我们需要将类型作为参数传递给 `Python` 函数，可使用`PyCore::type()`实现。

```php
$type_int = PyCore::type(0);
$type_float = PyCore::type(3.14);
$type_str = PyCore::type('hello');
$type_list = PyCore::type([1, 2, 3]);
$type_dict = PyCore::type(['a' => 1, 'b' => 2]);
$type_tuple = PyCore::type([1, 2, 3]);
$type_null = PyCore::type(null);
$type_bool = PyCore::type(true);
```

`PyCore::type()` 返回一个 `PyType` 对象，可用于传递给 `Python` 函数。`PyType` 对象作为
函数调用，可再次构造一个新的`Python`对象。

```php
$value = $type_int(100);
```