<?php

declare(strict_types=1);

namespace PhpyTool;

use ReflectionException;
use ReflectionExtension;
use ReflectionMethod;
use ReflectionParameter;

class Generator
{
    protected string $extension;
    protected ReflectionExtension $rf_ext;
    protected const KEYWORDS = [
        'assert' => 1,
        'del' => 1,
        'yield' => 1,
        'import' => 1,
        'from' => 1,
        'and' => 1,
        'or' => 1,
    ];

    public static string $rootDir = '';

    /**
     * @param $extension
     * @return void
     * @throws Exception
     * @throws ReflectionException
     */
    static function make($extension): void
    {
        if (self::$rootDir === '') {
            self::$rootDir = dirname(__DIR__) . '/output/';
        }
        $generator = new self($extension);
        $generator->export();
    }

    /**
     * AbstractStubGenerator constructor.
     *
     * @throws Exception
     * @throws ReflectionException
     */
    private function __construct($extension)
    {
        if (!extension_loaded($extension)) {
            throw new Exception("Extension $extension not enabled or not installed.");
        }

        $this->extension = $extension;
        $this->rf_ext = new ReflectionExtension($this->extension);
    }

    public function export(): void
    {
        $constants = $this->getConstants();
        $functions = $this->getFunctions();
        $classes = $this->getClasses();

        $mod = strtolower($this->extension);
        $mod = $mod === 'standard' ? 'std' : $mod;

        Tool::render(
            dirname(__DIR__) . '/templates/py-mod.tpl',
            self::$rootDir . '/' . $mod . '.py',
            compact('constants', 'functions', 'classes')
        );
    }

    /**
     * @return string
     */
    public function getVersion(): string
    {
        return $this->rf_ext->getVersion();
    }

    protected function getConstants(): array
    {
        $constants = [];
        if ($this->rf_ext->getConstants()) {
            foreach ($this->rf_ext->getConstants() as $name => $value) {
                // Duplicates the module name and should be deleted.
                if (str_starts_with(strtolower($name), $this->extension . '_')) {
                    $name = substr($name, strlen($this->extension) + 1);
                }
                $constants[$name] = Tool::valueToRepr($value, true);
            }
        }
        return $constants;
    }

    /**
     * @param ReflectionParameter $parameter
     * @return string|null
     */
    protected function getDefaultValue(ReflectionParameter $parameter): ?string
    {
        if ($parameter->isDefaultValueAvailable()) {
            $default_value = $parameter->getDefaultValue();
            return Tool::valueToRepr($default_value, true);
        } else {
            return 'None';
        }
    }

    static function changeCasePascal2Snake(string $name): string
    {
        return strtolower(preg_replace('/(?<!^)[A-Z]/', '_$0', $name));
    }

    protected function getArgs($params): array
    {
        $call = $args = [];
        foreach ($params as $param) {
            $arg_name = '_' . self::changeCasePascal2Snake($param->name);
            if ($param->isOptional()) {
                $args[] = "$arg_name=" . $this->getDefaultValue($param);
            } else {
                $args[] = $arg_name;
            }
            $call[] = $arg_name;
        }

        return [
            $args,
            $call,
        ];
    }

    protected function getFunctions(): array
    {
        $functions = [];
        foreach ($this->rf_ext->getFunctions() as $function) {
            $params = $function->getParameters();
            $fn_name = $function->getName();
            $fn_name_safe = $fn_name;
            // Duplicates the module name and should be deleted.
            if (str_starts_with($fn_name_safe, $this->extension . '_')) {
                $fn_name_safe = substr($fn_name_safe, strlen($this->extension) + 1);
            }
            if (array_key_exists($fn_name_safe, self::KEYWORDS)) {
                $fn_name_safe = '_' . $fn_name_safe;
            }
            [$args, $call] = $this->getArgs($params);
            $functions[$fn_name_safe] = [
                'args' => implode(', ', $args),
                'call' => "return phpy.call('$fn_name', " . implode(', ', $call) . ")\n",
            ];
        }
        return $functions;
    }

    protected function getClasses(): array
    {
        $classes = [];
        $list = $this->rf_ext->getClasses();
        foreach ($list as $className => $ref) {
            $constants = [];
            $methods = [];
            $classNameSafe = str_replace('\\', '\\\\', $className);
            foreach ($ref->getConstants() as $name => $value) {
                $constants[$name] = Tool::valueToRepr($value, true);
            }
            foreach ($ref->getMethods(ReflectionMethod::IS_STATIC | ReflectionMethod::IS_PUBLIC) as $method) {
                $params = $method->getParameters();
                $fn_name = $method->getName();
                if (array_key_exists($fn_name, self::KEYWORDS)) {
                    $fn_name_safe = '_' . $fn_name;
                } else {
                    $fn_name_safe = $fn_name;
                }
                [$args, $call] = $this->getArgs($params);
                if (!$method->isStatic()) {
                    array_unshift($args, 'self');
                }
                $args_call = implode(', ', $call);
                if ($fn_name == '__construct') {
                    $fn_name_safe = '__init__';
                    $call = "self.__this = phpy.Object(f'$classNameSafe', $args_call)";
                } elseif ($fn_name == '__destruct') {
                    $fn_name_safe = '__del__';
                    $call = "self.__this = None";
                } elseif ($method->isStatic()) {
                    $call = 'return phpy.call(f"' . $classNameSafe . '::' . $fn_name . '", ' . $args_call . ")";
                } else {
                    $call = 'return self.__this.call(f"' . $fn_name . '", ' . $args_call . ")";
                }
                $methods[$fn_name_safe] = [
                    'args' => implode(', ', $args),
                    'call' => $call,
                ];
            }

            $ns = explode('\\', $className);
            if (count($ns) > 1) {
                $className = implode('', array_slice($ns, 1));
            }

            if (empty($constants) and empty($methods)) {
                continue;
            }

            $classes[$className] = [
                'constants' => $constants,
                'methods' => $methods,
            ];
        }
        return $classes;
    }
}
