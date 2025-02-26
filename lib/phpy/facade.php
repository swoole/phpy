<?php

use phpy\Import;
use phpy\Inherit;
use phpy\PyClass;
use phpy\Annotation;

class_alias(Inherit::class, \Inherit::class);
class_alias(Import::class, \Import::class);
class_alias(Annotation::class, \Annotation::class);
class_alias(PyClass::class, \PyClass::class);

function PyNamedFn(string $fnName): PyObject
{
    return (new phpy\PyNamedFn($fnName))->get();
}
