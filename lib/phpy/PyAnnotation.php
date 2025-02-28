<?php

#[Attribute(Attribute::IS_REPEATABLE | Attribute::TARGET_CLASS | Attribute::TARGET_FUNCTION)]
class PyAnnotation
{
    public function __construct(string $annotation)
    {
    }

    static function parse(ReflectionMethod|ReflectionClass|ReflectionFunction $ref)
    {
        $annotationAttrs = $ref->getAttributes('PyAnnotation');
        $annotations = [];
        foreach ($annotationAttrs as $attr) {
            $args = $attr->getArguments();
            if (count($args) != 1) {
                throw new \Exception("Invalid annotation arguments");
            } else {
                $annotations[] = $args[0];
            }
        }
        return $annotations;
    }
}

