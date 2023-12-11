<?php

use PHPUnit\Framework\TestCase;

class ExecTest extends TestCase
{
    public function testExec()
    {
        $pycode = <<<PYCODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

today = datetime.now().strftime("%Y-%m-%d")
PYCODE;

        $globals = new PyDict();
        PyCore::exec($pycode, $globals);

        $this->assertEquals("phpy", $globals['name']);
        $this->assertEquals(0.1, $globals['version']);
        $this->assertEquals(date('Y-m-d'), $globals['today']);
    }

    public function testEvalWithInput()
    {
        $pycode = <<<PYCODE
square = {
    f'{prefix}{i}': i**2 for i in range(n)
}
PYCODE;

        $globals = new PyDict([
            'n' => 10,
            'prefix' => 'square_',
        ]);

        PyCore::exec($pycode, $globals);
        $this->assertEquals(64, $globals['square']['square_8']);
        $this->assertEquals(16, $globals['square']['square_4']);
    }

    public function testEvalErrorCode()
    {
        $pycode = <<<PYCODE
xx tt xx \t 
PYCODE;

        $globals = new PyDict([
            'n' => 10,
            'prefix' => 'square_',
        ]);

        try {
            PyCore::exec($pycode, $globals);
            $this->assertTrue(false);
        } catch (PyError $e) {
            $this->assertStringContainsString('invalid syntax', strval($e->value));
            $this->assertEquals("<class 'SyntaxError'>", strval($e->type));
            $this->assertEquals("<class 'SyntaxError'>", strval($e->error));
            $this->assertTrue(true);
        }
    }
}
