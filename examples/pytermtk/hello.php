<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$ttk = PyCore::import('TermTk');

$root = $ttk->TTk();
$helloWin = $ttk->TTkWindow(parent: $root, pos: [1, 1], size: [30, 10], title: "Hello Window", border: true);
$ttk->TTkLabel(parent: $helloWin, pos: [5, 5], text: "Hello World");
$root->mainloop();
