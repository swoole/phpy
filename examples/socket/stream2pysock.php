<?php

$socket = PyCore::import('socket');

$HOST = "127.0.0.1";
$PORT = 5432;

$fp = stream_socket_client("tcp://$HOST:$PORT", $errno, $errstr, 30);
if (!$fp) {
    exit("Error: $errstr ($errno)\n");
}
$client = $socket->fromfd(PyCore::fileno($fp), $socket->AF_INET, $socket->SOCK_STREAM);
fclose($fp);

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
