<?php

class PyHelper
{
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

    public static function parseReturnType(ReflectionFunction $ref): string
    {
        $refReturnType = $ref->getReturnType();
        if ($refReturnType) {
            $type = $refReturnType->getName();
            if ($type === 'void') {
                return '';
            } else {
                return '-> ' . $type;
            }
        } else {
            return '';
        }
    }
}
