<?php

class PyNamedFn
{
    private string $_proxyFile;
    private string $name;

    /**
     * @param string $name
     * @throws Exception
     */
    public function __construct(string $name)
    {
        $this->name = $name;
        if (!function_exists($name)) {
            throw new Exception("Function `$name` not found");
        }

        $proxyDir = PyClass::getProxyPath();
        $this->_proxyFile = $proxyDir . '/functions/' . $name . '.py';
        if (!is_file($this->_proxyFile)) {
            $this->makeProxy();
        }
    }

    /**
     * @return void
     * @throws Exception
     */
    private function makeProxy(): void
    {
        $ref = new \ReflectionFunction($this->name);

        $annotations = PyAnnotation::parse($ref);
        $imports = PyImport::parse($ref);

        $refParams = $ref->getParameters();
        $_args = [];
        $_argNames = [];
        foreach ($refParams as $param) {
            $type = $param->getType();
            $name = $param->getName();
            if ($type) {
                $_args[] = $name . ': ' . PyHelper::parseType($type->getName());
            } else {
                $_args[] = $name;
            }
            $_argNames[] = $name;
        }

        $returnType = PyHelper::parseReturnType($ref);

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
        if (!is_file(dirname($this->_proxyFile) . '/__init__.py')) {
            file_put_contents(dirname($this->_proxyFile) . '/__init__.py', '');
        }
        file_put_contents($this->_proxyFile, $content);
    }

    public function get()
    {
        return PyCore::import('functions.' . $this->name)->{$this->name};
    }
}
