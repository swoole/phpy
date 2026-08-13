# Operator Overloading

`phpy` intercepts PHP's operator opcodes so that `PyObject` can directly reuse Python's number and comparison protocols (`PyNumber_*` / `PyObject_RichCompareBool`). As long as one side of the operator is a `PyObject`, the other side is automatically converted to a Python object via `php2py` (e.g. a PHP array → `PyList`, `int`/`float`/`string`/`bool` → the corresponding Python type).

## Arithmetic and bitwise operators

| PHP operator | Python protocol | Notes |
| --- | --- | --- |
| `+` | `PyNumber_Add` | |
| `-` | `PyNumber_Subtract` | |
| `*` | `PyNumber_Multiply` | |
| `/` | `PyNumber_TrueDivide` | true division (returns float) |
| `%` | `PyNumber_Remainder` | |
| `**` | `PyNumber_Power` | power |
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

// A native PHP array/scalar on the other side is auto-converted to a Python object
$c = new PyList([1, 2, 3]);
PyCore::print($c + [4, 5]);       // [1, 2, 3, 4, 5]
```

- The result is a new `PyObject`; if the underlying call returns `Py_None` and `return_as_object` is not enabled, the result is PHP `null`.
- If the operation is unsupported or errors, a `PyError` is thrown.

## Augmented assignment (in-place)

`+= -= *= /= %= <<= >>= &= |= ^= **=` are all supported, calling Python's `PyNumber_InPlace*` family to compute in place:

```php
$c = new PyList([1, 2, 3]);
$c += new PyList([9]);            // PyNumber_InPlaceAdd
PyCore::print($c);               // [1, 2, 3, 9]
```

> Note: `.=` string concatenation is **not supported**; it emits a warning `PyObject do not support string concat operation` and does not perform the concatenation.

## Unary bitwise not

`~$a` maps to `PyNumber_Invert`:

```php
echo strval(~PyCore::int(5));     // -6
```

## Comparison operators

`== != < <= > >=` are all based on Python's value comparison (`PyObject_RichCompareBool`), with semantics identical to Python:

```php
$x = new PyList([1, 2, 3]);
$y = new PyList([1, 2, 3]);
$z = $x;
var_dump($x == $y);                  // bool(true)  equal by value
var_dump($x != $y);                  // bool(false)
var_dump($x < new PyList([1, 2, 4])); // bool(true)
var_dump($x > new PyList([1, 2, 4])); // bool(false)
```

> Note: `===` / `!==` are **object identity comparisons** (they compare the underlying Python object pointers, i.e. whether it is the same object), not value comparisons. Two different Python objects with the same content compare `===` as `false`:
>
> ```php
> var_dump($x === $y);   // bool(false)  not the same object
> var_dump($x === $z);   // bool(true)   same object
> ```

## String concatenation

- The plain `.` operator is **not intercepted**; it falls back to PHP's default behavior: the `PyObject` is first converted to a PHP string and then concatenated, so the result is a **native PHP string**, not a `PyObject`. If you need a Python string as the result, use the methods provided by `PyCore::str` or call a Python string method via `PyCore::eval()`.
- The augmented `.=` is not supported (see above; it emits a warning).
