<?php

namespace phpy;

use PyCore;
use PyObject;

class PyNamedFn
{
    private string $_proxyFile;
    private string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
        if (!function_exists($name)) {
            throw new \Exception("Function `$name` not found");
        }

        $proxyDir = PyClass::getProxyPath();
        $this->_proxyFile = $proxyDir . '/functions/' . $name . '.py';
        if (!is_file($this->_proxyFile)) {
            $this->makeProxy();
        }
    }

    /**
     * @return void
     * @throws \Exception
     */
    private function makeProxy(): void
    {
        $ref = new \ReflectionFunction($this->name);

        $annotationAttrs = $ref->getAttributes('annotation');
        $annotations = [];
        foreach ($annotationAttrs as $attr) {
            $args = $attr->getArguments();
            if (count($args) != 1) {
                throw new \Exception("Invalid annotation arguments");
            } else {
                $annotations[] = $args[0];
            }
        }

        $importAttrs = $ref->getAttributes('import');
        $packages = [];
        foreach ($importAttrs as $attr) {
            $args = $attr->getArguments();
            if (count($args) == 0 or count($args) > 2) {
                throw new \Exception("Invalid import arguments");
            }
            $packages[] = count($args) == 1 ?
                'import ' . Helper::checkName($args[0], 'package') :
                'from ' . Helper::checkName($args[0], 'package') . ' import ' . Helper::checkName($args[1], 'class');
        }

        $refParams = $ref->getParameters();
        $_args = [];
        $_argNames = [];
        foreach ($refParams as $param) {
            $type = $param->getType();
            $name = $param->getName();
            if ($type) {
                $_args[] = $name . ': ' . $type->getName();
            } else {
                $_args[] = $name;
            }
            $_argNames[] = $name;
        }

        $refReturnType = $ref->getReturnType();
        $returnType = $refReturnType ? ' -> ' . $refReturnType->getName() : '';

        $name = $this->name;
        $args = implode(', ', $_args);
        $argNames = implode(', ', $_argNames);
        ob_start();
        include __DIR__ . '/templates/function.tpl';
        $content = ob_get_clean();
        $dir = dirname($this->_proxyFile);
        if (!is_dir($dir)) {
            mkdir($dir, 0777, true);
        }
        file_put_contents($this->_proxyFile, $content);
    }

    function get()
    {
        return PyCore::import('functions.' . $this->name)->{$this->name};
    }
}