
# PyObject
`PyObject` 是除了 `PyCore` 之外，所有其他类型的基类。非内置类的对象是 `PyObject` 的实例。`PyObject` 实现了 `4` 个魔术方法，用于将操作映射到 `Python` 对象。

所有类方法、参数、返回值参考 `stubs` 目录中的文件，文档不再介绍。

## 内置类
- `PyObject`：所有其他类型的基类
- `PyDict`：字典类型，等同于 `PHP` 的关联数组
- `PyList`：列表类型，等同于 `PHP` 的索引数组
- `PyTuple`：元组，不可变的列表
- `PyStr`：字符串
- `PyModule`：`Python` 包，`PyModule` 也是 `PyObject` 的子类

## 继承关系

```
PyObject -> PyModule
         -> PySequenece -> PyList
                        -> PyTuple
         -> PySet
         -> PyStr
         -> PyDict
         -> PyType
```

## __get($name)
读取 `Python` 对象的属性，以下操作是等价的

```php
$pyobj->attr;
```

```py
pyobj.attr
```

## __set($name, $value)

设置 `Python` 对象的属性，以下操作是等价的

```php
$pyobj->attr = 'hello';
```

```py
pyobj.attr = 'hello'
```

## __call($name, $args)

调用 `Python` 对象的方法，以下操作是等价的

```php
$pyobj->fn($a, $b, $c);
```

```py
pyobj.fn(a, b, c)
```

## __invoke(...$args)

执行 `callable` 对象，通常用于执行函数、构造对象。以下操作是等价的

```php
// $user 是一个 PyModule
$user = PyCore::import('app.user');
// Info 是 app.user 中的一个类
$Info = $user->Info;
// 创建一个 Info 对象
$info = $Info('Rango', 2023);
```

```py
from app.user import Info

// 创建一个 Info 对象
info = Info('Rango', 2023);
```

## 命名参数
支持命名参数写法。实例：

### 传入命名参数
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

- 顺序参数必须在前，命名参数必须在最后

### 接收命名参数
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### 可变命名参数
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}
```
- `$kwargs` 将包含顺序参数和命名参数两部分，例如刚才的例子中就或获得
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### 透传命名参数
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

可将命名参数传递给另外函数。

## 切片语法
支持切片语法，使用`PyCore::slice($a, $b, $c = null)` 构建切片对象，作为数组的`Key`传递给对象即可。

### 实例：
```php
$s = new PyStr("Python Programming")

# 获取前三个字符
# Python: print(s[0:3])
PyCore::print($s[PyCore::slice(0, 3)]);  # 输出: "Pyt"

# 获取从索引 7 到索引 12 的字符
# Python: print(s[7:12])  # 输出: "Progr"
PyCore::print($s[PyCore::slice(7, 12)]);  # 输出: "Progr"

# 获取整个字符串
# Python: print(s[:])  # 输出: "Python Programming"
PyCore::print($s[PyCore::slice()]);  # 输出: "Python Programming

# 使用步长
# Python: print(s[::2])  # 输出: "Pto rgamn"（每两个字符取一个）
PyCore::print($s[PyCore::slice(null, null, 2)]);  # 输出: "Pto rgamn"

# 反向切片
# Python: print(s[::-1])  # 输出: "gnimmargorP nohtyP"（字符串反转）
PyCore::print($s[PyCore::slice(null, null, -1)]);  # 输出: "gnimmargorP nohtyP"

# 获取最后一个字符
# Python: print(s[-1])  # 输出: "g"
PyCore::print($s[PyCore::slice(-1)]);  # 输出: "g"

# 获取倒数第三个到倒数第一个字符
# Python: print(s[-3:-1])  # 输出: "mi"
PyCore::print($s[PyCore::slice(-3, -1)]);  # 输出: "mi"
```