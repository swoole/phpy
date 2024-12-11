API für Sockets
=============
In der Programmierung mit `phpy` ist es oft notwendig, mit dem `Socket API` NetzwerkcommUNICATIONProgramme zu schreiben.
Die folgenden Methoden können verwendet werden, um eine `Python Socket Object` in einen `PHP Stream Resource` und umgekehrt zu konvertieren.

Python in PHP umwandeln
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

- Verwenden Sie die `Python Socket.fileno()` Methode, um den Dateideskriptor zu erhalten

- Verwenden Sie `PHP fopen('php://fd/{$fileno}')`, um den `Socket` zu einem `PHP Stream` zu konvertieren, der dem Dateihandelt
- Verwenden Sie `fwrite/fread/fclose`, um den Handle zu lesen, zu schreiben und zu schließen

Das `fopen()` kopiert den Dateideskriptor, daher hat das Schließen des Handles mit `fclose()` keine Auswirkungen auf das `Python Socket Object` und es ist immer noch möglich, mit der `Python Socket API` Daten über diese Netzwerkverbindung zu übertragen.

PHP in Python umwandeln
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

- Verwenden Sie die `PyCore::fileno($fp)` Methode, um den Dateideskriptor des `PHP Stream` zu erhalten
- Verwenden Sie `Python Socket.fromfd()`, um den `Socket` zu einem `Python Socket Object` zu konvertieren, der dem Dateihandelt

Das `Socket.fromfd()` kopiert den Dateideskriptor, daher hat das Schließen des `Python Sockets` keine Auswirkungen auf den `PHP Stream`, und es ist immer noch möglich, mit `PHP` die `fwrite/fread/fclose` zu verwenden, um Daten über diese Netzwerkverbindung zu übertragen.
