<?php
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
        $staticProperties[$name] = value_to_repr($attr);
    } elseif ($attr === null) {
        $staticProperties[$name] = value_to_repr(null);
    } elseif ($name === '__doc__') {
        $comment = strval($attr);
    } elseif (in_array($name, $ignoreAttrs)) {
        continue;
    } elseif ($attr instanceof PyStr) {
        $staticProperties[$name] = value_to_repr(PyCore::scalar($attr));
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

ob_start();
include __DIR__ . '/templates/pymodule.tpl';
$out = '<?php' . PHP_EOL . ob_get_clean();

$path = OUT_DIR . '/' . $sub_dir . '.php';
$dir = dirname($path);
if (!is_dir($dir)) {
    mkdir($dir, 0777, true);
}

file_put_contents($path, $out);

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
            $list[$i] = $list[$i] . '=' . value_to_repr($v);
        }
    }
    return implode(', ', $list);
}


function value_to_repr($v)
{
    if (is_string($v)) {
        $v = str_replace(["\n", "\""], ["\\n", "\\\""], $v);
        return "\"$v\"";
    } elseif (is_numeric($v)) {
        return $v;
    } elseif (is_bool($v)) {
        return $v ? 'true' : 'false';
    } elseif (is_null($v)) {
        return 'null';
    } elseif (is_array($v)) {
        return var_export($v, true);
    } else {
        return 'null';
    }
}

function gen_namespace($module_name_ext)
{
    $list = explode('.', $module_name_ext);
    if (count($list) == 2) {
        return $list[0];
    }

    return implode('\\', array_slice($list, 0, count($list) - 1));
}
