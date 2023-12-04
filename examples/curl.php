<?php

$curl = curl_init();


var_dump(get_class($curl));
var_dump(gettype($curl));
var_dump($curl);

curl_setopt($curl, CURLOPT_URL, 'https://www.baidu.com/');
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_exec($curl);

debug_zval_dump($curl);
