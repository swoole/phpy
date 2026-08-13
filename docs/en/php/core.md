# Core

All built-in functions of `Python` are implemented as static methods of the `PyCore` class. Please refer to the `Python` documentation for usage of built-in methods.

## Importing Packages

```php
$os = PyCore::import('os');
```

This will return a `PyModule` object upon success. You can import built-in packages, as well as third-party packages or user-defined packages.

You can only load modules and it does not support the `from module import class` syntax in `Python`. You can use the following syntax instead.

```php
$module = PyCore::import($moduleName);
$class = $module->$className;
```

`Python` will cache the loaded modules internally. When a module is loaded for the second time, it will automatically return the module from the cache, avoiding duplicate loading. Therefore, it can be used in short-lived environments such as `PHP-FPM/Apache` without performance issues.

## Import Paths

You can use `PyCore::import('sys')->path->append()` to add directories to the import path list.
For example, if you have a custom package located at `/workspace/app/user.py`, you can load it using the following steps:

1. `PyCore::import('sys')->path->append('/workspace')` to add `/workspace` to `sys.path`.
2. `PyCore::import('app.user')` will automatically search `sys.path` and load the corresponding `app/user.py` package.

## Built-in Methods

- `PyCore::import($module)` - Import a module
- `PyCore::str()` - Convert an object to a string
- `PyCore::repr()` - Get the printable representation of an object
- `PyCore::type()` - Get the type of an object
- `PyCore::hash()` - Get the hash value
- `PyCore::hasattr()` - Check if an object has a specific attribute
- `PyCore::id()` - Get the internal identifier of an object
- `PyCore::len()` - Get the length
- `PyCore::dir()` - Get all attributes and methods of an object
- `PyCore::int()` - Construct an integer
- `PyCore::float()` - Construct a float
- `PyCore::fn()` - Construct a callable function
- `PyCore::eval()` - Execute Python code
- `PyCore::dict()` - Construct a dictionary object
- `PyCore::set()` - Construct a set object
- `PyCore::range()` - Construct a range sequence
- `PyCore::fileno($fp)` - Get the file descriptor of a `PHP Stream` resource. Note that only `tcp/udp/unix` type resources are supported

> `PyCore` implements the `__callStatic()` magic method, so calling a static method of `PyCore` will automatically call the corresponding method in the `builtins` module of Python. You can refer to [Built-in Functions](https://docs.python.org/3/library/functions.html) to learn more about the usage of built-in methods.

## Dynamic Linking Library Issue

If you encounter a dynamic linking library error when importing the library, the reason may be an incorrect `LD` path. You can set the environment variable to specify the dynamically linked library path for the Python C module.

> You can use `:` to separate and set multiple paths.

```shell
# Only use the anaconda3 base environment
export LD_LIBRARY_PATH=/opt/anaconda3/lib
# Using a specific environment named cef
export LD_LIBRARY_PATH=/opt/anaconda3/envs/cef/lib:/opt/anaconda3/lib
php plot.php
```

This approach only applies to the current bash session and will not affect the global settings. Do not directly modify `/etc/ld.so.conf.d/*.conf` to add `/opt/anaconda3/lib`, as this may cause conflicts with the `libc` library and affect the normal operation of other programs in the operating system.

## Case Sensitivity

In `Python`, all functions, methods, variables, and attributes are case-sensitive. You must use the exact same case as in `Python` when calling them.

For example:

```python
def TestUser():
    pass
```

In `PHP` code you must use `$module->TestUser()`. Other forms such as `$module->testUser()` or `$module->testuser()` are incorrect.

## Environment Variables

In `phpy`, `Python`'s `os.environ` is not automatically initialized, so `environ` is an empty dictionary. You need to iterate over `$_ENV` to inject the environment variables into the `Python` environment.

```php
$os = PyCore::import('os');
foreach ($_ENV as $k => $v) {
    $os->environ->__setitem__($k, $v);
}
```

## undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0

There may be a conflict in the dynamic linking library paths. You can try the following method to resolve it.
If the problem persists, it is recommended to use the system's built-in `Python` environment instead of the one created by `conda`.

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7
```

## Import Failure

In most cases, `from a import b` is equivalent to `PyCore::import('a')->b`,
but some special libraries cannot be loaded correctly using the above method. You can replace it with the following approach:

```php
# Cannot be loaded
$b = PyCore::import('a')->b;
# Replace with the following code
$b = PyCore::import('a.b');
```

## Built-in Types

In some cases, we need to pass a type as a parameter to a `Python` function, which can be done using `PyCore::type()`.

```php
$type_int = PyCore::type(0);
$type_float = PyCore::type(3.14);
$type_str = PyCore::type('hello');
$type_list = PyCore::type([1, 2, 3]);
$type_dict = PyCore::type(['a' => 1, 'b' => 2]);
$type_tuple = PyCore::type([1, 2, 3]);
$type_null = PyCore::type(null);
$type_bool = PyCore::type(true);
```

`PyCore::type()` returns a `PyType` object, which can be passed to `Python` functions. A `PyType` object can be called as a function to construct a new `Python` object again.

```php
$value = $type_int(100);
```
