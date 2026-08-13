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

    public function testSubmoduleFromSysModulesIsPreservedAsPyModule(): void
    {
        // A Python submodule fetched through a dict element crosses
        // PythonToPhpConverter::convertPreservingObjects() and hits the
        // PyModule_CheckExact branch, producing a PyModule PHP object.
        $os = PyCore::import('sys')->modules['os'];
        $this->assertInstanceOf(PyModule::class, $os);
        $this->assertSame('os', (string) $os->__name__);
    }
}
