<?php

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$tqdm = PyCore::import('tqdm')->tqdm;

$pbar = $tqdm(total: 100);

foreach (range(1, 100) as $current) {
    usleep(1000 * random_int(1, 100));
    $pbar->update(1);
}
$pbar->close();

