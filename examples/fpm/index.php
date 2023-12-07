<?php

$dict = PyCore::fetch('dict');
if (!$dict) {
    $dict = PyCore::dict();
    PyCore::storage('dict', $dict);
    $dict['test'] = uniqid();
    echo "no cache\n";
} else {
    echo "cached\n";
    var_dump(strval($dict['test']));
}



