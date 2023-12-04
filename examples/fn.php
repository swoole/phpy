<?php
function kwargs($a, $b, $name = '', $value = '', $date = '') {
    var_dump($a, $b);
    var_dump($name, $value, $date);
}


// kwargs('xd', 'jd', date: date('Y-m-d'));


class O {
    function __call($fn, $args) {
        var_dump($fn, $args);
    }
}

$o = new O;
$o->test('xd', 'jd', date: date('Y-m-d'));
