# 内存拷贝

`PHP` 调用 `Python` 函数/方法时，参数、返回值将可能存在内存拷贝，在编写性能敏感的程序时需要关注内存复制的开销。

## 参数
- 整型、布尔型、浮点型、空值 （`null`）始终为值传递
- 对象、资源、引用，始终为引用传递，不会复制内存
- 字符串、数组，将进行递归深拷贝转为原生类型

```php 
$user = PyCore::import("user");
$arg1 = 1234;
$arg2 = 1234.5678;
$arg3 = true;

$arg4 = new PyDict();
$arg5 = new stdClass();
$arg6 = fopen("php://input", "r");

$arg7 = ['hello' => 'world'];
$arg8 = "hello world";
$arg9 = [1, 2, 3, 4, 5];

$user->test($arg1, $arg2, $arg3, $arg4, $arg5, $arg6, $arg7, $arg8, $arg9);
```

- `$arg1`、`$arg2`、`$arg3` 将转为 `Python` 中的整型、浮点型、布尔型，直接复制数值
- `$arg4`、`$arg5`、`$arg6` 将直接传递引用到 `Python` 中，不会产生内存拷贝
- `$arg6`、`$arg7`、`$arg8` 将遍历、深度内存拷贝，并转为 `Python` 的 `list`、 `dict`、`str`

## 返回值
- 整型、布尔型、浮点型、空值（`None` 和 `null`）将转为 `PHP` 的原生类型
- 其他从 `Python` 中返回的内容全部为 `PyObject` 类型
- 也可以在 `Python` 代码中直接使用 `phpy.String` 或 `phpy.Array` 等 `PHP` 原生类型实现透明转发传递

## 避免内存复制
使用 `PyObject::object($value)` 方法可将字符串、数组类型转为 `PyObject`，在 `Python` 代码中得到的类型是
`phpy.String` 和 `phpy.Array`。

这种方式需要 `Python` 代码中适配 `phpy` 的类型系统。
