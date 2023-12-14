# Exception Handling

`phpy` provides encapsulation for handling exceptions in `Python` by introducing the `PyError` class, allowing `PHP` code to catch `Python` exceptions.

## Inheritance
`PyError` is a subclass of the `Exception` class.

## List of Properties
- `error`: The error object
- `type`: The error type
- `value`: The error value
- `traceback`: The traceback stack of the error

These properties are either `PyObject` objects or `null`.

## Catching Exceptions

```php
try {
    PyCore::import('not_exists');
} catch (PyError $e) {
    PyCore::print($e->error);
    PyCore::print($e->type);
    PyCore::print($e->value);
    PyCore::print($e->traceback);
}
```

- The underlying code will automatically set the string value of `$e->value` as the exception message, which can be accessed using `$e->getMessage()`.
- The `PyError` does not set an error code `$e->code`, so please do not use it.