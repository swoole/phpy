<?php

namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;

class ProxyTest extends TestCase
{
    public function __construct($name)
    {
        \PyClass::setProxyPath(BASE_PATH, true);
        parent::__construct($name);
    }

    public function testClass()
    {
        include BASE_PATH . '/tests/lib/Dog.php';

        $dog = new \Dog('dog', 1);
        $dog->speak('hello');
        $dog->age = 3;
        $this->assertEquals($dog->get_age(), 3);
    }

    public function testNamedFn()
    {
        PyCore::setOptions(['argument_as_object' => true]);
        $a = random_int(1, 10000000);
        $b = random_int(1, 10000000) / 33;
        $d = uniqid();
        $rs = PyNamedFn('test_fn_1')($a, $b, true, $d, PyCore::slice(1, 10, 2), PyCore::list([1, 2, 3]), PyCore::str('world'));
        $this->assertEquals($rs[0], $a);
        $this->assertEquals($rs[1], $b);
        $this->assertEquals($rs[2], true);
        $this->assertEquals($rs[3], $d);
        $this->assertEquals($rs[4], PyCore::slice(1, 10, 2));
        $this->assertEquals($rs[5], PyCore::list([1, 2, 3]));
        $this->assertEquals($rs[6], PyCore::str('world'));
    }

    public function testWith()
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
