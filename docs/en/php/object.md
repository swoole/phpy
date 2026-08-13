# PyObject
PyObject is the base class of all types other than PyCore. Objects of non-builtin classes are instances of PyObject. PyObject implements 4 magic methods to map operations to Python objects.

All class methods, parameters, and return values are defined in the files in the `stubs` directory. The documentation does not describe them in detail.

## Built-in classes
- `PyObject`: The base class of all other types
- `PyDict`: Dictionary type, equivalent to PHP associative arrays
- `PyList`: List type, equivalent to PHP indexed arrays
- `PyTuple`: Tuple, an immutable list
- `PyStr`: String
- `PyModule`: Python package, `PyModule` is also a subclass of `PyObject`

## Inheritance
```
PyObject -> PyModule
         -> PySequence -> PyList
                      -> PyTuple
         -> PySet
         -> PyStr
         -> PyDict
         -> PyType
```

## __get($name)
Reads the attribute of the Python object. 

```php
$pyobj->attr;
```

The following operations are equivalent:
```python
pyobj.attr
```

## __set($name, $value)
Sets the attribute of the Python object.

```php
$pyobj->attr = 'hello';
```

The following operations are equivalent:
```python
pyobj.attr = 'hello'
```

## __call($name, $args)
Calls the method of the Python object. 

```php
$pyobj->fn($a, $b, $c);
```

The following operations are equivalent:
```python
pyobj.fn(a, b, c)
```

## __invoke(...$args)
Executes a callable object, usually used to execute functions, construct objects. 

```php
// Import a py module, name is app.user
$user = PyCore::import('app.user');
// Info is a class
$Info = $user->Info;
// create an object, it is instance of app.user.Info
$info = $Info('Rango', 2023);
```

The following operations are equivalent:
```py
from app.user import Info

# create an Info object
info = Info('Rango', 2023)
```

## Named Parameters
Supports named parameters. Example:

### Passing named parameters
```php
kwargs($a, $b, $c, name: 'hello', world: 'rango');
```

- Positional parameters must come first, named parameters must come last.

### Receiving named parameters
```php
function kwargs($a, $b, $c, $name, $world) {

}
```

### Variable named parameters
```php
function kwargs(...$kwargs) {
    var_dump($kwargs);
}
```
- `$kwargs` will contain both the positional parameters and the named parameters, for example in the previous example it will receive:
```php
array(
 0 => $a,
 1 => $b,
 2 => $c,
 'name' => 'hello',
 'world' => 'rango',
)
```

### Forwarding named parameters
```php
function kwargs(...$kwargs) {
    kwargs_fn2(...$kwargs);
}
```

It is possible to forward the named parameters to another function.

## Slice Syntax

The sequence types `PyList` and `PyTuple` (both extend `PySequence`) provide a `slice(int $start, int $end)` method to extract a sub-sequence:

```php
$list = new PyList([10, 20, 30, 40, 50]);

// Extract elements in the index range [1, 3)
$sub = $list->slice(1, 3);
PyCore::print($sub);        // [20, 30]
```

Notes:

- `slice($start, $end)` accepts only two integer arguments for the start and end positions. **Step (stride) is not supported.**
- It is a method of `PySequence`, so it applies to `PyList` and `PyTuple`.
- The `[]` subscript operator only accepts an integer index. Passing a slice object as the key (e.g. `$s[PyCore::slice(0, 3)]`) is **not supported** in this build, and `PyStr` cannot be sliced through the subscript operator. If you need a substring, convert the string to a character `PyList` first, or use a Python string method via `PyCore::eval()`.
