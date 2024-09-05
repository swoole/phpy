<?php

namespace phpy;

use PyCore;
use PyObject;
use ReflectionClass;
use ReflectionMethod;

class PyClass
{
    static private string $_proxyPath = '';
    static private ?PyObject $_sys = null;
    protected ?PyObject $_self = null;
    protected ?PyObject $_super = null;
    protected string $_proxyClass;
    private string $_proxyFile;
    private string $_class;

    function __construct()
    {
        if (!self::$_sys) {
            self::$_sys = PyCore::import('sys');
        }
        if (!self::$_proxyPath) {
            self::setProxyPath(getcwd() . '/__phpy_proxy__');
        }

        $this->_class = get_class($this);
        $this->_proxyClass = strtolower(str_replace('\\', '_', $this->_class));
        $this->_proxyFile = self::$_proxyPath . '/' . $this->_proxyClass . '.py';

        if (!is_file($this->_proxyFile)) {
            $this->makeProxy();
        }
        PyCore::import($this->_proxyClass)->{$this->_proxyClass}($this);
        if (func_num_args() > 0) {
            $this->super()->__init__(...func_get_args());
        }
    }

    private function makeProxy()
    {
        $ref = new ReflectionClass($this);
        $refParents = $ref->getAttributes('parent');

        $import = '';
        $parents = [];

        if (empty($refParents)) {
            $parents[] = 'object';
        } else {
            foreach ($refParents as $refParent) {
                $parent = $refParent->getArguments();
                if (count($parent) == 1) {
                    $parents[] = $parent[0];
                } else {
                    [$class, $package] = $parent;
                    $import .= 'import ' . $package . PHP_EOL;
                    $parents[] = $package . '.' . $class;
                }
            }
        }

        $refMethods = $ref->getMethods(ReflectionMethod::IS_PUBLIC);
        $methods = [];
        foreach ($refMethods as $method) {
            $modifiers = $method->getModifiers();
            if (str_starts_with($method->name, '__') or $modifiers & ReflectionMethod::IS_STATIC) {
                continue;
            }
            $refParams = $method->getParameters();
            $params = [];
            foreach ($refParams as $param) {
                $params[] = $param->name;
            }
            $methods[] = [
                'name' => $method->name,
                'argv' => implode(', ', $params),
            ];
        }
        ob_start();
        include __DIR__ . '/proxy.tpl';
        $content = ob_get_clean();
        $dir = dirname($this->_proxyFile);
        if (!is_dir($dir)) {
            mkdir($dir, 0777, true);
        }
        file_put_contents($this->_proxyFile, $content);
    }

    protected function super()
    {
        return $this->_super;
    }

    protected function self()
    {
        return $this->_self;
    }

    static function setProxyPath(string $path): void
    {
        self::$_proxyPath = $path;
        self::$_sys->path->append($path);
    }
}
