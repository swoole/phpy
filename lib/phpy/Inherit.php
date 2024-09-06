<?php

namespace phpy;

#[\Attribute]
class Inherit
{
    public function __construct(string $parentClass, string $package = '')
    {
    }
}

class_alias(Inherit::class, \Inherit::class);
