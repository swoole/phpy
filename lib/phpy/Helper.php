<?php

namespace phpy;

use PyCore;

class Helper
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
     * @throws \Exception
     */
    public static function checkName(string $name, string $type): string
    {
        if ($type == 'class' and $name === '*') {
            return '*';
        }
        static $regx = [
            'class' => '#^[a-z_][a-z_0-9]*$#i',
            'package' => '#^[a-z_][a-z_0-9]*(\.[a-z_][a-z_0-9]*)*$#i'
        ];
        if (!preg_match($regx[$type], $name)) {
            throw new \Exception("Invalid $type name: '$name'");
        }
        return $name;
    }
}
