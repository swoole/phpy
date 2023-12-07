<?php
$py = PyCore::import('builtins');
$array = PyCore::scalar($py->range(3));
var_dump($array);
