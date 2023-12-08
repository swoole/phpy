<?php

PyCore::import('sys')->path->append(dirname(__DIR__, 2) . '/tests/lib');

$app = PyCore::import('app.user');
$storage = $app->storage;
if (!isset($storage['data'])) {
    $storage['data'] = uniqid();
    var_dump("no cache");
    $o = new stdClass();
    $o->hello = uniqid();
    $storage['obj'] = $o;
} else {
    var_dump(strval($storage['data']));
    var_dump($storage['obj']);
}

