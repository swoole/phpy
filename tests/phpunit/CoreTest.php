<?php


use PHPUnit\Framework\TestCase;

class CoreTest extends TestCase
{
    public function testDir()
    {
        $sys = PyCore::import("sys");
        $list = PyCore::dir($sys);
        $this->assertTrue($list instanceof \PyList);
        $array = PyCore::scalar($list);
        $this->assertGreaterThan(10, count($array));
        $this->assertSameSize($array, $list);
    }

    public function testStr()
    {
        $sys = PyCore::import("sys");
        $info = $sys->version_info;
        $this->assertStringContainsString('major=3', PyCore::str($info));
    }

    public function testRepr()
    {
        $platform = PyCore::import("platform");
        $repr = PyCore::repr($platform->uname());
        $this->assertStringContainsString('uname_result', $repr);
    }

    public function testId()
    {
        $os = PyCore::import("os");
        $this->assertIsNumeric(PyCore::id($os));
    }

    public function testType()
    {
        $platform = PyCore::import("platform");
        $this->assertEquals("<class 'module'>", PyCore::type($platform));
        $this->assertEquals("<class 'platform.uname_result'>", PyCore::type($platform->uname()));

        $dict = new PyDict();
        $this->assertEquals("<class 'dict'>", PyCore::type($dict));

        $dict = new PyObject();
        $this->assertEquals("<class 'NoneType'>", PyCore::type($dict));
    }

    public function testHash()
    {
        $dict = new PyStr(uniqid());
        $this->assertIsNumeric(PyCore::hash($dict));
    }

    public function testHasAttr()
    {
        $platform = PyCore::import("platform");
        $this->assertTrue(PyCore::hasattr($platform, 'uname'));
        $this->assertFalse(PyCore::hasattr($platform, 'not_exists'));
    }

    public function testLen()
    {
        $platform = PyCore::import("platform");
        $uname = $platform->uname();
        $this->assertGreaterThan(5, PyCore::len($uname));
        $this->assertGreaterThan(90, strlen(PyCore::str($uname)));

        $n = 14;
        $list = new PyList();
        while ($n--) {
            $list[] = uniqid();
        }
        $this->assertEquals(14, PyCore::len($list));
    }

    public function testScalar()
    {
        $rint = random_int(100000, 9999999);
        $uuid = uniqid();
        $so = new PyStr($uuid);
        $this->assertEquals($uuid, PyCore::scalar($so));


        $list = new PyList();
        $list[] = $uuid;
        $list[] = $rint;
        $this->assertEquals(PyCore::scalar($list), [$uuid, $rint]);

        $dict = new PyDict();
        $dict['uuid'] = $uuid;
        $dict['rint'] = $rint;
        $this->assertEquals(PyCore::scalar($dict), ['uuid' => $uuid, 'rint' => $rint]);
    }

    public function testRange()
    {
        $this->assertEquals(PyCore::scalar(PyCore::range(3)), range(0, 2));
    }

    public function testObject()
    {
        $o = PyCore::object("hello world");
        $this->assertTrue($o instanceof PyObject);
        $this->assertStringContainsString('zend_string', strval(PyCore::type($o)));

        $o = PyCore::object(123456789);
        $this->assertStringContainsString('int', strval(PyCore::type($o)));
    }

    public function testFileno()
    {
        $this->assertEquals(0, PyCore::fileno(STDIN));
        $this->assertEquals(1, PyCore::fileno(STDOUT));
        $this->assertEquals(2, PyCore::fileno(STDERR));

        $size = 1 * 1024 * 1024;
        try {
            $fp = fopen("php://temp/maxmemory:$size", 'r+');
            $fd = PyCore::fileno($fp);
        } catch (\Throwable $e) {
            $this->assertStringContainsString('not supported', $e->getMessage());
        }

        $fp = fopen(__FILE__, 'r');
        $this->assertGreaterThan(0, PyCore::fileno($fp));

        $svr = stream_socket_server("tcp://127.0.0.1:0", $errno, $errstr);
        $this->assertNotEmpty($svr);

        $name = stream_socket_get_name($svr, false);
        [$host, $port] = explode(':', $name);
        $this->assertEquals('127.0.0.1', $host);
        $this->assertGreaterThan(0, PyCore::fileno($svr));
        $this->assertGreaterThan(1024, $port);
    }

    public function testNumericAsObject()
    {
        PyCore::setOptions(['numeric_as_object' => true]);
        $rs = PyCore::int(2)->__add__(3)->__mul__(7);
        $this->assertEquals(35, PyCore::scalar($rs));

        PyCore::setOptions(['numeric_as_object' => false]);
        $rs = PyCore::int(2)->__add__(3);
        $this->assertEquals(5, $rs);
    }

    public function testRaise()
    {
        $m = PyCore::import('app.user');
        $builtins = PyCore::import("builtins");
        $message = $m->test_raise(function () use ($builtins) {
            PyCore::raise($builtins->ValueError, "test raise");
        });
        $this->assertStringContainsString('test raise', $message);

        $stop = $m->test_raise(function () use ($builtins) {
            PyCore::raise($builtins->StopIteration);
        });
        $this->assertEquals('StopIteration', $stop);

        $array = $m->test_raise(function () use ($builtins) {
            PyCore::raise($builtins->TypeError, new PyList([1, 2, 3, 4]));
        });
        $this->assertEquals([1, 2, 3, 4], PyCore::scalar($array));
    }
}
