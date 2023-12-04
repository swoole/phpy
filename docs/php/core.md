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

有些 `Python` 模块，使用了特殊的加载机制，导致无法使用上面的语法实现，例如 `transformers` 自己实现了一套 `LazyModule` 的加载器
这种情况请使用 `$class = $m->__getattr__($className);` 来加载模块中定义的类

## 加载路径
可使用 `PyCore::import('sys')->path->append()` 将一些目录加入到加载路径列表中。
例如：`/workspace/app/user.py` 自定义的包，可以通过下面的步骤实现加载：

1. `PyCore::import('sys')->path->append('/workspace')` 将 `/workspace` 添加到 `sys.path` 中
2. `PyCore::import('app.user')` 将自动搜索 `sys.path` 找到对应的 `app/user.py` 包并载入


## 内置方法
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
- `PyCore::scalar()` 将 `PyObject` 对象转为 `PHP` 的标量类型，例如 `PyStr` 将转为 `PHP 字符串`，`Dict/Tuple/Set/List` 将转为 `Array`
