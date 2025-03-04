<?php

#[Attribute(Attribute::TARGET_FUNCTION)]
class PyArguments
{
    public function __construct(string...$args)
    {
    }

    /**
     * @throws Exception
     */
    public static function parse(ReflectionAttribute $ref, array $realArgNames): string
    {
        $args = $ref->getArguments();
        if (count($args) != count($realArgNames)) {
            throw new Exception("Number of arguments does not match");
        }
        foreach ($realArgNames as $i => $realArgName) {
            $arg = $args[$i];
            do {
                // arg: int = 30
                $a1 = explode(':', $arg);
                if (count($a1) == 2) {
                    $argName = trim($a1[0]);
                    break;
                }
                $a2 = explode('=', $arg);
                if (count($a2) == 2) {
                    $argName = trim($a2[0]);
                    break;
                }
                $argName = trim($arg);
            } while (false);

            if ($argName != $realArgName) {
                throw new Exception("Argument name mismatch: $argName != $realArgName");
            }
        }
        return implode(', ', $args);
    }
}
