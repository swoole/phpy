<?php
$os = PyCore::import("os");
var_dump(PyCore::hasattr($os, 'uname'));
var_dump(PyCore::hasattr($os, 'not_exists'));
