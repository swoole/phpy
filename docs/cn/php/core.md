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
- `PyCore::scalar()` 将 `PyObject` 对象转为 `PHP` 的标量类型，例如 `PyStr` 将转为 `PHP 字符串`，`Dict/Tuple/Set/List` 将转为 `Array`

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
请注意 `Python` 中所有函数、方法、变量、属性等均命名全部为大小写敏感，调用时必须使用与`Python`大小写完全一致的名称。

例如：

```python
def TestUser():
    pass
```

在 `PHP` 代码中必须使用 `$module->TestUser()` ，其他的方式如 `$module->testUser()` 、`$module->testuser()` 均是错误的写法。
