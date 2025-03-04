<?php

class PyEnum
{
    private string $_proxyFile;
    private string $class;

    /**
     * @throws ReflectionException
     * @throws Exception
     */
    public function __construct(string $class)
    {
        $this->class = $class;
        if (!class_exists($class)) {
            throw new Exception("Class `$class` not found");
        }
        $this->_proxyFile = PyClass::getProxyPath() . '/enums/' . PyHelper::escapeName($class) . '.py';
        if (!PyClass::hasProxyFile($this->_proxyFile, $this)) {
            $this->makeProxy();
        }
    }

    public function getPyEnum(): PyObject
    {
        $class = PyHelper::escapeName($this->class);
        return PyCore::import('enums.' . $class)->{$class};
    }

    /**
     * @return void
     * @throws Exception
     */
    private function makeProxy(): void
    {
        $ref = new ReflectionClass($this->class);
        $constants = $ref->getConstants();
        $imports = PyImport::parse($ref);
        $class = PyHelper::escapeName($this->class);
        ob_start();
        include __DIR__ . '/templates/enum.tpl';
        $content = ob_get_clean();
        $dir = dirname($this->_proxyFile);
        if (!is_dir($dir)) {
            mkdir($dir, 0777, true);
        }
        if (!is_file($dir . '/__init__.py')) {
            file_put_contents($dir . '/__init__.py', '');
        }
        file_put_contents($this->_proxyFile, $content);
    }
}