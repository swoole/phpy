# 操作符重载

`phpy` 拦截了 PHP 的运算符 `opcode`，使 `PyObject` 能够直接复用 `Python` 的数值与比较协议（`PyNumber_*` / `PyObject_RichCompareBool`）。只要运算符两侧有一侧是 `PyObject`，另一侧会通过 `php2py` 自动转换为 `Python` 对象（如 `PHP` 数组 → `PyList`，`int`/`float`/`string`/`bool` → 对应的 `Python` 类型）。

## 配置

操作符重载默认开启。由于 Zend user opcode handler 可能限制 Opcache JIT 对相应 opcode 的优化，不需要这项语法糖的应用可以在 `php.ini` 中关闭：

```ini
phpy.enable_operator_overloading=0
```

这是 `PHP_INI_SYSTEM` 配置，只能在 PHP 启动时设置，不能通过 `ini_set()` 或 `PyCore::setOptions()` 动态修改；修改后需要重启 PHP 进程。关闭后 phpy 不会注册任何操作符 opcode handler，其他 phpy API 仍然可用。需要执行 Python 运算时可显式调用 Python 的 `operator` 模块：

```php
$operator = PyCore::import('operator');
$result = $operator->add($left, $right);
```

## 算术与位运算

| PHP 运算符 | 对应 Python 协议 | 说明 |
| --- | --- | --- |
| `+` | `PyNumber_Add` | |
| `-` | `PyNumber_Subtract` | |
| `*` | `PyNumber_Multiply` | |
| `/` | `PyNumber_TrueDivide` | 真除法（结果为浮点） |
| `%` | `PyNumber_Remainder` | |
| `**` | `PyNumber_Power` | 幂运算 |
| `<<` | `PyNumber_Lshift` | |
| `>>` | `PyNumber_Rshift` | |
| `&` | `PyNumber_And` | |
| `\|` | `PyNumber_Or` | |
| `^` | `PyNumber_Xor` | |

```php
$a = new PyList([1, 2, 3]);
$b = $a + new PyList([4, 5, 6]);   // PyNumber_Add
PyCore::print($b);                // [1, 2, 3, 4, 5, 6]

$i = PyCore::int(10);
echo strval($i * 3);              // 30
echo strval($i ** PyCore::int(2)); // 100

// 右侧为 PHP 原生数组/标量时，自动转换为 Python 对象
$c = new PyList([1, 2, 3]);
PyCore::print($c + [4, 5]);       // [1, 2, 3, 4, 5]
```

- 运算结果是一个新的 `PyObject`；若底层返回 `Py_None` 且未开启 `return_as_object`，则结果为 `PHP` 的 `null`。
- 若运算类型不支持或出错，会抛出 `PyError`。

## 增强赋值（就地运算）

`+= -= *= /= %= <<= >>= &= |= ^= **=` 均支持，调用 `Python` 的 `PyNumber_InPlace*` 系列，在原对象上就地计算：

```php
$c = new PyList([1, 2, 3]);
$c += new PyList([9]);            // PyNumber_InPlaceAdd
PyCore::print($c);               // [1, 2, 3, 9]
```

> 注意：`.=` 字符串拼接**不支持**，会触发警告 `PyObject do not support string concat operation` 且不执行拼接。

## 一元按位取反

`~$a` 对应 `PyNumber_Invert`：

```php
echo strval(~PyCore::int(5));     // -6
```

## 比较运算

`== != < <= > >=` 均基于 `Python` 的值比较（`PyObject_RichCompareBool`），语义与 `Python` 一致：

```php
$x = new PyList([1, 2, 3]);
$y = new PyList([1, 2, 3]);
$z = $x;
var_dump($x == $y);                  // bool(true)  值相等
var_dump($x != $y);                  // bool(false)
var_dump($x < new PyList([1, 2, 4])); // bool(true)
var_dump($x > new PyList([1, 2, 4])); // bool(false)
```

> 注意：`===` / `!==` 是**对象同一性比较**（比较底层 `Python` 对象的指针，即是否为同一个对象），而非值比较。两个内容相同但不同的 `Python` 对象，`===` 为 `false`：
>
> ```php
> var_dump($x === $y);   // bool(false)  不是同一个对象
> var_dump($x === $z);   // bool(true)   同一个对象
> ```

## 字符串拼接

- 普通 `.` 运算符**未被拦截**，会走 `PHP` 默认行为：先把 `PyObject` 转为 `PHP` 字符串再拼接，结果为 **`PHP` 原生字符串**而非 `PyObject`。如需得到 `Python` 字符串，请使用 `PyCore::str` 提供的方法或 `PyCore::eval()` 调用 `Python` 字符串方法。
- 增强赋值 `.=` 不支持（见上文，会触发警告）。
