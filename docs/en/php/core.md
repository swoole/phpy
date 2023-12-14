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
$class = $m->$className;
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
- `PyCore::repr()` - 
- `PyCore::type()` - Get the type of an object
- `PyCore::locals()` - Get all local variables in the current scope
- `PyCore::globals()` - Get all global variables
- `PyCore::hash()` - Get the hash value
- `PyCore::hasattr()` - Check if an object has a specific attribute- `PyCore::id()` Get the internal identifier of an object
- `PyCore::len()` Get the length
- `PyCore::dir()` Get all attributes and methods of an object
- `PyCore::int()` Construct an integer
- `PyCore::float()` Construct a float
- `PyCore::fn()` Construct a callable function
- `PyCore::eval()` Execute Python code
- `PyCore::dict()` Construct a dictionary object
- `PyCore::set()` Construct a set object
- `PyCore::range()` Construct a range sequence
- `PyCore::scalar()` Convert a `PyObject` object to a scalar type in PHP, for example, `PyStr` will be converted to `PHP string`, `Dict/Tuple/Set/List` will be converted to `Array`

> `PyCore` implements the `__callStatic()` magic method, so calling a static method of `PyCore` will automatically call the corresponding method in the `builtins` module of Python. You can refer to [Built-in Functions](https://docs.python.org/3/library/functions.html) to learn more about the usage of built-in methods.

## Dynamic Linking Library Issue
If you encounter a dynamic linking library error when importing the library, the reason may be an incorrect `LD` path. You can set the environment variable to specify the dynamically linked library path for the Python C module.

```shell
export LD_LIBRARY_PATH=/opt/anaconda3/lib
php plot.php
```

This approach only applies to the current bash session and will not affect the global settings. Do not directly modify `/etc/ld.so.conf.d/*.conf` to add `/opt/anaconda3/lib`, as this may cause conflicts with `libc` library and affect the normal operation of other programs in the operating system.