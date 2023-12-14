# User Guide

The purpose of this library is to compensate for the deficiencies of PHP using the Python ecosystem. If the functionality already exists in PHP, it is recommended to use the PHP language directly. If not, you can search for available libraries in the Python ecosystem.

`phpy` simply imports Python libraries into the PHP ecosystem, but the syntax used is PHP, so there is no additional learning cost.

In Python, everything is an object, whether it's a module, class, function, integer, float, None, boolean, object, dictionary, list, set, or tuple. These are all instances of `PyObject`.

Usually, there are about 4 things we do in programming:

- `PyCore::import()` to import a package
- Calling methods of an object: `$object->fn()`
- Reading and writing attributes of an object: `$object->attr` and `$object->attr = $value`
- Calling built-in functions `PyCore::$fn()` to achieve some basic functionality, such as `import()` which is actually a built-in function

Example:

```php
// Import Python os package
$os = PyCore::import('os');
// Call function
$uname = $os->uname();
// Read attribute
echo $uname->sysname;
// Print
echo strval(PyCore::str($uname));
```