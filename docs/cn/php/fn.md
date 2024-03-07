# 回调函数

可将 `PHP` 的可调用对象作为 `Python` 的回调函数。使用 `PyCore::fn(callable $fn)` 包裹即可。

```php
$m = PyCore::import('app.user');
$uuid = uniqid();
$rs = $m->test_callback(PyCore::fn(function ($namespace) use ($uuid) {
    var_dump($namespace);
    return $uuid;
}));
```

- `import app.user` 导入了一个自定义 `Python` 包
- 调用了包中的一个函数 `test_callback`，此函数接受一个参数为 `Python Callable` 对象
- 使用 `PyCore::fn()` 包裹了一个 `Closure` 闭包对象作为回调，这里也支持函数名称字符串、对象方法的调用方式
- 回调函数返回了一个字符串，在 `test_callback` 函数中会得到一个 `str` 类型返回值

## Closure 闭包函数
最新的版本中回调函数类型为 `Closure` 时，不再需要使用 `PyCore::fn()` 进行包裹，底层会直接转为回调对象。
但使用 `array`、`string` 类型的函数名称或类方法作为回调函数时，仍然需要使用 `PyCore::fn()` 进行封装。

```php
# Closure 闭包函数可直接传递
$m->test_callback(function ($namespace) use ($uuid) {
    return $uuid;
});

# 字符串函数名作为回调函数，则需要使用  `PyCore::fn()` 封装
function test_fn() {
    return $uuid;
}
$m->test_callback(PyCore::fn('test_fn'));
```

## 实例
这里使用了 `Python tkinter` 作为例子：

```php
<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('我的窗口');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Click Me!!", command: function () {
    var_dump(func_get_args());
    echo 'click me!!' . PHP_EOL;
});
$button->pack();

$tkinter->mainloop();
```

`PHP` 作为 `Tk Button` 的回调函数。 
