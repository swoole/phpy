<?php

#[Attribute(Attribute::IS_REPEATABLE | Attribute::TARGET_FUNCTION | Attribute::TARGET_CLASS)]
class PyImport
{
    public function __construct(string $module, string $package = '')
    {
    }

    /**
     * @throws Exception
     */
    public static function parse(ReflectionMethod|ReflectionClass|ReflectionFunction $ref): array
    {
        $importAttrs = $ref->getAttributes('PyImport');
        $imports = [];
        foreach ($importAttrs as $attr) {
            $args = $attr->getArguments();
            if (count($args) == 0 or count($args) > 2) {
                throw new Exception("Invalid import arguments");
            }
            if (count($args) === 1) {
                $imports[] = 'import ' . PyHelper::checkName($args[0], 'package');
            } else {
                [$class, $package] = $args;
                $imports[] =
                    'from ' . PyHelper::checkName($package, 'package') . ' ' .
                    'import ' . ($args[1] === '*' ? '*' : PyHelper::checkName($class, 'class'));
            }
        }
        return $imports;
    }
}
