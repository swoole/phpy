<?php

namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;

class ProxyTest extends TestCase
{
    function testClass()
    {
        $ROOT_PATH = dirname(__DIR__, 2);
        \PyClass::setProxyPath($ROOT_PATH, true);
        include $ROOT_PATH . '/tests/lib/Dog.php';

        $dog = new \Dog('dog', 1);
        $dog->speak('hello');
        $dog->age = 3;
        $this->assertEquals($dog->get_age(), 3);
    }

    function testNamedFn()
    {

    }

    function testWith()
    {
        $tmpname = tempnam(sys_get_temp_dir(), 'phpy');
        $bytes = random_bytes(random_int(1024, 8192));
        PyWith(function ($file) use ($bytes) {
            $file->write(PyCore::bytes($bytes));
        }, PyCore::open($tmpname, 'wb'));
        $this->assertEquals(file_get_contents($tmpname), $bytes);
        unlink($tmpname);
    }
}
