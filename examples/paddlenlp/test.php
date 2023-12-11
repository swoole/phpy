<?php
$pprint = PyCore::import('pprint')->pprint;
$Taskflow = PyCore::import('paddlenlp')->Taskflow;

$schema = new PyList(['时间', '选手', '赛事名称']);
$ie = $Taskflow('information_extraction', schema: $schema);
$pprint($ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！"));
