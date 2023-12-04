# 用户指南

这个库的目的是使用 `Python` 的生态来弥补 `PHP` 的不足。
若 `PHP` 已有的的功能特性， 直接使用 `PHP` 语言的即可，若没有则可以在 `Python` 生态中寻找可用的库。

`phpy` 只是将 `Python` 的库导入到了 `PHP` 生态中，但所使用的语法均为 `PHP`，没有额外的学习成本。

`Python` 是一切皆对象的，无论是模块、类、函数、整数、浮点数、None、布尔值、对象、字典、列表、集合、元组，皆是对象。 这些都是 `PyObject` 的实例。

通常我们编程所做的事情，大概就是`4`件事情

- `PyCore::import()` 导入一个包
- 调用对象的方法：`$object->fn()`
- 读写对象的属性：`$object->attr` 和 `$object->attr = $value`
- 调用内置函数 `PyCore::$fn()` 实现一些基础功能，例如 `import()` 其实就是一个内置函数

> 不建议在 `php-fpm/apache` 短生命周期运行环境下使用，频繁地导入/销毁模块的开销会消耗大量资源
 
## 例子

```php
// 导入 Python os 包
$os = PyCore::import('os');
// 调用函数
$uname = $os->uname();
// 读取属性
echo $uname->sysname; 
// 打印
echo strval(PyCore::str($uname));
```
