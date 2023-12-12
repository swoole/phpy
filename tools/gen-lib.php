#!/usr/bin/env php
<?php
require dirname(__DIR__) . '/vendor/autoload.php';

use PhpyTool\Tool;

if (empty($argv[1])) {
    exit("Usage: php gen-lib.php [python-module-name]\n");
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

$inspect = PyCore::import('inspect');

$ignoreAttrs = [
    '__builtins__',
    '__all__',
    '__loader__',
    '__cached__',
    '__file__',
    '__spec__',
];

$staticProperties = [];
$dynamicProperties = [];
$constants = [];
$functions = [];
$comment = '';
$attrs = PyCore::dir($module);

foreach ($attrs as $name) {
    $name = strval($name);
    $attr = $module->{$name};

    if (is_numeric($attr)) {
        $constants[$name] = $attr;
    } elseif (is_bool($attr) or is_string($attr)) {
        $staticProperties[$name] = Tool::valueToRepr($attr);
    } elseif ($attr === null) {
        $staticProperties[$name] = Tool::valueToRepr(null);
    } elseif ($name === '__doc__') {
        $comment = strval($attr);
    } elseif (in_array($name, $ignoreAttrs)) {
        continue;
    } elseif ($attr instanceof PyStr) {
        $staticProperties[$name] = Tool::valueToRepr(PyCore::scalar($attr));
    } else {
        $type = (strval(PyCore::type($attr)));
        if ($type === "<class 'builtin_function_or_method'>" or $type === "<class 'function'>") {
            try {
                $info = $inspect->getfullargspec($attr);
            } catch (\Throwable $e) {
                continue;
            }
            $args = $info[0];
            $defaultValue = $info[3];
            $functions[$name] = [
                'args' => gen_args($args, $defaultValue),
                'call' => gen_args($args),
            ];
        } else {
            $dynamicProperties[$name] = $type;
        }
    }
}

$module_name_ext = 'python.' . $module_name;
$namespace = gen_namespace($module_name_ext);
$sub_dir = str_replace('.', '/', $module_name_ext);
$class = basename($sub_dir);

Tool::render(
    __DIR__ . '/templates/php-lib.tpl',
    OUT_DIR . '/' . $sub_dir . '.php',
    compact('module_name', 'module', 'class', 'comment', 'namespace', 'constants', 'staticProperties', 'dynamicProperties', 'functions'),
    '<?php' . PHP_EOL,
);

function gen_args($args, $default = null)
{
    $n = count($args);
    if ($n == 0) {
        return '';
    }
    $list = [];
    foreach ($args as $arg) {
        $list[] = '$' . $arg;
    }
    if ($default) {
        $values = PyCore::scalar($default);
        $pos = $n - count($values);
        for ($i = $pos; $i < $n; $i++) {
            $v = $values[$i - $pos];
            $list[$i] = $list[$i] . ' = ' . Tool::valueToRepr($v);
        }
    }
    return implode(', ', $list);
}


function gen_namespace($module_name_ext)
{
    $list = explode('.', $module_name_ext);
    if (count($list) == 2) {
        return $list[0];
    }

    return implode('\\', array_slice($list, 0, count($list) - 1));
}
