<?php

class PyHelper
{
    public static $typeMap = [
        'PyTuple' => 'tuple',
        'PyList' => 'list',
        'PyDict' => 'dict',
        'PySet' => 'set',
        'PyStr' => 'str',
        'PyObject' => 'object',
        'int' => 'int',
        'float' => 'float',
        'bool' => 'bool',
        'string' => 'str',
    ];

    public static function printTraceback($traceback): void
    {
        $frame = $traceback;
        while ($frame) {
            PyCore::print($frame->tb_frame);
            $frame = $frame->tb_next;
        }
    }

    /**
     * @throws Exception
     */
    public static function checkName(string $name, string $type): string
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

    /**
     * @param string $type
     * @return string
     * @throws Exception
     */
    public static function parseType(string $type): string
    {
        if (!isset(self::$typeMap[$type])) {
            throw new Exception("Unsupported return type: $type");
        }
        return self::$typeMap[$type];
    }

    /**
     * @throws Exception
     */
    public static function parseReturnType(ReflectionFunction $ref): string
    {
        $refReturnType = $ref->getReturnType();
        if (!$refReturnType) {
            return '';
        }
        $type = $refReturnType->getName();
        if ($type === 'void') {
            return '';
        }

        return '-> ' . self::parseType($type);
    }

    public static function escapeName(string $name): string
    {
        return str_replace('\\', '_', $name);
    }
}
