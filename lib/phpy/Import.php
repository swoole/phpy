<?php

namespace phpy;

#[\Attribute]
class Import
{
    public function __construct(string $module, string $package = '')
    {
    }
}

