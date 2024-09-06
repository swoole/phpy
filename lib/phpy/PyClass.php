<?php

namespace phpy;

use PyCore;
use PyObject;
use ReflectionClass;
use ReflectionMethod;

class PyClass
{
    static private string $_proxyPath = '';
    static private bool $_checkStat = false;
    static private ?PyObject $_sys = null;
    protected ?PyObject $_self = null;
    protected ?PyObject $_super = null;
    protected string $_proxyClass;
    private string $_proxyFile;

    /**
     * @throws \Exception
     */
    function __construct()
    {
        if (!self::$_proxyPath) {
            self::setProxyPath(getcwd());
        }

        $class = get_class($this);
        $this->_proxyClass = strtolower(str_replace('\\', '_', $class));
        $this->_proxyFile = self::$_proxyPath . '/' . $this->_proxyClass . '.py';

        if (self::$_checkStat) {
            $this->checkProxyFile();
        }

        if (!is_file($this->_proxyFile)) {
            $this->makeProxy();
        }
        PyCore::import($this->_proxyClass)->{$this->_proxyClass}($this);
    }

    /**
     * @return void
     * @throws \Exception
     */
    private function makeProxy(): void
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
                    $parents[] = self::checkName($parent[0], 'class');
                } else {
                    [$class, $package] = $parent;
                    $import .= 'import ' . self::checkName($package, 'package') . PHP_EOL;
                    $parents[] = $package . '.' . self::checkName($class, 'class');
                }
            }
        }

        $refMethods = $ref->getMethods();
        $methods = [];
        foreach ($refMethods as $method) {
            $modifiers = $method->getModifiers();
            if (str_starts_with($method->name, '__')
                or ($modifiers & ReflectionMethod::IS_STATIC)
                or ($modifiers & ReflectionMethod::IS_PRIVATE)
                or ($modifiers & ReflectionMethod::IS_ABSTRACT)) {
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

    protected function super(): ?PyObject
    {
        return $this->_super;
    }

    public function self(): ?PyObject
    {
        return $this->_self;
    }

    /**
     * @param string $rootPath
     * @param bool $checkStat Check file changes and delete proxy files when PHP class files are updated
     * @return void
     */
    public static function setProxyPath(string $rootPath, bool $checkStat = false): void
    {
        self::$_proxyPath = $rootPath . '/__phpy_proxy__';
        if (!self::$_sys) {
            self::$_sys = PyCore::import('sys');
        }
        self::$_sys->path->append(self::$_proxyPath);
        self::$_checkStat = $checkStat;
    }

    /**
     * @throws \Exception
     */
    private static function checkName(string $name, string $type): string
    {
        static $regx = [
            'class' => '#^[a-z_][a-z_0-9]*$#i',
            'package' => '#^[a-z_][a-z_0-9]*(\.[a-z_][a-z_0-9]*)*$#i'
        ];
        if (!preg_match($regx[$type], $name)) {
            throw new \Exception("Invalid $type name: '$name'");
        }
        return $name;
    }

    private function checkProxyFile(): void
    {
        clearstatcache(true, $this->_proxyFile);
        $ref = new ReflectionClass($this);
        if (filemtime($ref->getFileName()) > filemtime($this->_proxyFile)) {
            unlink($this->_proxyFile);
        }
    }

    public function __get($name)
    {
        return $this->_self->{$name};
    }

    public function __set($name, $value)
    {
        $this->_self->{$name} = $value;
    }

    public function __call($name, $arguments)
    {
        return $this->_self->{$name}(...$arguments);
    }
}
