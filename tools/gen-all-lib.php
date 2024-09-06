#!/usr/bin/env php
<?php
$list = [
    'ast',
    'base64',
    'calendar',
    'json',
    'matplotlib.pyplot',
    'os',
    'pickle',
    'random',
    'string',
    'subprocess',
    'sys',
    'threading',
    'tkinter',
    'torch',
    'uuid'
];


foreach ($list as $module) {
    `php gen-php-lib.php $module`;
}
