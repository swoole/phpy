#!/usr/bin/env php
<?php
require dirname(__DIR__) . '/vendor/autoload.php';

use PhpyTool\Generator;

$extensions = get_loaded_extensions();

//$extensions = ['Core'];

Generator::$rootDir = dirname(__DIR__) . '/lib/php';

$rmAll = 'rm -rf ' . Generator::$rootDir . '/*.py';
shell_exec($rmAll);

foreach ($extensions as $extension) {
    if (strtolower($extension) === 'phpy') {
        continue;
    }
    Generator::make($extension);
    echo "IDE help files for {$extension} generated successfully.\n";
}
