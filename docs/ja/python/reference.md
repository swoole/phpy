# 引用タイプ

PHPでは参照を渡すことができ、Pythonではphpy.Referenceオブジェクトを wrapsして実現できます。

## 例

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```
