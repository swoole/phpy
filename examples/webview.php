<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$webview = PyCore::import('webview');
$webview->create_window("Hello world", "https://pywebview.flowrl.com/");
$webview->start();


