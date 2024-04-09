<?php
$itertools = PyCore::import('itertools');
$result = PyCore::list($itertools->product([1, 2], [3, 4]));
PyCore::print($result);

