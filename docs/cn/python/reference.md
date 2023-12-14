# 引用类型

在 `PHP` 中是支持传引用的，在 `Python` 中可以包裹为一个 `phpy.Reference` 对象实现。

## 示例

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```
