<?php
$np = PyCore::import('numpy');

$rs = $np->floor($np->random->random([3, 4])->__mul__(10));

PyCore::print($rs);
