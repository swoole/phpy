phpy
====
`Python` 与 `PHP` 互调用库，可以在 `PHP` 中使用 `Python` 语言的函数和类库，或者在 `Python` 中使用 `PHP` 的包。
但不是语言内嵌。编码依然使用各自的原生语法。

> 本项目授权协议为 `Apache2`

- 目前仅支持 Linux 平台（理论上可以支持所有操作系统，待实现）
- 不支持 Python 多线程、`async-io` 特性

![Alt](docs/wxg.png)


PHP 调用 Python
----
编译安装 `phpy.so` 作为扩展加载，修改 `php.ini` 追加 `extension=phpy.so` 即可。

例子：
```php
$os = PyCore::import("os");
$un = $os->uname();
echo strval($un);
```

Python 中调用 PHP
----
直接作为 `C++ Mudule` ，import 加载即可。

```python
import phpy

content = phpy.call('file_get_contents', 'test.txt')

o = phpy.Object('redis')
assert o.call('connect', '127.0.0.1', 6379)
rdata = phpy.call('uniqid')
assert o.call('set', 'key', rdata)
assert o.call('get', 'key') == rdata
```


实现原理
----
在进程内同时创建了 `ZendVM` 和 `CPython VM`，直接在进程堆栈空间内使用 `C` 函数互相调用，
开销只有 `zval <-> PyObject` 结构体转换，因此性能是非常高的。

