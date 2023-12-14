Integer
====
The Python language natively supports infinite precision integer calculations, which can be used to replace `ext-bcmath` with Python's integer computing capability.

Construction
---
Use the `PyCore::int()` function to construct a number, which can be initialized with an integer, float, or string.

```php
$i1 = PyCore::int(12345678);
$i2 = PyCore::int('1234567890123456789012345678901234567890');
$i3 = PyCore::int(12345678.03);
```

Operations
----
Integers are also instances of `PyObject` and can be manipulated using built-in methods.

```php
$i = PyCore::int(12345435);
var_dump(strval($i->__pow__(3)));
var_dump(strval($i->__add__(4)));
```

The output will be `1881564851360655187875`. Since it exceeds the maximum precision of `64-bit`, the output is automatically converted to a string type.