<?php

use PHPUnit\Framework\TestCase;

class EvalTest extends TestCase
{
    public function testEval()
    {
        $pycode = <<<PYCODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

today = datetime.now().strftime("%Y-%m-%d")
PYCODE;

        $mod = PyCore::eval($pycode);

        $this->assertEquals("phpy", $mod->name);
        $this->assertEquals(0.1, $mod->version);
        $this->assertEquals(date('Y-m-d'), $mod->today);
        $this->assertEquals("name:phpy version:0.1", $mod->build_version_info());
    }

    public function testEvalWithInput()
    {
        $pycode = <<<PYCODE
square = {
    f'{prefix}{i}': i**2 for i in range(n)
}
PYCODE;

        $mod = PyCore::eval($pycode, [
            'n' => 10,
            'prefix' => 'square_',
        ]);
        $this->assertNotEmpty($mod);
        $this->assertEquals(64, $mod->square['square_8']);
        $this->assertEquals(16, $mod->square['square_4']);
    }

    public function testEvalErrorCode()
    {
        $pycode = <<<PYCODE
xx tt xx \t 
PYCODE;

        $mod = PyCore::eval($pycode, [
            'n' => 10,
            'prefix' => 'square_',
        ]);
        $this->assertFalse($mod);
    }
}
