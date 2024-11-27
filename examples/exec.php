<?php
$globals = new PyDict();
$locals = new PyDict();
PyCore::exec(file_get_contents('./test.py'), $globals, $locals);
