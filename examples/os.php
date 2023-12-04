<?php
function main() {
    $m = PyCore::import("os");
    var_dump($m instanceof PyObject);
    $rs = $m->uname();
    echo $rs;
    echo $rs->version;
}

main();
