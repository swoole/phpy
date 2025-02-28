<?php

#[Attribute(Attribute::IS_REPEATABLE | Attribute::TARGET_CLASS)]
class PyInherit
{
    public function __construct(string $parentClass, string $package = '')
    {
    }
}
