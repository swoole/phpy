# Memory Copy

When `Python` calls `PHP` functions/methods, parameters and return values may involve memory copying. It is important to pay attention to the overhead of memory copying when writing performance-sensitive programs.

## Parameters

- Integer, Boolean, Float, and None (`None`) are always passed by value.

- Objects, Resources, and References are always passed by reference, and no memory is copied.
- Strings and Arrays will be recursively deep-copied into native types.

```python 

arg1 = 1234
arg2 = 1234.5678
arg3 = True

arg4 = phpy.Object('stdClass')
arg5 = phpy.Reference()
arg6 = phpy.call('fopen', "php://input", "r")

arg7 = {'hello' : 'world'}
arg8 = "hello world"
arg9 = [1, 2, 3, 4, 5]

phpy.call('test', arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)
```

- `arg1`, `arg2`, and `arg3` will be converted to integers, floats, and booleans in `PHP`, copying the values directly.

- `arg4`, `arg5`, and `arg6` will directly pass references to `PHP`, producing no memory copy.
- `arg6`, `arg7`, and `arg8` will be traversed, deeply copied in memory, and converted into `PHP`’s `array` and `string`.

## Return Values

- Integers, Booleans, Floats, and None (`None` and `null`) will be converted to Python's native types.

- All other content returned from `Python` will be of `PyObject` type.
- You can also use `PyObject` type in `PHP` code, allowing for transparent forwarding to return Python's native types.

## Avoid Memory Copy
By using `phpy.String` and `phpy.Array` objects when calling PHP functions, memory copying will not occur.
