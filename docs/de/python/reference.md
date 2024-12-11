# Anführungszeichenarten

In `PHP` werden Referenzen unterstützt, in `Python` kann dies durch Umhüllung mit einem `phpy.Reference` Objekt erreicht werden.

## Beispiel

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```
