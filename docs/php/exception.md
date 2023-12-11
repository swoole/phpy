# 异常处理

`phpy` 对 `Python` 的异常进行了封装，提供了 `PyError` 类型，使得 `PHP` 代码中可以捕获 `Python` 异常。

## 继承关系
`PyError` 是 `Exception` 类的子类。

## 属性列表
- `error`：错误对象
- `type`：错误类型
- `value`：错误值
- `traceback`：错误的回溯堆栈

这些属性是 `PyObject` 对象或者 `null`

## 捕获异常

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

- 底层会自动将 `$e->value` 的字符串值设置为异常消息，可使用 `$e->getMessage()` 获取
- `PyError` 未设置 `$e->code` 错误码，请勿使用

