# Типы ссылок

В `PHP` поддерживается передача ссылок, в `Python` это можно реализовать, обернув его объектом `phpy.Reference`.

## Пример

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```
