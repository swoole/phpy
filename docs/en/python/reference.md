# Reference Types

In `PHP`, it is possible to pass variables by reference. In `Python`, this can be achieved by wrapping the variable in a `phpy.Reference` object.

## Example

```python
import phpy

errno = phpy.Reference()
errstr = phpy.Reference()
rs = phpy.call("stream_socket_client", 'tcp://127.0.0.1:9999', errno, errstr, 30)
```