<?php
$socket = PyCore::import('socket');

const HOST = "127.0.0.1";
const PORT = 5432;

$client = $socket->socket($socket->AF_INET, $socket->SOCK_STREAM);
$client->connect(PyCore::tuple([HOST, PORT]));

while (1) {
    echo "> ";
    $msg = trim(fgets(STDIN));
    if ($msg == 'quit') {
        break;
    }
    $client->sendall(PyCore::bytes($msg));
    $data = $client->recv(1024);
    if (empty($data)) {
        break;
    }
    echo strval($data) . PHP_EOL;
}
