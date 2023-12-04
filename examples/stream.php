<?php
$rs = stream_socket_client('tcp://www.baidu.com:80', $errno, $errstr, 30);
debug_zval_dump($rs);
fwrite($rs, "GET / HTTP/1.0\r\nHost: www.baidu.com\r\nAccept: */*\r\n\r\n");
debug_zval_dump($rs);
$content = fread($rs, 8192);
var_dump(str_contains($content, '百度搜索'));
debug_zval_dump($rs);
