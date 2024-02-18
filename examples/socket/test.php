<?php
$svr = stream_socket_server("tcp://127.0.0.1:0", $errno, $errstr);
$name = stream_socket_get_name($svr, false);
var_dump($name);
