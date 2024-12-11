API Sockets
==========
Dans le développement de programmes de communication réseau avec `phpy`, il est fréquent d'utiliser l'API Sockets pour écrire des applications. Vous pouvez utiliser les méthodes suivantes pour convertir un objet `Socket Python` en une ressource de flux `PHP` et vice versa.

Conversion Python vers PHP
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

- Utilisez la méthode `Python Socket.fileno()` pour obtenir le numéro de descriptor de fichier.
- Utilisez `PHP fopen('php://fd/{$fileno}')` pour transformer le handle de fichier en un flux `PHP` correspondant à un `Socket`.
- Utilisez `fwrite/fread/fclose` pour écrire, lire et fermer le handle.

La fonction `fopen()` copie le numéro de descriptor de fichier, donc lorsque `fclose()` est appelé, cela n'affecte pas l'objet `Socket Python` et vous pouvez toujours utiliser l'API Sockets Python pour effectuer des opérations de transmission de données sur cette connexion réseau.

Conversion PHP vers Python
---------------------------
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

- Utilisez la méthode `PyCore::fileno($fp)` pour obtenir le numéro de descriptor de fichier du flux `PHP`.
- Utilisez la méthode `Python Socket.fromfd()` pour transformer le handle de fichier en un objet `Socket Python` correspondant.

La méthode `Socket.fromfd()` copie le numéro de descriptor de fichier, donc lorsque le `Socket Python` est fermé, cela n'affecte pas le flux `PHP`, et vous pouvez toujours utiliser les fonctions `fwrite/fread/fclose` de PHP pour effectuer des opérations de transmission de données sur cette connexion réseau.
