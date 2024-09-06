#!/usr/bin/env php
<?php
require dirname(__DIR__) . '/vendor/autoload.php';

use PhpyTool\Tool;

if (empty($argv[1])) {
    exit("Usage: php {$argv[0]} [python-module-name]\n");
}

/**
 * !!! experimental stage, only some features are supported.
 */
define('OUT_DIR', dirname(__DIR__) . '/lib');
$module_name = $argv[1];

$module = PyCore::import($module_name);
if (!($module instanceof PyModule)) {
    exit(1);
}

echo "module $module_name\n";

$info = Tool::parseModule($module_name, $module);
extract($info);

$module_name_ext = 'python.' . $module_name;
$namespace = Tool::genNameSpace($module_name_ext);
$sub_dir = str_replace('.', '/', $module_name_ext);
$class = basename($sub_dir);

Tool::render(
    __DIR__ . '/templates/php-lib.tpl',
    OUT_DIR . '/' . $sub_dir . '.php',
    compact('module_name', 'module', 'class', 'comment', 'namespace', 'constants', 'staticProperties', 'dynamicProperties', 'functions'),
    '<?php' . PHP_EOL,
);
