<?php

$os = PyCore::import('os');

var_dump(PyCore::scalar($os->uname()));
