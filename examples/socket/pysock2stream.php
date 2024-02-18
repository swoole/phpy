<?php
$socket = PyCore::import('socket');

const HOST = "127.0.0.1";
const PORT = 5432;

$client = $socket->socket($socket->AF_INET, $socket->SOCK_STREAM);
$client->connect(PyCore::tuple([HOST, PORT]));
$fp = fopen('php://fd/' . $client->fileno(), 'rw');

while (1) {
    echo "> ";
    $msg = trim(fgets(STDIN));
    if ($msg == 'quit') {
        break;
    }
    fwrite($fp, $msg);
    $data = fread($fp, 1024);
    if (empty($data)) {
        break;
    }
    echo $data . PHP_EOL;
}

echo 'Connection closed. Please enter any characters to exit the program. ' . PHP_EOL;
fclose($fp);

fgets(STDIN);
