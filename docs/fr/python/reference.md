# Type de référence

PHP prend en charge les références, tandis que Python peut les encapsuler dans un objet `phpy.Reference`.

## Exemple

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```
