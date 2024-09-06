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
}
