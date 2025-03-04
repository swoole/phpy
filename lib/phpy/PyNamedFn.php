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
        $this->_proxyFile = PyClass::getProxyPath() . '/functions/' . PyHelper::escapeName($name) . '.py';
        if (!PyClass::hasProxyFile($this->_proxyFile, $this)) {
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
            $argType = $param->getType();
            $argName = $param->getName();
            if ($argType) {
                $_args[] = $argName . ': ' . PyHelper::parseType($argType->getName());
            } else {
                $_args[] = $argName;
            }
            $_argNames[] = $argName;
        }

        $returnType = PyHelper::parseReturnType($ref);

        $name = PyHelper::escapeName($this->name);
        $refArgs = $ref->getAttributes(PyArguments::class);
        if (empty($refArgs)) {
            $args = implode(', ', $_args);
        } else {
            $args = PyArguments::parse($refArgs[0], $_argNames);
        }
        $argNames = implode(', ', $_argNames);

        ob_start();
        include __DIR__ . '/templates/function.tpl';
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

    public function getPyFn()
    {
        $name = PyHelper::escapeName($this->name);
        return PyCore::import('functions.' . $name)->{$name};
    }

    public function getName(): string
    {
        return $this->name;
    }
}
