<?php

$Client = PyCore::import('gradio_client')->Client;
$client = $Client("http://192.168.1.146:8088/");
$result = $client->predict("Hello!!", api_name: "/predict");
PyCore::print($result);
