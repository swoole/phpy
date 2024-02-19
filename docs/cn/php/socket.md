Socket API
=====
在 `phpy` 编程开发中经常需要使用 `Socket API` 编写网络通信程序，
可使用下面的方法实现 `Python Socket 对象` 与 `PHP Stream 资源` 互相转换。 

Python 转 PHP
-----
```php
$socket = PyCore::import('socket');
const HOST = "127.0.0.1";
const PORT = 5432;

$client = $socket->socket($socket->AF_INET, $socket->SOCK_STREAM);
$client->connect(PyCore::tuple([HOST, PORT]));

$fp = fopen('php://fd/' . $client->fileno(), 'rw');
fwrite($fp, $msg);
$data = fread($fp, 1024);
fclose($fp);
```

- 使用 `Python Socket.fileno()` 方法获取文件描述符
- 使用 `PHP fopen('php://fd/{$fileno}')` 将文件句柄对应的 `Socket` 转为 `PHP Stream`
- 使用 `fwrite/fread/fclose` 读写、关闭句柄

`fopen()` 会复制文件描述符，因此 `fclose()` 关闭时不会影响 `Python Socket 对象`，
依然可以使用 `Python Socket API` 对此网络连接进行数据传输操作。

PHP 转 Python
----
```php
$socket = PyCore::import('socket');

$HOST = "127.0.0.1";
$PORT = 5432;

$fp = stream_socket_client("tcp://$HOST:$PORT", $errno, $errstr, 30);
if (!$fp) {
    exit("Error: $errstr ($errno)\n");
}
$client = $socket->fromfd(PyCore::fileno($fp), $socket->AF_INET, $socket->SOCK_STREAM);
fclose($fp);
```

- 使用 `PyCore::fileno($fp)` 方法获取 `PHP Stream` 文件描述符
- 使用 `Python Socket.fromfd()` 将文件句柄对应的 `Socket` 转为 `Python Socket 对象`

`Socket.fromfd()` 会复制文件描述符，因此 `Python Socket` 关闭时不会影响 `PHP Stream`，
依然可以使用 `PHP` 的  `fwrite/fread/fclose` 对此网络连接进行数据传输操作。
