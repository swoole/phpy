# Memory Copy

When `PHP` calls `Python` functions/methods, parameter and return value may involve memory copying, which needs to be considered when writing performance-sensitive programs.

## Parameters

- Integer, boolean, floating point, and null (`null`) are always passed by value.

- Objects, resources, and references are always passed by reference, meaning no memory is copied.
- Strings and arrays will undergo recursive deep copying to convert to native types.

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

- `$arg1`, `$arg2`, and `$arg3` will be converted to integers, floating point, and boolean in `Python`, copying the values directly.

- `$arg4`, `$arg5`, and `$arg6` will directly pass references to `Python`, resulting in no memory copies.
- `$arg6`, `$arg7`, and `$arg8` will be traversed and deeply copied in memory, converting to `Python`'s `list`, `dict`, and `str`.

## Return Values

- Integers, booleans, floating point numbers, and null (`None` and `null`) will be converted to `PHP`'s native types.

- All other returned content from `Python` will be of type `PyObject`.
- You can also use `phpy.String` or `phpy.Array` in `Python` code to achieve transparent forwarding of `PHP` native types.

## Avoiding Memory Copy
Using the `PyObject::object($value)` method can convert string and array types to `PyObject`, where the type obtained in `Python` will be `phpy.String` and `phpy.Array`.

This method requires the `Python` code to adapt to the `phpy` type system.
