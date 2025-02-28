<?php

use PHPUnit\Framework\TestCase;

class ModuleTest extends TestCase
{
    public function testImport()
    {
        $platform = PyLoader::import('platform');
        $uname = $platform->uname();
        $this->assertStringContainsStringIgnoringCase([PHP_OS, 'WIN'][str_starts_with(PHP_OS, 'WIN')], (string)$uname->system);
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
