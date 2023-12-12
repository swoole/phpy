#!/usr/bin/env php
<?php

define("EXT_SRC_DIR", dirname(__DIR__) . '/src/php');
define('PROJECT_NAME', 'phpy');

require __DIR__ . '/bootstrap.php';
if (empty($argv[1])) {
    exit("Usage: php {$argv[0]} module_name\n");
}

$module_name = trim($argv[1]);

$gen_class_name = function ($module_name) {
    $list = explode('_', $module_name);
    $class = '';
    foreach ($list as $li) {
        $class .= ucfirst($li);
    }
    return $class;
};

$replacement = [
    'file_name' => $module_name,
    'module_name' => $module_name,
    'var_name' => $module_name,
    'class_name' => $gen_class_name($module_name),
];

$replacement['type_name'] = $replacement['class_name'] . 'Object';
$replacement['php_var_name'] = "{$replacement['var_name']}_object";
$replacement['class_name'] = addcslashes($replacement['class_name'], '\\');
$replacement['project_name'] = PROJECT_NAME;
foreach ($replacement as $name => $value) {
    $replacement[strtoupper($name)] = strtoupper($value);
}
$replacement['class_name_lower'] = strtolower($replacement['class_name']);

$result = '';
$srcTemplateFile = __DIR__ . '/templates/class.c';
$content = file_get_contents($srcTemplateFile);
foreach ($replacement as $name => $value) {
    $content = str_replace("{{{$name}}}", $value, $content);
}

$outFile = EXT_SRC_DIR . '/' . $module_name . '.cc' ;
if (!is_file($outFile)) {
    file_put_contents($outFile, $content);
} else {
    throw new Exception("file is exists");
}



//, __DIR__ . '/templates/class.h'];

