<?php

use PHPUnit\Framework\TestCase;


class ModuleTest extends TestCase
{
    public function testImport()
    {
        $os = PyLoader::import('os');
        $uname = $os->uname();
        $this->assertEquals(php_uname('s'), $uname->sysname);
    }

    public function testNewObject()
    {
        $sys = PyCore::import('sys');
        $sys->path->append(__DIR__);

        $m = PyCore::import('app.user');
        $name = uniqid();
        $o = $m->User($name);
        $this->assertEquals($o->getName(), $name);
    }
}
