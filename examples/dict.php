<?php
function main() {
    $dict = new PyDict;
//    $dict['hello'] = uniqid();
//    echo $dict['hello'];
//    echo PHP_EOL;
//
//    var_dump(isset($dict['hello']));
//    var_dump(isset($dict['golang']));
//
//    unset($dict['hello']);
//    var_dump(isset($dict['hello']));
//
//    $n = 10;
//    while ($n--) {
//        $dict['key-' . $n] = uniqid();
//    }


    echo "foreach [1]\n";
    foreach($dict as $k => $v) {
        var_dump($k, $v);
    }

    echo "foreach [2]\n";

    foreach($dict as $k => $v) {
        var_dump($k, $v);
    }
}

