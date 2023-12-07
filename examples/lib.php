<?php
require __DIR__.'/../lib/python/os.php';

$s = python\os::urandom(128);
var_dump(base64_encode(PyCore::scalar($s)));
