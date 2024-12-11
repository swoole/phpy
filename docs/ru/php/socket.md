Сетевой API
===========
В разработке программ на языке `phpy` часто требуется использование `Сетевого API` для написания сетевых коммуникационных программ.
Ниже представлены методы для преобразования между `Python Socket объектом` и `PHP Stream ресурсом`.

Передача из Python в PHP
-----------------------
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

- Использовать метод `Python Socket.fileno()` для получения файла дескриптора

- Использовать `PHP fopen('php://fd/{$fileno}')` для преобразования соответствующего `Socket` файла дескриптора в `PHP Stream`
- Использовать `fwrite/fread/fclose` для чтения, письма и закрытия дескриптора

`fopen()` копирует файл дескриптор, поэтому закрытие `fclose()` не повлияет на `Python Socket объект`, и вы все еще можете использовать `Python Socket API` для передачи данных по этой сетевой связи.

Передача из PHP в Python
----------------------
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

- Использовать метод `PyCore::fileno($fp)` для получения файла дескриптора `PHP Stream`
- Использовать `Python Socket.fromfd()` для преобразования соответствующего `Socket` файла дескриптора в `Python Socket объект`

`Socket.fromfd()` копирует файл дескриптор, поэтому закрытие `Python Socket` не повлияет на `PHP Stream`, и вы все еще можете использовать `PHP` для чтения, письма и закрытия этой сетевой связи с использованием `fwrite/fread/fclose`.
