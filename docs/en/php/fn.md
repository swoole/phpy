# Callback Function

You can use PHP callable objects as callback functions in Python. Simply wrap them with `PyCore::fn(callable $fn)`.

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user` imports a custom Python package
- Calls a function `test_callback` in the package, which takes a parameter as a Python Callable object
- Wraps a `Closure` object as the callback using `PyCore::fn()`, supports both function name string and object method call
- The callback function returns a string, which will be a `str` type return value in the `test_callback` function

## Example
Here, we use Python tkinter as an example:

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('My Window');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Click Me!!", command: PyCore::fn(function () {
    var_dump(func_get_args());
    echo 'Click Me!!' . PHP_EOL;
}));
$button->pack();

$tkinter->mainloop();
```

PHP serves as the callback function for the Tk Button.