<?php
require_once __DIR__ . '/../../vendor/autoload.php';

$os = python\os::import();

PyCore::print($os->getcwd());
