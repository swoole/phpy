<?php

namespace PhpyTool;

class  Tool
{
    static function render($tplFile, $outFile, $vars, $prefix = '')
    {
        extract($vars);
        ob_start();
        include $tplFile;
        $out = $prefix . ob_get_clean();

        $dir = dirname($outFile);
        if (!is_dir($dir)) {
            mkdir($dir, 0777, true);
        }

        file_put_contents($outFile, $out);
    }

    static function valueToRepr($v, $python = false)
    {
        if (is_string($v)) {
            $v = str_replace(
                ["\\", "\n", "\r", "\t", "\v", "\x00", "\""],
                ["\\\\", "\\n", "\\r", "\\t", "\\v", "\\x00", "\\\""],
                $v);
            return "\"$v\"";
        } elseif ($v === []) {
            return '[]';
        } elseif (is_numeric($v)) {
            if ($python) {
                if (is_infinite($v)) {
                    return "float('inf')";
                } elseif (is_nan($v)) {
                    return "float('nan')";
                }
            }
            return strval($v);
        } elseif (is_bool($v)) {
            return $python ? ($v ? 'True' : 'False') : ($v ? 'true' : 'false');
        } elseif (is_null($v)) {
            return $python ? 'None' : 'null';
        } elseif (is_array($v)) {
            return var_export($v, true);
        } else {
            return $python ? 'None' : 'null';
        }
    }
}
