<?php

namespace PhpyTool;

use PyCore;
use PyStr;

class Tool
{
    public static array $ignoreAttrs = [
        '__builtins__',
        '__all__',
        '__loader__',
        '__cached__',
        '__file__',
        '__spec__',
        '__weakref__',
        '__sizeof__',
    ];

    protected const KEYWORDS = [
        'and',
        'break',
        'continue',
        'for',
        'global',
        'if',
        'list',
        'match',
        'or',
        'return',
        'try',
        'while',
        'yield',
    ];

    public static function render($tplFile, $outFile, $vars, $prefix = ''): void
    {
        extract($vars);
        ob_start();
        include $tplFile;
        $out = $prefix . ob_get_clean();

        $dir = dirname($outFile);
        if (!is_dir($dir)) {
            mkdir($dir, 0777, true);
        }

        file_put_contents($outFile, $out);
    }

    public static function valueToRepr($v, $python = false): ?string
    {
        if (is_string($v)) {
            $v = str_replace(
                ["\\", "\n", "\r", "\t", "\v", "\x00", "\""],
                ["\\\\", "\\n", "\\r", "\\t", "\\v", "\\x00", "\\\""],
                $v
            );
            return "\"$v\"";
        } elseif ($v === []) {
            return '[]';
        } elseif (is_numeric($v)) {
            if ($python) {
                if (is_infinite($v)) {
                    return "float('inf')";
                } elseif (is_nan($v)) {
                    return "float('nan')";
                }
            }
            return strval($v);
        } elseif (is_bool($v)) {
            return $python ? ($v ? 'True' : 'False') : ($v ? 'true' : 'false');
        } elseif (is_null($v)) {
            return $python ? 'None' : 'null';
        } elseif (is_array($v)) {
            return var_export($v, true);
        } else {
            return $python ? 'None' : 'null';
        }
    }

    public static function parseClass($module_name, $class_name, $class): void
    {
        if (in_array(strtolower($class_name), self::KEYWORDS)) {
            $class_name = '_' . $class_name;
        }
        $methods = [];
        $properties = [];
        $constructor = ['call' => '', 'args' => ''];
        $attrs = PyCore::dir($class);
        foreach ($attrs as $name) {
            $name = $name->__toString();
            if (in_array($name, self::$ignoreAttrs) or ($name[0] === '_' and $name !== '__init__')) {
                continue;
            }
            $attr = $class->{$name};
            $type = PyCore::type($attr)->__toString();
            if ($type === "<class 'function'>") {
                $info = self::parseMethod($name, $attr);
                if ($name === '__init__') {
                    $constructor = $info;
                } else {
                    $methods[$name] = $info;
                }
            } elseif ($type === "<class 'property'>") {
                $properties[] = $name;
            } else {
                echo "[$module_name.$class_name.$name] attr unknown type: $type\n";
            }
        }

        $module_name_ext = 'python.' . $module_name . '.' . $class_name;
        $namespace = self::genNameSpace($module_name_ext);
        $sub_dir = str_replace('.', '/', $module_name_ext);
        self::render(
            __DIR__ . '/../templates/php-class.tpl',
            OUT_DIR . '/' . $sub_dir . '.php',
            compact('class_name', 'module_name', 'namespace', 'properties', 'methods', 'constructor'),
            '<?php' . PHP_EOL,
        );
    }

    public static function parseMethod($name, $func): array
    {
        $inspect = PyCore::import('inspect');
        $info = $inspect->getfullargspec($func);
        $args = $info[0];
        $args = $args->__getitem__(PyCore::slice(1, null));
        $defaultValue = $info[3];
        return [
            'args' => self::genArgs($args, $defaultValue),
            'call' => self::genArgs($args),
        ];
    }

    public static function parseFunction($name, $func): array
    {
        $inspect = PyCore::import('inspect');
        $info = $inspect->getfullargspec($func);
        $args = $info[0];
        $defaultValue = $info[3];
        return [
            'args' => self::genArgs($args, $defaultValue),
            'call' => self::genArgs($args),
        ];
    }

    public static function parseModule($module_name, $module): array
    {
        $staticProperties = [];
        $dynamicProperties = [];
        $constants = [];
        $functions = [];
        $classes = [];
        $comment = '';
        $attrs = PyCore::dir($module);

        foreach ($attrs as $name) {
            $name = strval($name);
            $attr = $module->{$name};

            if (is_numeric($attr)) {
                $constants[$name] = $attr;
            } elseif (is_bool($attr) or is_string($attr)) {
                $staticProperties[$name] = self::valueToRepr($attr);
            } elseif ($attr === null) {
                $staticProperties[$name] = self::valueToRepr(null);
            } elseif ($name === '__doc__') {
                $comment = strval($attr);
            } elseif (in_array($name, self::$ignoreAttrs)) {
                continue;
            } elseif ($attr instanceof PyStr) {
                $staticProperties[$name] = self::valueToRepr(PyCore::scalar($attr));
            } else {
                $type = (strval(PyCore::type($attr)));
                if ($type === "<class 'builtin_function_or_method'>" or $type === "<class 'function'>") {
                    try {
                        $functions[$name] = self::parseFunction($name, $attr);
                    } catch (\Exception $e) {
                        continue;
                    }
                } elseif ($type === "<class 'type'>") {
                    self::parseClass($module_name, $name, $attr);
                } else {
                    $dynamicProperties[$name] = $type;
                }
            }
        }

        return compact(
            'staticProperties',
            'dynamicProperties',
            'constants',
            'functions',
            'classes',
            'comment',
        );
    }

    public static function genArgs($args, $default = null)
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
                $list[$i] = $list[$i] . ' = ' . self::valueToRepr($v);
            }
        }
        return implode(', ', $list);
    }


    public static function genNameSpace($module_name_ext): string
    {
        $list = explode('.', $module_name_ext);
        if (count($list) == 2) {
            return $list[0];
        }

        return implode('\\', array_slice($list, 0, count($list) - 1));
    }
}
