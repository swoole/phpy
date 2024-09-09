<?php
require_once __DIR__ . '/../../vendor/autoload.php';

$thread_n = 4;
$threads = [];

$time = PyCore::import('time');

/**
 * !!! WARNING !!!
 * phpy does not support multithreading,
 * this program will crash
 */
for ($i = 0; $i < $thread_n; $i++) {
    $thread = new python\threading\Thread(target: function () use ($i, $time) {
        $n = 10;
        while ($n--) {
            $time->sleep(1);
            echo "[Thread#{$i}]\thello world\n";
        }
    });
    $thread->start();
    $threads[] = $thread;
    echo "Thread#{$i} is started\n";
}

