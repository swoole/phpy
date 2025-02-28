<?php

namespace phpunit;

use PHPUnit\Framework\TestCase;
use PyCore;

class BytesTest extends TestCase
{
    public function testBytes()
    {
        $data = random_bytes(128);
        $bytes = PyCore::bytes($data);
        $this->assertEquals(PyCore::len($bytes), 128);
        $b64 = PyCore::import('base64');
        $rs = $b64->b64encode($bytes);
        $this->assertTrue($rs->__eq__(PyCore::bytes(base64_encode($data))));
    }
}
