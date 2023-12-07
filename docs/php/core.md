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

## 加载路径
可使用 `PyCore::import('sys')->path->append()` 将一些目录加入到加载路径列表中。
例如：`/workspace/app/user.py` 自定义的包，可以通过下面的步骤实现加载：

1. `PyCore::import('sys')->path->append('/workspace')` 将 `/workspace` 添加到 `sys.path` 中
2. `PyCore::import('app.user')` 将自动搜索 `sys.path` 找到对应的 `app/user.py` 包并载入


## 内置方法
- `PyCore::import($module)` 导入模块
- `PyCore::storage($key, $pyobject)` 持久化存储 `Python` 对象
- `PyCore::fetch($key)` 从全局缓存中获取持久化存储的 `Python` 对象
- `PyCore::remove($key)` 从全局缓存中删除 `Python` 对象
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


## 在 `Apache/PHP-FPM` 短生命周期环境下使用

短生命周期运行环境下使用，需要将 `import` 的模块缓存起来，否则频繁地导入/销毁模块的开销会消耗大量资源。

```php
function import_with_cache($module_name) {
    $module = PyCore::fetch('module_' . $module_name);
    if (!$module) {
        $module = PyCore::import($module_name);
        PyCore::storage('module_' . $module_name, $module);
    }
    return $module;
}

$os = import_with_cache('os');
```

此函数使用了 `PyCore::fetch/storage` 方法，获取和保存 `PyObject`，它将不受 `ZendVM` 的生命周期控制。
保存到全局缓存中的对象不会在请求结束后销毁，而是在进程的整个生命周期内持久存在。这可能会导致内存泄露，请务必要谨慎使用。

**请勿将 `PHP 对象` 保存到全局缓存，否则将会造成内存错误，导致进程崩溃。**
