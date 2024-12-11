
Socket API
=====
In `phpy` programming development, it is often necessary to use the `Socket API` to write network communication programs. The following methods can be used to convert the `Python Socket object` and the `PHP Stream resource` to each other.

Python to PHP
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

- Use the `Python Socket.fileno()` method to get the file descriptor.
- Use `PHP fopen('php://fd/{$fileno}')` to convert the file handle corresponding to the `Socket` into a `PHP Stream`.
- Use `fwrite/fread/fclose` to read, write, and close the handle.

`fopen()` will copy the file descriptor, so calling `fclose()` will not affect the `Python Socket object`, and you can continue to use the `Python Socket API` to perform data transmission operations on this network connection.

PHP to Python
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

- Use the `PyCore::fileno($fp)` method to obtain the `PHP Stream` file descriptor.
- Use `Python Socket.fromfd()` to convert the file handle corresponding to the `Socket` into a `Python Socket object`.

`Socket.fromfd()` will copy the file descriptor, so closing the `Python Socket` will not affect the `PHP Stream`, and you can still use `PHP`'s `fwrite/fread/fclose` to perform data transmission operations on this network connection.
