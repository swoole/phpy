<?php

use PHPUnit\Framework\TestCase;

class EvalTest extends TestCase
{
    public function testEvalResult()
    {
        $pycode = <<<PYCODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

today = datetime.now().strftime("%Y-%m-%d")
PYCODE;

        $ret = PyCore::eval($pycode);

        $this->assertEquals("phpy", $ret->name);
        $this->assertEquals(0.1, $ret->version);
        $this->assertEquals(date('Y-m-d'), $ret->today);
        $this->assertEquals("name:phpy version:0.1", $ret->build_version_info());
    }
}
