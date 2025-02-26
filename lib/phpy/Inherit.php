<?php

namespace phpy;

#[\Attribute]
class Inherit
{
    public function __construct(string $parentClass, string $package = '')
    {
    }
}


