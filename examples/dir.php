<?php
$sys = PyCore::import("sys");
$list = PyCore::dir($sys);
var_dump(get_class($list));
